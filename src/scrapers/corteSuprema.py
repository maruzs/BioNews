from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
from utils.date_parser import parse_fecha

class CorteSupremaScraper:
    def __init__(self):
        self.url_home = "https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial"
        self.logo_pjud = "https://www.pjud.cl/assets/img/logo-pjud.png"
        
        # Palabras clave para filtrar noticias relevantes
        self.keywords = [
            "medio ambiente", "ambiental", "contaminacion", "agua", 
            "emisiones", "sustentable", "ecolog", "humedal", "minera", 
            "energia", "naturaleza", "biodiversidad", "sma", "sea",
            "litio", "salar", "forestal", "glaciar"
        ]

    def get_latest_news(self):
        print(f"Iniciando scraping en Corte Suprema: {self.url_home}")
        news_list = []

        with sync_playwright() as p:
            # Puedes dejarlo en True de nuevo cuando compruebes que funciona
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                page.goto(self.url_home, wait_until="networkidle")

                print("Aplicando filtros de busqueda...")
                
                # 1. Seleccionar Jurisdiccion
                page.select_option("#jurisdiction-id", label="Corte Suprema")
                
                # Esperamos a que el Ajax cargue las salas
                page.wait_for_timeout(2000)
                
                # 2. Seleccionar Sala (Usando tu selector corregido)
                page.select_option("#sala", label="Tercera sala")
                
                page.wait_for_timeout(1000)
                
                # 3. Click en filtrar (Usando tu selector corregido)
                page.click('#btn-filter')
                
                # IMPORTANTE: Pausa forzada. 
                # Le damos 4 segundos al servidor para responder y cambiar las tarjetas en pantalla.
                # Sin esto, lee las tarjetas viejas al instante.
                page.wait_for_timeout(4000)

                # Por seguridad verificamos que la tabla este visible
                page.wait_for_selector("a.jt-result-item", state="visible", timeout=20000)

                while True:
                    soup = BeautifulSoup(page.content(), "html.parser")
                    items = soup.find_all("a", class_="jt-result-item")

                    for item in items:
                        try:
                            h5 = item.find("h5")
                            if not h5: continue
                            titulo = h5.get_text(strip=True)
                            
                            titulo_lower = titulo.lower()
                            es_medioambiental = False
                            for kw in self.keywords:
                                if kw in titulo_lower:
                                    es_medioambiental = True
                                    break
                            
                            if not es_medioambiental:
                                continue

                            link = item.get("href", "")
                            if link and not link.startswith("http"):
                                link = f"https://www.pjud.cl{link}"

                            fecha_raw = ""
                            small = item.find("small")
                            if small:
                                fecha_txt = small.get_text(strip=True)
                                fecha_raw = fecha_txt.split(" ")[0] if " " in fecha_txt else fecha_txt
                            
                            if not fecha_raw:
                                fecha_raw = datetime.now().strftime("%Y-%m-%d")

                            news_list.append({
                                "titulo": titulo,
                                "fecha": parse_fecha(fecha_raw),
                                "link": link,
                                "imagen": self.logo_pjud,
                                "fuente": "Corte Suprema"
                            })
                        except Exception as e:
                            print(f"Error procesando noticia individual: {e}")

                    try:
                        current_page_val = page.eval_on_selector("#paginanew", "el => el.value")
                        next_page_option = page.locator(f"#paginanew option[value='{int(current_page_val) + 1}']")
                        
                        if next_page_option.count() > 0:
                            print(f"Cambiando a la pagina {int(current_page_val) + 1}...")
                            page.select_option("#paginanew", value=str(int(current_page_val) + 1))
                            
                            # Nuevamente, damos 4 segundos para que la siguiente pagina cargue
                            page.wait_for_timeout(4000) 
                        else:
                            break 
                    except:
                        break 

            except Exception as e:
                print(f"Fallo el flujo de navegacion: {e}")
            finally:
                browser.close()

        print(f"Exito: Se encontraron {len(news_list)} noticias medioambientales en la Corte Suprema")
        return news_list