from .engine import ScrapingEngine
from utils.date_parser import parse_fecha

class SernageominScraper:
    def __init__(self):
        self.url = "https://www.sernageomin.cl/category/noticias/"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en Sernageomin: {self.url}")
        # Segun sernageomin.md el contenedor es .fusion-posts-container
        soup = self.engine.get_soup(self.url, wait_for_selector=".fusion-posts-container")
        
        if not soup:
            return []

        news_list = []
        # Buscamos los articulos dentro del grid
        articles = soup.select("article.fusion-post-grid")

        for article in articles:
            try:
                # Titulo y Link
                title_tag = article.select_one(".entry-title a")
                title = title_tag.get_text(strip=True)
                link = title_tag["href"]
                
                # Imagen
                img_tag = article.select_one(".fusion-image-wrapper img")
                img_url = img_tag["src"] if img_tag else ""
                
                # Fecha
                # Segun el md, esta en un span dentro de p.fusion-single-line-meta
                date_tag = article.select_one(".fusion-single-line-meta span:nth-child(3)")
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                
                news_list.append({
                    "titulo": title,
                    "fecha": parse_fecha(fecha_raw),
                    "link": link,
                    "imagen": img_url,
                    "fuente": "Sernageomin"
                })
            except Exception as e:
                print(f"Error procesando noticia de Sernageomin: {e}")

        print(f"Se encontraron {len(news_list)} noticias en Sernageomin")
        return news_list