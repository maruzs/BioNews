import os
import re

scraper_dir = 'src/scrapers/'

db_map = {
    'sea_legal.py': 'bionews_legal_db', 'primerTribunal.py': 'bionews_legal_db',
    'segundoTribunal.py': 'bionews_legal_db', 'tercerTribunal.py': 'bionews_legal_db',
    'snifa.py': 'bionews_legal_db', 'sanciones.py': 'bionews_legal_db',
    'reqSEIA.py': 'bionews_legal_db', 'pdc.py': 'bionews_legal_db',
    'medidas.py': 'bionews_legal_db', 'fiscalizaciones.py': 'bionews_legal_db',
    'diario_oficial.py': 'bionews_legal_db',
    
    'minsal.py': 'bionews_consultations_db', 'mma_consultas.py': 'bionews_consultations_db',
    'dga_consultas.py': 'bionews_consultations_db',
    
    'mma.py': 'bionews_news_db', 'sbap.py': 'bionews_news_db',
    'sea.py': 'bionews_news_db', 'sernageomin.py': 'bionews_news_db',
    'tribunal2.py': 'bionews_news_db', 'sma.py': 'bionews_news_db',
    'corteSuprema.py': 'bionews_news_db', 'tribunal3.py': 'bionews_news_db',
    'scraper_dga.py': 'bionews_news_db'
}

def create_do_update(insert_columns, pk):
    updates = []
    for col in insert_columns:
        if col.strip(' \n"') != pk.strip(' \n"'):
            clean_col = col.strip(' \n"')
            updates.append(f"{clean_col} = EXCLUDED.{clean_col}")
    return " ON CONFLICT (" + pk + ") DO UPDATE SET " + ", ".join(updates)

for filename in os.listdir(scraper_dir):
    if not filename.endswith('.py') or filename in ['__init__.py', 'engine.py']:
        continue
        
    filepath = os.path.join(scraper_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    db_name = db_map.get(filename, 'bionews_news_db') 

    if 'import sqlite3' in content:
        content = content.replace('import sqlite3', 'from src.database.manager import DatabaseManager')
        content = re.sub(r'conn\s*=\s*sqlite3\.connect\([^\)]+\)', f"db_manager = DatabaseManager()\n        conn = db_manager.get_connection('{db_name}')", content)
        
    def replace_question_marks(match):
        sql = match.group(1)
        # Avoid replacing ? inside URL queries (like https://...?id=x)
        # Usually SQL strings are inside quotes, but we match the entire `(sql, params)`.
        # Replace ? with %s
        # BUT only if it is outside of URL. If 'requests.get(' or 'url = ' or 'href=' is in the same line, be careful.
        # Actually `cursor.execute` only contains SQL. So replacing `?` with `%s` is safe.
        sql = sql.replace('?', '%s')
        
        if 'INSERT OR IGNORE INTO' in sql:
            pk = 'id'
            if 'pertinencias' in sql: pk = 'Expediente'
            elif 'documentos' in sql: pk = 'link'
            elif 'normativas' in sql: pk = 'accion'
            elif 'noticias' in sql: pk = 'link'
            elif 'minsal_resultados' in sql: pk = 'id'
            elif 'minsal_vigentes' in sql: pk = 'id'
            elif 'Tribunales' in sql: pk = 'Rol'
            
            sql = sql.replace('INSERT OR IGNORE INTO', 'INSERT INTO')
            
            # append ON CONFLICT right before the end of the SQL string
            sql = re.sub(r'(\s*"""|\s*\'\'\'|\s*["\'])(,\s*\(.*?\))?$', r' ON CONFLICT (' + pk + r') DO NOTHING\1\2', sql)
            
        if 'INSERT OR REPLACE INTO' in sql:
            m = re.search(r'INSERT OR REPLACE INTO\s+(\w+)\s*\(([^)]+)\)', sql, re.IGNORECASE)
            if m:
                table = m.group(1)
                cols = [c.strip() for c in m.group(2).split(',')]
                
                pk = 'id'
                if table == 'Tribunales': pk = 'Rol'
                elif table == 'fiscalizaciones': pk = 'expediente'
                elif table == 'sancionatorios': pk = 'expediente'
                elif table == 'registroSanciones': pk = 'expediente'
                elif table == 'programasDeCumplimiento': pk = 'expediente'
                elif table == 'medidas_provisionales': pk = 'expediente'
                elif table == 'requerimientos': pk = 'expediente'
                
                do_update = create_do_update(cols, pk)
                sql = re.sub(r'INSERT OR REPLACE INTO', 'INSERT INTO', sql, flags=re.IGNORECASE)
                sql = re.sub(r'(\s*"""|\s*\'\'\'|\s*["\'])(,\s*\(.*?\))?$', r' ' + do_update + r'\1\2', sql)
        
        return 'cursor.execute(' + sql + ')'
        
    content = re.sub(r'cursor\.execute\((.*?)\)(?!\.)', replace_question_marks, content, flags=re.DOTALL)
    
    # Check if `cursor.executemany` exists
    content = re.sub(r'cursor\.executemany\((.*?)\)(?!\.)', replace_question_marks, content, flags=re.DOTALL)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Scrapers refactored")
