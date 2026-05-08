import sqlite3
import os

DB_PATH = "data/data.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

tables = [
    "mma_abiertas",
    "mma_cerradas",
    "minsal_vigentes",
    "minsal_resultados",
    "sea_proyectos_evaluados",
    "pertinencias"
]

for table in tables:
    print(f"Table: {table}")
    try:
        cursor.execute(f"PRAGMA table_info({table})")
        cols = cursor.fetchall()
        for col in cols:
            print(f"  {col[1]} ({col[2]})")
    except:
        print(f"  Error reading table {table}")
conn.close()
