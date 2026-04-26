import re
from .engine import ScrapingEngine
from urllib.parse import urljoin
from datetime import datetime
from ..utils.date_parser import parse_fecha

class SBAPScraper:
    def __init__(self):
        self.url = "https://sbap.gob.cl/sala-de-prensa/noticias-y-comunicados"
        self.base_url = "https://sbap.gob.cl"
        self.engine = ScrapingEngine()

    def _extraer_fecha(self, element, href):
        fecha_raw = ""
        
        # 1. Intentar desde la etiqueta HTML clase fecha
        date_tag = element.select_one(".fecha")
        if date_tag:
            fecha_raw = date_tag.get_text(strip=True)
        
        # 2. Si falla, usar el super-truco: extraer de la URL
        if not fecha_raw and href:
            match = re.search(r'/detalle/(\d{4})/(\d{2})/(\d{2})/', href)
            if match:
                a, m, d = match.groups()
                fecha_raw = f"{d}-{m}-{a}"
                
        # 3. Respaldo final
        if not fecha_raw:
            fecha_raw = datetime.now().strftime("%d-%m-%Y")
            
        return parse_fecha(fecha_raw)

    def get_latest_news(self):
        print(f"Iniciando scraping en SBAP: {self.url}", flush=True)
        soup = self.engine.get_soup(self.url, wait_for_selector=".noticias-prensa")
        
        if not soup:
            return []

        news_list = []

        # 1. Noticias principales (.not-big)
        for big in soup.select(".not-big"):
            try:
                title_tag = big.select_one("h3 a")
                img_tag = big.select_one(".not-big__img img")
                href = title_tag["href"] if title_tag else ""
                
                if title_tag:
                    news_list.append({
                        "titulo": title_tag.get_text(strip=True),
                        "fecha": self._extraer_fecha(big, href),
                        "link": urljoin(self.base_url, href),
                        "imagen": urljoin(self.base_url, img_tag["src"]) if img_tag else "",
                        "fuente": "SBAP"
                    })
            except Exception as e:
                print(f"Error en not-big SBAP: {e}", flush=True)

        # 2. Grid derecho (Otras noticias) (.otra-not)
        for otra in soup.select(".otra-not"):
            try:
                title_tag = otra.select_one("h3 a")
                href = title_tag["href"] if title_tag else ""
                
                if title_tag:
                    news_list.append({
                        "titulo": title_tag.get_text(strip=True),
                        "fecha": self._extraer_fecha(otra, href),
                        "link": urljoin(self.base_url, href),
                        "imagen": "", 
                        "fuente": "SBAP"
                    })
            except Exception as e:
                print(f"Error en otra-not SBAP: {e}", flush=True)

        # 3. Grid inferior de noticias (.card-not)
        for card in soup.select(".card-not"):
            try:
                title_tag = card.select_one("h4")
                img_tag = card.select_one(".card-not__img img")
                href = card["href"] if card.has_attr("href") else ""
                
                if title_tag:
                    news_list.append({
                        "titulo": title_tag.get_text(strip=True),
                        "fecha": self._extraer_fecha(card, href),
                        "link": urljoin(self.base_url, href),
                        "imagen": urljoin(self.base_url, img_tag["src"]) if img_tag else "",
                        "fuente": "SBAP"
                    })
            except Exception as e:
                print(f"Error en card-not SBAP: {e}", flush=True)

        print(f"Exito: Se encontraron {len(news_list)} noticias en SBAP", flush=True)
        return news_list