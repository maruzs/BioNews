"""
Scraper de Programas de Cumplimiento - SNIFA
https://snifa.sma.gob.cl/ProgramaCumplimiento/Resultado

Compara total de registros y busca nuevos por diferencia de expedientes.
"""
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from src.database.connection import scrapers_conn


def get_db_info():
    """Obtiene los expedientes existentes y la cantidad total en la BD."""
    with scrapers_conn() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT expediente FROM "programasDeCumplimiento"')
            expedientes = set(row[0] for row in cur.fetchall())
    return expedientes, len(expedientes)


def extract_ficha_id(url):
    """Extrae el número de ficha del final de la URL."""
    if not url:
        return None
    try:
        parts = url.rstrip('/').split('/')
        if parts:
            last_part = parts[-1]
            if last_part.isdigit():
                return int(last_part)
    except:
        pass
    return None


def parse_row(row):
    """Extrae los datos de una fila de la tabla HTML."""
    tds = row.find_all('td')
    if len(tds) < 4:
        return None

    data = {
        'expediente': '',
        'unidad_fiscalizable': '',
        'nombre_razon_social': '',
        'categoria': '',
        'region': '',
        'detalle_link': ''
    }

    for td in tds:
        label = (td.get('data-label') or '').strip()

        if label == 'Expediente':
            data['expediente'] = td.get_text(strip=True)
        elif label in ('Unidad Fiscalizable', 'Unidad fiscalizable'):
            items = [li.text.strip() for li in td.find_all('li')]
            if not items:
                items = [td.get_text(strip=True)]
            data['unidad_fiscalizable'] = ' / '.join(filter(None, items))
        elif label in ('Nombre Razón Social', 'Nombre razón social', 'Nombre Razon Social'):
            items = [li.text.strip() for li in td.find_all('li')]
            if not items:
                items = [td.get_text(strip=True)]
            data['nombre_razon_social'] = ' / '.join(filter(None, items))
        elif label in ('Categoría', 'Categoria'):
            items = [li.text.strip() for li in td.find_all('li')]
            if not items:
                items = [td.get_text(strip=True)]
            data['categoria'] = ' / '.join(filter(None, items))
        elif label in ('Región', 'Region'):
            items = [li.text.strip() for li in td.find_all('li')]
            if not items:
                items = [td.get_text(strip=True)]
            data['region'] = ' / '.join(filter(None, items))
        elif label == 'Detalle':
            a_tag = td.find('a')
            if a_tag:
                href = a_tag.get('href', '')
                if href.startswith('/'):
                    data['detalle_link'] = f"https://snifa.sma.gob.cl{href}"
                else:
                    data['detalle_link'] = href

    if not data['expediente']:
        return None
    
    data['ficha_id'] = extract_ficha_id(data['detalle_link'])
    return data


class ProgramasCumplimientoScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        print("Iniciando scraper de Programas de Cumplimiento...")
        url = "https://snifa.sma.gob.cl/ProgramaCumplimiento/Resultado"

        db_expedientes, db_count = get_db_info()
        print(f"Registros actuales en BD: {db_count}")

        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
        except Exception as e:
            print(f"Error al conectar con {url}: {e}")
            return 0

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')

        all_records = []
        for row in rows:
            data = parse_row(row)
            if data:
                all_records.append(data)

        web_count = len(all_records)
        print(f"Registros en la web: {web_count}")

        if web_count <= db_count:
            print("No hay registros nuevos. La BD esta actualizada.")
            return 0

        nuevos = [r for r in all_records if r['expediente'] not in db_expedientes]

        if not nuevos:
            print("No hay registros nuevos (todos los expedientes ya existen).")
            return 0

        print(f"Encontrados {len(nuevos)} registros nuevos.")

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for record in nuevos:
                    cur.execute('''
                        INSERT INTO "programasDeCumplimiento" (
                            expediente, nombre_razon_social, unidad_fiscalizable,
                            categoria, region, detalle_link, fecha_scraping, ficha_id
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (expediente) DO UPDATE SET
                            nombre_razon_social = EXCLUDED.nombre_razon_social,
                            unidad_fiscalizable = EXCLUDED.unidad_fiscalizable,
                            categoria = EXCLUDED.categoria, region = EXCLUDED.region,
                            detalle_link = EXCLUDED.detalle_link, ficha_id = EXCLUDED.ficha_id
                    ''', (
                        record['expediente'], record['nombre_razon_social'],
                        record['unidad_fiscalizable'], record['categoria'],
                        record['region'], record['detalle_link'],
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'), record.get('ficha_id')
                    ))
                    print(f"  + {record['expediente']}")
        print(f"Scraper finalizado. Se agregaron {len(nuevos)} registros a Programas de Cumplimiento.")
        return len(nuevos)


if __name__ == '__main__':
    scraper = ProgramasCumplimientoScraper()
    scraper.run()
