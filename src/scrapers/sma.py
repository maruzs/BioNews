from .engine import ScrapingEngine
from datetime import datetime
from utils.date_parser import parse_fecha

class SMAScraper:
    def __init__(self):
        self.url_home = "https://portal.sma.gob.cl/index.php/sala-de-prensa/"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en SMA: {self.url_home}")
        
        # Esperamos a que carguen los articulos de la clase type-post
        soup = self.engine.get_soup(self.url_home, wait_for_selector="article.type-post")
        
        if not soup:
            print("Error: No se pudo cargar el contenido de la pagina de la SMA")
            return []

        news_list = []
        
        # Buscamos todas las tarjetas de noticia
        articles = soup.find_all("article", class_="type-post")
        
        for article in articles:
            try:
                # 1. Extraer Titulo y Link
                h2 = article.find("h2", class_="entry-title")
                if not h2:
                    continue
                
                a_tag = h2.find("a")
                if not a_tag:
                    continue
                    
                titulo = a_tag.get_text(strip=True)
                link = a_tag.get("href")
                
                # 2. Extraer Imagen
                imagen_url = ""
                img_tag = article.find("img")
                if img_tag and img_tag.has_attr("src"):
                    imagen_url = img_tag["src"]
                
                # 3. Extraer Fecha
                fecha_raw = ""
                span_updated = article.find("span", class_="updated")
                if span_updated:
                    # El texto viene asi: 2026-04-01T14:56:56-03:00
                    fecha_iso = span_updated.get_text(strip=True)
                    if len(fecha_iso) >= 10:
                        # Cortamos los primeros 10 caracteres (YYYY-MM-DD)
                        fecha_raw = fecha_iso[:10]
                
                # Respaldo en caso de que no encuentre la fecha
                if not fecha_raw:
                    fecha_raw = datetime.now().strftime("%Y-%m-%d")

                # 4. Construir y guardar el diccionario
                news_list.append({
                    "titulo": titulo,
                    "fecha": parse_fecha(fecha_raw),
                    "link": link,
                    "imagen": imagen_url,
                    "fuente": "SMA"
                })
                
            except Exception as e:
                print(f"Error procesando articulo de SMA: {e}")

        print(f"Exito: Se encontraron {len(news_list)} noticias en la SMA")
        return news_list