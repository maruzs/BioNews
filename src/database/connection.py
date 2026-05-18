"""
src/database/connection.py
==========================
Pool de conexiones PostgreSQL thread-safe para BioNews.

Utiliza una única base de datos (bionews) con dos esquemas (users, scrapers).
Mantiene las funciones legacy (users_conn, scrapers_conn) apuntando al mismo
pool para mantener retrocompatibilidad con el resto del código.
"""

import os
import logging
from contextlib import contextmanager

import psycopg2
from psycopg2 import pool as pg_pool

log = logging.getLogger("bionews.db")

# ── Configuración desde variables de entorno ─────────────────────────────────

_DB_DSN = {
    "host":     os.getenv("DB_HOST",  "postgres-db"),
    "port":     int(os.getenv("DB_PORT", "5432")),
    "dbname":   os.getenv("DB_NAME",  "bionews"),
    "user":     os.getenv("DB_USER",  "bionews"),
    "password": os.getenv("DB_PASS",  "changeme"),
    # Clave: buscar en esquemas 'users' y 'scrapers' por defecto
    "options":  "-c client_encoding=UTF8 -c search_path=users,scrapers,public",
}

_POOL_MIN = 2
_POOL_MAX = 20  # Aumentamos ya que ahora es un solo pool

_pool: pg_pool.ThreadedConnectionPool | None = None

def _init_pool() -> pg_pool.ThreadedConnectionPool:
    global _pool
    if _pool is None:
        log.info("Inicializando pool DB Única (%s@%s/%s)",
                 _DB_DSN["user"], _DB_DSN["host"], _DB_DSN["dbname"])
        _pool = pg_pool.ThreadedConnectionPool(_POOL_MIN, _POOL_MAX, **_DB_DSN)
    return _pool

# ── API pública ───────────────────────────────────────────────────────────────

def get_connection() -> psycopg2.extensions.connection:
    return _init_pool().getconn()

def release_connection(conn: psycopg2.extensions.connection) -> None:
    if _pool and conn:
        _pool.putconn(conn)

# Wrappers para mantener compatibilidad
def get_users_conn() -> psycopg2.extensions.connection:
    return get_connection()

def release_users_conn(conn: psycopg2.extensions.connection) -> None:
    release_connection(conn)

def get_scrapers_conn() -> psycopg2.extensions.connection:
    return get_connection()

def release_scrapers_conn(conn: psycopg2.extensions.connection) -> None:
    release_connection(conn)

@contextmanager
def db_conn():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        release_connection(conn)

@contextmanager
def users_conn():
    with db_conn() as conn:
        yield conn

@contextmanager
def scrapers_conn():
    with db_conn() as conn:
        yield conn

def close_all_pools() -> None:
    global _pool
    if _pool:
        _pool.closeall()
        _pool = None
