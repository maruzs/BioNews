"""
=============================================================
BioNews - Script de Migración ETL: SQLite -> PostgreSQL
=============================================================
Fase 1 del plan de microservicios.

Uso:
    pip install psycopg2-binary
    python migrate_data.py

El script se conecta a la SQLite de origen (data/data.db)
y migra cada tabla a su base de datos PostgreSQL destino,
realizando la conversión de tipos necesaria.
=============================================================
"""

import sqlite3
import psycopg2
from psycopg2.extras import execute_values
from datetime import datetime, date
import sys
import traceback

# ─────────────────────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────────────────────
SQLITE_PATH = "data/data.db"
BATCH_SIZE = 500

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

# ─────────────────────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────────────────────

def parse_ts(value):
    """Intenta parsear un string a datetime. Retorna None si falla."""
    if value is None:
        return None
    if isinstance(value, (datetime, date)):
        return value
    for fmt in (
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
    ):
        try:
            return datetime.strptime(str(value).strip(), fmt)
        except ValueError:
            continue
    return None  # No parseable → NULL


def pg_connect(cfg):
    return psycopg2.connect(**cfg)


def migrate_table(sqlite_conn, pg_conn, table_name, create_sql, columns,
                  transform_fn=None, src_table=None):
    """
    Migra una tabla completa de SQLite a PostgreSQL en lotes.
    - create_sql  : DDL de CREATE TABLE IF NOT EXISTS para PG
    - columns     : lista de nombres de columnas en el orden del INSERT
    - transform_fn: función opcional que recibe una fila (tuple) y retorna otra
    - src_table   : nombre de tabla en SQLite (si difiere de table_name)
    """
    src = src_table or table_name
    pg_cur = pg_conn.cursor()

    if table_name == "tribunales":
        pg_cur.execute('DROP TABLE IF EXISTS "Tribunales"')
        pg_cur.execute('DROP TABLE IF EXISTS "tribunales"')
        pg_conn.commit()

    # 1. Crear tabla destino
    pg_cur.execute(create_sql)
    pg_conn.commit()

    # 2. Leer origen
    sq_cur = sqlite_conn.cursor()
    sq_cur.execute(f'SELECT * FROM "{src}"')
    col_names = [d[0] for d in sq_cur.description]

    placeholders = ",".join(["%s"] * len(columns))
    insert_sql = f"INSERT INTO \"{table_name}\" ({','.join(f'\"{c}\"' for c in columns)}) VALUES %s ON CONFLICT DO NOTHING"
    total_src = 0
    total_inserted = 0

    while True:
        rows = sq_cur.fetchmany(BATCH_SIZE)
        if not rows:
            break
        total_src += len(rows)

        if transform_fn:
            rows = [transform_fn(dict(zip(col_names, r))) for r in rows]
        else:
            rows = [tuple(r) for r in rows]

        # Filtrar Nones que vengan de transform_fn
        rows = [r for r in rows if r is not None]

        if rows:
            execute_values(pg_cur, insert_sql, rows)
            pg_conn.commit()
            total_inserted += len(rows)

    pg_cur.close()

    # 3. Validación de conteo
    pg_cur2 = pg_conn.cursor()
    pg_cur2.execute(f'SELECT COUNT(*) FROM "{table_name}"')
    pg_count = pg_cur2.fetchone()[0]
    pg_cur2.close()

    status = "✓" if pg_count >= total_src else "⚠ DIFERENCIA"
    print(f"  {status}  {table_name}: SQLite={total_src}  →  PostgreSQL={pg_count}")
    return total_src, pg_count


# ─────────────────────────────────────────────────────────────
# DDL DE TABLAS EN POSTGRESQL
# ─────────────────────────────────────────────────────────────

