from .engine import ScrapingEngine
from ..utils.date_parser import parse_fecha

class TribunalScraper:
    def __init__(self):
        self.url = "https://tribunalambiental.cl/resumen-de-noticias/"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en Tribunal Ambiental: {self.url}", flush=True)
        # Esperamos al contenedor principal del loop de noticias
        soup = self.engine.get_soup(self.url, wait_for_selector=".elementor-loop-container")
        
        if not soup:
            return []

        news_list = []
        # Segun tribunal.md, cada noticia es un e-loop-item
        items = soup.select(".e-loop-item")

        for item in items:
            try:
                # 1. Titulo
                title_tag = item.select_one(".elementor-widget-theme-post-title h3")
                if not title_tag:
                    continue
                title = title_tag.get_text(strip=True)
                
                # 2. Link al detalle (Boton 'Leer mas')
                link_tag = item.select_one("a.elementor-button-link")
                link = link_tag["href"] if link_tag else ""
                
                # 3. Imagen
                img_tag = item.select_one(".elementor-widget-theme-post-featured-image img")
                img_url = img_tag["src"] if img_tag else ""
                
                # 4. Fecha
                date_tag = item.select_one(".elementor-post-info__item--type-date time")
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                
                news_list.append({
                    "titulo": title,
                    "fecha": parse_fecha(fecha_raw),
                    "link": link,
                    "imagen": img_url,
                    "fuente": "Tribunal Ambiental"
                })
            except Exception as e:
                print(f"Error procesando noticia del Tribunal: {e}", flush=True)
                continue

        print(f"Se encontraron {len(news_list)} noticias en Tribunal Ambiental", flush=True)
        return news_list