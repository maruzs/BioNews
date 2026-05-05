from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class TercerTribunalNewsScraper:
    def __init__(self):
        self.url_base = "https://3ta.cl/category/noticias"
        self.engine = ScrapingEngine()

    def get_latest_news(self, pages=5):
        print("Iniciando scraping en Tercer Tribunal Ambiental", flush=True)
        news_list = []
        
        for page in range(1, pages + 1):
            if page == 1:
                url = f"{self.url_base}/"
            else:
                url = f"{self.url_base}/page/{page}/"
            
            print(f"Consultando pagina {page} del Tercer Tribunal...", flush=True)
            soup = self.engine.get_soup(url, wait_for_selector="article")
            
            if not soup:
                break
                
            articles = soup.find_all("article")
            if not articles: break
            
            for article in articles:
                try:
                    h2 = article.find("h2", class_="entry-title")
                    if not h2: continue 
                        
                    title_tag = h2.find("a")
                    if not title_tag: continue
                        
                    titulo = title_tag.get_text(strip=True)
                    link = title_tag["href"]

                    imagen_url = ""
                    img_tag = article.find("img")
                    if img_tag:
                        imagen_url = img_tag.get("data-src") if img_tag.has_attr("data-src") else img_tag.get("src")
                    
                    fecha_raw = ""
                    time_tag = article.find("time", class_="entry-date")
                    if not time_tag:
                        time_tag = article.find("time", class_="updated")
                        
                    if time_tag and time_tag.has_attr("datetime"):
                        fecha_raw = time_tag["datetime"].split("T")[0]
                    
                    if not fecha_raw:
                        p_date = article.find("p", class_="date")
                        if p_date:
                            texto_fecha = p_date.get_text(strip=True)
                            fecha_raw = texto_fecha.split("/")[0].strip() if "/" in texto_fecha else texto_fecha
                                
                    if not fecha_raw:
                        meta_info = article.find("div", class_="fusion-meta-info")
                        if meta_info:
                            fecha_raw = meta_info.get_text(separator=" ", strip=True)
                            
                    # Si no hay fecha, no forzamos hoy para evitar ensuciar la BD
                    if not fecha_raw:
                        continue

                    news_list.append({
                        "titulo": titulo,
                        "fecha": parse_fecha(fecha_raw),
                        "link": link,
                        "imagen": imagen_url,
                        "fuente": "Tercer Tribunal"
                    })
                except Exception as e:
                    print(f"Error procesando articulo del Tercer Tribunal: {e}", flush=True)

        print(f"Exito: Se encontraron {len(news_list)} noticias en el Tercer Tribunal Ambiental", flush=True)
        return news_list