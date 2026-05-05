"""
Scraper de Pertinencias - SEA
Consulta la API de pertinencias del SEA y guarda en la tabla pertinencias de data.db
"""
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')


class PertinenciasScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        usuario = "21324866-9"
        password = "Memr2026."
        
        url_base = "https://pertinencia.sea.gob.cl"
        url_login = f"{url_base}/login"
        url_buscar = f"{url_base}/buscar_pertinencia"
        url_api = f"{url_base}/api/proceso/buscarcp"
        url_logout = f"{url_base}/logout"
        
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0"
        })

        try:
            print("1. Accediendo a la pagina de login (SSO CAS)...")
            response_login_get = session.get(url_login)
            response_login_get.raise_for_status()
            
            soup_login = BeautifulSoup(response_login_get.text, 'html.parser')
            
            execution_input = soup_login.find('input', attrs={'name': 'execution'})
            if not execution_input:
                print("Error: No se encontro el token 'execution' en el HTML del CAS.")
                return 0
                
            execution_token = execution_input.get('value')
            print("Token CAS encontrado. Iniciando sesion...")
            
            login_data = {
                'username': usuario,
                'password': password,
                'execution': execution_token,
                '_eventId': 'submit',
                'geolocation': '',
                'submit': 'INICIAR SESION'
            }
            
            response_login_post = session.post(response_login_get.url, data=login_data)
            
            print("2. Accediendo a la app principal para obtener tokens de Laravel...")
            response_app = session.get(url_buscar)
            soup_app = BeautifulSoup(response_app.text, 'html.parser')
            
            csrf_meta = soup_app.find('meta', attrs={'name': 'csrf-token'})
            if not csrf_meta:
                print("Error: No se encontro el csrf-token de Laravel en la aplicacion.")
                return 0
                
            csrf_token = csrf_meta.get('content')
            
            xsrf_cookie = session.cookies.get('XSRF-TOKEN')
            xsrf_token = urllib.parse.unquote(xsrf_cookie) if xsrf_cookie else ''

            print(f"3. Consultando API para la fecha: {fecha_hoy}")
            headers_api = {
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF-TOKEN": csrf_token,
                "X-XSRF-TOKEN": xsrf_token,
                "Referer": url_buscar
            }

            payload = {
                "pertinenciaFilter": {
                    "estado": "",
                    "fechaPresentacionDesde": fecha_hoy,
                    "fechaPresentacionHasta": "",
                    "fechaRespuestaDesde": "",
                    "fechaRespuestaHasta": "",
                    "id": "",
                    "idLocalidades": [],
                    "idTipologias": [],
                    "nombre": "",
                    "tipoProyecto": "",
                    "titular": "",
                    "regiones": [],
                    "comunas": [],
                    "excelFull": False,
                    "activarFiltrosAvanzados": True,
                    "mainRowHeight": 84,
                    "advancedRow1Height": 84,
                    "advancedRow3Height": 84
                }
            }

            response_api = session.post(url_api, headers=headers_api, data=json.dumps(payload))
            
            if response_api.status_code != 200:
                print(f"Error en la API. Codigo HTTP: {response_api.status_code}")
                return 0
                
            datos = response_api.json()
            print(f"Se encontraron {len(datos)} registros en la API para hoy.")

            print("4. Guardando en base de datos...")
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            nuevos_registros = 0
            
            for item in datos:
                expediente = item.get("correlativeId", "")
                nombre = item.get("name", "")
                proponente = item.get("titularName", "")
                fecha = item.get("presentationDate", "")
                
                estado_dict = item.get("state")
                estado = estado_dict.get("valor", "") if isinstance(estado_dict, dict) else ""
                
                accion = f"{url_base}/api/public/expediente/{expediente}"
                
                from ..utils.date_parser import parse_fecha
                fecha_db = parse_fecha(fecha) if fecha else ""
                
                try:
                    cursor.execute('''
                        INSERT OR IGNORE INTO pertinencias 
                        (Expediente, "Nombre_de_Proyecto", Proponente, Fecha, Estado, Accion)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (expediente, nombre, proponente, fecha_db, estado, accion))
                    
                    if cursor.rowcount > 0:
                        nuevos_registros += 1
                except Exception as e_db:
                    print(f"Error procesando el expediente {expediente}: {e_db}")

            conn.commit()
            conn.close()
            
            print(f"Proceso finalizado con exito. Se agregaron {nuevos_registros} registros nuevos.")
            return nuevos_registros

        except Exception as e:
            print(f"Ocurrio un error general: {e}")
            return 0
            
        finally:
            print("5. Cerrando sesion...")
            try:
                session.get(url_logout)
            except:
                pass
            session.close()


if __name__ == '__main__':
    scraper = PertinenciasScraper()
    scraper.run()