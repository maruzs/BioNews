from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class TercerTribunalScraper:
    def __init__(self):
        self.url_base = "https://3ta.cl/category/noticias"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print("Iniciando scraping en Tercer Tribunal Ambiental", flush=True)
        news_list = []
        
        # Iteramos sobre la pagina 1 y 2 segun la investigacion
        for page in range(1, 3):
            if page == 1:
                url = f"{self.url_base}/"
            else:
                url = f"{self.url_base}/page/{page}/"
            
            print(f"Consultando pagina {page} del Tercer Tribunal...", flush=True)
            
            # Esperamos a que cargue al menos un articulo
            soup = self.engine.get_soup(url, wait_for_selector="article.entry-preview")
            
            if not soup:
                print(f"Error: No se pudo cargar la pagina {page}", flush=True)
                continue
                
            # Buscamos todas las tarjetas de noticia
            articles = soup.find_all("article", class_="entry-preview")
            
            for article in articles:
                try:
                    # 1. Extraer Titulo y Link (etiqueta h2 clase entry-title)
                    h2 = article.find("h2", class_="entry-title")
                    if not h2:
                        continue
                    
                    a_tag = h2.find("a")
                    if not a_tag:
                        continue
                        
                    titulo = a_tag.get_text(strip=True)
                    link = a_tag.get("href")
                    
                    # 2. Extraer Imagen (primera etiqueta img dentro del articulo)
                    imagen_url = ""
                    img_tag = article.find("img")
                    if img_tag and img_tag.has_attr("src"):
                        imagen_url = img_tag["src"]
                        
                    # 3. Extraer Fecha (etiqueta p clase date)
                    fecha_raw = ""
                    p_date = article.find("p", class_="date")
                    if p_date:
                        # El texto suele ser "29 abril, 2026 / Noticias"
                        texto_fecha = p_date.get_text(strip=True)
                        # Cortamos por el '/' y nos quedamos con la primera parte
                        if "/" in texto_fecha:
                            fecha_raw = texto_fecha.split("/")[0].strip()
                        else:
                            fecha_raw = texto_fecha
                            
                    # Respaldo en caso de que no encuentre la fecha
                    if not fecha_raw:
                        fecha_raw = datetime.now().strftime("%Y-%m-%d")

                    # 4. Construir y guardar el diccionario
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