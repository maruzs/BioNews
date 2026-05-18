"""
Scraper del Primer Tribunal Ambiental
Consulta la API REST del portal judicial 1TA y guarda en la tabla Tribunales de data.db
"""
import requests
import json
import os
from datetime import datetime
from src.database.connection import scrapers_conn, get_scrapers_conn, release_scrapers_conn


def obtener_ultima_fecha(conn):
    """
    Busca la fecha mas reciente ingresada en la base de datos para el Primer Tribunal.
    """
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT \"Fecha\" FROM \"Tribunales\" WHERE \"Tribunal\" = 'Primer Tribunal'")
            filas = cur.fetchall()

        if not filas:
            return None

        fechas_validas = []
        for fila in filas:
            fecha_str = fila[0]
            if fecha_str:
                try:
                    if '-' in fecha_str and len(fecha_str.split('-')[0]) == 4:
                        dt = datetime.strptime(fecha_str, "%Y-%m-%d")
                    else:
                        dt = datetime.strptime(fecha_str, "%d-%m-%Y")
                    fechas_validas.append(dt)
                except ValueError:
                    continue

        if fechas_validas:
            return max(fechas_validas)
        return None
    except Exception:
        return None


def obtener_causas_ano_actual():
    """
    Hace la peticion POST filtrando unicamente por el ano en curso.
    """
    url = "https://www.portaljudicial1ta.cl/sgc-ws/rest/consulta-causa/get-consulta-causa"
    
    ano_actual = str(datetime.now().year)
    
    payload = {
        'tipoCausa': (None, 'null'),
        'numeroRol': (None, ''),
        'anioIngreso': (None, ano_actual),
        'estado': (None, 'null')
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        print(f"Buscando causas del ano {ano_actual} en el Primer Tribunal...")
        response = requests.post(url, files=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        if 'response' in data and data['response']:
            causas = json.loads(data['response'])
            return causas
        return []
            
    except Exception as e:
        print(f"Error al consultar la API: {e}")
        return []


def procesar_nuevos_registros(causas, conn, ultima_fecha_db):
    nuevos_registros = 0
    causas_procesadas = []
    for causa in causas:
        fecha_raw = causa.get('fechaCausa', '')
        fecha_str = fecha_raw.split(' ')[0] if fecha_raw else ''
        try:
            dt = datetime.strptime(fecha_str, "%d-%m-%Y")
            fecha_iso = dt.strftime("%Y-%m-%d")
            causas_procesadas.append((dt, fecha_iso, causa))
        except ValueError:
            continue

    causas_procesadas.sort(key=lambda x: x[0], reverse=True)

    with conn.cursor() as cur:
        for dt, fecha_str, causa in causas_procesadas:
            if ultima_fecha_db and dt < ultima_fecha_db:
                break
            rol = causa.get('numeroRol')
            if not rol:
                continue
            caratula = causa.get('caratula', '')
            tribunal = 'Primer Tribunal'
            tipo_procedimiento = causa.get('tipoCausa', '')
            estado_raw = causa.get('estado', '')
            estado = estado_raw.split('(')[0].strip() if estado_raw else ''
            accion = f"https://www.portaljudicial1ta.cl/sgc-web/ver-causa.html?rol={rol}"

            cur.execute('''
                INSERT INTO "Tribunales"
                ("Rol", "Fecha", "Caratula", "Tribunal", "Tipo_de_Procedimiento", "Estado_Procesal", "Accion", fecha_scraping)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT ("Rol") DO UPDATE SET
                    "Fecha" = EXCLUDED."Fecha",
                    "Caratula" = EXCLUDED."Caratula",
                    "Estado_Procesal" = EXCLUDED."Estado_Procesal"
            ''', (rol, fecha_str, caratula, tribunal, tipo_procedimiento, estado, accion,
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            nuevos_registros += 1
            if nuevos_registros >= 10:
                print("Se alcanzo el limite de 10 registros procesados.")
                break

    conn.commit()
    print(f"Actualizacion completada. Se revisaron/guardaron {nuevos_registros} registros.")
    return nuevos_registros


class PrimerTribunalScraper:
    """Wrapper para integracion con el sistema BioNews."""

    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        try:
            conn = get_scrapers_conn()
            ultima_fecha = obtener_ultima_fecha(conn)

            if ultima_fecha:
                print(f"Ultima fecha registrada en BD: {ultima_fecha.strftime('%d-%m-%Y')}")
            else:
                print("No se encontraron fechas previas. Se procesaran hasta 10 del ano actual.")

            causas = obtener_causas_ano_actual()

            nuevos = 0
            if causas:
                nuevos = procesar_nuevos_registros(causas, conn, ultima_fecha)
            else:
                print("No se obtuvieron datos de la API.")

            return nuevos
        except Exception as e:
            print(f"Error de base de datos: {e}")
            return 0
        finally:
            release_scrapers_conn(conn)


if __name__ == "__main__":
    scraper = PrimerTribunalScraper()
    scraper.run()