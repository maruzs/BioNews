"""
Scraper de Fiscalizaciones - SNIFA
https://snifa.sma.gob.cl/Fiscalizacion

Usa Playwright porque la pagina carga los datos via JavaScript/AJAX.
Filtra por DFZ-{año_actual} y cambia la paginacion para obtener todos los registros.
"""
import sqlite3
import os
import traceback
from datetime import datetime
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')


def get_db_expedientes():
    """Obtiene todos los expedientes existentes en la BD."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT expediente FROM fiscalizaciones")
    expedientes = set(row[0] for row in cursor.fetchall())
    db_count = len(expedientes)
    conn.close()
    return expedientes, db_count


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
        'estado': '',
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
        elif label == 'Estado':
            data['estado'] = td.get_text(strip=True)
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
    return data


def wait_for_table(page, max_retries=8):
    """Espera inteligentemente a que la tabla termine de cargar."""
    page.wait_for_timeout(3000)
    for attempt in range(max_retries):
        soup = BeautifulSoup(page.content(), "html.parser")
        rows = soup.select("table tbody tr")
        if rows:
            tds = rows[0].find_all("td")
            texto_fila = rows[0].get_text().lower()
            if len(tds) < 4 and ("procesando" in texto_fila or "cargando" in texto_fila):
                print(f"  Tabla cargando, reintento {attempt + 1}/{max_retries}...")
                page.wait_for_timeout(5000)
            else:
                return True
        else:
            print(f"  Sin filas aun, reintento {attempt + 1}/{max_retries}...")
            page.wait_for_timeout(5000)
    return False


class SnifaFiscalizacionScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        print("Iniciando scraper de Fiscalizaciones (via Playwright)...")
        url = "https://snifa.sma.gob.cl/Fiscalizacion"
        current_year = datetime.now().year
        txt_numero = f"DFZ-{current_year}"

        db_expedientes, db_count = get_db_expedientes()
        print(f"Registros actuales en BD: {db_count}")

        all_records = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            try:
                print(f"Navegando a {url}...")
                page.goto(url, wait_until="networkidle", timeout=60000)

                page.wait_for_selector("#expediente", state="visible", timeout=30000)

                print(f"Ingresando filtro: {txt_numero}")
                page.locator("#expediente").fill(txt_numero)

                buscar_btn = page.locator("button.btn:has-text('Buscar')").first
                with page.expect_navigation(wait_until="domcontentloaded", timeout=90000):
                    buscar_btn.click()

                print("Esperando resultados iniciales...")
                wait_for_table(page)

                print("Cambiando a mostrar todos los registros...")
                page.evaluate("""
                    () => {
                        const select = document.querySelector('select[name$="_length"]');
                        if (select) {
                            const opt = document.createElement('option');
                            opt.value = '-1';
                            opt.text = 'Todos';
                            select.appendChild(opt);
                            select.value = '-1';
                            select.dispatchEvent(new Event('change'));
                        }
                    }
                """)

                print("Esperando que se carguen todos los registros...")
                page.wait_for_timeout(5000)
                wait_for_table(page, max_retries=10)

                soup = BeautifulSoup(page.content(), 'html.parser')
                rows = soup.select("table tbody tr")
                for row in rows:
                    data = parse_row(row)
                    if data:
                        all_records.append(data)

            except Exception as e:
                print(f"Error en la navegacion: {e}")
                traceback.print_exc()

            browser.close()

        if not all_records:
            print("No se encontraron registros en la web.")
            return 0

        web_count = len(all_records)
        print(f"Total registros en la web (año {current_year}): {web_count}")

        nuevos = [r for r in all_records if r['expediente'] not in db_expedientes]

        if not nuevos:
            print("No hay registros nuevos. La BD esta actualizada.")
            return 0

        print(f"Encontrados {len(nuevos)} registros nuevos.")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for record in nuevos:
            cursor.execute('''
                INSERT OR REPLACE INTO fiscalizaciones (
                    expediente, nombre_razon_social, unidad_fiscalizable,
                    categoria, region, estado, detalle_link, fecha_scraping
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                record['expediente'],
                record['nombre_razon_social'],
                record['unidad_fiscalizable'],
                record['categoria'],
                record['region'],
                record['estado'],
                record['detalle_link'],
                datetime.now()
            ))
            print(f"  + {record['expediente']}")

        conn.commit()
        conn.close()
        print(f"Scraper finalizado. Se agregaron {len(nuevos)} registros a Fiscalizaciones.")
        return len(nuevos)


if __name__ == '__main__':
    scraper = SnifaFiscalizacionScraper()
    scraper.run()