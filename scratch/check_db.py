import sqlite3
import os

db_path = "data/data.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT expediente FROM fiscalizaciones LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])
    conn.close()
else:
    print("Database not found")
