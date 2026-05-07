
import sqlite3
import os
import re

DB_PATH = "data/data.db"

def extract_ficha_id(url):
    """Extrae el número de ficha del final de la URL."""
    if not url:
        return None
    try:
        # Casos SNIFA: https://snifa.sma.gob.cl/.../Ficha/1075741
        # Casos Diario Oficial: .../2805795.pdf
        url = url.split('?')[0] # Quitar parámetros
        url = url.rstrip('/')
        if url.endswith('.pdf'):
            url = url[:-4]
        
        parts = url.split('/')
        if parts:
            last_part = parts[-1]
            if last_part.isdigit():
                return int(last_part)
    except:
        pass
    return None

def migrate():
    if not os.path.exists(DB_PATH):
        print(f"Base de datos no encontrada en {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables = [
        'fiscalizaciones', 
        'sancionatorios', 
        'registroSanciones', 
        'programasDeCumplimiento', 
        'requerimientos', 
        'medidas_provisionales',
        'normativas'
    ]

    for table in tables:
        print(f"Procesando tabla: {table}")
        
        # 1. Agregar columna ficha_id si no existe
        cursor.execute(f"PRAGMA table_info({table})")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'ficha_id' not in columns:
            print(f"  Agregando columna ficha_id a {table}...")
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN ficha_id INTEGER")
        else:
            print(f"  Columna ficha_id ya existe en {table}.")

        # 2. Poblar ficha_id para registros existentes
        link_col = 'accion' if table == 'normativas' else 'detalle_link'
        cursor.execute(f"SELECT rowid, {link_col} FROM {table} WHERE ficha_id IS NULL")
        rows = cursor.fetchall()
        
        if rows:
            print(f"  Actualizando {len(rows)} registros con ficha_id...")
            updates = []
            for rowid, link in rows:
                fid = extract_ficha_id(link)
                if fid is not None:
                    updates.append((fid, rowid))
            
            if updates:
                cursor.executemany(f"UPDATE {table} SET ficha_id = ? WHERE rowid = ?", updates)
                print(f"  {len(updates)} registros actualizados.")
        else:
            print(f"  No hay registros pendientes de ficha_id en {table}.")

    # 3. Caso especial Normativas: Eliminar duplicados y establecer PK si es posible
    # El usuario pidió que 'accion' sea PK.
    print("Optimizando tabla normativas...")
    
    # Primero limpiar duplicados reales (por accion)
    cursor.execute("SELECT accion, COUNT(*) FROM normativas GROUP BY accion HAVING COUNT(*) > 1")
    duplicates = cursor.fetchall()
    if duplicates:
        print(f"  Encontrados {len(duplicates)} grupos de duplicados en normativas. Limpiando...")
        for accion, count in duplicates:
            # Mantener el que tenga rowid más bajo (o más alto, da igual si son idénticos)
            cursor.execute("DELETE FROM normativas WHERE accion = ? AND rowid NOT IN (SELECT MIN(rowid) FROM normativas WHERE accion = ?)", (accion, accion))
    
    # Recrear tabla para asegurar que accion es PRIMARY KEY y tiene ficha_id
    cursor.execute("PRAGMA table_info(normativas)")
    cols_info = cursor.fetchall()
    cols_names = [c[1] for c in cols_info]
    
    # Verificamos si ya es PRIMARY KEY (pk column in PRAGMA is index 5)
    is_pk = any(c[5] > 0 for c in cols_info if c[1] == 'accion')
    
    if not is_pk:
        print("  Redefiniendo normativas con accion como PRIMARY KEY...")
        # Definir la estructura deseada
        cursor.execute("ALTER TABLE normativas RENAME TO normativas_old")
        cursor.execute('''
            CREATE TABLE normativas (
                fecha TEXT,
                normativa TEXT,
                tipo_normativa TEXT,
                organismo TEXT,
                suborganismo TEXT,
                accion TEXT PRIMARY KEY,
                fecha_scraping TEXT,
                ficha_id INTEGER
            )
        ''')
        # Mapear columnas existentes
        common_cols = [c for c in cols_names if c != 'id'] # evitar id autoincrement si existía
        cols_str = ", ".join(common_cols)
        cursor.execute(f"INSERT OR IGNORE INTO normativas ({cols_str}) SELECT {cols_str} FROM normativas_old")
        cursor.execute("DROP TABLE normativas_old")
        print("  Tabla normativas recreada con PRIMARY KEY en 'accion'.")

    conn.commit()
    conn.close()
    print("Migración completada.")

if __name__ == "__main__":
    migrate()
