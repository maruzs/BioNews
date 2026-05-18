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
        clean_col = col.strip(' \n"')
        clean_pk = pk.strip(' \n"')
        if clean_col.lower() != clean_pk.lower():
            updates.append(f'"{clean_col}" = EXCLUDED."{clean_col}"')
    return " ON CONFLICT (\"" + pk + "\") DO UPDATE SET " + ", ".join(updates)

def refactor_call_string(call_str):
    # Find all string boundaries inside the call
    matches = list(re.finditer(r"'''|\"\"\"|'|\"", call_str))
    if not matches:
        return call_str
    
    first_match = matches[0]
    quote_type = first_match.group()
    start_idx = first_match.start()
    
    # Find the end of the very first string literal (the SQL query)
    end_idx = -1
    cur = start_idx + len(quote_type)
    while cur < len(call_str):
        if call_str[cur:cur+len(quote_type)] == quote_type and call_str[cur-1] != '\\':
            end_idx = cur
            break
        cur += 1
        
    if end_idx == -1:
        return call_str
        
    sql_str = call_str[start_idx:end_idx + len(quote_type)]
    
    # Apply SQL refactoring ONLY to the SQL string literal
    sql_str = sql_str.replace('?', '%s')
    
    # 2. Check and replace INSERT OR IGNORE
    if 'INSERT OR IGNORE INTO' in sql_str or 'insert or ignore into' in sql_str:
        pk = 'id'
        if 'pertinencias' in sql_str.lower(): pk = 'Expediente'
        elif 'documentos' in sql_str.lower(): pk = 'link'
        elif 'normativas' in sql_str.lower(): pk = 'accion'
        elif 'noticias' in sql_str.lower(): pk = 'link'
        elif 'minsal_resultados' in sql_str.lower(): pk = 'id'
        elif 'minsal_vigentes' in sql_str.lower(): pk = 'id'
        elif 'tribunales' in sql_str.lower(): pk = 'rol'
        
        m_table = re.search(r'INSERT OR IGNORE INTO\s+(\w+)', sql_str, re.IGNORECASE)
        if m_table:
            table_name = m_table.group(1).lower()
            sql_str = re.sub(r'INSERT OR IGNORE INTO\s+(\w+)', f'INSERT INTO "{table_name}"', sql_str, flags=re.IGNORECASE)
        else:
            sql_str = re.sub(r'INSERT OR IGNORE INTO', 'INSERT INTO', sql_str, flags=re.IGNORECASE)
        
        sql_str = sql_str[:-len(quote_type)] + ' ON CONFLICT ("' + pk + '") DO NOTHING' + quote_type
        
    # 3. Check and replace INSERT OR REPLACE
    elif 'INSERT OR REPLACE INTO' in sql_str or 'insert or replace into' in sql_str:
        m = re.search(r'INSERT OR REPLACE INTO\s+(\w+)\s*\(([^)]+)\)', sql_str, re.IGNORECASE)
        if m:
            table = m.group(1).lower()
            cols = [c.strip() for c in m.group(2).split(',')]
            
            pk = 'id'
            if table == 'tribunales': pk = 'rol'
            elif table == 'fiscalizaciones': pk = 'expediente'
            elif table == 'sancionatorios': pk = 'expediente'
            elif table == 'registrosanciones': pk = 'expediente'
            elif table == 'programasdecumplimiento': pk = 'expediente'
            elif table == 'medidas_provisionales': pk = 'expediente'
            elif table == 'requerimientos': pk = 'expediente'
            
            do_update = create_do_update(cols, pk)
            sql_str = re.sub(r'INSERT OR REPLACE INTO\s+(\w+)', f'INSERT INTO "{table}"', sql_str, flags=re.IGNORECASE)
            sql_str = sql_str[:-len(quote_type)] + ' ' + do_update + quote_type
            
    # Reconstruct the call_str!
    return call_str[:start_idx] + sql_str + call_str[end_idx + len(quote_type):]

def parse_and_refactor_calls(content):
    for method in ['cursor.execute', 'cursor.executemany']:
        start_idx = 0
        while True:
            idx = content.find(method + '(', start_idx)
            if idx == -1:
                break
            
            # Find the matching closing parenthesis
            paren_count = 1
            cur = idx + len(method) + 1
            
            # State tracking to ignore parentheses inside strings
            in_single_quote = False
            in_double_quote = False
            in_triple_single = False
            in_triple_double = False
            
            while cur < len(content) and paren_count > 0:
                char = content[cur]
                
                # Check for string boundaries
                if not in_single_quote and not in_double_quote and not in_triple_single and not in_triple_double:
                    if content[cur:cur+3] == "'''":
                        in_triple_single = True
                        cur += 2
                    elif content[cur:cur+3] == '"""':
                        in_triple_double = True
                        cur += 2
                    elif char == "'":
                        in_single_quote = True
                    elif char == '"':
                        in_double_quote = True
                    elif char == '(':
                        paren_count += 1
                    elif char == ')':
                        paren_count -= 1
                else:
                    if in_triple_single and content[cur:cur+3] == "'''":
                        in_triple_single = False
                        cur += 2
                    elif in_triple_double and content[cur:cur+3] == '"""':
                        in_triple_double = False
                        cur += 2
                    elif in_single_quote and char == "'" and content[cur-1] != '\\':
                        in_single_quote = False
                    elif in_double_quote and char == '"' and content[cur-1] != '\\':
                        in_double_quote = False
                        
                cur += 1
            
            if paren_count == 0:
                call_str = content[idx:cur]
                refactored = refactor_call_string(call_str)
                
                if refactored != call_str:
                    content = content[:idx] + refactored + content[cur:]
                    start_idx = idx + len(refactored)
                else:
                    start_idx = idx + len(method) + 1
            else:
                start_idx = idx + len(method) + 1
    return content

for filename in os.listdir(scraper_dir):
    if not filename.endswith('.py') or filename in ['__init__.py', 'engine.py']:
        continue
        
    filepath = os.path.join(scraper_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    db_name = db_map.get(filename, 'bionews_news_db') 

    # 1. Reemplazar imports y conexiones
    if 'import sqlite3' in content:
        content = content.replace('import sqlite3', 'from src.database.manager import DatabaseManager')
    
    # Asegurar que se use DatabaseManager
    if 'DatabaseManager' not in content:
        content = "from src.database.manager import DatabaseManager\n" + content

    content = re.sub(r'conn\s*=\s*sqlite3\.connect\([^\)]+\)', f"db_manager = DatabaseManager()\n    conn = db_manager.get_connection('{db_name}')", content)
    content = re.sub(r'conn\s*=\s*sqlite3\.connect\([^\)]+\)', f"db_manager = DatabaseManager()\n        conn = db_manager.get_connection('{db_name}')", content)

    # 2. Normalizar nombres de tabla a minúsculas en queries generales de SELECT/DELETE/etc.
    content = content.replace('registroSanciones', 'registrosanciones')
    content = content.replace('programasDeCumplimiento', 'programasdecumplimiento')
    content = content.replace('Tribunales', 'tribunales')

    # 3. Reemplazar placeholders y sintaxis SQL en cursor.execute/executemany
    content = parse_and_refactor_calls(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Scrapers refactored successfully.")
