import sqlite3
import os

db_path = "data/data.db"
if not os.path.exists(db_path):
    print("data.db not found")
else:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [r[0] for r in cur.fetchall()]
        print("Tables:", tables)
        
        if "sea_proyectos_evaluados" in tables:
            cur.execute("SELECT fecha_presentacion FROM sea_proyectos_evaluados LIMIT 10")
            rows = cur.fetchall()
            print("First 10 values of fecha_presentacion:")
            for r in rows:
                print(r[0], type(r[0]))
        else:
            print("sea_proyectos_evaluados not in tables")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
