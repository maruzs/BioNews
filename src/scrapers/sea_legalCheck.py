from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from ..utils.date_parser import parse_fecha

class SEALegalScraper:
    def __init__(self):
        self.url_home = "https://www.sea.gob.cl/"
        # ID del boton segun tu investigacion
        self.id_boton_buscar = "#edit-seia-submit"

    def get_legal_data(self):
        print(f"Iniciando scraping legal desde Home SEA (Modo Invisible): {self.url_home}")
        
        with sync_playwright() as p:
            # Forzamos un navegador con caracteristicas humanas
            browser = p.chromium.launch(headless=True)
            
            # Configuracion de contexto critico para evitar deteccion en headless
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080},
                device_scale_factor=1,
            )
            
            page = context.new_page()
            
            try:
                # 1. Navegar a la Home
                # Usamos 'networkidle' para asegurar que los scripts de busqueda carguen
                page.goto(self.url_home, wait_until="networkidle", timeout=60000)
                
                # 2. Esperar y clickear el boton de busqueda
                print("Esperando boton de busqueda...")
                page.wait_for_selector(self.id_boton_buscar, state="visible", timeout=30000)
                
                # Un pequeno delay humano antes de clickear ayuda a evitar bloqueos
                page.wait_for_timeout(1000)
                page.click(self.id_boton_buscar)
                
                # 3. Esperar a que la tabla de resultados aparezca
                print("Esperando tabla de resultados...")
                page.wait_for_selector("#datatable-proyectos", timeout=45000)
                
                # 4. Cambiar a 20 registros
                selector_cantidad = "select.dt-input"
                page.select_option(selector_cantidad, "100")
                
                # Esperar a que la tabla se refresque con la fila 11
                page.wait_for_selector("table#datatable-proyectos tbody tr:nth-child(11)", timeout=30000)
                page.wait_for_timeout(2000)

                soup = BeautifulSoup(page.content(), "html.parser")
                browser.close()
                
                legal_list = []
                table = soup.find("table", id="datatable-proyectos")
                if not table: return []
                
                rows = table.find("tbody").find_all("tr")

                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) < 10: continue
                    
                    try:
                        link_tag = cols[0].find("a")
                        nombre = link_tag.get_text(strip=True)
                        link = link_tag["href"]
                        tipo = cols[1].get_text(strip=True)
                        fecha_raw = cols[8].get_text(strip=True)
                        estado = cols[10].get_text(strip=True)
                        
                        legal_list.append({
                            "nombre": nombre,
                            "fecha": parse_fecha(fecha_raw),
                            "estado": estado,
                            "tipo": tipo,
                            "fuente": "SEA",
                            "link": link
                        })
                    except: continue
                
                print(f"Exito: Se encontraron {len(legal_list)} proyectos en SEA")
                return legal_list
                
            except Exception as e:
                print(f"Fallo el scraping del SEA en modo headless: {e}")
                # Si falla, tomamos una captura para ver que esta viendo el bot
                # page.screenshot(path="debug_sea.png") 
                browser.close()
                return []