DDL = {

    # ── bionews_news_db ──────────────────────────────────────
    "noticias": """
        CREATE TABLE IF NOT EXISTS noticias (
            link            TEXT PRIMARY KEY,
            titulo          TEXT,
            fecha           TEXT,
            imagen          TEXT,
            fuente          TEXT,
            fecha_scraping  TIMESTAMP
        )
    """,

    # ── bionews_users_db ─────────────────────────────────────
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            id              SERIAL PRIMARY KEY,
            name            TEXT,
            email           TEXT UNIQUE,
            password_hash   TEXT,
            role            TEXT,
            blocked         INTEGER DEFAULT 0,
            preferences     TEXT,
            last_login      TIMESTAMP,
            status          TEXT DEFAULT 'ACTIVO'
        )
    """,
    "favoritos": """
        CREATE TABLE IF NOT EXISTS favoritos (
            user_id         INTEGER,
            id_o_link       TEXT,
            fuente          TEXT,
            nombre          TEXT,
            fecha_agregado  TIMESTAMP,
            accion          TEXT,
            PRIMARY KEY (user_id, id_o_link)
        )
    """,
    "user_category_views": """
        CREATE TABLE IF NOT EXISTS user_category_views (
            id              SERIAL PRIMARY KEY,
            user_id         INTEGER,
            category_slug   TEXT,
            last_exit_at    TIMESTAMP,
            UNIQUE (user_id, category_slug)
        )
    """,
    "user_item_views": """
        CREATE TABLE IF NOT EXISTS user_item_views (
            id              SERIAL PRIMARY KEY,
            user_id         INTEGER,
            item_id_or_link TEXT,
            category_slug   TEXT,
            viewed_at       TIMESTAMP,
            UNIQUE (user_id, item_id_or_link, category_slug)
        )
    """,
    "bug_reports": """
        CREATE TABLE IF NOT EXISTS bug_reports (
            id              SERIAL PRIMARY KEY,
            user_id         INTEGER,
            titulo          TEXT,
            descripcion     TEXT,
            screenshot_path TEXT,
            fecha_reporte   TIMESTAMP,
            status          TEXT DEFAULT 'pendiente'
        )
    """,

    # ── bionews_legal_db ─────────────────────────────────────
    "fiscalizaciones": """
        CREATE TABLE IF NOT EXISTS fiscalizaciones (
            expediente          TEXT PRIMARY KEY,
            nombre_razon_social TEXT,
            unidad_fiscalizable TEXT,
            categoria           TEXT,
            region              TEXT,
            estado              TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "medidas_provisionales": """
        CREATE TABLE IF NOT EXISTS medidas_provisionales (
            expediente          TEXT PRIMARY KEY,
            unidad_fiscalizable TEXT,
            nombre_razon_social TEXT,
            categoria           TEXT,
            region              TEXT,
            estado              TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "normativas": """
        CREATE TABLE IF NOT EXISTS normativas (
            fecha           TEXT,
            normativa       TEXT,
            tipo_normativa  TEXT,
            organismo       TEXT,
            suborganismo    TEXT,
            accion          TEXT PRIMARY KEY,
            fecha_scraping  TEXT,
            ficha_id        INTEGER
        )
    """,
    "pertinencias": """
        CREATE TABLE IF NOT EXISTS pertinencias (
            "Expediente"           TEXT PRIMARY KEY,
            "Nombre_de_Proyecto"   TEXT,
            "Proponente"           TEXT,
            "Fecha"                TEXT,
            "Estado"               TEXT,
            "Accion"               TEXT,
            fecha_scraping         TIMESTAMP,
            tipo_proyecto          TEXT,
            categoria_economica    TEXT
        )
    """,
    "programasDeCumplimiento": """
        CREATE TABLE IF NOT EXISTS programasdecumplimiento (
            expediente          TEXT PRIMARY KEY,
            unidad_fiscalizable TEXT,
            nombre_razon_social TEXT,
            categoria           TEXT,
            region              TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "registroSanciones": """
        CREATE TABLE IF NOT EXISTS registrosanciones (
            expediente          TEXT PRIMARY KEY,
            unidad_fiscalizable TEXT,
            nombre_razon_social TEXT,
            categoria           TEXT,
            region              TEXT,
            multa_uta           TEXT,
            pago_multa          TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "requerimientos": """
        CREATE TABLE IF NOT EXISTS requerimientos (
            expediente          TEXT PRIMARY KEY,
            unidad_fiscalizable TEXT,
            nombre_razon_social TEXT,
            categoria           TEXT,
            region              TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "sancionatorios": """
        CREATE TABLE IF NOT EXISTS sancionatorios (
            expediente          TEXT PRIMARY KEY,
            unidad_fiscalizable TEXT,
            nombre_razon_social TEXT,
            categoria           TEXT,
            region              TEXT,
            estado              TEXT,
            detalle_link        TEXT,
            fecha_scraping      TIMESTAMP,
            ficha_id            INTEGER
        )
    """,
    "Tribunales": """
        CREATE TABLE IF NOT EXISTS tribunales (
            rol                 TEXT PRIMARY KEY,
            fecha               TEXT,
            caratula            TEXT,
            tribunal            TEXT,
            tipo_de_procedimiento TEXT,
            estado_procesal     TEXT,
            accion              TEXT,
            fecha_scraping      TIMESTAMP
        )
    """,
    "sea_proyectos_evaluados": """
        CREATE TABLE IF NOT EXISTS sea_proyectos_evaluados (
            id                   TEXT PRIMARY KEY,
            nombre               TEXT,
            titular              TEXT,
            via_ingreso          TEXT,
            estado_proyecto      TEXT,
            razon_ingreso        TEXT,
            fecha_presentacion   TEXT,
            subestado_proyecto   TEXT,
            categoria_economica  TEXT,
            url                  TEXT,
            fecha_scraping       TIMESTAMP,
            region               TEXT,
            tipo_proyecto        TEXT
        )
    """,
    "scraper_logs": """
        CREATE TABLE IF NOT EXISTS scraper_logs (
            fuente          TEXT PRIMARY KEY,
            ultimo_intento  TIMESTAMP,
            ultimo_exito    TIMESTAMP,
            estado          TEXT,
            error           TEXT,
            nuevos_registros INTEGER
        )
    """,

    # ── bionews_consultations_db ─────────────────────────────
    "minsal_vigentes": """
        CREATE TABLE IF NOT EXISTS minsal_vigentes (
            id               TEXT PRIMARY KEY,
            titulo           TEXT,
            fecha_inicio     TEXT,
            periodo_consulta TEXT,
            indicaciones     TEXT,
            fecha_scraping   TIMESTAMP
        )
    """,
    "minsal_resultados": """
        CREATE TABLE IF NOT EXISTS minsal_resultados (
            id             TEXT PRIMARY KEY,
            titulo         TEXT,
            fecha_scraping TIMESTAMP
        )
    """,
    "mma_abiertas": """
        CREATE TABLE IF NOT EXISTS mma_abiertas (
            id                   TEXT PRIMARY KEY,
            nombre_instrumento   TEXT,
            fecha_inicio         TEXT,
            fecha_termino        TEXT,
            tipo_instrumento     TEXT,
            tipo_proceso         TEXT,
            ambito_territorial   TEXT,
            link_detalle         TEXT,
            fecha_scraping       TIMESTAMP
        )
    """,
    "mma_cerradas": """
        CREATE TABLE IF NOT EXISTS mma_cerradas (
            id                   TEXT PRIMARY KEY,
            nombre_instrumento   TEXT,
            fecha_inicio         TEXT,
            fecha_termino        TEXT,
            tipo_instrumento     TEXT,
            ambito_territorial   TEXT,
            link_detalle         TEXT,
            fecha_scraping       TIMESTAMP
        )
    """,
    "dga_consultas": """
        CREATE TABLE IF NOT EXISTS dga_consultas (
            id             TEXT PRIMARY KEY,
            nombre         TEXT,
            imagen         TEXT,
            url            TEXT,
            fecha_scraping TIMESTAMP
        )
    """,
    "documentos": """
        CREATE TABLE IF NOT EXISTS documentos (
            id               SERIAL PRIMARY KEY,
            consulta_id      TEXT,
            tipo_consulta    TEXT,
            nombre_documento TEXT,
            link             TEXT
        )
    """,
}

# ─────────────────────────────────────────────────────────────
# TRANSFORMADORES (FILAS SQLITE -> TUPLAS POSTGRES)
# ─────────────────────────────────────────────────────────────

def tr_noticias(r):
    return (r["link"], r["titulo"], r["fecha"], r["imagen"],
            r["fuente"], parse_ts(r["fecha_scraping"]))

def tr_users(r):
    return (r["id"], r["name"], r["email"], r["password_hash"],
            r["role"], r["blocked"], r["preferences"],
            parse_ts(r["last_login"]), "ACTIVO")

def tr_favoritos(r):
    return (r["user_id"], r["id_o_link"], r["fuente"], r["nombre"],
            parse_ts(r["fecha_agregado"]), r["accion"])

def tr_user_category_views(r):
    return (r["id"], r["user_id"], r["category_slug"],
            parse_ts(r["last_exit_at"]))

def tr_user_item_views(r):
    return (r["id"], r["user_id"], r["item_id_or_link"],
            r["category_slug"], parse_ts(r["viewed_at"]))

def tr_bug_reports(r):
    return (r["id"], r["user_id"], r["titulo"], r["descripcion"],
            r["screenshot_path"], parse_ts(r["fecha_reporte"]), r.get("status", "pendiente"))

def tr_fiscalizaciones(r):
    return (r["expediente"], r["nombre_razon_social"], r["unidad_fiscalizable"],
            r["categoria"], r["region"], r["estado"], r["detalle_link"],
            parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_medidas_provisionales(r):
    return (r["expediente"], r["unidad_fiscalizable"], r["nombre_razon_social"],
            r["categoria"], r["region"], r["estado"], r["detalle_link"],
            parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_normativas(r):
    return (r["fecha"], r["normativa"], r["tipo_normativa"], r["organismo"],
            r["suborganismo"], r["accion"], r["fecha_scraping"], r["ficha_id"])

def tr_pertinencias(r):
    return (r["Expediente"], r["Nombre_de_Proyecto"], r["Proponente"],
            r["Fecha"], r["Estado"], r["Accion"],
            parse_ts(r["fecha_scraping"]), r.get("tipo_proyecto"), r.get("categoria_economica"))

def tr_programas(r):
    return (r["expediente"], r["unidad_fiscalizable"], r["nombre_razon_social"],
            r["categoria"], r["region"], r["detalle_link"],
            parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_registro_sanciones(r):
    return (r["expediente"], r["unidad_fiscalizable"], r["nombre_razon_social"],
            r["categoria"], r["region"], r["multa_uta"], r["pago_multa"],
            r["detalle_link"], parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_requerimientos(r):
    return (r["expediente"], r["unidad_fiscalizable"], r["nombre_razon_social"],
            r["categoria"], r["region"], r["detalle_link"],
            parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_sancionatorios(r):
    return (r["expediente"], r["unidad_fiscalizable"], r["nombre_razon_social"],
            r["categoria"], r["region"], r["estado"], r["detalle_link"],
            parse_ts(r["fecha_scraping"]), r["ficha_id"])

def tr_tribunales(r):
    return (r.get("Rol"), r.get("Fecha"), r.get("Caratula"),
            r.get("Tribunal"), r.get("Tipo_de_Procedimiento"), r.get("Estado_Procesal"),
            r.get("Accion"), parse_ts(r.get("fecha_scraping")))

def tr_sea(r):
    return (r["id"], r["nombre"], r["titular"], r["via_ingreso"],
            r["estado_proyecto"], r["razon_ingreso"], r["fecha_presentacion"],
            r["subestado_proyecto"], r["categoria_economica"], r["url"],
            parse_ts(r["fecha_scraping"]), r["region"], r.get("tipo_proyecto"))

def tr_scraper_logs(r):
    return (r["fuente"], parse_ts(r["ultimo_intento"]), parse_ts(r["ultimo_exito"]),
            r["estado"], r["error"], r["nuevos_registros"])

def tr_minsal_vigentes(r):
    return (r["id"], r["titulo"], r["fecha_inicio"], r["periodo_consulta"],
            r["indicaciones"], parse_ts(r["fecha_scraping"]))

def tr_minsal_resultados(r):
    return (r["id"], r["titulo"], parse_ts(r["fecha_scraping"]))

def tr_mma_abiertas(r):
    return (r["id"], r["nombre_instrumento"], r["fecha_inicio"], r["fecha_termino"],
            r["tipo_instrumento"], r["tipo_proceso"], r["ambito_territorial"],
            r["link_detalle"], parse_ts(r["fecha_scraping"]))

def tr_mma_cerradas(r):
    return (r["id"], r["nombre_instrumento"], r["fecha_inicio"], r["fecha_termino"],
            r["tipo_instrumento"], r["ambito_territorial"],
            r["link_detalle"], parse_ts(r["fecha_scraping"]))

def tr_dga(r):
    return (r["id"], r["nombre"], r["imagen"], r["url"],
            parse_ts(r["fecha_scraping"]))

def tr_documentos(r):
    return (r["id"], r["consulta_id"], r["tipo_consulta"],
            r["nombre_documento"], r["link"])


# ─────────────────────────────────────────────────────────────
# PLAN DE MIGRACIÓN
# ─────────────────────────────────────────────────────────────
#  (tabla_sqlite, tabla_pg, db_config, ddl_key, columnas, transform_fn)

MIGRATION_PLAN = [
    # ── bionews_news_db ──────────────────────────────────────
    ("noticias", "noticias", DB_NEWS, "noticias",
     ["link","titulo","fecha","imagen","fuente","fecha_scraping"], tr_noticias),

    # ── bionews_users_db ─────────────────────────────────────
    ("users", "users", DB_USERS, "users",
     ["id","name","email","password_hash","role","blocked","preferences","last_login","status"], tr_users),
    ("favoritos", "favoritos", DB_USERS, "favoritos",
     ["user_id","id_o_link","fuente","nombre","fecha_agregado","accion"], tr_favoritos),
    ("user_category_views", "user_category_views", DB_USERS, "user_category_views",
     ["id","user_id","category_slug","last_exit_at"], tr_user_category_views),
    ("user_item_views", "user_item_views", DB_USERS, "user_item_views",
     ["id","user_id","item_id_or_link","category_slug","viewed_at"], tr_user_item_views),
    ("bug_reports", "bug_reports", DB_USERS, "bug_reports",
     ["id","user_id","titulo","descripcion","screenshot_path","fecha_reporte","status"], tr_bug_reports),

    # ── bionews_legal_db ─────────────────────────────────────
    ("fiscalizaciones", "fiscalizaciones", DB_LEGAL, "fiscalizaciones",
     ["expediente","nombre_razon_social","unidad_fiscalizable","categoria","region","estado","detalle_link","fecha_scraping","ficha_id"], tr_fiscalizaciones),
    ("medidas_provisionales", "medidas_provisionales", DB_LEGAL, "medidas_provisionales",
     ["expediente","unidad_fiscalizable","nombre_razon_social","categoria","region","estado","detalle_link","fecha_scraping","ficha_id"], tr_medidas_provisionales),
    ("normativas", "normativas", DB_LEGAL, "normativas",
     ["fecha","normativa","tipo_normativa","organismo","suborganismo","accion","fecha_scraping","ficha_id"], tr_normativas),
    ("pertinencias", "pertinencias", DB_LEGAL, "pertinencias",
     ["Expediente","Nombre_de_Proyecto","Proponente","Fecha","Estado","Accion","fecha_scraping","tipo_proyecto","categoria_economica"], tr_pertinencias),
    ("programasDeCumplimiento", "programasdecumplimiento", DB_LEGAL, "programasDeCumplimiento",
     ["expediente","unidad_fiscalizable","nombre_razon_social","categoria","region","detalle_link","fecha_scraping","ficha_id"], tr_programas),
    ("registroSanciones", "registrosanciones", DB_LEGAL, "registroSanciones",
     ["expediente","unidad_fiscalizable","nombre_razon_social","categoria","region","multa_uta","pago_multa","detalle_link","fecha_scraping","ficha_id"], tr_registro_sanciones),
    ("requerimientos", "requerimientos", DB_LEGAL, "requerimientos",
     ["expediente","unidad_fiscalizable","nombre_razon_social","categoria","region","detalle_link","fecha_scraping","ficha_id"], tr_requerimientos),
    ("sancionatorios", "sancionatorios", DB_LEGAL, "sancionatorios",
     ["expediente","unidad_fiscalizable","nombre_razon_social","categoria","region","estado","detalle_link","fecha_scraping","ficha_id"], tr_sancionatorios),
    ("Tribunales", "tribunales", DB_LEGAL, "Tribunales",
     ["rol","fecha","caratula","tribunal","tipo_de_procedimiento","estado_procesal","accion","fecha_scraping"], tr_tribunales),
    ("sea_proyectos_evaluados", "sea_proyectos_evaluados", DB_LEGAL, "sea_proyectos_evaluados",
     ["id","nombre","titular","via_ingreso","estado_proyecto","razon_ingreso","fecha_presentacion","subestado_proyecto","categoria_economica","url","fecha_scraping","region","tipo_proyecto"], tr_sea),
    ("scraper_logs", "scraper_logs", DB_LEGAL, "scraper_logs",
     ["fuente","ultimo_intento","ultimo_exito","estado","error","nuevos_registros"], tr_scraper_logs),

    # ── bionews_consultations_db ─────────────────────────────
    ("minsal_vigentes", "minsal_vigentes", DB_CONSULTATIONS, "minsal_vigentes",
     ["id","titulo","fecha_inicio","periodo_consulta","indicaciones","fecha_scraping"], tr_minsal_vigentes),
    ("minsal_resultados", "minsal_resultados", DB_CONSULTATIONS, "minsal_resultados",
     ["id","titulo","fecha_scraping"], tr_minsal_resultados),
    ("mma_abiertas", "mma_abiertas", DB_CONSULTATIONS, "mma_abiertas",
     ["id","nombre_instrumento","fecha_inicio","fecha_termino","tipo_instrumento","tipo_proceso","ambito_territorial","link_detalle","fecha_scraping"], tr_mma_abiertas),
    ("mma_cerradas", "mma_cerradas", DB_CONSULTATIONS, "mma_cerradas",
     ["id","nombre_instrumento","fecha_inicio","fecha_termino","tipo_instrumento","ambito_territorial","link_detalle","fecha_scraping"], tr_mma_cerradas),
    ("dga_consultas", "dga_consultas", DB_CONSULTATIONS, "dga_consultas",
     ["id","nombre","imagen","url","fecha_scraping"], tr_dga),
    ("documentos", "documentos", DB_CONSULTATIONS, "documentos",
     ["id","consulta_id","tipo_consulta","nombre_documento","link"], tr_documentos),
]


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def ensure_databases_exist():
    # Conectarse a la base de datos principal (bionews_master)
    master_cfg = {**PG_BASE, "dbname": "bionews_master"}
    print("[INFO] Asegurando existencia de las bases de datos lógicas en PostgreSQL...")
    try:
        conn = psycopg2.connect(**master_cfg)
        conn.autocommit = True
        cur = conn.cursor()
        
        # Obtener bases de datos existentes
        cur.execute("SELECT datname FROM pg_database;")
        existing_dbs = [row[0] for row in cur.fetchall()]
        
        target_dbs = ["bionews_users_db", "bionews_news_db", "bionews_legal_db", "bionews_consultations_db"]
        for db in target_dbs:
            if db not in existing_dbs:
                print(f"  -> Creando base de datos: {db}")
                cur.execute(f'CREATE DATABASE "{db}"')
                cur.execute(f'GRANT ALL PRIVILEGES ON DATABASE "{db}" TO {master_cfg["user"]}')
            else:
                print(f"  -> Base de datos {db} ya existe.")
        
        cur.close()
        conn.close()
        print("[OK] Bases de datos listas y configuradas.\n")
    except Exception as e:
        print(f"[ERROR] No se pudieron aprovisionar las bases de datos en PostgreSQL: {e}")
        print("[INFO] Asegúrate de que el contenedor de Postgres esté en ejecución y los datos de acceso en PG_BASE sean correctos.")
        sys.exit(1)


def main():
    print("=" * 60)
    print("  BioNews - Migración ETL: SQLite → PostgreSQL")
    print("=" * 60)

    # 1. Asegurar bases de datos en Postgres
    ensure_databases_exist()

    # Verificar conexión SQLite
    try:
        sqlite_conn = sqlite3.connect(SQLITE_PATH)
        sqlite_conn.row_factory = sqlite3.Row
        print(f"[OK] Conectado a SQLite: {SQLITE_PATH}\n")
    except Exception as e:
        print(f"[ERROR] No se pudo abrir SQLite: {e}")
        sys.exit(1)

    # Pool de conexiones PG (una por DB)
    pg_conns = {}
    for cfg in [DB_USERS, DB_NEWS, DB_LEGAL, DB_CONSULTATIONS]:
        dbname = cfg["dbname"]
        try:
            pg_conns[dbname] = pg_connect(cfg)
            print(f"[OK] Conectado a PostgreSQL: {dbname}")
        except Exception as e:
            print(f"[ERROR] No se pudo conectar a {dbname}: {e}")
            sys.exit(1)

    print()
    errors = []
    db_headers_printed = set()

    for (src_tbl, dst_tbl, db_cfg, ddl_key, columns, transform_fn) in MIGRATION_PLAN:
        dbname = db_cfg["dbname"]
        if dbname not in db_headers_printed:
            print(f"\n── {dbname} {'─'*(45-len(dbname))}")
            db_headers_printed.add(dbname)

        # Verificar si la tabla existe en el origen SQLite
        sq_cur = sqlite_conn.cursor()
        sq_cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name = ?", (src_tbl,))
        if not sq_cur.fetchone():
            print(f"  ⚠  {src_tbl}: No existe en SQLite (se omite de forma segura)")
            continue

        try:
            migrate_table(
                sqlite_conn=sqlite_conn,
                pg_conn=pg_conns[dbname],
                table_name=dst_tbl,
                create_sql=DDL[ddl_key],
                columns=columns,
                transform_fn=transform_fn,
                src_table=src_tbl,
            )
        except Exception as e:
            msg = f"  ✗ ERROR en {src_tbl} → {dbname}.{dst_tbl}: {e}"
            print(msg)
            errors.append(msg)
            traceback.print_exc()
            pg_conns[dbname].rollback()

    # Cerrar conexiones
    sqlite_conn.close()
    for conn in pg_conns.values():
        conn.close()

    print("\n" + "=" * 60)
    if errors:
        print(f"  Migración completada con {len(errors)} error(es):")
        for err in errors:
            print(f"  {err}")
    else:
        print("  ✓ Migración completada sin errores.")
    print("=" * 60)


if __name__ == "__main__":
    main()
