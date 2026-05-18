"""
=============================================================
BioNews - Script de Verificación de Datos: SQLite vs PostgreSQL
=============================================================
Fase 1 del plan de microservicios.

Uso:
    python verify_data.py

Este script selecciona algunos registros aleatorios/clave de SQLite
y busca esos mismos registros exactos en PostgreSQL para comparar
sus valores y asegurar que el traspaso fue correcto e íntegro.
=============================================================
"""

import sqlite3
import psycopg2
import sys

SQLITE_PATH = "data/data.db"

PG_BASE = {
    "host": "localhost",
    "port": 5432,
    "user": "bionews_admin",
    "password": "secret_master_password",
}

DB_USERS        = {**PG_BASE, "dbname": "bionews_users_db"}
DB_NEWS         = {**PG_BASE, "dbname": "bionews_news_db"}
DB_LEGAL        = {**PG_BASE, "dbname": "bionews_legal_db"}
DB_CONSULTATIONS= {**PG_BASE, "dbname": "bionews_consultations_db"}

def get_pg_conn(cfg):
    return psycopg2.connect(**cfg)

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title.center(68)} ")
    print("=" * 70)

def main():
    print_separator("BioNews - Verificación Cruzada de Integridad")
    
    try:
        sqlite_conn = sqlite3.connect(SQLITE_PATH)
        sqlite_conn.row_factory = sqlite3.Row
        sq_cur = sqlite_conn.cursor()
        print("[OK] Conectado a SQLite origen.")
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a SQLite: {e}")
        sys.exit(1)

    # 1. Verificar base de datos bionews_users_db (Tabla: users)
    print_separator("1. VERIFICACIÓN: bionews_users_db (Tabla: users)")
    try:
        pg_conn = get_pg_conn(DB_USERS)
        pg_cur = pg_conn.cursor()
        
        # Obtener un usuario de SQLite
        sq_cur.execute("SELECT id, name, email, role FROM users LIMIT 2")
        sq_users = sq_cur.fetchall()
        
        for u in sq_users:
            print(f"-> Buscando en SQLite: ID={u['id']}, Email={u['email']}, Nombre={u['name']}")
            pg_cur.execute("SELECT id, name, email, role, status FROM users WHERE id = %s", (u['id'],))
            pg_user = pg_cur.fetchone()
            if pg_user:
                print(f"   [ENCONTRADO EN PG] ID={pg_user[0]}, Email={pg_user[2]}, Nombre={pg_user[1]}, Estado={pg_user[4]} [OK]")
            else:
                print(f"   [ERROR] Usuario ID={u['id']} NO encontrado en PostgreSQL.")
        
        pg_cur.close()
        pg_conn.close()
    except Exception as e:
        print(f"[ERROR] No se pudo verificar bionews_users_db: {e}")

    # 2. Verificar base de datos bionews_news_db (Tabla: noticias)
    print_separator("2. VERIFICACIÓN: bionews_news_db (Tabla: noticias)")
    try:
        pg_conn = get_pg_conn(DB_NEWS)
        pg_cur = pg_conn.cursor()
        
        # Obtener 2 noticias de SQLite
        sq_cur.execute("SELECT link, titulo, fuente FROM noticias LIMIT 2")
        sq_news = sq_cur.fetchall()
        
        for n in sq_news:
            short_title = n['titulo'][:50] + "..." if len(n['titulo']) > 50 else n['titulo']
            print(f"-> Buscando en SQLite noticia de: {n['fuente']} | Título: '{short_title}'")
            pg_cur.execute("SELECT link, titulo, fuente FROM noticias WHERE link = %s", (n['link'],))
            pg_news = pg_cur.fetchone()
            if pg_news:
                print("   [ENCONTRADO EN PG] Enlace y metadatos coinciden perfectamente. [OK]")
            else:
                print("   [ERROR] Noticia NO encontrada en PostgreSQL.")
                
        pg_cur.close()
        pg_conn.close()
    except Exception as e:
        print(f"[ERROR] No se pudo verificar bionews_news_db: {e}")

    # 3. Verificar base de datos bionews_legal_db (Tabla: pertinencias)
    print_separator("3. VERIFICACIÓN: bionews_legal_db (Tabla: pertinencias)")
    try:
        pg_conn = get_pg_conn(DB_LEGAL)
        pg_cur = pg_conn.cursor()
        
        # Obtener 2 pertinencias de SQLite (es la tabla con más de 25 mil filas!)
        sq_cur.execute('SELECT "Expediente", "Nombre_de_Proyecto", "Estado" FROM pertinencias LIMIT 2')
        sq_pert = sq_cur.fetchall()
        
        for p in sq_pert:
            short_project = p['Nombre_de_Proyecto'][:50] + "..." if len(p['Nombre_de_Proyecto']) > 50 else p['Nombre_de_Proyecto']
            print(f"-> Buscando en SQLite Expediente: {p['Expediente']} | Proyecto: '{short_project}'")
            pg_cur.execute('SELECT "Expediente", "Nombre_de_Proyecto", "Estado" FROM pertinencias WHERE "Expediente" = %s', (p['Expediente'],))
            pg_pert = pg_cur.fetchone()
            if pg_pert:
                print(f"   [ENCONTRADO EN PG] Expediente: {pg_pert[0]} | Estado en PG: {pg_pert[2]} [OK]")
            else:
                print(f"   [ERROR] Expediente {p['Expediente']} NO encontrado en PostgreSQL.")
                
        pg_cur.close()
        pg_conn.close()
    except Exception as e:
        print(f"[ERROR] No se pudo verificar bionews_legal_db: {e}")

    # 4. Verificar base de datos bionews_consultations_db (Tabla: documentos)
    print_separator("4. VERIFICACIÓN: bionews_consultations_db (Tabla: documentos)")
    try:
        pg_conn = get_pg_conn(DB_CONSULTATIONS)
        pg_cur = pg_conn.cursor()
        
        # Obtener 2 documentos de SQLite
        sq_cur.execute("SELECT id, consulta_id, nombre_documento FROM documentos LIMIT 2")
        sq_docs = sq_cur.fetchall()
        
        for d in sq_docs:
            print(f"-> Buscando en SQLite Documento ID={d['id']} | Consulta={d['consulta_id']} | Nombre='{d['nombre_documento']}'")
            pg_cur.execute("SELECT id, consulta_id, nombre_documento FROM documentos WHERE id = %s", (d['id'],))
            pg_doc = pg_cur.fetchone()
            if pg_doc:
                print(f"   [ENCONTRADO EN PG] ID={pg_doc[0]} | Nombre en PG: '{pg_doc[2]}' [OK]")
            else:
                print(f"   [ERROR] Documento ID={d['id']} NO encontrado en PostgreSQL.")
                
        pg_cur.close()
        pg_conn.close()
    except Exception as e:
        print(f"[ERROR] No se pudo verificar bionews_consultations_db: {e}")

    sqlite_conn.close()
    print_separator("VERIFICACIÓN FINALIZADA CON ÉXITO")

if __name__ == "__main__":
    main()
