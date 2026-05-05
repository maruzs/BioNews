from .engine import ScrapingEngine
from ..utils.date_parser import parse_fecha
import requests
import urllib3
import hashlib
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SernageominScraper:
    def __init__(self):
        self.url = "https://www.sernageomin.cl/category/noticias/"
        self.engine = ScrapingEngine()

    def get_latest_news(self, pages=3):
        news_list = []
        for p in range(1, pages + 1):
            url = self.url if p == 1 else f"{self.url}page/{p}/"
            print(f"Iniciando scraping en Sernageomin (Pagina {p}): {url}", flush=True)
            soup = self.engine.get_soup(url, wait_for_selector=".fusion-posts-container")
            
            if not soup:
                break

            articles = soup.select("article.fusion-post-grid")
            if not articles: break

            for article in articles:
                try:
                    title_tag = article.select_one(".entry-title a")
                    if not title_tag:
                        continue
                    
                    title = title_tag.get_text(strip=True)
                    link = title_tag["href"]
                    
                    # Imagen
                    imagen_url = ""
                    # Buscamos la imagen en el contenedor fusion-image-wrapper
                    img_container = article.select_one(".fusion-image-wrapper img")
                    if img_container:
                        imagen_url = img_container.get("src")
                    
                    if not imagen_url:
                        # Respaldo logo
                        imagen_url = "logo_sernageomin.png"
                    
                    date_tag = article.select_one(".fusion-single-line-meta span:nth-child(3)")
                    fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                    
                    if not fecha_raw: continue

                    news_list.append({
                        "titulo": title,
                        "fecha": parse_fecha(fecha_raw),
                        "link": link,
                        "imagen": imagen_url,
                        "fuente": "Sernageomin"
                    })
                except Exception as e:
                    print(f"Error en noticia de Sernageomin: {e}", flush=True)
                    continue

        print(f"Se encontraron {len(news_list)} noticias en Sernageomin", flush=True)
        return news_list