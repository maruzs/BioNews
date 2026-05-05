"""
Scraper del Tercer Tribunal Ambiental (Legal)
Consulta la API REST del 3TA y guarda en la tabla Tribunales de data.db
"""
import requests
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

# Mapeos predefinidos
MAPEO_ROLES = {
    1: ("Demanda", "D"),
    2: ("Solicitud", "S"),
    3: ("Reclamacion", "R"),
    4: ("Otros", "O"),
    6: ("Consulta", "C"),
    7: ("Exhorto", "E"),
    8: ("Demanda Ejecutiva", "DE")
}

MAPEO_CORTES = {
    1: "Primer",
    2: "Segundo",
    3: "Tercer"
}


def obtener_ultima_fecha(conn):
    """
    Busca la fecha mas reciente ingresada en la BD para el Tercer Tribunal.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT Fecha FROM Tribunales WHERE Tribunal = 'Tercer'")
        filas = cursor.fetchall()
        
        if not filas:
            return None
            
        fechas_validas = []
        for fila in filas:
            fecha_str = fila[0]
            if fecha_str:
                try:
                    dt = datetime.strptime(fecha_str, "%d-%m-%Y")
                    fechas_validas.append(dt)
                except ValueError:
                    continue
                    
        if fechas_validas:
            return max(fechas_validas)
        return None
        
    except sqlite3.OperationalError:
        return None


def determinar_estado(causa):
    """
    Evalua el estado en cascada segun la existencia de las fechas de cierre.
    """
    if causa.get('archived_at'):
        return "Archivada"
    elif causa.get('ended_at'):
        return "Terminada"
    elif causa.get('suspended_at'):
        return "Suspendida"
    else:
        return "En tramitacion"


def actualizar_tercer_tribunal(conn, ultima_fecha_db):
    url = "https://causas.3ta.cl/api/v1/causes/?cause_state=ALL&page=1"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
        "Accept": "application/json"
    }
    
    print("Descargando registros desde la API del Tercer Tribunal...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        objects = data.get('objects', {})
        causes_dict = objects.get('causes', {})
        
        if not causes_dict:
            print("No se encontraron resultados en la API.")
            return 0
            
        # Pre-procesar y ordenar por fecha descendente
        causas_procesadas = []
        for id_causa_str, causa in causes_dict.items():
            created_at = causa.get('created_at', '')
            if not created_at:
                continue
                
            fecha_raw = created_at.split('T')[0]
            try:
                dt = datetime.strptime(fecha_raw, "%Y-%m-%d")
                fecha_str = dt.strftime("%d-%m-%Y")
                causas_procesadas.append((dt, fecha_str, causa))
            except ValueError:
                continue
                
        causas_procesadas.sort(key=lambda x: x[0], reverse=True)
        
        cursor = conn.cursor()
        nuevos_registros = 0
        
        for dt, fecha_str, causa in causas_procesadas:
            if ultima_fecha_db and dt < ultima_fecha_db:
                break
                
            role_number = causa.get('role_number')
            cause_role_id = causa.get('cause_role_id')
            court_id = causa.get('court_id')
            id_causa = causa.get('id')
            
            if not role_number or not cause_role_id:
                continue
                
            anio = dt.year
            rol_info = MAPEO_ROLES.get(cause_role_id, ("Desconocido", "X"))
            tipo_procedimiento = rol_info[0]
            letra_rol = rol_info[1]
            
            tribunal = MAPEO_CORTES.get(court_id, "Tercer")
            rol = f"{letra_rol}-{role_number}-{anio}"
            
            caratula = causa.get('cover_title') or "sin caratula"
            estado_procesal = determinar_estado(causa)
            accion = f"https://causas.3ta.cl/causes/{id_causa}"
            
            cursor.execute('''
                INSERT OR REPLACE INTO Tribunales
                (Rol, Fecha, Caratula, Tribunal, Tipo_de_Procedimiento, Estado_Procesal, Accion)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (rol, fecha_str, caratula, tribunal, tipo_procedimiento, estado_procesal, accion))
            
            nuevos_registros += 1
            
            if nuevos_registros >= 10:
                print("Se alcanzo el limite maximo de 10 nuevos registros.")
                break
                
        conn.commit()
        print(f"Actualizacion completada. Se guardaron o actualizaron {nuevos_registros} registros.")
        return nuevos_registros
        
    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")
        return 0
    except Exception as e:
        print(f"Error procesando los datos: {e}")
        return 0


class TercerTribunalScraperLegal:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        if not os.path.exists(DB_PATH):
            print("La base de datos no existe.")
            return 0
            
        try:
            conn = sqlite3.connect(DB_PATH)
            ultima_fecha = obtener_ultima_fecha(conn)
            
            if ultima_fecha:
                print(f"Ultima fecha en BD para el Tercer Tribunal: {ultima_fecha.strftime('%d-%m-%Y')}")
            else:
                print("No se encontraron fechas previas. Se procesaran los mas recientes.")
                
            nuevos = actualizar_tercer_tribunal(conn, ultima_fecha)
            conn.close()
            return nuevos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return 0


if __name__ == "__main__":
    scraper = TercerTribunalScraperLegal()
    scraper.run()