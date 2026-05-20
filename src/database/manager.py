"""
src/database/manager.py  –  BioNews DatabaseManager (PostgreSQL)
=================================================================
Usa psycopg2 con dos pools thread-safe definidos en connection.py:
  - users_pool   → bionews_users
  - scrapers_pool → bionews_scrapers

Convenciones:
  - Placeholder: %s  (psycopg2, NO sqlite3 ?)
  - INSERT OR REPLACE  → INSERT ... ON CONFLICT DO UPDATE
  - INSERT OR IGNORE   → INSERT ... ON CONFLICT DO NOTHING
  - PRAGMA table_info  → information_schema.columns
  - julianday()        → EXTRACT(EPOCH FROM ...)
  - Fechas: se pasan como strings TEXT; Postgres hace cast implícito a TIMESTAMP
"""

from datetime import datetime
import json
import hashlib
from psycopg2.extras import RealDictCursor

from src.database.connection import users_conn, scrapers_conn, get_users_conn, release_users_conn, get_scrapers_conn, release_scrapers_conn


def _now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Caché en memoria para el schema de columnas por tabla
# (las columnas no cambian en runtime, solo al reiniciar el contenedor)
_column_schema_cache: dict = {}

# Mapeo de columnas para búsquedas globales por texto (ILIKE) en cada tabla
SEARCH_COLUMNS = {
    'sea_proyectos_evaluados': ['nombre', 'titular', 'id'],
    'fiscalizaciones': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'sancionatorios': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'normativas': ['detalle', 'organismo', 'materia', 'numero'],
    'medidas_provisionales': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'programasDeCumplimiento': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'registroSanciones': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'requerimientos': ['expediente', 'nombre_razon_social', 'unidad_fiscalizable', 'categoria'],
    'Tribunales': ['Caratula', 'Rol', 'Tribunal'],
    'minsal_vigentes': ['titulo', 'periodo_consulta'],
    'minsal_resultados': ['titulo', 'periodo_consulta'],
    'mma_abiertas': ['nombre_instrumento', 'ambito_territorial', 'tipo_proceso', 'tipo_instrumento'],
    'mma_cerradas': ['nombre_instrumento', 'ambito_territorial', 'tipo_proceso', 'tipo_instrumento'],
    'dga_consultas': ['nombre'],
    'noticias': ['titulo', 'resumen', 'url'],
}

# Mapeo de expresiones SQL para obtener la fecha formateada/parseada como DATE por tabla
TABLE_DATE_EXPRESSIONS = {
    'sea_proyectos_evaluados': 'f_parse_fecha_sea(fecha_presentacion)',
    'mma_abiertas': "to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY')",
    'mma_cerradas': "to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY')",
    'Tribunales': 'to_date(nullif("Fecha", \'\'), \'YYYY-MM-DD\')',
    'pertinencias': 'to_date(nullif("Fecha", \'\'), \'YYYY-MM-DD\')',
    'minsal_vigentes': "to_date(nullif(fecha_inicio, ''), 'YYYY-MM-DD')",
    'minsal_resultados': "to_date(nullif(fecha_inicio, ''), 'YYYY-MM-DD')",
    'normativas': "to_date(nullif(fecha, ''), 'YYYY-MM-DD')",
    'noticias': "to_date(nullif(fecha, ''), 'YYYY-MM-DD')"
}

