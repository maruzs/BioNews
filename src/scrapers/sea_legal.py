import os
import json
from playwright.sync_api import sync_playwright
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager
from dotenv import load_dotenv

load_dotenv()

class SEALegalScraper:
    def __init__(self):
        self.url_login = "https://pertinencia.sea.gob.cl/login"
        self.url_api = "https://pertinencia.sea.gob.cl/api/proceso/buscarcp"
        self.user = os.getenv("SEA_USER")
        self.password = os.getenv("SEA_PASSWORD")
        self.db = DatabaseManager()

    def get_legal_data(self):
        print("Iniciando scraping SEA (Modo optimizado por fuente)", flush=True)
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_login)
                page.fill("#username", self.user)
                page.fill("#password", self.password)
                page.click("input[name='submit']")
                page.wait_for_load_state("networkidle")

                # Esperamos la respuesta de la API tras el click en buscar
                with page.expect_response(self.url_api) as response_info:
                    page.click("button.boton-buscar")
                
                data = response_info.value.json()
                if not data:
                    return []
                nombre_fuente = "SEA Pertinencias"
                ultimo_registro_sea = self.db.get_last_by_source(nombre_fuente)
                primer_api_nombre = data[0].get("name")
                # ultimo_registro_sea[1] asumiendo que el nombre es la segunda columna
                if ultimo_registro_sea and ultimo_registro_sea[1] == primer_api_nombre:
                    print(f"No hay cambios en {nombre_fuente}. Fin del proceso.")
                    return []

                return self._parse_json_data(data[:99])

            except Exception as e:
                print(f"Error en scraper SEA: {str(e)}", flush=True)
                return []
            finally:
                browser.close()

    def _parse_json_data(self, data):
        legal_list = []
        for item in data:
            try:
                #link = f"https://pertinencia.sea.gob.cl/proceso/pertinencias/obtener/{item.get('correlativeId')}"
                link = f"https://pertinencia.sea.gob.cl/api/public/expediente/{item.get('correlativeId')}"
                legal_list.append({
                    "nombre": item.get("name"),
                    "fecha": parse_fecha(item.get("presentationDate")),
                    "estado": item.get("state", {}).get("valor"),
                    "tipo": item.get("projectType", {}).get("valor"),
                    "fuente": "SEA Pertinencias",
                    "link": link
                })
            except Exception as e:
                print(f"Error parseando fila de SEA Pertinencias: {e}", flush=True)
                continue
        return legal_list