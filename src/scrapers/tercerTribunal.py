from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager
class TercerTribunalScraperLegal:
    def __init__(self):
        self.url_base = "https://causas.3ta.cl"
        self.db = DatabaseManager()

    def get_legal_data(self):
        print("Iniciando scraping legal en Tercer Tribunal Ambiental (3TA)")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_base, wait_until="networkidle")

                # Esperamos a que aparezcan las filas de causas
                page.wait_for_selector("a.cause-row", state="visible", timeout=15000)

                # Extraemos el HTML una vez que React termino de renderizar
                content = page.content()
                soup = BeautifulSoup(content, "html.parser")

                rows = soup.find_all("a", class_="cause-row")

                if not rows:
                    print("No se encontraron causas en el 3TA")
                    return []

                # Logica de eficiencia: comparar con DB
                # Segun el html, la caratula esta en un span con clase cause-cover
                primer_caratula_tag = rows[0].find(class_="cause-cover")
                primer_api_nombre = primer_caratula_tag.get_text(strip=True) if primer_caratula_tag else "Sin caratula"

                nombre_fuente = "3TA"
                ultimo_db = self.db.get_last_by_source(nombre_fuente)

                if ultimo_db and ultimo_db[1] == primer_api_nombre:
                    print(f"No hay cambios en {nombre_fuente}. Fin del proceso.")
                    return []

                # Procesamos solo las primeras 15 tal como lo solicitaste
                return self._parse_html_data(rows[:15])

            except Exception as e:
                print(f"Error durante el proceso del 3TA: {str(e)}")
                return []
            finally:
                browser.close()

    def _parse_html_data(self, rows):
        legal_list = []
        for row in rows:
            try:
                # 1. Link (viene relativo, ej: /causes/5101)
                href = row.get("href", "")
                if not href:
                    continue
                link = f"{self.url_base}{href}" if href.startswith("/") else href

                # 2. Caratula / Nombre
                caratula_tag = row.find(class_="cause-cover")
                nombre = caratula_tag.get_text(strip=True) if caratula_tag else "Sin caratula"

                # 3. Fecha
                fecha_tag = row.find(class_="cause-issue-date")
                fecha_raw = fecha_tag.get_text(strip=True) if fecha_tag else ""

                # 4. Tipo y Rol (Ej: Reclamacion R-18-2026)
                # Como estan sueltos en el mismo span que contiene la fecha, 
                # extraemos todo el texto del padre y le restamos la fecha.
                tipo_completo = "Sin tipo"
                if fecha_tag and fecha_tag.parent:
                    texto_padre = fecha_tag.parent.get_text(" ", strip=True).replace('\xa0', ' ')
                    tipo_completo = texto_padre.replace(fecha_raw, "").strip()

                legal_list.append({
                    "nombre": nombre,
                    "fecha": parse_fecha(fecha_raw),
                    "estado": "Ver detalle", # La UI principal no muestra el estado
                    "tipo": tipo_completo,
                    "fuente": "3TA",
                    "link": link
                })

            except Exception as e:
                print(f"Error parseando causa especifica en 3TA: {e}")
                continue

        print(f"Exito: Se procesaron {len(legal_list)} registros legales del 3TA")
        return legal_list