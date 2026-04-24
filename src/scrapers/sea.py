from .engine import ScrapingEngine
from urllib.parse import urljoin
from ..utils.date_parser import parse_fecha

class SEAScraper:
    def __init__(self):
        self.url = "https://www.sea.gob.cl/noticias"
        self.base_url = "https://www.sea.gob.cl"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en SEA: {self.url}", flush=True)
        # Aumentamos el tiempo de espera por si la pagina esta lenta
        soup = self.engine.get_soup(self.url, wait_for_selector=".views-row")
        
        if not soup:
            return []

        news_list = []
        rows = soup.select(".views-row")

        for row in rows:
            try:
                # 1. Validar Titulo y Link
                title_tag = row.select_one(".views-field-title a")
                if not title_tag:
                    continue
                
                title = title_tag.get_text(strip=True)
                link = urljoin(self.base_url, title_tag["href"])
                
                # 2. Validar Imagen
                img_tag = row.select_one(".views-field-field-shared-imagen-portada img")
                img_url = urljoin(self.base_url, img_tag["src"]) if img_tag else ""
                
                # 3. Validar Fecha (Prioridad al atributo datetime)
                date_tag = row.select_one(".datetime")
                if date_tag and date_tag.has_attr("datetime"):
                    # Extrae '2026-04-17' de '2026-04-17T21:34:18Z'
                    fecha_final = date_tag["datetime"].split("T")[0]
                elif date_tag:
                    fecha_final = parse_fecha(date_tag.get_text(strip=True))
                else:
                    fecha_final = "2026-04-20"
                
                news_list.append({
                    "titulo": title,
                    "fecha": fecha_final,
                    "link": link,
                    "imagen": img_url,
                    "fuente": "SEA"
                })
            except Exception as e:
                # Si una noticia falla, pasamos a la siguiente sin romper todo
                print(f"Error procesando una noticia de SEA: {e}", flush=True)
                continue

        print(f"Se encontraron {len(news_list)} noticias en SEA", flush=True)
        return news_list