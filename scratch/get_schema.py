import sqlite3

def get_schema():
    conn = sqlite3.connect('data/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for name, sql in tables:
        print(f"--- TABLE: {name} ---")
        print(sql)
        print("\n")
    conn.close()

if __name__ == "__main__":
    get_schema()
