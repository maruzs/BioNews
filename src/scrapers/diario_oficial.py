"""
Scraper del Diario Oficial - Normativas
Extrae normativas del Diario Oficial y las guarda en la tabla normativas de data.db
"""
import os
import sqlite3
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

# Cambiar a 1 para obtener solo los datos del dia actual.
# Cambiar a 30 para obtener los ultimos 30 dias.
DIAS_A_EXTRAER = 1


def crear_tabla_si_no_existe(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS normativas (
            fecha TEXT,
            normativa TEXT,
            tipo_normativa TEXT,
            organismo TEXT,
            suborganismo TEXT,
            accion TEXT
        )
    ''')
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
                    
                    cursor.execute('''
                        INSERT INTO normativas (fecha, normativa, tipo_normativa, organismo, suborganismo, accion)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (fecha_str, normativa_texto, tipo_normativa, organismo_actual, suborganismo_actual, accion_link))
                    
    except Exception as e:
        print(f"Error procesando seccion {tipo_normativa} para la fecha {fecha_str}: {e}")


class DiarioOficialScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        if not os.path.exists(DB_PATH):
            print("La base de datos no existe.")
            return 0
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        crear_tabla_si_no_existe(conn)
        
        fecha_actual = datetime.now()
        registros_antes = 0
        try:
            cursor.execute("SELECT COUNT(*) FROM normativas")
            registros_antes = cursor.fetchone()[0]
        except:
            pass
        
        print(f"Iniciando extraccion para {DIAS_A_EXTRAER} dia(s)...")
        
        for i in range(DIAS_A_EXTRAER):
            fecha_iter = fecha_actual - timedelta(days=i)
            
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