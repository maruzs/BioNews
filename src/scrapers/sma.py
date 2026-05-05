from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class SMAScraper:
    def __init__(self):
        self.url_home = "https://portal.sma.gob.cl/index.php/sala-de-prensa/"
        self.engine = ScrapingEngine()

    def get_latest_news(self, pages=3):
        news_list = []
        for p in range(1, pages + 1):
            url = self.url_home if p == 1 else f"{self.url_home}page/{p}/"
            print(f"Iniciando scraping en SMA (Pagina {p}): {url}", flush=True)
            soup = self.engine.get_soup(url, wait_for_selector="article.type-post")
            
            if not soup:
                break

            articles = soup.find_all("article", class_="type-post")
            if not articles: break
            
            for article in articles:
                try:
                    h2 = article.find("h2", class_="entry-title")
                    if not h2: continue
                    
                    a_tag = h2.find("a")
                    if not a_tag: continue
                        
                    titulo = a_tag.get_text(strip=True)
                    link = a_tag.get("href")
                    
                    imagen_url = ""
                    img_tag = article.find("img")
                    if img_tag and img_tag.has_attr("src"):
                        imagen_url = img_tag["src"]
                    
                    fecha_raw = ""
                    span_updated = article.find("span", class_="updated")
                    if span_updated:
                        fecha_iso = span_updated.get_text(strip=True)
                        if len(fecha_iso) >= 10:
                            fecha_raw = fecha_iso[:10]
                    
                    if not fecha_raw:
                        meta_info = article.find("div", class_="fusion-meta-info")
                        if meta_info:
                            fecha_raw = meta_info.get_text(separator=" ", strip=True)

                    if not fecha_raw:
                        continue

                    news_list.append({
                        "titulo": titulo,
                        "fecha": parse_fecha(fecha_raw),
                        "link": link,
                        "imagen": imagen_url,
                        "fuente": "SMA"
                    })
                except Exception as e:
                    print(f"Error procesando articulo de SMA: {e}", flush=True)

        print(f"Exito: Se encontraron {len(news_list)} noticias en la SMA", flush=True)
        return news_list