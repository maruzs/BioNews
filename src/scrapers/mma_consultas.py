import os
from src.database.manager import DatabaseManager
import time
from datetime import datetime
from bs4 import BeautifulSoup
from .engine import ScrapingEngine
from playwright.sync_api import sync_playwright

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')
db_manager = DatabaseManager()

class MMAConsultasScraper:
    def __init__(self):
        self.url_base = "https://consultasciudadanas.mma.gob.cl"
        self.url_abiertas = f"{self.url_base}/portal"
        self.url_cerradas = f"{self.url_base}/portal/consultas_cerradas"
        self.engine = ScrapingEngine()

    def _get_connection(self):
        return db_manager.get_connection('bionews_consultations_db')

    def _normalize_date_to_target(self, date_str):
        """Convierte cualquier fecha a mm/dd/yyyy como pide el prompt."""
        if not date_str: return ""
        date_str = date_str.split(' ')[0] # Quitar hora si existe
        
        try:
            # Caso yyyy-mm-dd
            if '-' in date_str and len(date_str.split('-')[0]) == 4:
                dt = datetime.strptime(date_str, '%Y-%m-%d')
                return dt.strftime('%m/%d/%Y')
            # Caso m/d/yyyy o mm/dd/yyyy
            if '/' in date_str:
                parts = date_str.split('/')
                if len(parts) == 3:
                    m, d, y = parts[0].zfill(2), parts[1].zfill(2), parts[2]
                    return f"{m}/{d}/{y}"
        except:
            pass
        return date_str

    def scrape_abiertas(self, page):
        print("Scrapeando consultas MMA Abiertas...")
        page.goto(self.url_abiertas, wait_until="networkidle")
        
        # Esperar a que las cards carguen
        try:
            page.wait_for_selector('a[href*="/portal/consulta/"]', timeout=10000)
        except:
            print("No se encontraron consultas abiertas.")
            return []

        soup = BeautifulSoup(page.content(), 'html.parser')
        cards = soup.find_all('a', href=True)
        consultas_links = []
        for card in cards:
            if '/portal/consulta/' in card['href']:
                href = card['href']
                link = href if href.startswith('http') else self.url_base + href
                consultas_links.append(link)
        
        # Eliminar duplicados
        consultas_links = list(set(consultas_links))
        results = []

        for link in consultas_links:
            try:
                print(f"  Detalle: {link}")
                page.goto(link, wait_until="networkidle", timeout=60000)
                # Esperar a que el detalle cargue
                page.wait_for_selector('.card-body', timeout=20000)
                detail_soup = BeautifulSoup(page.content(), 'html.parser')
                
                # Extraer datos
                consulta_id = link.split('/')[-1]
                
                # Nombre
                nombre = ""
                nombre_p = detail_soup.find('p', string=lambda t: t and 'Nombre instrumento' in t)
                if nombre_p:
                    nombre = nombre_p.find_next('p').get_text(strip=True)
                else:
                    # Fallback por si el texto cambia un poco
                    h6_nombre = detail_soup.find('h6', class_='m-3')
                    if h6_nombre: nombre = h6_nombre.get_text(strip=True)

                # Campos en la tabla lateral
                def get_field(label):
                    p = detail_soup.find('p', string=lambda t: t and label in t)
                    if p:
                        # Buscar en el div hermano el valor
                        parent_div = p.find_parent('div')
                        if parent_div:
                            val_div = parent_div.find_next_sibling('div')
                            if val_div:
                                val_p = val_div.find('p')
                                if val_p: return val_p.get_text(strip=True)
                    return ""

                f_inicio = self._normalize_date_to_target(get_field("Fecha de inicio"))
                f_termino = self._normalize_date_to_target(get_field("Fecha de término"))
                tipo_inst = get_field("Tipo de Instrumento")
                tipo_proc = get_field("Tipo de Proceso")
                ambito = get_field("Ámbito Territorial")

                results.append({
                    "id": consulta_id,
                    "nombre_instrumento": nombre,
                    "fecha_inicio": f_inicio,
                    "fecha_termino": f_termino,
                    "tipo_instrumento": tipo_inst,
                    "tipo_proceso": tipo_proc,
                    "ambito_territorial": ambito,
                    "link_detalle": link
                })
            except Exception as e:
                print(f"  Error en {link}: {e}")
        
        return results

    def scrape_cerradas(self, page):
        print("Scrapeando consultas MMA Cerradas...")
        page.goto(self.url_cerradas, wait_until="networkidle")
        
        tabs = [
            {"name": "Planes", "selector": 'text="Planes"'},
            {"name": "Normas", "selector": 'text="Normas"'},
            {"name": "Otros", "selector": 'text="Otros Instrumentos"'},
            {"name": "Especies", "selector": 'text="Clasificación de Especies"'}
        ]

        all_results = []

        for tab in tabs:
            try:
                print(f"  Pestaña: {tab['name']}")
                
                # 1. Encontrar y clickear la pestaña
                tab_locator = page.locator(f'a[role="tab"]:has-text("{tab["name"]}")').first
                if not tab_locator.count():
                    tab_locator = page.locator(tab['selector']).first
                
                # Obtener el ID del panel que controla esta pestaña (aria-controls)
                panel_id = tab_locator.get_attribute('aria-controls')
                
                # Clickear
                tab_locator.click(force=True)
                
                # 2. Esperar a que la pestaña sea marcada como activa en el DOM
                # BootstrapVue pone la clase 'active' en el nav-link
                try:
                    page.wait_for_function(
                        """(sel) => document.querySelector(sel)?.classList.contains('active')""",
                        arg=f'a[role="tab"]:has-text("{tab["name"]}")',
                        timeout=5000
                    )
                except:
                    print(f"    Aviso: La pestaña {tab['name']} no cambió de clase, continuando...")

                # 3. Esperar a que el contenido se actualice. 
                # Nuxt suele mostrar un loader o vaciar el contenedor.
                # Vamos a esperar a que el panel correspondiente tenga la clase 'active' Y 'show'
                if panel_id:
                    try:
                        page.wait_for_selector(f'div#{panel_id}.active.show', timeout=5000)
                    except:
                        pass

                # Esperar un poco más por el renderizado de las cards
                time.sleep(3)
                
                # 4. Parsear con BeautifulSoup pero filtrando por el contenedor ACTIVO
                soup = BeautifulSoup(page.content(), 'html.parser')
                
                # Buscar el tab-pane que está activo. Solo ese tiene la info real de la pestaña.
                active_pane = soup.select_one('div.tab-pane.active.show')
                if not active_pane:
                    # Fallback por si las clases son distintas
                    active_pane = soup.select_one('div.tab-pane.active')
                
                if not active_pane:
                    print(f"    No se encontró panel activo para {tab['name']}")
                    continue

                # Encontrar las cards DENTRO del panel activo
                cards = active_pane.find_all('a', href=True)
                
                count_tab = 0
                for card in cards:
                    href = card['href']
                    if '/portal/consulta/' in href and (card.find('i', class_='fa-lock') or card.find('i', class_='fas fa-lock')):
                        
                        consulta_id = href.split('/')[-1]
                        
                        # TÍTULO: Usar la columna central
                        title_div = card.select_one('div.col-sm-5')
                        titulo = ""
                        if title_div and title_div.find('h6'):
                            titulo = title_div.find('h6').get_text(strip=True)
                        else:
                            h6_tags = card.find_all('h6')
                            for h6 in h6_tags:
                                text = h6.get_text(strip=True)
                                if text.lower() != "cerrada" and text.lower() != "cerrado":
                                    titulo = text
                                    break
                        
                        if not titulo: continue

                        # Metadatos
                        def get_card_meta(label):
                            strong = card.find('strong', string=lambda t: t and label in t)
                            if strong:
                                return strong.parent.get_text(strip=True).replace(label, "").strip()
                            return ""

                        ambito = get_card_meta("Ambito territorial:")
                        f_inicio = self._normalize_date_to_target(get_card_meta("Fecha inicio:"))
                        f_termino = self._normalize_date_to_target(get_card_meta("Fecha término:"))
                        
                        link_detalle = href if href.startswith('http') else self.url_base + href

                        all_results.append({
                            "id": consulta_id,
                            "nombre_instrumento": titulo,
                            "fecha_inicio": f_inicio,
                            "fecha_termino": f_termino,
                            "tipo_instrumento": tab['name'],
                            "ambito_territorial": ambito,
                            "link_detalle": link_detalle
                        })
                        count_tab += 1
                
                print(f"    Encontrados {count_tab} registros en {tab['name']}")
                
                # Si no encontramos nada, puede ser que el panel no tuviera cards aún
                if count_tab == 0:
                    if "No existen consultas" in active_pane.get_text() or "No se han encontrado registros" in active_pane.get_text():
                        print(f"    Confirmado: {tab['name']} está vacío.")
            
            except Exception as e:
                print(f"  Error en pestaña {tab['name']}: {e}")

        return all_results

    def save_results(self, abiertas, cerradas):
        conn = self._get_connection()
        cursor = conn.cursor()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        nuevos = 0
        
        # Guardar Abiertas
        for item in abiertas:
            cursor.execute("SELECT 1 FROM mma_abiertas WHERE id = %s", (item['id'],))
            exists = cursor.fetchone()
            
            cursor.execute("""
                INSERT INTO mma_abiertas 
                (id, nombre_instrumento, fecha_inicio, fecha_termino, tipo_instrumento, tipo_proceso, ambito_territorial, link_detalle, fecha_scraping)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT(id) DO UPDATE SET
                    nombre_instrumento=excluded.nombre_instrumento,
                    fecha_inicio=excluded.fecha_inicio,
                    fecha_termino=excluded.fecha_termino,
                    tipo_instrumento=excluded.tipo_instrumento,
                    tipo_proceso=excluded.tipo_proceso,
                    ambito_territorial=excluded.ambito_territorial,
                    link_detalle=excluded.link_detalle
            """, (item['id'], item['nombre_instrumento'], item['fecha_inicio'], item['fecha_termino'], 
                  item['tipo_instrumento'], item['tipo_proceso'], item['ambito_territorial'], item['link_detalle'], now))
            if not exists: nuevos += 1

        # Guardar Cerradas
        for item in cerradas:
            cursor.execute("SELECT 1 FROM mma_cerradas WHERE id = %s", (item['id'],))
            exists = cursor.fetchone()

            cursor.execute("""
                INSERT INTO mma_cerradas 
                (id, nombre_instrumento, fecha_inicio, fecha_termino, tipo_instrumento, ambito_territorial, link_detalle, fecha_scraping)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT(id) DO UPDATE SET
                    nombre_instrumento=excluded.nombre_instrumento,
                    fecha_inicio=excluded.fecha_inicio,
                    fecha_termino=excluded.fecha_termino,
                    tipo_instrumento=excluded.tipo_instrumento,
                    ambito_territorial=excluded.ambito_territorial,
                    link_detalle=excluded.link_detalle
            """, (item['id'], item['nombre_instrumento'], item['fecha_inicio'], item['fecha_termino'], 
                  item['tipo_instrumento'], item['ambito_territorial'], item['link_detalle'], now))
            if not exists: nuevos += 1
            
            # Si ahora está cerrada, eliminar de abiertas si existía
            cursor.execute("DELETE FROM mma_abiertas WHERE id = %s", (item['id'],))

        conn.commit()
        conn.close()
        return nuevos

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            
            try:
                abiertas = self.scrape_abiertas(page)
                cerradas = self.scrape_cerradas(page)
                nuevos = self.save_results(abiertas, cerradas)
                print(f"Scraping MMA finalizado. Nuevos registros: {nuevos}")
                return nuevos
            finally:
                browser.close()

if __name__ == "__main__":
    scraper = MMAConsultasScraper()
    scraper.run()
