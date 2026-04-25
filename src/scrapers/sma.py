from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class SMAScraper:
    def __init__(self):
        self.url_home = "https://portal.sma.gob.cl/index.php/sala-de-prensa/"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en SMA: {self.url_home}", flush=True)
        
        # Esperamos a que carguen los articulos de la clase type-post
        soup = self.engine.get_soup(self.url_home, wait_for_selector="article.type-post")
        
        if not soup:
            print("Error: No se pudo cargar el contenido de la pagina de la SMA", flush=True)
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
                        # Cortamos a YYYY-MM-DD y lo separamos
                        partes = fecha_iso[:10].split("-")
                        if len(partes) == 3:
                            # Lo invertimos a DD-MM-YYYY para que date_parser lo entienda
                            fecha_raw = f"{partes[2]}-{partes[1]}-{partes[0]}"
                
                # Respaldo usando el texto visible (ej: "1 Abril, 2026")
                if not fecha_raw:
                    meta_info = article.find("div", class_="fusion-meta-info")
                    if meta_info:
                        fecha_raw = meta_info.get_text(separator=" ", strip=True)

                # Respaldo final si todo falla
                if not fecha_raw:
                    fecha_raw = datetime.now().strftime("%d-%m-%Y")

                # 4. Construir y guardar el diccionario
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