from .engine import ScrapingEngine
from urllib.parse import urljoin
from ..utils.date_parser import parse_fecha

class SBAPScraper:
    def __init__(self):
        self.url = "https://sbap.gob.cl/sala-de-prensa/noticias-y-comunicados"
        self.base_url = "https://sbap.gob.cl"
        self.engine = ScrapingEngine()

    def get_latest_news(self):
        print(f"Iniciando scraping en SBAP: {self.url}", flush=True)
        soup = self.engine.get_soup(self.url, wait_for_selector=".noticias-prensa")
        
        if not soup:
            return []

        news_list = []

        # 1. Noticias principales
        for big in soup.select(".not-big"):
            try:
                title_tag = big.select_one("h3 a")
                img_tag = big.select_one(".not-big__img img")
                date_tag = big.select_one(".fecha")
                
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                
                news_list.append({
                    "titulo": title_tag.get_text(strip=True),
                    "fecha": parse_fecha(fecha_raw) if fecha_raw else "2026-04-20",
                    "link": urljoin(self.base_url, title_tag["href"]),
                    "imagen": urljoin(self.base_url, img_tag["src"]) if img_tag else "",
                    "fuente": "SBAP"
                })
            except Exception as e:
                print(f"Error en noticia principal SBAP: {e}", flush=True)

        # 2. Otras noticias secundarias
        for otra in soup.select(".otra-not"):
            try:
                title_tag = otra.select_one("h3 a")
                news_list.append({
                    "titulo": title_tag.get_text(strip=True),
                    "fecha": "2026-04-20", 
                    "link": urljoin(self.base_url, title_tag["href"]),
                    "imagen": "", 
                    "fuente": "SBAP"
                })
            except Exception as e:
                print(f"Error en otra-not SBAP: {e}", flush=True)

        # 3. Grid inferior de noticias
        for card in soup.select(".card-not"):
            try:
                title_tag = card.select_one("h4")
                img_tag = card.select_one(".card-not__img img")
                date_tag = card.select_one(".fecha")
                
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
                
                news_list.append({
                    "titulo": title_tag.get_text(strip=True),
                    "fecha": parse_fecha(fecha_raw) if fecha_raw else "2026-04-20",
                    "link": urljoin(self.base_url, card["href"]),
                    "imagen": urljoin(self.base_url, img_tag["src"]) if img_tag else "",
                    "fuente": "SBAP"
                })
            except Exception as e:
                print(f"Error en card SBAP: {e}", flush=True)

        print(f"Se encontraron {len(news_list)} noticias en SBAP", flush=True)
        return news_list