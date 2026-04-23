import traceback
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager

class SnifaScraper:
    def __init__(self):
        self.url_base = "https://snifa.sma.gob.cl"
        self.url_home = f"{self.url_base}/Sancionatorio"
        self.db = DatabaseManager()
        
        self.categorias = {
            "6": "Agroindustrias",
            "10": "Energia",
            "5": "Infraestructura Portuaria",
            "1": "Instalacion fabril",
            "9": "Mineria"#,
            #"21": "Saneamiento Ambiental",
            #"13": "Transportes y almacenajes"
        }

    def get_legal_data(self):
        print("Iniciando scraping legal en SNIFA (Sancionatorios)")
        all_legal_data = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                for cat_id, cat_nombre in self.categorias.items():
                    print(f"Consultando categoria: {cat_nombre}...")
                    
                    try:
                        # 1. Volver a la url principal. Esto actua como el "reiniciar busqueda" perfecto.
                        page.goto(self.url_home, wait_until="networkidle", timeout=60000)
                        print("Muestra 1")
                        # 2. Esperar que el selector este visible y elegir la categoria
                        page.wait_for_selector("#categoria", state="visible", timeout=15000)
                        page.select_option("#categoria", value=cat_id)
                        
                        # 3. Buscar el boton por su texto (mas seguro que por ID) y clickear
                        boton_buscar = page.locator("button:has-text('Buscar')").first
                        boton_buscar.click()
                        
                        # 4. Esperar a que la tabla de resultados cargue
                        print("Muestra 2")
                        page.wait_for_selector("table tbody tr", state="visible", timeout=30000)
                        
                        # 5. Extraer el HTML de la pagina
                        print("Extrayendo")
                        soup = BeautifulSoup(page.content(), "html.parser")
                        print('Extraido 1')
                        rows = soup.select("table tbody tr")
                        print('Extraido 2')
                        if not rows:
                            print(f"No se encontraron filas para la categoria {cat_nombre}")
                            continue

                        # 6. Parsear solo las primeras 15 filas segun requerimiento
                        print(f"Parseando datos de la categoria {cat_nombre}...")
                        datos_categoria = self._parse_html_data(rows[:15], cat_nombre)
                        all_legal_data.extend(datos_categoria)

                    except Exception as e:
                        print(f"Error procesando categoria {cat_nombre}: {str(e)}")
                        continue

            except Exception:
                print("Error critico en el flujo de navegacion de SNIFA")
                traceback.print_exc()
            finally:
                browser.close()

        print(f"Exito: Se procesaron {len(all_legal_data)} registros totales de SNIFA")
        return all_legal_data

    def _parse_html_data(self, rows, tipo_categoria):
        print("Parseando filas HTML de SNIFA...")
        legal_list = []
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        
        for row in rows:
            try:
                tds = row.find_all("td")
                if len(tds) < 4:
                    continue
                
                # Expediente y Enlace
                td_expediente = tds[0]
                a_tag = td_expediente.find("a")
                if not a_tag:
                    continue
                    
                rol = a_tag.get_text(strip=True)
                href = a_tag.get("href", "")
                link = f"{self.url_base}{href}" if href.startswith("/") else href
                
                # Nombre de la instalacion
                instalacion_text = ""
                td_instalacion = tds[1]
                ul_inst = td_instalacion.find("ul")
                if ul_inst:
                    li_inst = ul_inst.find("li")
                    instalacion_text = li_inst.get_text(strip=True) if li_inst else ""
                
                nombre_completo = f"{rol} - {instalacion_text}" if instalacion_text else rol
                
                # Estado
                estado_text = "Desconocido"
                for td in tds:
                    if td.get("data-label") == "Estado":
                        estado_text = td.get_text(strip=True)
                        break
                
                legal_list.append({
                    "nombre": nombre_completo,
                    "fecha": parse_fecha(fecha_hoy),
                    "estado": estado_text,
                    "tipo": f"Sancionatorio ({tipo_categoria})",
                    "fuente": "SNIFA",
                    "link": link
                })
                
            except Exception as e:
                print(f"Error parseando una fila especifica en SNIFA: {e}")
                continue
                
        return legal_list