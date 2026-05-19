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
from psycopg2.extras import RealDictCursor

from src.database.connection import users_conn, scrapers_conn, get_users_conn, release_users_conn, get_scrapers_conn, release_scrapers_conn


def _now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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

    def get_table_data(self, table_name, limit=1000, offset=0):
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
            'dga_consultas', 'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")

        with scrapers_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Detectar columnas para ordenar
                cur.execute("""
                    SELECT column_name FROM information_schema.columns
                    WHERE table_name = %s AND table_schema IN ('scrapers', 'users', 'public')
                """, (table_name,))
                columns = [r['column_name'] for r in cur.fetchall()]

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

                order_by = ""
                if table_name in date_sorts:
                    order_by = f"ORDER BY {date_sorts[table_name]} NULLS LAST"
                    if 'fecha_scraping' in columns:
                        order_by += ", fecha_scraping DESC"
                elif 'fecha_scraping' in columns:
                    order_by = "ORDER BY fecha_scraping DESC"
                elif 'ficha_id' in columns:
                    order_by = "ORDER BY ficha_id DESC"

                if limit and limit > 0:
                    if offset and offset > 0:
                        cur.execute(f'SELECT * FROM "{table_name}" {order_by} LIMIT %s OFFSET %s', (limit, offset))
                    else:
                        cur.execute(f'SELECT * FROM "{table_name}" {order_by} LIMIT %s', (limit,))
                else:
                    cur.execute(f'SELECT * FROM "{table_name}" {order_by}')
                rows = cur.fetchall()
                return [dict(r) for r in rows]

    def get_table_count(self, table_name):
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales', 'noticias', 'favoritos',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas', 'dga_consultas',
            'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")

        # favoritos y noticias están en users y scrapers respectivamente
        if table_name == 'favoritos':
            ctx = users_conn
        else:
            ctx = scrapers_conn

        with ctx() as conn:
            with conn.cursor() as cur:
                cur.execute(f'SELECT COUNT(*) FROM "{table_name}"')
                return cur.fetchone()[0]

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
                cur.execute("""
                    INSERT INTO user_category_views (user_id, category_slug, last_exit_at)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (user_id, category_slug) DO UPDATE SET last_exit_at = EXCLUDED.last_exit_at
                """, (user_id, category_slug, _now_str()))

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
                cur.execute("SELECT last_exit_at FROM user_category_views WHERE user_id = %s AND category_slug = %s",
                            (user_id, category_slug))
                row = cur.fetchone()
                return row[0] if row else None

    def get_viewed_items_ids(self, user_id, category_slug):
        with users_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT item_id_or_link FROM user_item_views WHERE user_id = %s AND category_slug = %s",
                            (user_id, category_slug))
                return [r[0] for r in cur.fetchall()]

    def get_notification_status(self, user_id):
        categories = [
            "noticias", "normativas", "pertinencias", "fiscalizaciones",
            "sancionatorios", "registroSanciones", "programasDeCumplimiento",
            "medidas_provisionales", "requerimientos", "Tribunales",
            "minsal_vigentes", "minsal_resultados", "mma", "dga", "sea_proyectos_evaluados"
        ]
        return {cat: self._check_if_category_has_new(user_id, cat) for cat in categories}

    def _check_if_category_has_new(self, user_id, category_slug):
        last_exit = self.get_user_category_last_exit(user_id, category_slug)
        viewed_ids = self.get_viewed_items_ids(user_id, category_slug)

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
        id_col_map = {
            "noticias": "link", "normativas": "accion",
            "pertinencias": "Expediente", "Tribunales": "Accion",
        }
        snifa_cats = {"fiscalizaciones","medidas_provisionales","programasDeCumplimiento",
                      "registroSanciones","requerimientos","sancionatorios"}
        if category_slug in snifa_cats:
            id_col = "expediente"
        elif category_slug in id_col_map:
            id_col = id_col_map[category_slug]
        else:
            id_col = "id"

        table = table_mapping.get(category_slug)
        if not table:
            return False

        tables = table if isinstance(table, list) else [table]

        with scrapers_conn() as conn:
            with conn.cursor() as cur:
                for t in tables:
                    if last_exit is None:
                        if viewed_ids:
                            placeholders = ','.join(['%s'] * len(viewed_ids))
                            cur.execute(f'SELECT 1 FROM "{t}" WHERE "{id_col}" NOT IN ({placeholders}) LIMIT 1', viewed_ids)
                        else:
                            cur.execute(f'SELECT 1 FROM "{t}" LIMIT 1')
                    else:
                        if viewed_ids:
                            placeholders = ','.join(['%s'] * len(viewed_ids))
                            cur.execute(f'SELECT 1 FROM "{t}" WHERE CAST(fecha_scraping AS TIMESTAMP) > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1',
                                        [last_exit] + viewed_ids)
                        else:
                            cur.execute(f'SELECT 1 FROM "{t}" WHERE CAST(fecha_scraping AS TIMESTAMP) > %s LIMIT 1', (last_exit,))
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
        notif_mapping = {"mma_abiertas": "mma", "mma_cerradas": "mma", "dga_consultas": "dga"}
        notif_category = notif_mapping.get(category_slug, category_slug)

        last_exit = self.get_user_category_last_exit(user_id, notif_category)
        viewed_ids = set(self.get_viewed_items_ids(user_id, notif_category))

        id_col_map = {"noticias": "link", "normativas": "accion",
                      "pertinencias": "Expediente", "Tribunales": "Accion"}
        snifa_cats = {"fiscalizaciones","medidas_provisionales","programasDeCumplimiento",
                      "registroSanciones","requerimientos","sancionatorios"}
        if notif_category in snifa_cats:
            id_col = "expediente"
        elif notif_category in id_col_map:
            id_col = id_col_map[notif_category]
        else:
            id_col = "id"

        norm_last_exit = self._normalize_date(last_exit)

        for item in items:
            item_id = str(item.get(id_col) or item.get("id_o_link") or "")
            if item_id in viewed_ids:
                item['is_new'] = False
                continue
            if last_exit is None:
                item['is_new'] = True
                continue
            item_date = item.get("fecha_scraping") or item.get("Fecha") or item.get("fecha")
            if not item_date:
                item['is_new'] = False
            else:
                item['is_new'] = self._normalize_date(item_date) > norm_last_exit
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