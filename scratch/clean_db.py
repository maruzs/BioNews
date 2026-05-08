import sqlite3
import os

db_path = os.path.join('data', 'data.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("DELETE FROM mma_cerradas")
    conn.commit()
    print("Tabla mma_cerradas limpiada con éxito.")
except Exception as e:
    print(f"Error al limpiar tabla: {e}")
finally:
    conn.close()
