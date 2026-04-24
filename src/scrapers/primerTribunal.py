import json
import traceback
from playwright.sync_api import sync_playwright
from utils.date_parser import parse_fecha
from database.manager import DatabaseManager
class PrimerTribunalScraper:
    def __init__(self):
        self.url_ui = "https://www.portaljudicial1ta.cl/sgc-web/consulta-causa.html"
        self.api_endpoint = "**/get-consulta-causa"
        self.db = DatabaseManager()

    def get_legal_data(self):
        print("Iniciando scraping legal en Primer Tribunal Ambiental (1TA)")
        
        with sync_playwright() as p:
            # Puedes cambiar a headless=False para monitorear visualmente
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_ui, wait_until="networkidle")
                
                # Esperamos a que el boton sea visible
                page.wait_for_selector("#btnBuscar", state="visible", timeout=10000)
                
                # Interceptamos la respuesta de la API al hacer click
                with page.expect_response(self.api_endpoint, timeout=15000) as response_info:
                    page.click("#btnBuscar")
                
                response = response_info.value
                raw_data = response.json()
                
                # El KeyError 0 ocurria porque raw_data es un diccionario
                # Segun el .md, los datos reales vienen en la llave 'response' como string
                if isinstance(raw_data, dict) and "response" in raw_data:
                    # Convertimos el string JSON interno en una lista de Python
                    data = json.loads(raw_data["response"])
                else:
                    data = raw_data

                if not data or not isinstance(data, list):
                    print("La API del 1TA no devolvio una lista de datos valida")
                    return []

                nombre_fuente = "1TA"
                ultimo_db = self.db.get_last_by_source(nombre_fuente)
                
                # Ahora que data es una lista, podemos acceder al indice 0
                primer_api_nombre = data[0].get("caratula")

                if ultimo_db and ultimo_db[1] == primer_api_nombre:
                    print(f"No hay cambios en {nombre_fuente}. Fin del proceso.")
                    return []

                return self._parse_json_data(data[:99])

            except Exception:
                print("Error durante el proceso del 1TA")
                traceback.print_exc()
                return []
            finally:
                browser.close()

    def _parse_json_data(self, data):
        legal_list = []
        for item in data:
            try:
                fecha_raw = item.get("fechaCausa", "")
                if " " in fecha_raw:
                    fecha_raw = fecha_raw.split(" ")[0]
                
                id_causa = item.get("idCausa", "")
                link = f"https://www.portaljudicial1ta.cl/sgc-web/ver-causa.html?idCausa={id_causa}"
                
                legal_list.append({
                    "nombre": item.get("caratula", "Sin caratula"),
                    "fecha": parse_fecha(fecha_raw),
                    "estado": item.get("estado", "Sin estado").strip(),
                    "tipo": item.get("tipoCausa", "Sin tipo"),
                    "fuente": "1TA",
                    "link": link
                })
            except Exception:
                continue
        
        print(f"Exito: Se procesaron {len(legal_list)} registros del 1TA")
        return legal_list