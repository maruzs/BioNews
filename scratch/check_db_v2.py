import sqlite3
import os

db_path = 'data/data.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
for t in ['Tribunales', 'normativas', 'fiscalizaciones', 'pertinencias']:
    print(f"\nTable: {t}")
    c.execute(f'PRAGMA table_info("{t}")')
    for col in c.fetchall():
        print(col)
conn.close()
