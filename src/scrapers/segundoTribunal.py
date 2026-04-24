from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager

class SegundoTribunalScraper:
    def __init__(self):
        self.url_base = "https://2ta.lexsoft.cl/2ta/"
        self.url_home = f"{self.url_base}search?proc=4"
        self.db = DatabaseManager()

    def get_legal_data(self):
        print("Iniciando scraping legal en Segundo Tribunal Ambiental (2TA)", flush=True)
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_home, wait_until="networkidle")
                
                # Esperar a que la tabla dinamica inyecte las filas
                page.wait_for_selector("table#selectable tbody tr", state="visible", timeout=15000)
                
                # Extraemos el HTML una vez que JS termino de armar la tabla
                content = page.content()
                soup = BeautifulSoup(content, "html.parser")
                
                table = soup.find("table", id="selectable")
                if not table:
                    print("Error: No se encontro la tabla de causas en el 2TA")
                    return []
                    
                tbody = table.find("tbody")
                # Si hay tbody usamos sus filas, sino todas las tr ignorando la cabecera
                rows = tbody.find_all("tr") if tbody else table.find_all("tr")[1:]
                
                if not rows:
                    print("La tabla del 2TA no tiene filas")
                    return []
                
                # Logica de eficiencia: Comparar la causa mas reciente con la base de datos
                primer_row_tds = rows[0].find_all("td")
                if len(primer_row_tds) >= 3:
                    # El indice 2 contiene la Caratula segun tu investigacion
                    primer_api_nombre = primer_row_tds[2].get_text(strip=True)
                    
                    nombre_fuente = "2TA"
                    ultimo_db = self.db.get_last_by_source(nombre_fuente)
                    
                    if ultimo_db and ultimo_db[1] == primer_api_nombre:
                        print(f"No hay cambios en {nombre_fuente}. Fin del proceso.")
                        return []

                return self._parse_html_data(rows)

            except Exception as e:
                print(f"Error durante el proceso del 2TA: {str(e)}", flush=True)
                return []
            finally:
                browser.close()

    def _parse_html_data(self, rows):
        legal_list = []
        for row in rows:
            try:
                tds = row.find_all("td")
                # Aseguramos que la fila tenga al menos las 5 columnas de datos principales
                if len(tds) < 5:
                    continue
                    
                # 1. Rol y Link de Detalle (Estan en el primer td)
                a_tag = tds[0].find("a")
                href = a_tag.get("href", "") if a_tag else ""
                
                if href:
                    # El href viene como 'search?proc=3&idCausa=400693', le anadimos la url base
                    link = f"{self.url_base}{href}"
                else:
                    # Si no tiene enlace, no sirve para nuestra base de datos (Primary Key)
                    continue 
                    
                # 2. Fecha (Segundo td)
                fecha_raw = tds[1].get_text(strip=True)
                
                # 3. Caratula/Nombre (Tercer td)
                nombre = tds[2].get_text(strip=True)
                
                # 4. Procedimiento/Tipo (Cuarto td)
                tipo = tds[3].get_text(strip=True)
                
                # 5. Etapa/Estado (Quinto td)
                estado = tds[4].get_text(strip=True)
                
                legal_list.append({
                    "nombre": nombre,
                    "fecha": parse_fecha(fecha_raw),
                    "estado": estado,
                    "tipo": tipo,
                    "fuente": "2TA",
                    "link": link
                })
                
            except Exception as e:
                print(f"Error parseando una fila especifica en 2TA: {e}", flush=True)
                continue
        
        print(f"Exito: Se procesaron {len(legal_list)} registros del 2TA", flush=True   )
        return legal_list