from .engine import ScrapingEngine
from urllib.parse import urljoin
from ..utils.date_parser import parse_fecha

class SEAScraper:
    def __init__(self):
        self.url = "https://www.sea.gob.cl/noticias"
        self.base_url = "https://www.sea.gob.cl"
        self.engine = ScrapingEngine()

    def get_latest_news(self, pages=3):
        news_list = []
        for p in range(0, pages):
            url = self.url if p == 0 else f"{self.url}?page={p}"
            print(f"Iniciando scraping en SEA (Pagina {p}): {url}", flush=True)
            soup = self.engine.get_soup(url, wait_for_selector=".views-row")
            
            if not soup:
                break

            rows = soup.select(".views-row")
            if not rows: break

            for row in rows:
                try:
                    title_tag = row.select_one(".views-field-title a")
                    if not title_tag:
                        continue
                    
                    title = title_tag.get_text(strip=True)
                    link = urljoin(self.base_url, title_tag["href"])
                    
                    img_tag = row.select_one(".views-field-field-shared-imagen-portada img")
                    img_url = urljoin(self.base_url, img_tag["src"]) if img_tag else ""
                    
                    date_tag = row.select_one(".datetime")
                    if date_tag and date_tag.has_attr("datetime"):
                        fecha_final = date_tag["datetime"].split("T")[0]
                    elif date_tag:
                        fecha_final = parse_fecha(date_tag.get_text(strip=True))
                    else:
                        continue
                    
                    news_list.append({
                        "titulo": title,
                        "fecha": fecha_final,
                        "link": link,
                        "imagen": img_url,
                        "fuente": "SEA"
                    })
                except Exception as e:
                    print(f"Error procesando una noticia de SEA: {e}", flush=True)
                    continue

        print(f"Se encontraron {len(news_list)} noticias en SEA", flush=True)
        return news_list