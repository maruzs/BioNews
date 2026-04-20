from .engine import ScrapingEngine
from ..utils.date_parser import parse_fecha

class SEALegalScraper:
    def __init__(self):
        # URL de busqueda de proyectos segun sea.md
        self.url = "https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php"
        self.engine = ScrapingEngine()

    def get_legal_data(self):
        print(f"Iniciando scraping legal en SEA: {self.url}")
        # Esperamos a que la tabla dinamica cargue una fila
        soup = self.engine.get_soup(self.url, wait_for_selector="table tbody tr")
        
        if not soup:
            return []

        legal_list = []
        # Segun sea.md, la tabla tiene filas tr con la info
        rows = soup.select("table tbody tr")

        for row in rows:
            try:
                cols = row.find_all("td")
                if len(cols) < 10:
                    continue
                
                # Nombre y Link (columna 0)
                link_tag = cols[0].find("a")
                nombre = link_tag.get_text(strip=True)
                link = link_tag["href"]
                
                # Tipo (columna 1 - DIA, EIA, etc.)
                tipo_ingreso = cols[1].get_text(strip=True)
                
                # Fecha (columna 8 - Fecha Presentacion)
                fecha_raw = cols[8].get_text(strip=True)
                
                # Estado (columna 10)
                estado = cols[10].get_text(strip=True)
                
                legal_list.append({
                    "nombre": nombre,
                    "fecha": parse_fecha(fecha_raw),
                    "estado": estado,
                    "tipo": f"Ingreso {tipo_ingreso}",
                    "fuente": "SEA",
                    "link": link
                })
            except Exception as e:
                print(f"Error procesando fila legal de SEA: {e}")
                continue

        print(f"Se encontraron {len(legal_list)} proyectos en SEA")
        return legal_list