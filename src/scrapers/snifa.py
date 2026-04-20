from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from ..utils.date_parser import parse_fecha
import time

class SNIFAScraper:
    def __init__(self):
        self.url_base = "https://snifa.sma.gob.cl/Sancionatorio"
        self.url_ficha_prefix = "https://snifa.sma.gob.cl"
        # Categorias principales segun snifa.md (puedes agregar mas)
        self.categorias = [
            {"val": "9", "nom": "Mineria"},
            {"val": "10", "nom": "Energia"},
            {"val": "12", "nom": "Vivienda e Inmobiliarios"},
            {"val": "3", "nom": "Saneamiento Ambiental"}
        ]

    def get_legal_data(self):
        print(f"Iniciando scraping en SNIFA: {self.url_base}")
        legal_data = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            # Usamos un contexto con User-Agent para evitar bloqueos
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            for cat in self.categorias:
                try:
                    print(f"Procesando categoria: {cat['nom']}")
                    page.goto(self.url_base, wait_until="networkidle", timeout=60000)
                    
                    # 1. Seleccionar categoria y buscar
                    page.select_option("select#categoria", cat["val"])
                    page.click("button.btn-default[onclick='buscar()']")
                    
                    # 2. Esperar a que la tabla cargue
                    page.wait_for_selector("table#tabla-sancionatorio tbody tr", timeout=30000)
                    
                    soup = BeautifulSoup(page.content(), "html.parser")
                    rows = soup.select("table#tabla-sancionatorio tbody tr")

                    # Procesamos solo los primeros 10 de cada categoria para mayor eficiencia
                    for row in rows[:10]:
                        cols = row.find_all("td")
                        if len(cols) < 8: continue

                        expediente = cols[1].get_text(strip=True)
                        nombre_razon = cols[3].get_text(strip=True)
                        estado = cols[6].get_text(strip=True)
                        link_rel = cols[7].find("a")["href"]
                        link_ficha = self.url_ficha_prefix + link_rel

                        # 3. Entrar a la ficha si el estado es 'En curso'
                        fecha_inicio = "No especificada"
                        ultima_act = "Sin documentos"

                        if "En curso" in estado:
                            # Abrimos una pestaña nueva para la ficha
                            ficha_page = context.new_page()
                            ficha_page.goto(link_ficha, wait_until="domcontentloaded", timeout=40000)
                            f_soup = BeautifulSoup(ficha_page.content(), "html.parser")
                            
                            # Extraer Fecha Inicio
                            # Buscamos el h4 que contiene 'Fecha Inicio'
                            h4_inicio = f_soup.find("h4", string=lambda x: x and "Fecha Inicio" in x)
                            if h4_inicio:
                                fecha_inicio = h4_inicio.find("i").get_text(strip=True)

                            # Extraer Fecha del ultimo documento
                            # La tabla de documentos tiene la fecha en la 4ta columna
                            doc_rows = f_soup.select("table.tabla-resultado-busqueda tbody tr")
                            if doc_rows:
                                # El ultimo documento es la ultima fila
                                last_doc_cols = doc_rows[-1].find_all("td")
                                if len(last_doc_cols) >= 4:
                                    ultima_act = last_doc_cols[3].get_text(strip=True)
                            
                            ficha_page.close()

                        legal_data.append({
                            "nombre": f"{expediente} - {nombre_razon}",
                            "fecha": parse_fecha(ultima_act if ultima_act != "Sin documentos" else fecha_inicio),
                            "estado": estado,
                            "tipo": f"Sancionatorio - {cat['nom']}",
                            "fuente": "SNIFA",
                            "link": link_ficha
                        })

                except Exception as e:
                    print(f"Error en categoria {cat['nom']}: {e}")
                    continue

            browser.close()
            print(f"Finalizado: Se obtuvieron {len(legal_data)} registros de SNIFA")
            return legal_data