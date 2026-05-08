"""
Scraper de Proyectos Evaluados - SEA
Consulta la API publica del SEA y guarda en la tabla sea_proyectos_evaluados
"""
import requests
import json
import os
import sqlite3
import re
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

class SEAEvaluadosScraper:
    MAPPING_CATEGORIAS = {
        'a': 'Infraestructura Hidráulica',
        'b': 'Energía',
        'c': 'Energía',
        'd': 'Energía',
        'e': 'Infraestructura de Transporte',
        'f': 'Infraestructura Portuaria',
        'g': 'Inmobiliarios',
        'h': 'Inmobiliarios',
        'h2': 'Instalaciones fabriles varias',
        'i': 'Minería',
        'j1': 'Energía',
        'j3': 'Minería',
        'j4': 'Otros',
        'k': 'Instalaciones fabriles varias',
        'l': 'Agropecuario',
        'm': 'Forestal',
        'n': 'Pesca y Acuicultura',
        'ñ': 'Otros',
        'o': 'Saneamiento Ambiental',
        'p': 'Otros',
        'q': 'Agropecuario',
        'r': 'Otros',
        's': 'Otros',
        't': 'Equipamiento',
        'u': 'Otros'
    }

    def get_categoria_economica(self, tipo_code):
        if not tipo_code:
            return None
        
        tipo_code = tipo_code.lower()
        match = re.match(r'([a-zñ]+)(\d*)', tipo_code)
        if not match:
            return "Otros"
        
        letter = match.group(1)
        number = match.group(2)
        
        if letter == 'h' and number == '2':
            return self.MAPPING_CATEGORIAS.get('h2')
        if letter == 'j' and number in ['1', '3', '4']:
            return self.MAPPING_CATEGORIAS.get(f'j{number}')
        
        return self.MAPPING_CATEGORIAS.get(letter, "Otros")

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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        })

        fecha_hoy = datetime.now().strftime('%d/%m/%Y')
        limit = 100
        offset = 0
        
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
                import time
                time.sleep(1) # Delay para evitar bloqueos
                
                response = session.post(url_api, data=payload, timeout=30)
                if response.status_code != 200:
                    print(f"Error: Codigo {response.status_code} en offset {offset}")
                    print(f"Respuesta: {response.text[:200]}")
                    break
                
                try:
                    data = response.json()
                except Exception as e_json:
                    print(f"Error parseando JSON en offset {offset}: {e_json}")
                    print(f"Contenido: {response.text[:500]}")
                    break
                    
                if not data.get("status") or not data.get("data"):
                    print(f"API retorno status False o sin datos en offset {offset}")
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
                    categoria_economica = self.get_categoria_economica(tipo)
                    region = item.get("REGION_NOMBRE", "")
                    url = item.get("EXPEDIENTE_URL_PPAL", "")
                    
                    cursor.execute("SELECT 1 FROM sea_proyectos_evaluados WHERE id = ?", (exp_id,))
                    exists = cursor.fetchone()
                    
                    if exists:
                        cursor.execute("""
                            UPDATE sea_proyectos_evaluados 
                            SET nombre=?, titular=?, via_ingreso=?, estado_proyecto=?, razon_ingreso=?, fecha_presentacion=?, subestado_proyecto=?, categoria_economica=?, tipo_proyecto=?, region=?, url=?
                            WHERE id=?
                        """, (nombre, titular, via_ingreso, estado, razon, fecha, subestado, categoria_economica, tipo, region, url, exp_id))
                    else:
                        cursor.execute("""
                            INSERT INTO sea_proyectos_evaluados 
                            (id, nombre, titular, via_ingreso, estado_proyecto, razon_ingreso, fecha_presentacion, subestado_proyecto, categoria_economica, tipo_proyecto, region, url, fecha_scraping)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (exp_id, nombre, titular, via_ingreso, estado, razon, fecha, subestado, categoria_economica, tipo, region, url, now_str))
                        nuevos_registros += 1
                        
                conn.commit()
                
                # Siguiente pagina
                offset += limit
                print(f"Offset {offset} procesado. Nuevos registros: {nuevos_registros}")
                
            except Exception as e:
                print(f"Error en scraping SEA Proyectos Evaluados: {e}")
                break
                
        conn.close()
        print(f"Scraping SEA Proyectos finalizado. Nuevos: {nuevos_registros}")
        return nuevos_registros

if __name__ == '__main__':
    scraper = SEAEvaluadosScraper()
    scraper.run()
