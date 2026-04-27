import traceback
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager

class SnifaFiscalizacionScraper:
    def __init__(self):
        self.url_base = "https://snifa.sma.gob.cl"
        self.url_home = f"{self.url_base}/Fiscalizacion"
        self.db = DatabaseManager()
        
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
        print("Iniciando scraping legal en SNIFA (Fiscalizaciones)", flush=True)
        all_legal_data = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                for cat_nombre in self.categorias:
                    print(f"\n--- Consultando categoria: {cat_nombre} ---", flush=True)
                    
                    try:
                        # 1. Cargar pagina limpia
                        page.goto(self.url_home, wait_until="networkidle", timeout=60000)
                        page.wait_for_selector("#categoria", state="visible", timeout=15000)
                        
                        # 2. Seleccionar categoria
                        options = page.locator("#categoria option").all()
                        target_val = None
                        search_text = cat_nombre.lower()
                        
                        for opt in options:
                            opt_text = opt.inner_text().lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                            if search_text in opt_text:
                                target_val = opt.get_attribute("value")
                                break
                        
                        if not target_val:
                            print(f"No se encontro la opcion para: {cat_nombre}", flush=True)
                            continue
                            
                        page.select_option("#categoria", value=target_val)
                        
                        # 3. Escribir Expediente apuntando EXACTAMENTE al ID correcto
                        page.locator("input#expediente").fill("DFZ-2026")
                        print("Filtro DFZ-2026 aplicado en el campo Expediente.", flush=True)
                        
                        # 4. Click y esperar redireccion
                        boton_buscar = page.locator("button:has-text('Buscar')").first
                        with page.expect_navigation(wait_until="domcontentloaded", timeout=40000):
                            boton_buscar.click()
                        
                        # 5. Bucle de espera inteligente para AJAX
                        print("Esperando que el servidor devuelva los datos (AJAX)...")
                        page.wait_for_timeout(5000)
                        
                        for _ in range(4):
                            soup = BeautifulSoup(page.content(), "html.parser")
                            rows = soup.select("table tbody tr")
                            if rows:
                                tds = rows[0].find_all("td")
                                texto_fila = rows[0].get_text().lower()
                                if len(tds) < 4 and ("procesando" in texto_fila or "cargando" in texto_fila):
                                    print("La tabla sigue cargando, esperando 4 segundos extra...")
                                    page.wait_for_timeout(4000)
                                else:
                                    break 
                            else:
                                break
                        
                        # 6. Extraer HTML final
                        soup = BeautifulSoup(page.content(), "html.parser")
                        rows = soup.select("table tbody tr")
                        
                        if not rows:
                            print(f"No se encontraron filas para {cat_nombre}")
                            continue
                            
                        if len(rows) == 1 and len(rows[0].find_all("td")) < 4:
                            print(f"Sin resultados reales para {cat_nombre} en DFZ-2026")
                            continue

                        print(f"Detectadas {len(rows)} fiscalizaciones en la pagina.")

                        # 7. Parsear
                        datos_categoria = self._parse_html_data(rows[:15], cat_nombre)
                        all_legal_data.extend(datos_categoria)
                        print(f"Guardados {len(datos_categoria)} registros de {cat_nombre}")

                    except Exception as e:
                        print(f"Error procesando categoria {cat_nombre}: {str(e)}", flush=True)
                        continue

            except Exception:
                print("Error critico en el flujo de navegacion de SNIFA Fiscalizaciones", flush=True)
                traceback.print_exc()
            finally:
                browser.close()

        print(f"\nExito: Se procesaron {len(all_legal_data)} registros totales de SNIFA Fiscalizaciones", flush=True)
        return all_legal_data

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
                unidad_fiscalizable = ""
                link = ""
                estado_text = "Desconocido"
                
                # Extraccion flexible por data-label
                for td in tds:
                    label = td.get("data-label", "")
                    
                    if label == "Expediente":
                        expediente = td.get_text(strip=True)
                    elif label == "Nombre razón social" or label == "Nombre razon social":
                        razon_social = td.get_text(strip=True)
                    elif label == "Unidad Fiscalizable":
                        unidad_fiscalizable = td.get_text(strip=True)
                    elif label == "Estado":
                        estado_text = td.get_text(strip=True)
                    elif label == "Detalle":
                        a_tag = td.find("a")
                        if a_tag:
                            href = a_tag.get("href", "")
                            link = f"{self.url_base}{href}" if href.startswith("/") else href

                if not link:
                    continue
                
                if unidad_fiscalizable:
                    nombre_completo = f"{expediente} {unidad_fiscalizable}"
                else:
                    nombre_completo = f"{expediente} - {razon_social}" if razon_social else expediente
                
                legal_list.append({
                    "nombre": nombre_completo,
                    "fecha": parse_fecha(fecha_hoy),
                    "estado": estado_text,
                    "tipo": f"Fiscalizacion ({tipo_categoria})",
                    "fuente": "SNIFA",
                    "link": link
                })
                
            except Exception as e:
                print(f"Error parseando fila de SNIFA Fiscalizaciones: {e}", flush=True)
                continue
                
        return legal_list