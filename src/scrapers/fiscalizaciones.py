"""
Scraper de Fiscalizaciones - SNIFA
https://snifa.sma.gob.cl/Fiscalizacion

Compara el total de registros del año actual y busca nuevos por diferencia de expedientes usando la API JSON.
Nota: SNIFA ordena del más nuevo al más viejo, por lo que siempre pedimos start=0.
"""
import math
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from src.database.connection import scrapers_conn


def get_db_expedientes_for_year(year):
    """Obtiene todos los expedientes de un año específico y su cantidad en la BD."""
    pattern = f"DFZ-{year}%"
    with scrapers_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT expediente FROM fiscalizaciones WHERE expediente LIKE %s", (pattern,))
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


def parse_html_field(html):
    """Extrae texto limpio de un campo HTML de la API de SNIFA."""
    if not html or not html.strip():
        return ''
    soup = BeautifulSoup(html, 'html.parser')
    items = [li.text.strip() for li in soup.find_all('li')]
    if items:
        return ' / '.join(filter(None, items))
    return soup.get_text(strip=True)


def extract_ficha_id_from_html(html):
    """Extrae el ficha_id desde el HTML del campo de detalle."""
    if not html:
        return None
    soup = BeautifulSoup(html, 'html.parser')
    a_tag = soup.find('a')
    if not a_tag:
        return None
    href = a_tag.get('href', '')
    try:
        parts = href.rstrip('/').split('/')
        if parts and parts[-1].isdigit():
            return int(parts[-1])
    except:
        pass
    return None


def parse_json_row(row):
    """
    Parsea una fila del JSON de Fiscalizaciones SNIFA.
    Estructura del array (9 columnas):
      [0] nro, [1] expediente, [2] nombre_razon_social (fa-user),
      [3] categoria (fa-angle-right), [4] unidad_fiscalizable (fa-building),
      [5] region, [6] comuna (ignorada), [7] estado, [8] detalle_link
    """
    if len(row) < 9:
        return None

    expediente = row[1].strip()
    nombre_razon_social = parse_html_field(row[2])
    categoria           = parse_html_field(row[3])
    unidad_fiscalizable = parse_html_field(row[4])
    region              = parse_html_field(row[5])
    estado              = row[7].strip() if len(row) > 7 else ''

    # Detalle link y ficha_id desde el HTML del índice 8
    detalle_link = ''
    ficha_id = None
    if len(row) > 8:
        soup_det = BeautifulSoup(row[8], 'html.parser')
        a_tag = soup_det.find('a')
        if a_tag:
            href = a_tag.get('href', '')
            detalle_link = f"https://snifa.sma.gob.cl{href}" if href.startswith('/') else href
            try:
                parts = href.rstrip('/').split('/')
                if parts and parts[-1].isdigit():
                    ficha_id = int(parts[-1])
            except:
                pass

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


class SnifaFiscalizacionScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        current_year = datetime.now().year
        filter_expediente = f"DFZ-{current_year}"
        print(f"Iniciando scraper de Fiscalizaciones para el año {current_year} (via HTTP POST)...")
        url = "https://snifa.sma.gob.cl/Fiscalizacion/ObtenerResultadosGrid"

        db_expedientes, db_count = get_db_expedientes_for_year(current_year)
        print(f"Registros del año {current_year} en BD: {db_count}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://snifa.sma.gob.cl'
        }

        # 1. Obtener recordsTotal para el año actual con una petición rápida de 1 elemento
        payload_init = {
            'draw': '1',
            'start': '0',
            'length': '1',
            'expediente': filter_expediente
        }

        try:
            r = requests.post(url, headers=headers, data=payload_init, timeout=30)
            r.raise_for_status()
            res_init = r.json()
        except Exception as e:
            print(f"Error al obtener recordsTotal de Fiscalizaciones: {e}")
            return 0

        records_total = res_init.get('recordsTotal', 0)
        print(f"Total registros del año {current_year} en la web (recordsTotal): {records_total}")

        if records_total <= db_count:
            print(f"No hay registros nuevos para el año {current_year}. La BD esta actualizada.")
            return 0

        # 2. SNIFA ordena del más nuevo al más viejo → start=0 siempre captura los más recientes.
        #    Calculamos el length como la diferencia redondeada a la decena superior (mínimo 20).
        diff = records_total - db_count
        fetch_length = max(20, math.ceil(diff / 10) * 10)
        print(f"Diferencia: {diff} registros. Solicitando los primeros {fetch_length} (start=0)...")

        payload_data = {
            'draw': '2',
            'start': '0',
            'length': str(fetch_length),
            'expediente': filter_expediente
        }

        try:
            r = requests.post(url, headers=headers, data=payload_data, timeout=60)
            r.raise_for_status()
            res_data = r.json()
        except Exception as e:
            print(f"Error al obtener los registros de Fiscalizaciones: {e}")
            return 0

        all_records = []
        for row in res_data.get('data', []):
            parsed = parse_json_row(row)
            if parsed:
                all_records.append(parsed)

        nuevos = [rec for rec in all_records if rec['expediente'] not in db_expedientes]

        if not nuevos:
            print("No hay registros nuevos en el lote obtenido.")
            return 0

        print(f"Encontrados {len(nuevos)} registros nuevos.")

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for record in nuevos:
                    cur.execute('''
                        INSERT INTO fiscalizaciones (
                            expediente, nombre_razon_social, unidad_fiscalizable,
                            categoria, region, estado, detalle_link, fecha_scraping, ficha_id
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (expediente) DO UPDATE SET
                            nombre_razon_social = EXCLUDED.nombre_razon_social,
                            unidad_fiscalizable = EXCLUDED.unidad_fiscalizable,
                            categoria = EXCLUDED.categoria, region = EXCLUDED.region,
                            estado = EXCLUDED.estado, detalle_link = EXCLUDED.detalle_link,
                            ficha_id = EXCLUDED.ficha_id
                    ''', (
                        record['expediente'], record['nombre_razon_social'],
                        record['unidad_fiscalizable'], record['categoria'],
                        record['region'], record['estado'], record['detalle_link'],
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'), record.get('ficha_id')
                    ))
                    print(f"  + {record['expediente']}")
        print(f"Scraper finalizado. Se agregaron {len(nuevos)} registros a Fiscalizaciones.")
        return len(nuevos)


if __name__ == '__main__':
    scraper = SnifaFiscalizacionScraper()
    scraper.run()