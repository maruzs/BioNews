import sqlite3

def create_tables():
    conn = sqlite3.connect('data/data.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS minsal_vigentes (
        id TEXT PRIMARY KEY,
        titulo TEXT,
        fecha_inicio TEXT,
        periodo_consulta TEXT,
        indicaciones TEXT,
        fecha_scraping TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS minsal_resultados (
        id TEXT PRIMARY KEY,
        titulo TEXT,
        fecha_scraping TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        consulta_id TEXT,
        tipo_consulta TEXT,
        nombre_documento TEXT,
        link TEXT
    );
    """)
    
    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
