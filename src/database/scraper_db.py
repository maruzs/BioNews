"""
src/database/scraper_db.py
==========================
Helper minimalista para que los scrapers accedan a la DB de scrapers
sin importar sqlite3. Reemplaza el patrón:

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    ...
    conn.commit()
    conn.close()

Por:

    with get_scraper_connection() as conn:
        cursor = conn.cursor()
        ...
        conn.commit()   ← o dejar que el context manager lo haga
"""

from src.database.connection import scrapers_conn, get_scrapers_conn, release_scrapers_conn

# Re-exportar para uso directo en scrapers
__all__ = ["scrapers_conn", "get_scrapers_conn", "release_scrapers_conn"]
