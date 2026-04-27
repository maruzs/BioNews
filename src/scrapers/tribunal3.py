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
        
        for page in range(1, 3):
            if page == 1:
                url = f"{self.url_base}/"
            else:
                url = f"{self.url_base}/page/{page}/"
            
            print(f"Consultando pagina {page} del Tercer Tribunal...", flush=True)
            
            soup = self.engine.get_soup(url, wait_for_selector="article")
            
            if not soup:
                print(f"Error: No se pudo cargar la pagina {page}", flush=True)
                continue
                
            articles = soup.find_all("article")
            
            for article in articles:
                try:
                    h2 = article.find("h2", class_="entry-title")
                    if not h2: 
                        continue 
                        
                    title_tag = h2.find("a")
                    if not title_tag: 
                        continue
                        
                    titulo = title_tag.get_text(strip=True)
                    link = title_tag["href"]

                    imagen_url = ""
                    img_tag = article.find("img")
                    if img_tag:
                        imagen_url = img_tag.get("data-src") if img_tag.has_attr("data-src") else img_tag.get("src")
                    
                    fecha_raw = ""
                    
                    # 1. NUEVA LOGICA: Extraer desde la etiqueta <time> segun el analisis
                    time_tag = article.find("time", class_="entry-date")
                    #print("Intentando extraer fecha desde <time class='entry-date'>...", flush=True)
                    if not time_tag:
                        time_tag = article.find("time", class_="updated")
                        
                    if time_tag and time_tag.has_attr("datetime"):
                        fecha_iso = time_tag["datetime"] # Ej: 2026-04-23T08:59:30-04:00
                        if "T" in fecha_iso:
                            fecha_solo = fecha_iso.split("T")[0] # Nos quedamos con 2026-04-23
                            partes = fecha_solo.split("-")
                            if len(partes) == 3:
                                # Invertimos a DD-MM-YYYY para que el date_parser lo entienda
                                fecha_raw = f"{partes[2]}-{partes[1]}-{partes[0]}"
                    
                    # 2. Respaldos por si alguna noticia antigua no tiene la etiqueta time
                    if not fecha_raw:
                        print("Etiqueta <time> no encontrada o sin atributo datetime, intentando con <p class='date'>...", flush=True)
                        p_date = article.find("p", class_="date")
                        if p_date:
                            texto_fecha = p_date.get_text(strip=True)
                            if "/" in texto_fecha:
                                fecha_raw = texto_fecha.split("/")[0].strip()
                            else:
                                fecha_raw = texto_fecha
                                
                    if not fecha_raw:
                        meta_info = article.find("div", class_="fusion-meta-info")
                        if meta_info:
                            fecha_raw = meta_info.get_text(separator=" ", strip=True)
                            
                    # 3. Respaldo final absoluto
                    if not fecha_raw:
                        fecha_raw = datetime.now().strftime("%d-%m-%Y")

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