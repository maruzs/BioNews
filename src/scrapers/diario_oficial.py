import hashlib
from .engine import ScrapingEngine
from datetime import datetime
from ..utils.date_parser import parse_fecha

class DiarioOficialScraper:
    def __init__(self):
        self.url_home = "https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php"
        self.logo_gob = "https://www.diariooficial.interior.gob.cl/edicionelectronica/css/bitmaps/logo_do.jpg"
        self.engine = ScrapingEngine()
        
        self.target_ministerios = {
            "MINISTERIO DEL MEDIO AMBIENTE": "Medioambiente",
            "MINISTERIO DE MINERÍA": "Mineria",
            "MINISTERIO DE ENERGÍA": "Energia",
            "MINISTERIO DE AGRICULTURA": "Agricultura",
            "MINISTERIO DE OBRAS PÚBLICAS": "Obras Publicas",
            "MINISTERIO DE SALUD": "Salud"
        }

    def get_latest_news(self):
        print(f"Iniciando scraping en Diario Oficial: {self.url_home}")
        soup = self.engine.get_soup(self.url_home, wait_for_selector=".wrapsection")
        
        if not soup:
            print("Error: No se pudo cargar el contenido de la pagina")
            return []

        news_list = []
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        
        rows = soup.find_all("tr")
        current_min = None
        current_sub = ""
        
        for row in rows:
            td_title4 = row.find("td", class_="title4")
            if td_title4:
                header_text = td_title4.get_text(" ", strip=True).upper().replace('\xa0', ' ')
                
                match = None
                for key, val in self.target_ministerios.items():
                    if key in header_text:
                        match = val
                        break
                
                if match:
                    current_min = match
                    current_sub = "" 
                else:
                    current_min = None
                    current_sub = ""
                continue

            td_title5 = row.find("td", class_="title5")
            if td_title5:
                current_sub = td_title5.get_text(" ", strip=True)
                continue

            if current_min and "content" in row.get("class", []):
                try:
                    tds = row.find_all("td")
                    if tds:
                        info_limpia = tds[0].get_text(" ", strip=True)
                        info_limpia = info_limpia.split("Ver PDF")[0].strip()
                        
                        if info_limpia:
                            prefijo_sub = f"{current_sub} " if current_sub else ""
                            titulo_final = f"Diario Oficial - {current_min}\n{prefijo_sub}{info_limpia}"
                            
                            # SOLUCION: Generamos un hash unico basado en el texto de la noticia
                            # Esto asegura que el "link" sea unico en SQLite pero siga abriendo el home
                            id_unico = hashlib.md5(titulo_final.encode('utf-8')).hexdigest()
                            link_unico = f"{self.url_home}#{id_unico}"
                            
                            news_list.append({
                                "titulo": titulo_final,
                                "fecha": fecha_hoy,
                                "link": link_unico,
                                "imagen": self.logo_gob,
                                "fuente": "Diario Oficial"
                            })
                except Exception as e:
                    print(f"Error procesando fila de {current_min}: {e}")

        print(f"Exito: Se encontraron {len(news_list)} registros validos en el Diario Oficial")
        return news_list