class DatabaseManager:
    """Fachada única manteniendo la misma API que la versión SQLite."""

    # ── Conexiones raw (para compatibilidad con server.py que llama db.get_connection()) ──

    def get_connection(self):
        """Retorna conexión de scrapers (uso legacy en server.py). DEBE cerrarse manualmente."""
        return get_scrapers_conn()

    def get_users_connection(self):
        return get_users_conn()

    # ── INIT ────────────────────────────────────────────────────────────────
    def __init__(self):
        # No hace nada: los schemas ya existen por docker-entrypoint-initdb.d/
        pass

    # ── NOTICIAS ─────────────────────────────────────────────────────────────

    def save_news(self, news_list):
        inserted = 0
        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for item in news_list:
                    try:
                        cur.execute("""
                            INSERT INTO noticias (link, titulo, fecha, imagen, fuente, fecha_scraping)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ON CONFLICT (link) DO NOTHING
                        """, (item['link'], item['titulo'], item['fecha'],
                              item['imagen'], item['fuente'], _now_str()))
                        if cur.rowcount > 0:
                            inserted += 1
                    except Exception as e:
                        print(f"Error guardando noticia: {e}")
        return inserted

    def get_latest_news(self, limit=100):
        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT link, titulo, fecha, imagen, fuente, fecha_scraping
                    FROM noticias
                    ORDER BY fecha DESC, fecha_scraping DESC
                    LIMIT %s
                """, (limit,))
                return cur.fetchall()

    def clean_old_data(self, days=10):
        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM noticias
                    WHERE fecha_scraping < NOW() - INTERVAL '%s days'
                """, (days,))

    # ── TABLAS ESPECIFICAS ────────────────────────────────────────────────────

    def _build_where_clause(self, table_name, columns, search, date_start, date_end, filters):
        where_clauses = []
        params = []

        # 1. Búsqueda de palabra clave global
        if search:
            search_cols = SEARCH_COLUMNS.get(table_name, [])
            if search_cols:
                clauses = []
                for col in search_cols:
                    col_name = col if col.startswith('"') else f'"{col}"'
                    clauses.append(f"{col_name}::text ILIKE %s")
                    params.append(f"%{search}%")
                if clauses:
                    where_clauses.append("(" + " OR ".join(clauses) + ")")

        # 2. Filtros de fecha (Desde / Hasta)
        if date_start and table_name in TABLE_DATE_EXPRESSIONS:
            expr = TABLE_DATE_EXPRESSIONS[table_name]
            where_clauses.append(f"{expr} >= to_date(%s, 'YYYY-MM-DD')")
            params.append(date_start)
        if date_end and table_name in TABLE_DATE_EXPRESSIONS:
            expr = TABLE_DATE_EXPRESSIONS[table_name]
            where_clauses.append(f"{expr} <= to_date(%s, 'YYYY-MM-DD')")
            params.append(date_end)

        # 3. Filtros específicos por columnas
        if filters:
            for col, val in filters.items():
                if val is None or val == '' or val == 'all':
                    continue
                # Filtro especial de año para expedientes
                if col == 'expediente_year':
                    if 'expediente' in columns:
                        where_clauses.append('expediente ILIKE %s')
                        params.append(f"%{val}%")
                    elif 'expediente_id' in columns:
                        where_clauses.append('expediente_id ILIKE %s')
                        params.append(f"%{val}%")
                    continue

                # Buscar la columna en las columnas reales de la tabla de forma case-insensitive
                matching_cols = [c for c in columns if c.lower() == col.lower()]
                if matching_cols:
                    real_col = matching_cols[0]
                    where_clauses.append(f'"{real_col}" = %s')
                    params.append(val)

        where_sql = ""
        if where_clauses:
            where_sql = "WHERE " + " AND ".join(where_clauses)

        return where_sql, params

    def get_table_data(self, table_name, limit=1000, offset=0, search=None, date_start=None, date_end=None, filters=None):
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
            'dga_consultas', 'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")

        # Intentar obtener de caché Redis primero
        from src.database.cache import cache
        filter_data = {
            'search': search,
            'date_start': date_start,
            'date_end': date_end,
            'filters': filters
        }
        filter_str = json.dumps(filter_data, sort_keys=True)
        filter_hash = hashlib.md5(filter_str.encode('utf-8')).hexdigest()
        cache_key = f"table_data:{table_name}:{limit}:{offset}:{filter_hash}"
        
        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        with scrapers_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Schema de columnas: usar caché en memoria
                if table_name not in _column_schema_cache:
                    cur.execute("""
                        SELECT column_name FROM information_schema.columns
                        WHERE table_name = %s AND table_schema IN ('scrapers', 'users', 'public')
                    """, (table_name,))
                    _column_schema_cache[table_name] = [r['column_name'] for r in cur.fetchall()]
                columns = _column_schema_cache[table_name]

                # Construir Cláusulas WHERE
                where_sql, params = self._build_where_clause(table_name, columns, search, date_start, date_end, filters)

                # Definir orden cronológico por fecha de más nuevo a más antiguo
                date_sorts = {
                    'sea_proyectos_evaluados': "to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC",
                    'mma_abiertas': "to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY') DESC",
                    'mma_cerradas': "to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY') DESC",
                    'Tribunales': 'to_date(nullif("Fecha", \'\'), \'YYYY-MM-DD\') DESC',
                    'pertinencias': 'to_date(nullif("Fecha", \'\'), \'YYYY-MM-DD\') DESC',
                    'minsal_vigentes': "to_date(nullif(fecha_inicio, ''), 'YYYY-MM-DD') DESC",
                    'normativas': "to_date(nullif(fecha, ''), 'YYYY-MM-DD') DESC",
                    'noticias': "to_date(nullif(fecha, ''), 'YYYY-MM-DD') DESC",
                }

                snifa_tables = {'fiscalizaciones', 'medidas_provisionales', 'programasDeCumplimiento', 'registroSanciones', 'requerimientos', 'sancionatorios'}

                order_by = ""
                if table_name in date_sorts:
                    order_by = f"ORDER BY {date_sorts[table_name]} NULLS LAST"
                    if 'fecha_scraping' in columns:
                        order_by += ", fecha_scraping DESC"
                elif table_name in snifa_tables:
                    order_by = "ORDER BY CAST(SUBSTRING(detalle_link FROM '/([0-9]+)$') AS INTEGER) DESC NULLS LAST"
                elif 'ficha_id' in columns:
                    order_by = "ORDER BY ficha_id DESC NULLS LAST"
                elif 'fecha_scraping' in columns:
                    order_by = "ORDER BY fecha_scraping DESC"

                query_params = list(params)
                sql = f'SELECT * FROM "{table_name}" {where_sql} {order_by}'

                if limit and limit > 0:
                    sql += " LIMIT %s"
                    query_params.append(limit)
                    if offset and offset > 0:
                        sql += " OFFSET %s"
                        query_params.append(offset)

                cur.execute(sql, query_params)
                rows = cur.fetchall()
                result = [dict(r) for r in rows]

        # Guardar en caché Redis: tablas que cambian poco duran 5min, otras 2min
        static_tables = {'normativas', 'sea_proyectos_evaluados', 'pertinencias',
                         'mma_abiertas', 'mma_cerradas', 'minsal_vigentes', 'minsal_resultados',
                         'dga_consultas', 'Tribunales'}
        ttl = 300 if table_name in static_tables else 120  # 5 min o 2 min
        cache.set(cache_key, result, expire_seconds=ttl)

        return result

    def get_table_count(self, table_name, search=None, date_start=None, date_end=None, filters=None):
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales', 'noticias', 'favoritos',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas', 'dga_consultas',
            'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")

        # Intentar obtener de caché Redis primero
        from src.database.cache import cache
        filter_data = {
            'search': search,
            'date_start': date_start,
            'date_end': date_end,
            'filters': filters
        }
        filter_str = json.dumps(filter_data, sort_keys=True)
        filter_hash = hashlib.md5(filter_str.encode('utf-8')).hexdigest()
        cache_key = f"table_count:{table_name}:{filter_hash}"

        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        # favoritos y noticias están en users y scrapers respectivamente
        if table_name == 'favoritos':
            ctx = users_conn
        else:
            ctx = scrapers_conn

        with ctx() as conn:
            with conn.cursor() as cur:
                # Schema de columnas
                if table_name not in _column_schema_cache:
                    cur.execute("""
                        SELECT column_name FROM information_schema.columns
                        WHERE table_name = %s AND table_schema IN ('scrapers', 'users', 'public')
                    """, (table_name,))
                    _column_schema_cache[table_name] = [r[0] for r in cur.fetchall()]
                columns = _column_schema_cache[table_name]

                # Construir Cláusulas WHERE
                where_sql, params = self._build_where_clause(table_name, columns, search, date_start, date_end, filters)

                sql = f'SELECT COUNT(*) FROM "{table_name}" {where_sql}'
                cur.execute(sql, params)
                count = cur.fetchone()[0]

        cache.set(cache_key, count, expire_seconds=120)
        return count

    def get_distinct_column_options(self, table_name, column_name):
        allowed_tables = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
            'dga_consultas', 'sea_proyectos_evaluados'
        }
        if table_name not in allowed_tables:
            raise ValueError(f"Tabla no permitida: {table_name}")

        # Intentar obtener de caché Redis primero
        from src.database.cache import cache
        cache_key = f"options:{table_name}:{column_name}"
        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        # Obtener columnas
        if table_name not in _column_schema_cache:
            with scrapers_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT column_name FROM information_schema.columns
                        WHERE table_name = %s AND table_schema IN ('scrapers', 'users', 'public')
                    """, (table_name,))
                    _column_schema_cache[table_name] = [r[0] for r in cur.fetchall()]
        columns = _column_schema_cache[table_name]

        # Validar case-insensitive de la columna
        matching = [c for c in columns if c.lower() == column_name.lower()]
        if not matching:
            raise ValueError(f"Columna no válida para tabla {table_name}: {column_name}")
        real_col = matching[0]

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT DISTINCT "{real_col}"
                    FROM "{table_name}"
                    WHERE "{real_col}" IS NOT NULL AND "{real_col}" != ''
                    ORDER BY "{real_col}"
                """)
                res = [r[0] for r in cur.fetchall()]

        cache.set(cache_key, res, expire_seconds=600)  # 10 minutos
        return res

    # ── FAVORITOS ─────────────────────────────────────────────────────────────

    def add_favorite(self, user_id, id_o_link, fuente, nombre, accion=""):
        with users_conn() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        INSERT INTO favoritos (user_id, id_o_link, fuente, nombre, fecha_agregado, accion)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (user_id, id_o_link) DO UPDATE SET
                            fuente = EXCLUDED.fuente,
                            nombre = EXCLUDED.nombre,
                            accion = EXCLUDED.accion
                    """, (user_id, id_o_link, fuente, nombre, _now_str(), accion))
                    return True
                except Exception as e:
                    print(f"Error guardando favorito: {e}")
                    return False

    def remove_favorite(self, user_id, id_o_link):
        with users_conn() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("DELETE FROM favoritos WHERE user_id = %s AND id_o_link = %s",
                                (user_id, id_o_link))
                    return cur.rowcount > 0
                except Exception as e:
                    print(f"Error eliminando favorito: {e}")
                    return False

    def get_favorites(self, user_id, fuente=None):
        with users_conn() as conn:
            with conn.cursor() as cur:
                if fuente:
                    if fuente == "Tribunales":
                        cur.execute("""
                            SELECT user_id, id_o_link, fuente, nombre, fecha_agregado, accion
                            FROM favoritos
                            WHERE user_id = %s AND (fuente ILIKE '%TA%' OR fuente ILIKE '%Tribunal%' OR fuente ILIKE '%Corte%')
                            ORDER BY fecha_agregado DESC
                        """, (user_id,))
                    elif fuente == "SNIFA":
                        cur.execute("""
                            SELECT user_id, id_o_link, fuente, nombre, fecha_agregado, accion
                            FROM favoritos
                            WHERE user_id = %s AND (fuente ILIKE '%Fiscalizacion%' OR fuente ILIKE '%Sancionatorio%' OR fuente ILIKE '%Ingreso%' OR fuente ILIKE '%SNIFA%')
                            ORDER BY fecha_agregado DESC
                        """, (user_id,))
                    else:
                        cur.execute("""
                            SELECT user_id, id_o_link, fuente, nombre, fecha_agregado, accion
                            FROM favoritos WHERE user_id = %s AND fuente ILIKE %s
                            ORDER BY fecha_agregado DESC
                        """, (user_id, f"%{fuente}%"))
                else:
                    cur.execute("""
                        SELECT user_id, id_o_link, fuente, nombre, fecha_agregado, accion
                        FROM favoritos WHERE user_id = %s ORDER BY fecha_agregado DESC
                    """, (user_id,))
                return cur.fetchall()

    def is_favorite(self, user_id, id_o_link):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM favoritos WHERE user_id = %s AND id_o_link = %s",
                            (user_id, id_o_link))
                return cur.fetchone() is not None

    # ── USERS ─────────────────────────────────────────────────────────────────

    def get_user_by_email(self, email):
        with users_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                row = cur.fetchone()
                return dict(row) if row else None

    def create_user(self, name, email, password_hash, role="user"):
        with users_conn() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        INSERT INTO users (name, email, password_hash, role, blocked, preferences)
                        VALUES (%s, %s, %s, %s, 0, '{}')
                        RETURNING id
                    """, (name, email, password_hash, role))
                    return cur.fetchone()[0]
                except Exception:
                    return None

    def get_all_users(self):
        with users_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, email, role, blocked, preferences, last_login FROM users")
                return [dict(r) for r in cur.fetchall()]

    def update_user_last_login(self, user_id):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET last_login = %s WHERE id = %s", (_now_str(), user_id))

    def update_user_status(self, user_id, blocked):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET blocked = %s WHERE id = %s", (blocked, user_id))
                return cur.rowcount > 0

    def delete_user(self, user_id):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
                return cur.rowcount > 0

    def update_user_preferences(self, user_id, preferences_json):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET preferences = %s WHERE id = %s",
                            (preferences_json, user_id))
                return cur.rowcount > 0

    # ── SCRAPER LOGS ──────────────────────────────────────────────────────────

    def log_scraper_run(self, fuente, exito, error="", nuevos=0):
        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                ahora = _now_str()
                cur.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
                row = cur.fetchone()
                ultimo_exito = ahora if exito else (row[0] if row else None)
                estado = "OK" if exito else "ERROR"
                cur.execute("""
                    INSERT INTO scraper_logs (fuente, ultimo_intento, ultimo_exito, estado, error, nuevos_registros)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (fuente) DO UPDATE SET
                        ultimo_intento   = EXCLUDED.ultimo_intento,
                        ultimo_exito     = EXCLUDED.ultimo_exito,
                        estado           = EXCLUDED.estado,
                        error            = EXCLUDED.error,
                        nuevos_registros = EXCLUDED.nuevos_registros
                """, (fuente, ahora, ultimo_exito, estado, error, nuevos))

    def get_scraper_logs(self):
        with scrapers_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM scraper_logs ORDER BY ultimo_intento DESC")
                return [dict(r) for r in cur.fetchall()]

    # ── STATS ─────────────────────────────────────────────────────────────────

    def get_stats(self, table_name):
        with scrapers_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Verificar que existe
                cur.execute("""
                    SELECT 1 FROM information_schema.tables
                    WHERE table_schema='public' AND table_name=%s
                """, (table_name,))
                if not cur.fetchone():
                    return None

                stats = {}
                cur.execute(f'SELECT COUNT(*) AS c FROM "{table_name}"')
                stats['total'] = cur.fetchone()['c']

                if table_name == 'normativas':
                    cur.execute("""
                        SELECT organismo AS name, COUNT(*) AS count FROM normativas
                        WHERE organismo IS NOT NULL GROUP BY organismo ORDER BY count DESC LIMIT 15
                    """)
                    stats['by_organismo'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("""
                        SELECT
                            CASE
                                WHEN fecha ~ '^\\d{4}-' THEN SUBSTRING(fecha,1,4)
                                ELSE RIGHT(fecha,4)
                            END AS anio,
                            tipo_normativa AS tipo, COUNT(*) AS count
                        FROM normativas
                        WHERE fecha IS NOT NULL
                        GROUP BY anio, tipo_normativa ORDER BY anio DESC
                    """)
                    stats['by_year_type'] = [dict(r) for r in cur.fetchall() if r['anio'] and len(str(r['anio'])) == 4]

                elif table_name == 'fiscalizaciones':
                    cur.execute("SELECT region AS name, COUNT(*) AS count FROM fiscalizaciones WHERE region IS NOT NULL GROUP BY region ORDER BY count DESC")
                    stats['by_region'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("SELECT categoria AS name, COUNT(*) AS count FROM fiscalizaciones WHERE categoria IS NOT NULL GROUP BY categoria ORDER BY count DESC")
                    stats['by_tipo'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("""
                        SELECT SUBSTRING(expediente FROM '-(20\\d\\d)-') AS anio, COUNT(*) AS count
                        FROM fiscalizaciones WHERE expediente ~ '-(20\\d\\d)-'
                        GROUP BY anio ORDER BY anio DESC
                    """)
                    stats['by_year'] = [dict(r) for r in cur.fetchall()]

                elif table_name == 'medidas_provisionales':
                    cur.execute("SELECT region AS name, COUNT(*) AS count FROM medidas_provisionales WHERE region IS NOT NULL GROUP BY region ORDER BY count DESC")
                    stats['by_region'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("SELECT estado AS name, COUNT(*) AS count FROM medidas_provisionales WHERE estado IS NOT NULL GROUP BY estado ORDER BY count DESC")
                    stats['by_estado'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("""
                        SELECT SUBSTRING(expediente FROM '-(20\\d\\d)-') AS anio, COUNT(*) AS count
                        FROM medidas_provisionales WHERE expediente ~ '-(20\\d\\d)-'
                        GROUP BY anio ORDER BY anio DESC
                    """)
                    stats['by_year'] = [dict(r) for r in cur.fetchall()]

                elif table_name == 'Tribunales':
                    cur.execute("""SELECT "Tribunal" AS name, COUNT(*) AS count FROM "Tribunales" WHERE "Tribunal" IS NOT NULL GROUP BY "Tribunal" ORDER BY count DESC""")
                    stats['by_tribunal'] = [dict(r) for r in cur.fetchall()]
                    cur.execute("""
                        SELECT
                            CASE
                                WHEN "Fecha" ~ '^\\d{4}-' THEN SUBSTRING("Fecha",1,4)
                                ELSE RIGHT("Fecha",4)
                            END AS anio,
                            COUNT(*) AS count
                        FROM "Tribunales" WHERE "Fecha" IS NOT NULL
                        GROUP BY anio ORDER BY anio DESC
                    """)
                    stats['by_year'] = [dict(r) for r in cur.fetchall() if r['anio'] and len(str(r['anio'])) == 4]
                    cur.execute("""SELECT "Tipo_de_Procedimiento" AS name, COUNT(*) AS count FROM "Tribunales" WHERE "Tipo_de_Procedimiento" IS NOT NULL GROUP BY "Tipo_de_Procedimiento" ORDER BY count DESC""")
                    stats['by_procedimiento'] = [dict(r) for r in cur.fetchall()]

                return stats

    # ── NOTIFICACIONES ────────────────────────────────────────────────────────

    def update_category_exit(self, user_id, category_slug):
        with users_conn() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("""
                        INSERT INTO user_category_views (user_id, category_slug, last_exit_at)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (user_id, category_slug) DO UPDATE SET last_exit_at = EXCLUDED.last_exit_at
                    """, (int(user_id), category_slug, _now_str()))
                except Exception as e:
                    print(f"Error updating category exit: {e}")

    def mark_item_viewed(self, user_id, item_id_or_link, category_slug):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO user_item_views (user_id, item_id_or_link, category_slug, viewed_at)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (user_id, item_id_or_link, category_slug) DO NOTHING
                """, (user_id, item_id_or_link, category_slug, _now_str()))

    def get_user_category_last_exit(self, user_id, category_slug):
        with users_conn() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("SELECT last_exit_at FROM user_category_views WHERE user_id = %s AND category_slug = %s",
                                (int(user_id), category_slug))
                    row = cur.fetchone()
                    return row[0] if row else None
                except Exception as e:
                    print(f"Error getting last exit: {e}")
                    return None

    def get_viewed_items_ids(self, user_id, category_slug):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT item_id_or_link FROM user_item_views WHERE user_id = %s AND category_slug = %s",
                            (user_id, category_slug))
                return [r[0] for r in cur.fetchall()]

    def get_notification_status(self, user_id):
        """Retorna el estado de notificaciones para todas las categorías.
        Optimizado: batch-fetch de los últimos exits en 1 query + cache Redis 30s.
        """
        from src.database.cache import cache
        cache_key = f"notif_status:{user_id}"
        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        categories = [
            "noticias", "normativas", "pertinencias", "fiscalizaciones",
            "sancionatorios", "registroSanciones", "programasDeCumplimiento",
            "medidas_provisionales", "requerimientos", "Tribunales",
            "minsal_vigentes", "minsal_resultados", "mma", "dga", "sea_proyectos_evaluados"
        ]

        # Batch-fetch TODOS los last_exit_at del usuario en una sola query
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT category_slug, last_exit_at FROM user_category_views WHERE user_id = %s",
                    (int(user_id),)
                )
                exits = {row[0]: row[1] for row in cur.fetchall()}

        result = {cat: self._check_if_category_has_new_fast(user_id, cat, exits) for cat in categories}
        cache.set(cache_key, result, expire_seconds=30)
        return result

    def _check_if_category_has_new_fast(self, user_id, category_slug, exits_map: dict) -> bool:
        """Verifica si hay items nuevos usando el mapa de exits pre-cargado."""
        table_mapping = {
            "noticias": "noticias", "normativas": "normativas",
            "pertinencias": "pertinencias", "fiscalizaciones": "fiscalizaciones",
            "sancionatorios": "sancionatorios", "registroSanciones": "registroSanciones",
            "programasDeCumplimiento": "programasDeCumplimiento",
            "medidas_provisionales": "medidas_provisionales", "requerimientos": "requerimientos",
            "Tribunales": "Tribunales", "minsal_vigentes": "minsal_vigentes",
            "minsal_resultados": "minsal_resultados",
            "mma": ["mma_abiertas", "mma_cerradas"],
            "dga": "dga_consultas", "sea_proyectos_evaluados": "sea_proyectos_evaluados"
        }
        table = table_mapping.get(category_slug)
        if not table:
            return False
        tables = table if isinstance(table, list) else [table]
        last_exit = exits_map.get(category_slug)

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for t in tables:
                    if last_exit is None:
                        cur.execute(f'SELECT 1 FROM "{t}" LIMIT 1')
                    else:
                        # Comparar como text: funciona tanto si fecha_scraping es TEXT como TIMESTAMP
                        # TIMESTAMP::text produce 'YYYY-MM-DD HH:MM:SS' que ordena correctamente
                        last_exit_str = str(last_exit)[:19].replace('T', ' ')
                        cur.execute(
                            f'SELECT 1 FROM "{t}" WHERE fecha_scraping::text > %s LIMIT 1',
                            (last_exit_str,)
                        )
                    if cur.fetchone():
                        return True
        return False

    def _check_if_category_has_new(self, user_id, category_slug):
        """Compatibilidad legacy: sigue funcionando para el endpoint de categoría individual."""
        last_exit = self.get_user_category_last_exit(user_id, category_slug)

        table_mapping = {
            "noticias": "noticias", "normativas": "normativas",
            "pertinencias": "pertinencias", "fiscalizaciones": "fiscalizaciones",
            "sancionatorios": "sancionatorios", "registroSanciones": "registroSanciones",
            "programasDeCumplimiento": "programasDeCumplimiento",
            "medidas_provisionales": "medidas_provisionales", "requerimientos": "requerimientos",
            "Tribunales": "Tribunales", "minsal_vigentes": "minsal_vigentes",
            "minsal_resultados": "minsal_resultados",
            "mma": ["mma_abiertas", "mma_cerradas"],
            "dga": "dga_consultas", "sea_proyectos_evaluados": "sea_proyectos_evaluados"
        }

        table = table_mapping.get(category_slug)
        if not table:
            return False

        tables = table if isinstance(table, list) else [table]

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for t in tables:
                    if last_exit is None:
                        cur.execute(f'SELECT 1 FROM "{t}" LIMIT 1')
                    else:
                        # Comparar como text: funciona tanto si fecha_scraping es TEXT como TIMESTAMP
                        last_exit_str = str(last_exit)[:19].replace('T', ' ')
                        cur.execute(
                            f'SELECT 1 FROM "{t}" WHERE fecha_scraping::text > %s LIMIT 1',
                            (last_exit_str,)
                        )
                    if cur.fetchone():
                        return True
        return False

    def _normalize_date(self, date_val):
        if not date_val:
            return ""
        s = str(date_val).strip()
        if "/" in s or ("-" in s and len(s.split("-")[0]) != 4):
            sep = "/" if "/" in s else "-"
            parts = s.split(" ")[0].split(sep)
            time_part = " ".join(s.split(" ")[1:]) if " " in s else ""
            if len(parts) == 3:
                try:
                    d, m, y = parts
                    if len(y) == 2:
                        y = "20" + y
                    result = f"{y}-{m.zfill(2)}-{d.zfill(2)}"
                    return result + (f" {time_part}" if time_part else "")
                except Exception:
                    pass
        return s

    def get_items_with_new_flag(self, user_id, category_slug, items):
        """Marca cada item con is_new=True si fue scrapeado DESPUÉS del último exit del usuario.
        Si no hay last_exit (nunca visitó), todos son nuevos.
        Si hay last_exit, solo son nuevos los scrapeados después de ese momento.
        """
        notif_mapping = {"mma_abiertas": "mma", "mma_cerradas": "mma", "dga_consultas": "dga"}
        notif_category = notif_mapping.get(category_slug, category_slug)

        last_exit = self.get_user_category_last_exit(user_id, notif_category)

        if last_exit is None:
            # Nunca visitó → todos son nuevos
            for item in items:
                item['is_new'] = True
            return items

        # Normalizar last_exit a string comparable 'YYYY-MM-DD HH:MM:SS'
        last_exit_str = str(last_exit)[:19].replace('T', ' ')

        for item in items:
            item_date = item.get("fecha_scraping")
            if not item_date:
                item['is_new'] = False
            else:
                # Normalizar fecha_scraping del item igual que last_exit
                item_date_str = str(item_date)[:19].replace('T', ' ')
                # Ambos son 'YYYY-MM-DD HH:MM:SS' → comparación lexicográfica válida
                item['is_new'] = item_date_str > last_exit_str

        return items

    # ── DOCUMENTOS ────────────────────────────────────────────────────────────

    def get_consultation_documents(self, consulta_id, tipo_consulta):
        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT nombre_documento, link FROM documentos
                    WHERE consulta_id = %s AND tipo_consulta = %s
                """, (consulta_id, tipo_consulta))
                return [{"nombre": r[0], "link": r[1]} for r in cur.fetchall()]

    # ── BUG REPORTS ───────────────────────────────────────────────────────────

    def save_bug_report(self, user_id, titulo, descripcion, screenshot_path=None):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO bug_reports (user_id, titulo, descripcion, screenshot_path, fecha_reporte, status)
                    VALUES (%s, %s, %s, %s, %s, 'pendiente') RETURNING id
                """, (user_id, titulo, descripcion, screenshot_path, _now_str()))
                return cur.fetchone()[0]

    def get_bug_reports(self, user_id=None):
        with users_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                if user_id:
                    cur.execute("""
                        SELECT b.*, u.name AS user_name FROM bug_reports b
                        JOIN users u ON b.user_id = u.id
                        WHERE b.user_id = %s ORDER BY b.fecha_reporte DESC
                    """, (user_id,))
                else:
                    cur.execute("""
                        SELECT b.*, u.name AS user_name FROM bug_reports b
                        JOIN users u ON b.user_id = u.id
                        ORDER BY b.fecha_reporte DESC
                    """)
                return [dict(r) for r in cur.fetchall()]

    def update_bug_status(self, bug_id, status):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE bug_reports SET status = %s WHERE id = %s", (status, bug_id))
                return cur.rowcount > 0

    def get_bug_report(self, bug_id):
        with users_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM bug_reports WHERE id = %s", (bug_id,))
                row = cur.fetchone()
                return dict(row) if row else None

    def delete_bug_report(self, bug_id):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM bug_reports WHERE id = %s", (bug_id,))
                return cur.rowcount > 0