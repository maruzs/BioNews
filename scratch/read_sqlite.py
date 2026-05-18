import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/data.db'))
print(f"Checking SQLite DB at: {db_path}")

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Check if table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sea_proyectos_evaluados';")
    exists = cur.fetchone()
    print(f"Table exists: {exists}")
    
    if exists:
        cur.execute("SELECT fecha_presentacion FROM sea_proyectos_evaluados LIMIT 15;")
        rows = cur.fetchall()
        print("SQLite Sample dates:")
        for r in rows:
            print(r)
    else:
        print("Table 'sea_proyectos_evaluados' not found.")
    conn.close()
else:
    print("SQLite DB file not found.")
