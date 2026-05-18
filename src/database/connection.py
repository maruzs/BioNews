"""
src/database/connection.py
==========================
Pool de conexiones PostgreSQL thread-safe para BioNews.

Expone dos pools globales:
  - users_pool  → bionews_users  (users, favoritos, notificaciones, bug_reports)
  - scrapers_pool → bionews_scrapers (noticias, tablas de scrapers, logs)

Uso en scrapers:
    from src.database.connection import get_scrapers_conn, release_scrapers_conn
    conn = get_scrapers_conn()
    try:
        ...
    finally:
        release_scrapers_conn(conn)

O usando el context manager:
    from src.database.connection import scrapers_conn
    with scrapers_conn() as conn:
        ...
"""

import os
import logging
from contextlib import contextmanager

import psycopg2
from psycopg2 import pool as pg_pool
from psycopg2.extras import RealDictCursor

log = logging.getLogger("bionews.db")

# ── Configuración desde variables de entorno ─────────────────────────────────

_USERS_DSN = {
    "host":     os.getenv("DB_USERS_HOST",  "postgres-users"),
    "port":     int(os.getenv("DB_USERS_PORT", "5432")),
    "dbname":   os.getenv("DB_USERS_NAME",  "bionews_users"),
    "user":     os.getenv("DB_USERS_USER",  "bionews"),
    "password": os.getenv("DB_USERS_PASS",  "changeme"),
    "options":  "-c client_encoding=UTF8",
}

_SCRAPERS_DSN = {
    "host":     os.getenv("DB_SCRAPERS_HOST", "postgres-scrapers"),
    "port":     int(os.getenv("DB_SCRAPERS_PORT", "5432")),
    "dbname":   os.getenv("DB_SCRAPERS_NAME",  "bionews_scrapers"),
    "user":     os.getenv("DB_SCRAPERS_USER",  "bionews"),
    "password": os.getenv("DB_SCRAPERS_PASS",  "changeme"),
    "options":  "-c client_encoding=UTF8",
}

# Tamaño del pool: mínimo 2, máximo 10 por pool.
# Con 2 contenedores (api + scheduler) eso da hasta 20 conexiones por DB,
# muy por debajo del límite por defecto de Postgres (100).
_POOL_MIN = 2
_POOL_MAX = 10

# ── Pools globales (inicializados lazy en primera llamada) ────────────────────

_users_pool: pg_pool.ThreadedConnectionPool | None = None
_scrapers_pool: pg_pool.ThreadedConnectionPool | None = None


def _init_users_pool() -> pg_pool.ThreadedConnectionPool:
    global _users_pool
    if _users_pool is None:
        log.info("Inicializando pool DB Usuarios (%s@%s/%s)",
                 _USERS_DSN["user"], _USERS_DSN["host"], _USERS_DSN["dbname"])
        _users_pool = pg_pool.ThreadedConnectionPool(_POOL_MIN, _POOL_MAX, **_USERS_DSN)
    return _users_pool


def _init_scrapers_pool() -> pg_pool.ThreadedConnectionPool:
    global _scrapers_pool
    if _scrapers_pool is None:
        log.info("Inicializando pool DB Scrapers (%s@%s/%s)",
                 _SCRAPERS_DSN["user"], _SCRAPERS_DSN["host"], _SCRAPERS_DSN["dbname"])
        _scrapers_pool = pg_pool.ThreadedConnectionPool(_POOL_MIN, _POOL_MAX, **_SCRAPERS_DSN)
    return _scrapers_pool


# ── API pública ───────────────────────────────────────────────────────────────

def get_users_conn() -> psycopg2.extensions.connection:
    """Obtiene una conexión del pool de usuarios. Llamar release_users_conn() cuando termines."""
    return _init_users_pool().getconn()


def release_users_conn(conn: psycopg2.extensions.connection) -> None:
    """Devuelve una conexión al pool de usuarios."""
    if _users_pool and conn:
        _users_pool.putconn(conn)


def get_scrapers_conn() -> psycopg2.extensions.connection:
    """Obtiene una conexión del pool de scrapers. Llamar release_scrapers_conn() cuando termines."""
    return _init_scrapers_pool().getconn()


def release_scrapers_conn(conn: psycopg2.extensions.connection) -> None:
    """Devuelve una conexión al pool de scrapers."""
    if _scrapers_pool and conn:
        _scrapers_pool.putconn(conn)


@contextmanager
def users_conn():
    """Context manager para conexión de usuarios con commit/rollback automático."""
    conn = get_users_conn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        release_users_conn(conn)


@contextmanager
def scrapers_conn():
    """Context manager para conexión de scrapers con commit/rollback automático."""
    conn = get_scrapers_conn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        release_scrapers_conn(conn)


def close_all_pools() -> None:
    """Cierra todos los pools. Llamar en shutdown de la app."""
    global _users_pool, _scrapers_pool
    if _users_pool:
        _users_pool.closeall()
        _users_pool = None
    if _scrapers_pool:
        _scrapers_pool.closeall()
        _scrapers_pool = None
