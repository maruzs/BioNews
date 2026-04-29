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

    def get_latest_news(self):
        print(f"Iniciando scraping en Sernageomin: {self.url}", flush=True)
        # Esperamos al contenedor del grid de noticias
        soup = self.engine.get_soup(self.url, wait_for_selector=".fusion-posts-container")
        
        if not soup:
            return []

        news_list = []
        # Buscamos los articulos segun sernageomin.md
        articles = soup.select("article.fusion-post-grid")

        for article in articles:
            try:
                # Titulo y Link
                title_tag = article.select_one(".entry-title a")
                if not title_tag:
                    continue
                
                title = title_tag.get_text(strip=True)
                link = title_tag["href"]
                
                # Imagen (usar solo el logo de Sernageomin segun lo solicitado)
                local_img_path = "logo_sernageomin.png"
                img_url = "logo_sernageomin.png"
                
                # Fecha: segun el md esta en el tercer span del meta
                # Formato esperado: "16 de Abril de 2026"
                date_tag = article.select_one(".fusion-single-line-meta span:nth-child(3)")
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                
                news_list.append({
                    "titulo": title,
                    "fecha": parse_fecha(fecha_raw),
                    "link": link,
                    "imagen": local_img_path if local_img_path else img_url,
                    "fuente": "Sernageomin"
                })
            except Exception as e:
                print(f"Error en noticia de Sernageomin: {e}", flush=True)
                continue

        print(f"Se encontraron {len(news_list)} noticias en Sernageomin", flush=True    )
        return news_list