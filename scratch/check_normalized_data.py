import sqlite3
import collections

db_path = "data/data.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT DISTINCT fecha_presentacion FROM sea_proyectos_evaluados LIMIT 50")
rows = cur.fetchall()
print("=== Sample fecha_presentacion ===")
for r in rows:
    print(repr(r[0]))

cur.execute("SELECT count(*) FROM sea_proyectos_evaluados WHERE fecha_presentacion IS NULL")
print("NULL count:", cur.fetchone()[0])

cur.execute("SELECT count(*) FROM sea_proyectos_evaluados")
print("Total rows in sea_proyectos_evaluados:", cur.fetchone()[0])

conn.close()
