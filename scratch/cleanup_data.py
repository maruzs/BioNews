import sqlite3
import os

DB_PATH = "data/data.db"

def cleanup():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables = [
        "mma_abiertas",
        "minsal_vigentes",
        "sea_proyectos_evaluados"
    ]

    for table in tables:
        try:
            cursor.execute(f"DELETE FROM {table} WHERE rowid = (SELECT MAX(rowid) FROM {table})")
            print(f"Deleted last record from {table}")
        except Exception as e:
            print(f"Error deleting from {table}: {e}")

    # Tribunales (last from each)
    tribunales = ["Primer Tribunal", "Segundo Tribunal", "Tercer Tribunal"]
    for trib in tribunales:
        try:
            cursor.execute("DELETE FROM Tribunales WHERE rowid = (SELECT MAX(rowid) FROM Tribunales WHERE Tribunal = ?)", (trib,))
            print(f"Deleted last record from Tribunales for {trib}")
        except Exception as e:
            print(f"Error deleting from Tribunales ({trib}): {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    cleanup()
