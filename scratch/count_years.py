import sqlite3

db_path = "data/data.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
    SELECT substr(fecha_presentacion, 7, 4) as anio, count(*)
    FROM sea_proyectos_evaluados
    GROUP BY anio
    ORDER BY anio DESC
""")
rows = cur.fetchall()
print("=== Grouped by Year in Database ===")
for r in rows:
    print(f"Year: {r[0]}, Count: {r[1]}")

conn.close()
