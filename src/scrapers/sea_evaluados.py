"""
Scraper de Proyectos Evaluados - SEA
Consulta la API publica del SEA y guarda en la tabla sea_proyectos_evaluados
"""
import requests
import json
import os
import re
from datetime import datetime
from src.database.connection import scrapers_conn, get_scrapers_conn, release_scrapers_conn

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

    def run(self, start_date=None, end_date=None):
        url_base = "https://seia.sea.gob.cl"
        url_buscar = f"{url_base}/busqueda/buscarProyectoResumen.php"
        url_api = f"{url_base}/busqueda/buscarProyectoResumenAction.php"
        
        fecha_hoy = datetime.now().strftime('%d/%m/%Y')
        fecha_hoy_iso = datetime.now().strftime('%Y-%m-%d')
        fecha_desde = fecha_hoy
        fecha_hasta = fecha_hoy
        is_empty = True
        
        if start_date and end_date:
            # Manual trigger
            try:
                # Convert from YYYY-MM-DD to DD/MM/YYYY
                fecha_desde = datetime.strptime(start_date, '%Y-%m-%d').strftime('%d/%m/%Y')
                fecha_hasta = datetime.strptime(end_date, '%Y-%m-%d').strftime('%d/%m/%Y')
                is_empty = False
            except Exception as e:
                print(f"Error parsing dates: {e}")
        else:
            # Verificar si la tabla esta vacia para decidir si hacer scraping completo o solo de hoy
            try:
                with scrapers_conn() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT COUNT(*) FROM sea_proyectos_evaluados")
                        count = cur.fetchone()[0]
                        if count > 0:
                            is_empty = False
                            cur.execute("""
                                SELECT DISTINCT DATE(fecha_scraping)
                                FROM sea_proyectos_evaluados
                                WHERE fecha_scraping IS NOT NULL
                                ORDER BY DATE(fecha_scraping) DESC
                                LIMIT 2
                            """)
                            scrape_dates = cur.fetchall()
                            if len(scrape_dates) > 0:
                                last_date_str = scrape_dates[0][0]
                                if str(last_date_str) == fecha_hoy_iso and len(scrape_dates) > 1:
                                    prev_date_str = str(scrape_dates[1][0])
                                    prev_date_obj = datetime.strptime(prev_date_str, '%Y-%m-%d')
                                    fecha_desde = prev_date_obj.strftime('%d/%m/%Y')
                                else:
                                    last_date_obj = datetime.strptime(str(last_date_str), '%Y-%m-%d')
                                    fecha_desde = last_date_obj.strftime('%d/%m/%Y')
            except Exception as e:
                print(f"Error verificando DB: {e}")

        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://seia.sea.gob.cl",
            "Referer": "https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php"
        })
        
        # Inicializar cookies
        try:
            session.get(url_buscar, timeout=30)
        except Exception as e:
            print(f"Error en GET inicial: {e}")

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
            "PresentacionMin": "" if is_empty else fecha_desde,
            "PresentacionMax": "" if is_empty else fecha_hasta,
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

        conn = get_scrapers_conn()
        cur = conn.cursor()

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
                    
                    cur.execute("SELECT 1 FROM sea_proyectos_evaluados WHERE id = %s", (exp_id,))
                    exists = cur.fetchone()

                    if exists:
                        cur.execute("""
                            UPDATE sea_proyectos_evaluados
                            SET nombre=%s, titular=%s, via_ingreso=%s, estado_proyecto=%s, razon_ingreso=%s, fecha_presentacion=%s, subestado_proyecto=%s, categoria_economica=%s, tipo_proyecto=%s, region=%s, url=%s
                            WHERE id=%s
                        """, (nombre, titular, via_ingreso, estado, razon, fecha, subestado, categoria_economica, tipo, region, url, exp_id))
                    else:
                        cur.execute("""
                            INSERT INTO sea_proyectos_evaluados
                            (id, nombre, titular, via_ingreso, estado_proyecto, razon_ingreso, fecha_presentacion, subestado_proyecto, categoria_economica, tipo_proyecto, region, url, fecha_scraping)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (exp_id, nombre, titular, via_ingreso, estado, razon, fecha, subestado, categoria_economica, tipo, region, url, now_str))
                        nuevos_registros += 1
                        conn.commit()
                
                print(f"Offset {offset} procesado. Registros nuevos hasta ahora: {nuevos_registros}")
                # Siguiente pagina
                offset += limit
                
            except Exception as e:
                print(f"Error en scraping SEA Proyectos Evaluados: {e}")
                break
                
        cur.close()
        release_scrapers_conn(conn)
        print(f"Scraping SEA Proyectos finalizado. Nuevos: {nuevos_registros}")
        return nuevos_registros

if __name__ == '__main__':
    scraper = SEAEvaluadosScraper()
    scraper.run()
