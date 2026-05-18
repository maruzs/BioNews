#!/usr/bin/env python3
"""
migrate_sqlite.py
=================
Script ONE-SHOT para migrar datos históricos desde data/data.db (SQLite)
hacia la base de datos PostgreSQL única (bionews) con dos esquemas.

Uso:
    # Desde el directorio raíz del proyecto:
    python migrate_sqlite.py

    # Pasar ruta custom al sqlite:
    python migrate_sqlite.py --db /ruta/a/data.db

Requisitos previos:
    - El contenedor postgres-db debe estar corriendo
    - Las variables de entorno deben estar definidas (o cargar el .env)
    - El archivo data/data.db debe existir
"""
import os
import sys
import sqlite3
import argparse
from datetime import datetime

# ── Cargador de .env robusto (sin depender de python-dotenv) ──────────────────
def load_env_fallback():
    # Buscar .env en el directorio actual o el directorio del script
    paths = [
        os.path.join(os.getcwd(), '.env'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    ]
    for path in paths:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        parts = line.split('=', 1)
                        k = parts[0].strip()
                        v = parts[1].strip()
                        # Quitar comillas si tiene
                        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                            v = v[1:-1]
                        if k not in os.environ:
                            os.environ[k] = v
            break

load_env_fallback()

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import psycopg2

# ── Configuración ────────────────────────────────────────────────────────────

DEFAULT_SQLITE = os.path.join(os.path.dirname(__file__), 'data', 'data.db')

DB_DSN = {
    "host":     os.getenv("DB_HOST",  "127.0.0.1"),
    "port":     int(os.getenv("DB_PORT", "5432")),
    "dbname":   os.getenv("DB_NAME",  "bionews"),
    "user":     os.getenv("DB_USER",  "bionews"),
    "password": os.getenv("DB_PASS",  "changeme"),
    "options":  "-c client_encoding=UTF8 -c search_path=users,scrapers,public",
}

def try_connect(dsn, fallback_port):
    """Intenta conectar usando el DSN provisto. Si falla y el host no es 127.0.0.1, hace fallback local."""
    try:
        return psycopg2.connect(**dsn)
    except Exception as primary_err:
        host = dsn.get("host")
        if host and host != "127.0.0.1" and host != "localhost":
            print(f"  [INFO] No se pudo conectar a {host}:{dsn.get('port')}. Intentando fallback a 127.0.0.1:{fallback_port}...")
            fallback_dsn = dsn.copy()
            fallback_dsn["host"] = "127.0.0.1"
            fallback_dsn["port"] = fallback_port
            try:
                return psycopg2.connect(**fallback_dsn)
            except Exception:
                pass
        raise primary_err



# ── Helpers ──────────────────────────────────────────────────────────────────

def sqlite_rows(sl_conn, table, extra_where=""):
    """Lee todas las filas de una tabla SQLite como lista de dicts."""
    try:
        cur = sl_conn.cursor()
        cur.execute(f"SELECT * FROM \"{table}\" {extra_where}")
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
    except sqlite3.OperationalError as e:
        print(f"  [WARN] Tabla '{table}' no existe o error: {e}")
        return []


def bulk_upsert(pg_cur, table, rows, conflict_col, cols_to_skip=None):
    """
    Inserta filas en PostgreSQL ignorando conflictos (ON CONFLICT DO NOTHING).
    cols_to_skip: lista de columnas a omitir en el INSERT (ej. columnas SERIAL).
    Usa SAVEPOINTs para evitar que fallas individuales aborten la transacción de Postgres.
    Convierte cadenas vacías '' a None (NULL) para prevenir errores de tipos (como TIMESTAMP)
    pero las conserva en columnas que forman parte de la clave primaria (conflict_col).
    """
    if not rows:
        return 0

    cols_to_skip = set(cols_to_skip or [])
    all_cols = [c for c in rows[0].keys() if c not in cols_to_skip]

    placeholders = ', '.join(['%s'] * len(all_cols))
    cols_quoted  = ', '.join([f'"{c}"' for c in all_cols])

    conflict_cols_set = set()
    if isinstance(conflict_col, (list, tuple)):
        conflict_cols_set.update(conflict_col)
    elif conflict_col:
        conflict_cols_set.add(conflict_col)

    if isinstance(conflict_col, (list, tuple)):
        conflict_str = ', '.join([f'"{c}"' for c in conflict_col])
    else:
        conflict_str = f'"{conflict_col}"'

    inserted = 0
    for row in rows:
        # Convertir "" a None para evitar errores de casteo en Postgres, excepto si es PK
        values = tuple((None if (v == "" and c not in conflict_cols_set) else v) for c, v in ((col, row.get(col)) for col in all_cols))
        try:
            pg_cur.execute("SAVEPOINT bulk_row_upsert")
            pg_cur.execute(
                f'INSERT INTO "{table}" ({cols_quoted}) VALUES ({placeholders})'
                f' ON CONFLICT ({conflict_str}) DO NOTHING',
                values
            )
            # Capturar el rowcount antes de ejecutar RELEASE SAVEPOINT ya que este último lo resetea
            row_added = pg_cur.rowcount > 0
            pg_cur.execute("RELEASE SAVEPOINT bulk_row_upsert")
            if row_added:
                inserted += 1
        except Exception as e:
            try:
                pg_cur.execute("ROLLBACK TO SAVEPOINT bulk_row_upsert")
            except Exception:
                pass
            print(f"  [WARN] Fila en '{table}' omitida debido a error: {e} | valores principales={values[:3]}...")
    return inserted


def sync_sequence(pg_cur, table, col="id"):
    """Resetea el contador de la secuencia SERIAL en PostgreSQL para que coincida con el máximo id actual."""
    try:
        # Nota: pg_get_serial_sequence no usa esquemas directamente tan facil si no pasas el nombre completo, 
        # pero podemos forzar el search_path.
        pg_cur.execute(f"SELECT setval(pg_get_serial_sequence('{table}', '{col}'), COALESCE(max(\"{col}\"), 1)) FROM \"{table}\"")
    except Exception as e:
        print(f"  [WARN] No se pudo sincronizar la secuencia para '{table}': {e}")


# ── Migración ────────────────────────────────────────────────────────────────

def migrate_users(sl_conn, pg_conn):
    cur = pg_conn.cursor()

    # users
    rows = sqlite_rows(sl_conn, "users")
    n = bulk_upsert(cur, "users", rows, "id")
    print(f"  users: {n}/{len(rows)} insertados")
    sync_sequence(cur, "users")

    # favoritos
    rows = sqlite_rows(sl_conn, "favoritos")
    n = bulk_upsert(cur, "favoritos", rows, ["user_id", "id_o_link"])
    print(f"  favoritos: {n}/{len(rows)} insertados")

    # user_category_views
    rows = sqlite_rows(sl_conn, "user_category_views")
    n = bulk_upsert(cur, "user_category_views", rows, "id")
    print(f"  user_category_views: {n}/{len(rows)} insertados")
    sync_sequence(cur, "user_category_views")

    # user_item_views
    rows = sqlite_rows(sl_conn, "user_item_views")
    n = bulk_upsert(cur, "user_item_views", rows, "id")
    print(f"  user_item_views: {n}/{len(rows)} insertados")
    sync_sequence(cur, "user_item_views")

    # bug_reports
    rows = sqlite_rows(sl_conn, "bug_reports")
    n = bulk_upsert(cur, "bug_reports", rows, "id")
    print(f"  bug_reports: {n}/{len(rows)} insertados")
    sync_sequence(cur, "bug_reports")

    pg_conn.commit()
    cur.close()


def migrate_scrapers(sl_conn, pg_conn):
    cur = pg_conn.cursor()

    simple_tables = [
        # (sqlite_table, pg_table, pk_col, skip_cols)
        ("noticias",               "noticias",               "link",        []),
        ("normativas",             "normativas",             "accion",      []),
        ("fiscalizaciones",        "fiscalizaciones",        "expediente",  []),
        ("medidas_provisionales",  "medidas_provisionales",  "expediente",  []),
        ("programasDeCumplimiento","programasDeCumplimiento","expediente",  []),
        ("registroSanciones",      "registroSanciones",      "expediente",  []),
        ("requerimientos",         "requerimientos",         "expediente",  []),
        ("sancionatorios",         "sancionatorios",         "expediente",  []),
        ("Tribunales",             "Tribunales",             "Rol",         []),
        ("pertinencias",           "pertinencias",           "Expediente",  []),
        ("sea_proyectos_evaluados","sea_proyectos_evaluados","id",           []),
        ("dga_consultas",          "dga_consultas",          "id",          []),
        ("minsal_resultados",      "minsal_resultados",      "id",          []),
        ("minsal_vigentes",        "minsal_vigentes",        "id",          []),
        ("mma_abiertas",           "mma_abiertas",           "id",          []),
        ("mma_cerradas",           "mma_cerradas",           "id",          []),
    ]

    for sl_tbl, pg_tbl, pk, skip in simple_tables:
        rows = sqlite_rows(sl_conn, sl_tbl)
        n = bulk_upsert(cur, pg_tbl, rows, pk, skip)
        print(f"  {pg_tbl}: {n}/{len(rows)} insertados")

    # documentos (PK serial, sin conflicto por id)
    rows = sqlite_rows(sl_conn, "documentos")
    inserted = 0
    for row in rows:
        cols = [c for c in row.keys() if c != 'id']
        ph   = ', '.join(['%s'] * len(cols))
        vals = tuple((None if v == "" else v) for v in (row.get(c) for c in cols))
        try:
            cur.execute("SAVEPOINT doc_insert")
            cur.execute(
                f'INSERT INTO "documentos" ({", ".join(cols)}) VALUES ({ph})',
                vals
            )
            doc_added = cur.rowcount > 0
            cur.execute("RELEASE SAVEPOINT doc_insert")
            if doc_added:
                inserted += 1
        except Exception as e:
            try:
                cur.execute("ROLLBACK TO SAVEPOINT doc_insert")
            except Exception:
                pass
            print(f"  [WARN] documentos: {e} | valores principales={vals[:2]}...")
    print(f"  documentos: {inserted}/{len(rows)} insertados")

    # scraper_logs
    rows = sqlite_rows(sl_conn, "scraper_logs")
    n = bulk_upsert(cur, "scraper_logs", rows, "fuente")
    print(f"  scraper_logs: {n}/{len(rows)} insertados")

    pg_conn.commit()
    cur.close()


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Migra data.db de SQLite a PostgreSQL Única")
    parser.add_argument("--db", default=DEFAULT_SQLITE, help="Ruta al archivo SQLite")
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"[ERROR] No se encontró el archivo SQLite: {args.db}")
        sys.exit(1)

    print(f"=== Iniciando migración desde: {args.db} ===")
    
    print("\n[DEBUG] Configuración cargada DB_DSN:")
    print(f"    Host: {DB_DSN['host']}")
    print(f"    Port: {DB_DSN['port']}")
    print(f"    DBName: {DB_DSN['dbname']}")
    print(f"    User: {DB_DSN['user']}")
    print(f"    Password: {'***' if DB_DSN['password'] else '(vacío)'}\n")

    sl_conn = sqlite3.connect(args.db)
    sl_conn.row_factory = sqlite3.Row

    try:
        pg_conn = try_connect(DB_DSN, 5432)
        
        print("\n--- Migrando esquema Users ---")
        migrate_users(sl_conn, pg_conn)
        print("✓ Esquema Users migrado correctamente")
        
        print("\n--- Migrando esquema Scrapers ---")
        migrate_scrapers(sl_conn, pg_conn)
        print("✓ Esquema Scrapers migrado correctamente")
        
        pg_conn.close()
    except Exception as e:
        print(f"[ERROR] Migración: {e}")

    sl_conn.close()
    print("\n=== Migración finalizada ===")

if __name__ == "__main__":
    main()
