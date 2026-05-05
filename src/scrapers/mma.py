from .engine import ScrapingEngine
from ..utils.date_parser import parse_fecha

class MMAScraper:
    def __init__(self):
        self.url = "https://mma.gob.cl/noticias/"
        self.engine = ScrapingEngine()

    def get_latest_news(self, pages=3):
        news_list = []
        for p in range(1, pages + 1):
            url = self.url if p == 1 else f"{self.url}page/{p}/"
            print(f"Iniciando scraping en MMA (Pagina {p}): {url}", flush=True)
            soup = self.engine.get_soup(url, wait_for_selector="#vantage-grid-loop")
            
            if not soup:
                break

            articles = soup.find_all("article", class_="grid-post")
            if not articles:
                break

            for article in articles:
                try:
                    title_tag = article.find("h2").find("a")
                    title = title_tag.get_text(strip=True)
                    link = title_tag["href"]
                    
                    fecha_raw = article.find("div", class_="date").get_text(strip=True)                
                    img_tag = article.find("img")
                    img_url = img_tag.get("data-src") if img_tag.has_attr("data-src") else img_tag.get("src")
                    
                    news_list.append({
                        "titulo": title,
                        "fecha": parse_fecha(fecha_raw),
                        "link": link,
                        "imagen": img_url,
                        "fuente": "MMA"
                    })
                except Exception as e:
                    print(f"Error procesando un articulo de MMA: {e}", flush=True)
                    continue
        
        print(f"Se encontraron {len(news_list)} noticias en MMA", flush=True)
        return news_list