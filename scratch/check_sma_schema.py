import sqlite3
import os

DB_PATH = "data/data.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

tables = [
    "fiscalizaciones",
    "sancionatorios",
    "registroSanciones",
    "programasDeCumplimiento",
    "medidas_provisionales",
    "requerimientos"
]

for table in tables:
    print(f"Table: {table}")
    cursor.execute(f"PRAGMA table_info({table})")
    cols = cursor.fetchall()
    for col in cols:
        print(f"  {col[1]} ({col[2]})")
conn.close()
