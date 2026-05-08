import os
import sqlite3
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')

class MINSALScraper:
    def run(self):
        """Ejecuta el scraper de MINSAL."""
        url = "https://www.minsal.cl/consultas-publicas-vigentes/"
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code != 200:
                print(f"Error al acceder a MINSAL: {resp.status_code}")
                return 0
            html = resp.text
        except Exception as e:
            print(f"Error de conexión con MINSAL: {e}")
            return 0

        soup = BeautifulSoup(html, 'html.parser')
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Identificar la posición de la sección de resultados
        resultados_title = soup.find('h2', string=lambda t: t and "Resultados de consultas públicas" in t)
        
        all_details = soup.find_all('details', class_='e-n-accordion-item')
        
        total_nuevos = 0
        total_procesados = 0
        
        for details in all_details:
            id_attr = details.get('id', '')
            if not id_attr or 'accordion-item-' not in id_attr:
                continue
                
            consulta_id = id_attr.split('-')[-1]
            total_procesados += 1
            
            # ... resto del código ...
            # Título de la consulta
            title_tag = details.find('div', class_='e-n-accordion-item-title-text')
            titulo = title_tag.get_text(strip=True) if title_tag else ""
            
            # Verificar si es tabla de resultados (columnas Documento y Descarga)
            table = details.find('table')
            if not table: continue
            
            headers = [th.get_text(strip=True).lower() for th in table.find_all('th')]
            is_resultado = "documento" in headers and "descarga" in headers
            
            if is_resultado:
                # Es un resultado de consulta
                cursor.execute("SELECT 1 FROM minsal_resultados WHERE id = ?", (consulta_id,))
                if not cursor.fetchone():
                    print(f"  Nuevo Resultado: {titulo}")
                    cursor.execute("""
                        INSERT INTO minsal_resultados (id, titulo, fecha_scraping)
                        VALUES (?, ?, ?)
                    """, (consulta_id, titulo, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    
                    # Documentos de resultados
                    rows = table.find_all('tr')
                    for row in rows:
                        tds = row.find_all('td')
                        if len(tds) >= 2:
                            doc_name = tds[0].get_text(strip=True)
                            link_tag = tds[1].find('a')
                            if link_tag:
                                href = link_tag.get('href')
                                cursor.execute("""
                                    INSERT INTO documentos (consulta_id, tipo_consulta, nombre_documento, link)
                                    VALUES (?, ?, ?, ?)
                                """, (consulta_id, 'minsal_resultado', doc_name, href))
                    total_nuevos += 1
            else:
                # Es una consulta vigente
                cursor.execute("SELECT 1 FROM minsal_vigentes WHERE id = ?", (consulta_id,))
                if not cursor.fetchone():
                    print(f"  Nueva Consulta Vigente: {titulo}")
                    data = {'fecha_inicio': None, 'periodo_consulta': None, 'indicaciones': None}
                    rows = table.find_all('tr')
                    
                    docs = []
                    for row in rows:
                        tds = row.find_all('td')
                        if len(tds) < 2: continue
                        
                        label = tds[0].get_text(strip=True)
                        value = " ".join([t.get_text(strip=True) for t in tds[1:]])
                        
                        if "Fecha de Publicación" in label:
                            data['fecha_inicio'] = self.parse_date(value)
                        elif "Periodo de Consulta" in label:
                            data['periodo_consulta'] = value
                        elif "Indicaciones" in label:
                            data['indicaciones'] = value
                        
                        # Buscar documentos en esta fila
                        links = row.find_all('a')
                        for link in links:
                            href = link.get('href')
                            if href and ('.pdf' in href or '.doc' in href or '.docx' in href):
                                docs.append({'nombre': label, 'link': href})

                    cursor.execute("""
                        INSERT INTO minsal_vigentes (id, titulo, fecha_inicio, periodo_consulta, indicaciones, fecha_scraping)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (consulta_id, titulo, data['fecha_inicio'], data['periodo_consulta'], data['indicaciones'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    
                    for doc in docs:
                        cursor.execute("""
                            INSERT INTO documentos (consulta_id, tipo_consulta, nombre_documento, link)
                            VALUES (?, ?, ?, ?)
                        """, (consulta_id, 'minsal_vigente', doc['nombre'], doc['link']))
                    
                    total_nuevos += 1

        print(f"  MINSAL: {total_procesados} consultas analizadas, {total_nuevos} nuevas.")
        conn.commit()
        conn.close()
        return total_nuevos

    def parse_date(self, text):
        """Parsea fechas en español como '05 de mayo de 2026' a '2026-05-05'."""
        months = {
            'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
            'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
            'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
        }
        text_lower = text.lower()
        found_month = None
        for m_name, m_num in months.items():
            if m_name in text_lower:
                found_month = m_num
                break
        
        if found_month:
            day_match = re.search(r'(\d{1,2})', text)
            year_match = re.search(r'(\d{4})', text)
            if day_match and year_match:
                day = day_match.group(1).zfill(2)
                year = year_match.group(1)
                return f"{year}-{found_month}-{day}"
        return text

if __name__ == "__main__":
    scraper = MINSALScraper()
    print(f"Nuevos registros: {scraper.run()}")
