import traceback
import re
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager

class SnifaIngresoScraper:
    def __init__(self):
        self.url_base = "https://snifa.sma.gob.cl"
        self.url_home = f"{self.url_base}/RequerimientoIngreso"
        self.db = DatabaseManager()
        
        # Categorias de interes segun la investigacion
        self.categorias = [
            "Agroindustrias",
            "Energia",
            "Infraestructura Portuaria",
            "Instalacion fabril",
            "Mineria",
            "Saneamiento Ambiental",
            "Transportes y almacenajes"
        ]

    def get_legal_data(self):
        print("Iniciando scraping legal en SNIFA (Requerimientos de Ingreso)", flush=True)
        all_legal_data = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                for cat_nombre in self.categorias:
                    print(f"--- Consultando categoria: {cat_nombre} ---", flush=True)
                    
                    try:
                        # 1. Cargar pagina limpia (equivale a reiniciar busqueda)
                        page.goto(self.url_home, wait_until="networkidle", timeout=60000)
                        page.wait_for_selector("#categoria", state="visible", timeout=15000)
                        
                        # 2. Buscar el value de la categoria dinamicamente para evitar errores de ID
                        options = page.locator("#categoria option").all()
                        target_val = None
                        search_text = cat_nombre.lower()
                        
                        for opt in options:
                            opt_text = opt.inner_text().lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                            if search_text in opt_text:
                                target_val = opt.get_attribute("value")
                                break
                        
                        if not target_val:
                            print(f"No se encontro el ID para: {cat_nombre}", flush=True)
                            continue
                            
                        # 3. Seleccionar y buscar
                        page.select_option("#categoria", value=target_val)
                        
                        boton_buscar = page.locator("button:has-text('Buscar')").first
                        with page.expect_navigation(wait_until="domcontentloaded", timeout=30000):
                            boton_buscar.click()
                        
                        # 4. Esperar tabla de resultados
                        page.wait_for_selector("table tbody tr", state="visible", timeout=30000)
                        
                        soup = BeautifulSoup(page.content(), "html.parser")
                        rows = soup.select("table tbody tr")
                        
                        if not rows:
                            continue

                        # 5. Parsear datos de la categoria
                        datos_categoria = self._parse_html_data(rows, cat_nombre)
                        all_legal_data.extend(datos_categoria)

                    except Exception as e:
                        print(f"Error en categoria {cat_nombre}: {str(e)}", flush=True)
                        continue

            except Exception:
                print("Error critico en el flujo de SNIFA Ingreso", flush=True)
                traceback.print_exc()
            finally:
                browser.close()

        # 6. ORDENAMIENTO POR ID (El numero al final del link indica el orden real)
        # Segun la investigacion, los mas nuevos tienen un numero mas alto.
        all_legal_data.sort(key=self._extract_id, reverse=True)
        
        print(f"Exito: Se procesaron {len(all_legal_data)} registros totales ordenados", flush=True )
        return all_legal_data

    def _extract_id(self, item):
        # Extrae el numero final del link (ej: Ficha/10 -> 10)
        match = re.search(r'/(\d+)$', item['link'])
        return int(match.group(1)) if match else 0

    def _parse_html_data(self, rows, tipo_categoria):
        legal_list = []
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        
        for row in rows:
            try:
                tds = row.find_all("td")
                if len(tds) < 5:
                    continue
                    
                expediente = "Sin Expediente"
                razon_social = ""
                link = ""
                estado_text = "Desconocido"
                
                # Extraccion basada en data-label segun el analisis del .md
                for td in tds:
                    label = td.get("data-label", "")
                    
                    if label == "Expediente":
                        expediente = td.get_text(strip=True)
                    elif label == "Nombre razón social" or label == "Nombre razon social":
                        razon_social = td.get_text(strip=True)
                    elif label == "Estado":
                        estado_text = td.get_text(strip=True)
                    elif label == "Detalle":
                        a_tag = td.find("a")
                        if a_tag:
                            href = a_tag.get("href", "")
                            link = f"{self.url_base}{href}" if href.startswith("/") else href

                if not link:
                    continue
                
                # Combinamos Expediente y Razon Social para el nombre en el dashboard
                nombre_completo = f"{expediente} - {razon_social}" if razon_social else expediente
                
                legal_list.append({
                    "nombre": nombre_completo,
                    "fecha": parse_fecha(fecha_hoy),
                    "estado": estado_text,
                    "tipo": f"Ingreso SEIA ({tipo_categoria})",
                    "fuente": "SNIFA",
                    "link": link
                })
                
            except Exception as e:
                print(f"Error parseando fila de SNIFA Requerimientos de Ingreso: {e}", flush=True)
                continue
                
        return legal_list