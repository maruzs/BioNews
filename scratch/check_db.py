import sqlite3
import os

db_path = 'data/data.db'
if not os.path.exists(db_path):
    print(f"Database {db_path} not found.")
else:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [t[0] for t in c.fetchall()]
    print('Tables:', tables)
    for t in tables:
        print(f"\nTable: {t}")
        c.execute(f'PRAGMA table_info("{t}")')
        for col in c.fetchall():
            print(col)
    conn.close()
