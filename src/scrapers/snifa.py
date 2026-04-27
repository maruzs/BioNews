import traceback
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
from ..utils.date_parser import parse_fecha
from ..database.manager import DatabaseManager

class SnifaScraper:
    def __init__(self):
        self.url_base = "https://snifa.sma.gob.cl"
        self.url_home = f"{self.url_base}/Sancionatorio"
        self.db = DatabaseManager()
        
        # Ahora solo pasamos los nombres (sin tildes), el codigo buscara su ID en vivo
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
        print("Iniciando scraping legal en SNIFA (Sancionatorios)", flush=True)
        all_legal_data = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                for cat_nombre in self.categorias:
                    print(f"\n--- Consultando categoria: {cat_nombre} ---", flush=True  )
                    
                    try:
                        # 1. Cargar pagina limpia
                        page.goto(self.url_home, wait_until="networkidle", timeout=60000)
                        page.wait_for_selector("#categoria", state="visible", timeout=15000)
                        
                        # 2. Buscar el valor (value) de la categoria dinamicamente
                        options = page.locator("#categoria option").all()
                        target_val = None
                        search_text = cat_nombre.lower()
                        
                        for opt in options:
                            # Obtenemos texto de la opcion y quitamos tildes para comparar seguro
                            opt_text = opt.inner_text().lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                            if search_text in opt_text:
                                target_val = opt.get_attribute("value")
                                break
                        
                        if not target_val:
                            print(f"No se encontro la opcion en el dropdown para: {cat_nombre}",flush=True)
                            continue
                            
                        # 3. Seleccionamos usando el valor real que extrajimos
                        page.select_option("#categoria", value=target_val)
                        
                        # 4. Click y ESPERAR LA REDIRECCION
                        boton_buscar = page.locator("button:has-text('Buscar')").first
                        with page.expect_navigation(wait_until="domcontentloaded", timeout=30000):
                            boton_buscar.click()
                        
                        # 5. En /Resultado, esperamos la tabla
                        page.wait_for_selector("table tbody tr", state="visible", timeout=30000)
                        
                        soup = BeautifulSoup(page.content(), "html.parser")
                        rows = soup.select("table tbody tr")
                        
                        if not rows:
                            print(f"No se encontraron filas para {cat_nombre}",flush=True)
                            continue
                            
                        print(f"Detectadas {len(rows)} filas en la pagina.")

                        # 6. Parsear
                        datos_categoria = self._parse_html_data(rows[:15], cat_nombre)
                        all_legal_data.extend(datos_categoria)
                        print(f"Guardados {len(datos_categoria)} registros de {cat_nombre}", flush=True)

                    except Exception as e:
                        print(f"Error procesando categoria {cat_nombre}: {str(e)}", flush=True)
                        continue

            except Exception:
                print("Error critico en el flujo de navegacion de SNIFA", flush=True)
                traceback.print_exc()
            finally:
                browser.close()

        print(f"\nExito: Se procesaron {len(all_legal_data)} registros totales de SNIFA",flush=True )
        return all_legal_data

    def _parse_html_data(self, rows, tipo_categoria):
        legal_list = []
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        
        for row in rows:
            try:
                tds = row.find_all("td")
                if len(tds) < 4:
                    continue
                    
                rol = "Sin Rol"
                link = ""
                unidad_fiscalizable = ""
                instalacion_text = ""
                estado_text = "Desconocido"
                
                # Busqueda dinamica por data-label para ser inmunes al orden de las columnas
                for td in tds:
                    label = td.get("data-label", "")
                    
                    if label == "Expediente":
                        rol = td.get_text(strip=True)
                    elif label == "Unidad Fiscalizable":
                        unidad_fiscalizable = td.get_text(" ", strip=True)
                    elif label == "Instalación" or label == "Instalacion":
                        instalacion_text = td.get_text(" ", strip=True)
                    elif label == "Estado":
                        estado_text = td.get_text(strip=True)
                    elif label == "Detalle":
                        a_tag = td.find("a")
                        if a_tag:
                            href = a_tag.get("href", "")
                            link = f"{self.url_base}{href}" if href.startswith("/") else href

                # Si no pudimos extraer el enlace, lo descartamos
                if not link:
                    continue
                
                if unidad_fiscalizable:
                    nombre_completo = f"{rol} {unidad_fiscalizable}"
                else:
                    nombre_completo = f"{rol} - {instalacion_text}" if instalacion_text else rol
                
                legal_list.append({
                    "nombre": nombre_completo,
                    "fecha": parse_fecha(fecha_hoy),
                    "estado": estado_text,
                    "tipo": f"Sancionatorio ({tipo_categoria})",
                    "fuente": "SNIFA",
                    "link": link
                })
                
            except Exception as e:
                print(f"Error parseando una fila especifica en SNIFA: {e}", flush=True)
                continue
                
        return legal_list