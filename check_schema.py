import sqlite3
import json

def get_schema():
    conn = sqlite3.connect('data/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    schema = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        schema[table_name] = [col[1] for col in columns]
    
    conn.close()
    return schema

if __name__ == "__main__":
    print(json.dumps(get_schema(), indent=2))
