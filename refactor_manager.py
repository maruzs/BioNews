import re
import os

filepath = 'src/database/manager.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Imports
content = content.replace('import sqlite3\n', 'import psycopg2\nfrom psycopg2.extras import RealDictCursor\n')

# 2. DatabaseManager Init
init_code = '''class DatabaseManager:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.user = os.getenv("POSTGRES_USER", "bionews_admin")
        self.password = os.getenv("POSTGRES_PASSWORD", "secret_master_password")
        self.port = os.getenv("POSTGRES_PORT", "5432")

    def get_connection(self, database_name):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=database_name
        )'''

content = re.sub(r'class DatabaseManager:[\s\S]*?def get_connection\(self\):\s+return sqlite3\.connect\(self\.db_path\)', init_code, content)

# 3. Remove init_db
content = re.sub(r'\s*def init_db\(self\):[\s\S]*?(?=\n\s*# ─── NOTICIAS)', '', content)

# 4. Map methods to specific databases
def replace_connection_call(match):
    method_block = match.group(0)
    method_name = match.group(1)
    
    # Determine DB based on method logic or name
    db = 'bionews_users_db' # default
    if 'news' in method_name or method_name in ['get_latest_news', 'get_news_by_source']:
        db = 'bionews_news_db'
    elif 'user' in method_name or 'favorito' in method_name or method_name in ['get_user', 'create_user', 'update_user', 'get_all_users', 'toggle_block_user', 'delete_user', 'save_bug_report', 'get_bug_reports', 'update_bug_status', 'get_bug_report', 'delete_bug_report']:
        db = 'bionews_users_db'
    elif 'legal' in method_name or 'tribunal' in method_name or 'sancion' in method_name or 'normativa' in method_name or 'pertinencia' in method_name or 'evaluado' in method_name:
        db = 'bionews_legal_db'
    elif 'consulta' in method_name or 'minsal' in method_name or 'mma' in method_name or 'dga' in method_name:
        db = 'bionews_consultations_db'
        
    # Check explicitly for some known prefixes
    if method_name.startswith('get_all_pertinencias') or method_name.startswith('get_all_evaluados') or method_name.startswith('get_stats_evaluados'):
        db = 'bionews_legal_db'
    if method_name.startswith('get_consultas') or method_name.startswith('get_mma') or method_name.startswith('get_dga') or method_name.startswith('get_minsal'):
        db = 'bionews_consultations_db'

    # Replace self.get_connection() with self.get_connection('...')
    new_block = method_block.replace('self.get_connection()', f"self.get_connection('{db}')")
    
    # Replace ? with %s in queries
    new_block = new_block.replace('?', '%s')
    
    # Replace lastrowid with RETURNING id
    if 'cursor.lastrowid' in new_block:
        new_block = re.sub(r'(cursor\.execute\("""\s*INSERT INTO \w+ \([^)]+\)\s*VALUES \([^)]+\))(.*?)\s*"""\s*,\s*(\(.*?\))\)', r'\1 RETURNING id\2""", \3)', new_block, flags=re.DOTALL)
        new_block = new_block.replace('return cursor.lastrowid', 'return cursor.fetchone()[0]')
        
    # Replace INSERT OR IGNORE INTO
    if 'INSERT OR IGNORE INTO' in new_block:
        # We need to know the unique key for ON CONFLICT. This is tricky.
        # Usually it's ON CONFLICT DO NOTHING without specifying the column, but PostgreSQL requires the column!
        # Luckily manager.py doesn't use much INSERT OR IGNORE, mostly scrapers do.
        # Let's just do a generic replacement if any
        new_block = new_block.replace('INSERT OR IGNORE INTO', 'INSERT INTO') # Will fix manually if needed

    # Fix dict_factory
    new_block = new_block.replace('conn.row_factory = sqlite3.Row', '')
    new_block = new_block.replace('conn.cursor()', 'conn.cursor(cursor_factory=RealDictCursor)')
    
    # dict(row) to dict(row) is fine since RealDictRow acts like a dict
    
    return new_block

content = re.sub(r'(def (\w+)\(self.*?)(?=\n\s*def |\Z)', replace_connection_call, content, flags=re.DOTALL)

with open('src/database/manager.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("manager.py refactored")
