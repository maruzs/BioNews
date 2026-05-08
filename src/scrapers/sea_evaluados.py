"""
Scraper de Proyectos Evaluados - SEA
Consulta la API publica del SEA y guarda en la tabla sea_proyectos_evaluados
"""
import requests
import json
import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

class SEAEvaluadosScraper:
    def run(self):
        url_base = "https://seia.sea.gob.cl"
        url_buscar = f"{url_base}/busqueda/buscarProyectoResumen.php"
        url_api = f"{url_base}/busqueda/buscarProyectoResumenAction.php"
        
        # Verificar si la tabla esta vacia para decidir si hacer scraping completo o solo de hoy
        is_empty = True
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM sea_proyectos_evaluados")
            count = cursor.fetchone()[0]
            if count > 0:
                is_empty = False
        except Exception as e:
            print(f"Error verificando DB: {e}")
        finally:
            conn.close()

        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": url_base,
            "Referer": url_buscar
        })
        
        # Visita inicial para setear cookies
        try:
            session.get(url_buscar, timeout=15)
        except Exception as e:
            print(f"Error en GET inicial: {e}")
            return 0

        fecha_hoy = datetime.now().strftime('%d/%m/%Y')
        limit = 100
        offset = 1
        
        payload_base = {
            "nombre": "",
            "titular": "",
            "folio": "",
            "selectRegion": "",
            "selectComuna": "",
            "tipoPresentacion": "Ambos",
            "projectStatus": "",
            "PresentacionMin": "" if is_empty else fecha_hoy,
            "PresentacionMax": "" if is_empty else fecha_hoy,
            "CalificaMin": "",
            "CalificaMax": "",
            "sectores_economicos": "",
            "razoningreso": "",
            "id_tipoexpediente": "",
            "limit": limit,
            "orderColumn": "FECHA_PRESENTACION",
            "orderDir": "desc"
        }

        nuevos_registros = 0
        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print(f"Iniciando scraping SEA Proyectos Evaluados. {'Modo completo' if is_empty else 'Modo diario'}.")

        while True:
            payload = payload_base.copy()
            payload["offset"] = offset
            
            try:
                response = session.post(url_api, data=payload, timeout=30)
                if response.status_code != 200:
                    print(f"Error: Codigo {response.status_code} en offset {offset}")
                    break
                    
                data = response.json()
                if not data.get("status") or not data.get("data"):
                    break
                
                items = data.get("data", [])
                if len(items) == 0:
                    break
                    
                for item in items:
                    exp_id = item.get("EXPEDIENTE_ID", "")
                    nombre = item.get("EXPEDIENTE_NOMBRE", "")
                    titular = item.get("TITULAR", "")
                    via_ingreso = item.get("WORKFLOW_DESCRIPCION", "")
                    estado = item.get("ESTADO_PROYECTO", "")
                    razon = item.get("RAZON_INGRESO", "")
                    fecha = item.get("FECHA_PRESENTACION_FORMAT", "")
                    subestado = item.get("SUSPENDIDO", "")
                    tipo = item.get("TIPO_PROYECTO", "")
                    url = item.get("EXPEDIENTE_URL_PPAL", "")
                    
                    cursor.execute("SELECT 1 FROM sea_proyectos_evaluados WHERE id = ?", (exp_id,))
                    exists = cursor.fetchone()
                    
                    if exists:
                        # Actualizar estado y url, etc.
                        cursor.execute("""
                            UPDATE sea_proyectos_evaluados 
                            SET nombre=?, titular=?, via_ingreso=?, estado_proyecto=?, razon_ingreso=?, fecha_presentacion=?, subestado_proyecto=?, tipo_proyecto=?, url=?
                            WHERE id=?
                        """, (nombre, titular, via_ingreso, estado, razon, fecha, subestado, tipo, url, exp_id))
                    else:
                        cursor.execute("""
                            INSERT INTO sea_proyectos_evaluados 
                            (id, nombre, titular, via_ingreso, estado_proyecto, razon_ingreso, fecha_presentacion, subestado_proyecto, tipo_proyecto, url, fecha_scraping)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (exp_id, nombre, titular, via_ingreso, estado, razon, fecha, subestado, tipo, url, now_str))
                        nuevos_registros += 1
                        
                conn.commit()
                
                # Siguiente pagina
                offset += 1 # La paginacion usa offset 0 para pagina 1, 1 para pagina 2, etc. (En el analisis dice offset=1 pag 1, offset=2 pag 2, etc., asi que usamos offset += 1. Espera, analisis dice "offset=1" y luego "offset=2")
                # Wait, lets check offset behavior. If offset=1 is pag 1 (first 10), then offset=2 is pag 2.
                # Actually, limit=100. Offset = (page_num - 1) * limit or is it literally page number?
                # The prompt payload had "limit=10" and offset=1 for page 1, offset=2 for page 2. So offset is the page number!
                print(f"Página {offset} procesada.")
                
            except Exception as e:
                print(f"Error en scraping SEA Proyectos Evaluados: {e}")
                break
                
        conn.close()
        print(f"Scraping SEA Proyectos finalizado. Nuevos: {nuevos_registros}")
        return nuevos_registros

if __name__ == '__main__':
    scraper = SEAEvaluadosScraper()
    scraper.run()
