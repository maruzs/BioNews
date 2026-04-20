from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class SINIAScraper:
    def __init__(self):
        self.url = "https://sinia.mma.gob.cl/estudios-ambientales/"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en SINIA: {self.url}")
        # Esperamos a que carguen las tarjetas de estudios
        soup = self.engine.get_soup(self.url, wait_for_selector=".card-body")
        
        if not soup:
            return []

        news_list = []
        # Segun sinia.md la info esta en card-body
        cards = soup.select(".card-body")

        for card in cards:
            try:
                # 1. Titulo
                title_tag = card.select_one(".card-title")
                if not title_tag:
                    continue
                title = title_tag.get_text(strip=True)
                
                # 2. Fuente (esta en el subtitle)
                source_tag = card.select_one(".card-subtitle")
                fuente_especifica = source_tag.get_text(strip=True).replace("Fuente:", "") if source_tag else "SINIA"
                
                # 3. Enlace (el primero que encuentre con class card-link)
                link_tag = card.select_one("a.card-link")
                link = link_tag["href"] if link_tag else self.url
                
                # 4. Descripcion (la usaremos para el titulo si es muy corto o como info extra)
                # En tu DB solo guardamos titulo, asi que concatenaremos si es necesario
                
                news_list.append({
                    "titulo": f"Estudio: {title}",
                    "fecha": datetime.now().strftime("%Y-%m-%d"), # SINIA no muestra fecha clara en el grid
                    "link": link,
                    "imagen": "https://sinia.mma.gob.cl/wp-content/uploads/2018/09/logo-sinia.png", # Logo por defecto
                    "fuente": f"SINIA - {fuente_especifica[:15]}"
                })
            except Exception as e:
                print(f"Error procesando estudio de SINIA: {e}")
                continue

        print(f"Se encontraron {len(news_list)} estudios en SINIA")
        return news_list