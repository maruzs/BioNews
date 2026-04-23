import os
import json
from playwright.sync_api import sync_playwright
from ..src.utils.date_parser import parse_fecha
from dotenv import load_dotenv

load_dotenv()

class SEALegalScraper:
    def __init__(self):
        self.url_login = "https://pertinencia.sea.gob.cl/login"
        self.url_api = "https://pertinencia.sea.gob.cl/api/proceso/buscarcp"
        self.user = os.getenv("SEA_USER")
        self.password = os.getenv("SEA_PASSWORD")

    def get_legal_data(self):
        print("Iniciando scraping de pertinencias SEA via API")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            # User agent para evitar bloqueos basicos
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_login, wait_until="networkidle")
                page.fill("#username", self.user)
                page.fill("#password", self.password)
                page.click("input[name='submit']")                
                page.wait_for_load_state("networkidle")

                # 2. Capturar la respuesta de la API al hacer click en Buscar
                # Definimos una promesa para esperar la respuesta del JSON
                with page.expect_response(self.url_api) as response_info:
                    page.click("button.boton-buscar")
                
                response = response_info.value
                if response.status == 200:
                    data = response.json()
                    data_limitada = data[:99] 
                    return self._parse_json_data(data_limitada)
                    #return self._parse_json_data(data)
                else:
                    print(f"Error en API: Codigo {response.status}")
                    return []

            except Exception as e:
                print(f"Error durante el proceso: {str(e)}")
                return []
            finally:
                browser.close()

    def _parse_json_data(self, data):
        legal_list = []
        # Segun nuevaInvSEALegal.md el JSON es una lista de objetos
        for item in data:
            try:
                # Construccion del link usando el correlativeId o qidProcess
                #correlativo = item.get("correlativeId", "")
                link = f"https://pertinencia.sea.gob.cl/proceso/pertinencias/obtener/{item.get('correlativeId')}"
                
                legal_list.append({
                    "nombre": item.get("name"),
                    "fecha": parse_fecha(item.get("presentationDate")),
                    "estado": item.get("state", {}).get("valor"),
                    "tipo": item.get("projectType", {}).get("valor"),
                    "fuente": "SEA Pertinencias",
                    "link": link
                })
            except Exception:
                continue
        
        print(f"Exito: Se procesaron {len(legal_list)} registros desde la API")
        return legal_list