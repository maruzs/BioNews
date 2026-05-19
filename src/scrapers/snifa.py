"""
Scraper de Procedimientos Sancionatorios - SNIFA
https://snifa.sma.gob.cl/Sancionatorio/Resultado

Compara el total de registros y busca por diferencia de expedientes contra la BD usando la API JSON.
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
            cur.execute("SELECT expediente FROM sancionatorios")
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


def parse_json_row(row):
    """Parsea una fila del JSON obtenido de la API y extrae los campos estructurados."""
    if len(row) < 8:
        return None

    expediente = row[1].strip()

    # Unidad Fiscalizable (Index 2)
    soup_uf = BeautifulSoup(row[2], 'html.parser')
    items_uf = [li.text.strip() for li in soup_uf.find_all('li')]
    if not items_uf:
        items_uf = [soup_uf.get_text(strip=True)]
    unidad_fiscalizable = ' / '.join(filter(None, items_uf))

    # Nombre Razón Social (Index 3)
    soup_nrs = BeautifulSoup(row[3], 'html.parser')
    items_nrs = [li.text.strip() for li in soup_nrs.find_all('li')]
    if not items_nrs:
        items_nrs = [soup_nrs.get_text(strip=True)]
    nombre_razon_social = ' / '.join(filter(None, items_nrs))

    # Categoría (Index 4)
    soup_cat = BeautifulSoup(row[4], 'html.parser')
    items_cat = [li.text.strip() for li in soup_cat.find_all('li')]
    if not items_cat:
        items_cat = [soup_cat.get_text(strip=True)]
    categoria = ' / '.join(filter(None, items_cat))

    # Región (Index 5)
    soup_reg = BeautifulSoup(row[5], 'html.parser')
    items_reg = [li.text.strip() for li in soup_reg.find_all('li')]
    if not items_reg:
        items_reg = [soup_reg.get_text(strip=True)]
    region = ' / '.join(filter(None, items_reg))

    estado = row[6].strip()

    # Detalle Link (Index 7)
    soup_det = BeautifulSoup(row[7], 'html.parser')
    a_tag = soup_det.find('a')
    detalle_link = ''
    if a_tag:
        href = a_tag.get('href', '')
        if href.startswith('/'):
            detalle_link = f"https://snifa.sma.gob.cl{href}"
        else:
            detalle_link = href

    ficha_id = extract_ficha_id(detalle_link)

    return {
        'expediente': expediente,
        'nombre_razon_social': nombre_razon_social,
        'unidad_fiscalizable': unidad_fiscalizable,
        'categoria': categoria,
        'region': region,
        'estado': estado,
        'detalle_link': detalle_link,
        'ficha_id': ficha_id
    }


class SancionatoriosScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        print("Iniciando scraper de Procedimientos Sancionatorios (via HTTP POST)...")
        url = "https://snifa.sma.gob.cl/Sancionatorio/ObtenerResultadosGrid"

        db_expedientes, db_count = get_db_info()
        print(f"Registros actuales en BD: {db_count}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://snifa.sma.gob.cl'
        }

        # Realizamos el POST con límite de 10
        payload = {
            'draw': '1',
            'start': '0',
            'length': '10',
            'order[0][column]': '0',
            'order[0][dir]': 'asc'
        }

        try:
            r = requests.post(url, headers=headers, data=payload, timeout=60)
            r.raise_for_status()
            res = r.json()
        except Exception as e:
            print(f"Error al conectar con la API de SNIFA Sancionatorios: {e}")
            return 0

        records_total = res.get('recordsTotal', 0)
        print(f"Total registros reportados por la web (recordsTotal): {records_total}")

        if records_total <= db_count:
            print("No hay registros nuevos. La BD esta actualizada.")
            return 0

        # Hay registros nuevos, procedemos a parsear los 10 registros obtenidos (los más recientes)
        all_records = []
        data_rows = res.get('data', [])

        for row in data_rows:
            parsed = parse_json_row(row)
            if parsed:
                all_records.append(parsed)

        nuevos = [r for r in all_records if r['expediente'] not in db_expedientes]

        if not nuevos:
            print("No hay registros nuevos en el lote de los 10 mas recientes.")
            return 0

        print(f"Encontrados {len(nuevos)} registros nuevos.")

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for record in nuevos:
                    cur.execute('''
                        INSERT INTO sancionatorios (
                            expediente, unidad_fiscalizable, nombre_razon_social,
                            categoria, region, estado, detalle_link, fecha_scraping, ficha_id
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (expediente) DO UPDATE SET
                            unidad_fiscalizable = EXCLUDED.unidad_fiscalizable,
                            nombre_razon_social = EXCLUDED.nombre_razon_social,
                            categoria = EXCLUDED.categoria, region = EXCLUDED.region,
                            estado = EXCLUDED.estado, detalle_link = EXCLUDED.detalle_link,
                            ficha_id = EXCLUDED.ficha_id
                    ''', (
                        record['expediente'], record['unidad_fiscalizable'],
                        record['nombre_razon_social'], record['categoria'],
                        record['region'], record['estado'], record['detalle_link'],
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'), record.get('ficha_id')
                    ))
                    print(f"  + {record['expediente']}")
        print(f"Scraper finalizado. Se agregaron {len(nuevos)} registros a Sancionatorios.")
        return len(nuevos)


if __name__ == '__main__':
    scraper = SancionatoriosScraper()
    scraper.run()