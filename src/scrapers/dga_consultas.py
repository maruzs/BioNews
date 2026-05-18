import os
from src.database.manager import DatabaseManager
from datetime import datetime
from bs4 import BeautifulSoup
from .engine import ScrapingEngine
from ..database.manager import DatabaseManager

class DGAConsultasScraper:
    def __init__(self):
        self.url = "https://dga.mop.gob.cl/consulta-publica/"
        self.engine = ScrapingEngine()
        self.db = DatabaseManager()

    def _get_connection(self):
        return self.db.get_connection()

    def scrape(self):
        print(f"Scrapeando consultas DGA: {self.url}")
        soup = self.engine.get_soup(self.url, wait_for_selector=".et_pb_section_1")
        if not soup:
            print("No se pudo obtener el contenido de DGA.")
            return []

        results = []
        # Buscamos los bloques de 'blurb' que contienen los formularios
        blurbs = soup.select(".et_pb_module.et_pb_blurb")
        
        for blurb in blurbs:
            try:
                # 1. Nombre y URL del formulario
                header_link = blurb.select_one(".et_pb_module_header a")
                if not header_link:
                    continue
                
                nombre = header_link.get_text(strip=True)
                url_form = header_link['href']
                
                # 2. ID (lo que está después de .gl/ en el URL)
                # Ejemplo: http://forms.gle/7frq6iWfj41MDeuy6 -> 7frq6iWfj41MDeuy6
                form_id = ""
                if ".gl/" in url_form:
                    form_id = url_form.split(".gl/")[-1].split("?")[0]
                else:
                    # Fallback si no es un link de Google Forms corto
                    form_id = url_form.split("/")[-1].split("?")[0]
                
                if not form_id:
                    continue

                # 3. Imagen (Icono)
                # El usuario dice que carga con JS pero sin JS funciona.
                # En el snippet se ve un span con una letra que es el icono.
                # Buscamos el contenedor de la imagen
                img_container = blurb.select_one(".et_pb_main_blurb_image")
                # Intentamos obtener un icono o imagen
                imagen = ""
                if img_container:
                    # Si hay una imagen real
                    img_tag = img_container.find("img")
                    if img_tag:
                        imagen = img_tag.get("src", "")
                    else:
                        # Si es un icono de Divi (span con texto)
                        icon_span = img_container.find("span", class_="et-pb-icon")
                        if icon_span:
                            imagen = icon_span.get_text(strip=True)

                results.append({
                    "id": form_id,
                    "nombre": nombre,
                    "imagen": imagen,
                    "url": url_form
                })
            except Exception as e:
                print(f"Error procesando un blurb de DGA: {e}")

        return results

    def save_results(self, items):
        if not items:
            return 0

        conn = self._get_connection()
        cursor = conn.cursor()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        nuevos = 0
        
        # Primero, vamos a manejar la actualización de la tabla.
        # El usuario dice: "Si en un futuro desaparece uno de esos formularios y/o hay uno nuevo debera actualizarse borrando los formularios viejos y agregando el nuevo"
        # Esto significa que la tabla debe reflejar EXACTAMENTE lo que está en la página ahora.
        
        # 1. Obtener IDs actuales en la base de datos
        cursor.execute("SELECT id FROM dga_consultas")
        db_ids = {row[0] for row in cursor.fetchall()}
        
        current_ids = {item['id'] for item in items}
        
        # 2. Borrar los que ya no están en la página
        ids_to_delete = db_ids - current_ids
        for id_to_del in ids_to_delete:
            cursor.execute("DELETE FROM dga_consultas WHERE id = %s", (id_to_del,))
        
        # 3. Insertar o actualizar los actuales
        for item in items:
            cursor.execute("SELECT 1 FROM dga_consultas WHERE id = %s", (item['id'],))
            exists = cursor.fetchone()
            
            cursor.execute("""
                INSERT INTO dga_consultas (id, nombre, imagen, url, fecha_scraping)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT(id) DO UPDATE SET
                    nombre=excluded.nombre,
                    imagen=excluded.imagen,
                    url=excluded.url
            """, (item['id'], item['nombre'], item['imagen'], item['url'], now))
            
            if not exists:
                nuevos += 1

        conn.commit()
        conn.close()
        return nuevos

    def run(self):
        items = self.scrape()
        nuevos = self.save_results(items)
        print(f"Scraping DGA finalizado. Nuevos registros: {nuevos}")
        return nuevos

if __name__ == "__main__":
    scraper = DGAConsultasScraper()
    scraper.run()
