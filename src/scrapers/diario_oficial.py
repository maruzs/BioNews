"""
Scraper del Diario Oficial - Normativas
Extrae normativas del Diario Oficial y las guarda en la tabla normativas de data.db
"""
import os
from src.database.manager import DatabaseManager
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

# Cambiar a 1 para obtener solo los datos del dia actual.
# Cambiar a 30 para obtener los ultimos 30 dias.
DIAS_A_EXTRAER = 1


def extract_ficha_id(url):
    """Extrae el número de ficha del final de la URL."""
    if not url:
        return None
    try:
        # Ejemplo: .../2805795.pdf
        url = url.split('?')[0]
        url = url.rstrip('/')
        if url.endswith('.pdf'):
            url = url[:-4]
        parts = url.split('/')
        if parts:
            last_part = parts[-1]
            if last_part.isdigit():
                return int(last_part)
    except:
        pass
    return None


def crear_tabla_si_no_existe(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS normativas (
            fecha TEXT,
            normativa TEXT,
            tipo_normativa TEXT,
            organismo TEXT,
            suborganismo TEXT,
            accion TEXT PRIMARY KEY,
            fecha_scraping TEXT,
            ficha_id INTEGER
        )
    ''')
    # Migración: agregar UNIQUE a accion si la tabla ya existe sin él
    # y agregar columna fecha_scraping si no existe
    try:
        cursor.execute("PRAGMA table_info(normativas)")
        columns = [col[1] for col in cursor.fetchall()]
        if 'fecha_scraping' not in columns:
            cursor.execute("ALTER TABLE normativas ADD COLUMN fecha_scraping TEXT")
    except:
        pass
    conn.commit()


def extraer_datos_seccion(url, tipo_normativa, fecha_str, cursor):
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return
            
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        filas = soup.find_all('tr')
        
        organismo_actual = None
        suborganismo_actual = None
        
        for fila in filas:
            # Detectar cambio de Organismo
            td_org = fila.find('td', class_='title4')
            if td_org:
                organismo_actual = td_org.text.strip()
                suborganismo_actual = None
                continue
                
            # Detectar cambio de Suborganismo
            td_suborg = fila.find('td', class_='title5')
            if td_suborg:
                suborganismo_actual = td_suborg.text.strip()
                continue
                
            # Extraer el contenido de la normativa
            clases = fila.get('class', [])
            if 'content' in clases:
                tds = fila.find_all('td')
                if len(tds) >= 2:
                    normativa_texto = tds[0].text.strip()
                    
                    enlace = tds[1].find('a')
                    accion_link = enlace.get('href') if enlace else ""
                    
                    # Convertir para la BD (YYYY-MM-DD)
                    try:
                        fecha_db = datetime.strptime(fecha_str, '%d-%m-%Y').strftime('%Y-%m-%d')
                    except:
                        fecha_db = fecha_str

                    fid = extract_ficha_id(accion_link)

                    # Usar INSERT OR IGNORE para evitar duplicados por URL (accion)
                    cursor.execute('''
                        INSERT INTO normativas (fecha, normativa, tipo_normativa, organismo, suborganismo, accion, fecha_scraping, ficha_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (fecha_db, normativa_texto, tipo_normativa, organismo_actual, suborganismo_actual, accion_link, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fid))
                    
    except Exception as e:
        print(f"Error procesando seccion {tipo_normativa} para la fecha {fecha_str}: {e}")


class DiarioOficialScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self, start_date=None, end_date=None):
        """Ejecuta el scraper y guarda directamente en la BD."""
        if not os.path.exists(DB_PATH):
            print("La base de datos no existe.")
            return 0
        
        db_manager = DatabaseManager()
        conn = db_manager.get_connection('bionews_legal_db')
        cursor = conn.cursor()
        crear_tabla_si_no_existe(conn)
        
        registros_antes = 0
        try:
            cursor.execute("SELECT COUNT(*) FROM normativas")
            registros_antes = cursor.fetchone()[0]
        except:
            pass
        
        if start_date and end_date:
            try:
                start_obj = datetime.strptime(start_date, '%Y-%m-%d')
                end_obj = datetime.strptime(end_date, '%Y-%m-%d')
                days_diff = (end_obj - start_obj).days
                dates_to_extract = [end_obj - timedelta(days=i) for i in range(days_diff + 1)]
            except Exception as e:
                print(f"Error parseando fechas manuales: {e}")
                dates_to_extract = []
        else:
            fecha_actual = datetime.now()
            dates_to_extract = [fecha_actual - timedelta(days=i) for i in range(DIAS_A_EXTRAER)]
        
        print(f"Iniciando extraccion para {len(dates_to_extract)} dia(s)...")
        
        for fecha_iter in dates_to_extract:
            # Ignorar los domingos
            if fecha_iter.weekday() == 6:
                print(f"Saltando domingo: {fecha_iter.strftime('%d-%m-%Y')}")
                continue
                
            fecha_str = fecha_iter.strftime('%d-%m-%Y')
            print(f"Buscando informacion para la fecha: {fecha_str}")
            
            url_base = f"https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php?date={fecha_str}"
            try:
                resp_base = requests.get(url_base)
                
                match = re.search(r'edition=(\d+)', resp_base.text)
                
                if not match:
                    print(f"No se encontro publicacion para {fecha_str}. Se asume feriado.")
                    continue
                    
                edicion = match.group(1)
                
                secciones_a_extraer = [
                    (f"https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php?date={fecha_str}&edition={edicion}", "Normas Generales"),
                    (f"https://www.diariooficial.interior.gob.cl/edicionelectronica/normas_particulares.php?date={fecha_str}&edition={edicion}", "Normas Particulares"),
                    (f"https://www.diariooficial.interior.gob.cl/edicionelectronica/bom.php?date={fecha_str}&edition={edicion}", "Boletin Oficial Mineria")
                ]
                
                for url_seccion, tipo_norm in secciones_a_extraer:
                    extraer_datos_seccion(url_seccion, tipo_norm, fecha_str, cursor)
                    
            except Exception as e:
                print(f"Error de conexion al procesar la fecha {fecha_str}: {e}")
                
        conn.commit()
        
        registros_despues = 0
        try:
            cursor.execute("SELECT COUNT(*) FROM normativas")
            registros_despues = cursor.fetchone()[0]
        except:
            pass
        
        conn.close()
        nuevos = registros_despues - registros_antes
        print(f"El proceso de extraccion ha finalizado. {nuevos} registros nuevos.")
        return nuevos


if __name__ == "__main__":
    scraper = DiarioOficialScraper()
    scraper.run()