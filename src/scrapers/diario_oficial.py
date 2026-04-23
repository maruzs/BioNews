from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class DiarioOficialScraper:
    def __init__(self):
        self.url = "https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php"
        self.engine = ScrapingEngine()
        # Se agregan palabras clave de prueba como hacienda, mineria y transporte
        self.keywords = ["medioambiente", "ecologia", "seremi", "superintendencia", "mma", "sea", "sma", "biodiversidad", "sustentable"]

    def get_latest_news(self):
        print(f"Iniciando scraping en Diario Oficial: {self.url}")
        soup = self.engine.get_soup(self.url, wait_for_selector=".wrapsection")
        
        if not soup:
            return []

        news_list = []
        fecha_hoy = datetime.now().strftime("%d-%m-%Y")
        
        rows = soup.select("tr.content")
        
        for row in rows:
            text_content = row.get_text().lower()
            
            if any(key in text_content for key in self.keywords):
                try:
                    desc_cell = row.find("td")
                    link_tag = row.find("a")
                    
                    if desc_cell and link_tag:
                        titulo_limpio = desc_cell.get_text(strip=True).split("Ver PDF")[0]
                        pdf_link = link_tag["href"]
                        
                        news_list.append({
                            "titulo": f"Actualizacion: {titulo_limpio}",
                            "fecha": parse_fecha(f"Diario Oficial {fecha_hoy}"),
                            "link": pdf_link,
                            "imagen": "https://www.diariooficial.interior.gob.cl/media/logo-diario-oficial.png",
                            "fuente": "Diario Oficial"
                        })
                except Exception as e:
                    print(f"Error procesando fila Diario Oficial: {e}")

        print(f"Se encontraron {len(news_list)} publicaciones en Diario Oficial")
        return news_list