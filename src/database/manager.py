import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime

def _now_str():
    """Retorna la fecha/hora actual como string sin microsegundos: YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class DatabaseManager:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.user = os.getenv("POSTGRES_USER", "bionews_admin")
        self.password = os.getenv("POSTGRES_PASSWORD", "secret_master_password")
        self.port = os.getenv("POSTGRES_PORT", "5432")

    def get_connection(self, database_name):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=database_name
        )

    # ─── NOTICIAS ────────────────────────────────────────────────────────────

    def save_news(self, news_list):
        """Guarda noticias nuevas. NO actualiza fecha_scraping de las ya existentes."""
        with self.get_connection('bionews_news_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            inserted_count = 0
            for item in news_list:
                try:
                    # Verificar si ya existe
                    cursor.execute("SELECT 1 FROM noticias WHERE link = %s", (item['link'],))
                    if cursor.fetchone():
                        # Ya existe, no hacer nada (no actualizar fecha_scraping)
                        continue
                    cursor.execute("""
                        INSERT INTO noticias 
                        (link, titulo, fecha, imagen, fuente, fecha_scraping)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        item['link'], 
                        item['titulo'], 
                        item['fecha'], 
                        item['imagen'], 
                        item['fuente'],
                        _now_str()
                    ))
                    inserted_count += 1
                except Exception as e:
                    print(f"Error al guardar noticia: {e}")
            conn.commit()
            return inserted_count

    def get_latest_news(self, limit=100):
        with self.get_connection('bionews_news_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT * FROM noticias 
                ORDER BY fecha DESC, fecha_scraping DESC 
                LIMIT %s
            """, (limit,))
            return cursor.fetchall()

    def clean_old_data(self, days=10):
        with self.get_connection('bionews_news_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                DELETE FROM noticias 
                WHERE fecha_scraping < NOW() - (INTERVAL '1 day' * %s)
            """, (days,))
            conn.commit()

    # ─── TABLAS ESPECIFICAS (lectura genérica) ────────────────────────────────

    def get_table_data(self, table_name, limit=1000):
        """Obtiene todos los registros de una tabla especifica."""
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales',
            'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
            'dga_consultas', 'sea_proyectos_evaluados'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")
            
        db = 'bionews_legal_db'
        if table_name in ['minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas', 'dga_consultas']:
            db = 'bionews_consultations_db'
        
        with self.get_connection(db) as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
            """, (table_name.lower(),))
            columns = [col['column_name'] for col in cursor.fetchall()]
            
            order_by = ""
            if 'fecha_scraping' in columns:
                order_by = "ORDER BY fecha_scraping DESC"
            elif 'fecha' in columns:
                order_by = "ORDER BY fecha DESC"
            elif 'id' in columns:
                order_by = "ORDER BY id DESC"
                
            query = f"SELECT * FROM {table_name} {order_by} LIMIT %s"
            cursor.execute(query, (limit,))
            return cursor.fetchall()

    def is_favorite(self, user_id, id_o_link):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT 1 FROM favoritos WHERE user_id = %s AND id_o_link = %s", (user_id, id_o_link))
            return cursor.fetchone() is not None

    # ─── USERS ────────────────────────────────────────────────────────────────
    def get_user_by_email(self, email):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            row = cursor.fetchone()
            if row:
                columns = [col[0] for col in cursor.description]
                return dict(zip(columns, row))
            return None

    def create_user(self, name, email, password_hash, role="user"):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            try:
                cursor.execute("""
                    INSERT INTO users (name, email, password_hash, role, blocked, preferences)
                    VALUES (%s, %s, %s, %s, 0, '{}') RETURNING id""", (name, email, password_hash, role))
                conn.commit()
                return cursor.fetchone()[0]
            except sqlite3.IntegrityError:
                return None

    def get_all_users(self):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT id, name, email, role, blocked, preferences, last_login FROM users")
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def update_user_last_login(self, user_id):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("UPDATE users SET last_login = %s WHERE id = %s", (_now_str(), user_id))
            conn.commit()

    def update_user_status(self, user_id, blocked):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("UPDATE users SET blocked = %s WHERE id = %s", (blocked, user_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            return cursor.rowcount > 0

    def update_user_preferences(self, user_id, preferences_json):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("UPDATE users SET preferences = %s WHERE id = %s", (preferences_json, user_id))
            conn.commit()
            return cursor.rowcount > 0

    # ─── LOGS DE SCRAPERS ──────────────────────────────────────────────────────

    def log_scraper_run(self, fuente, exito, error="", nuevos=0):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            ahora = _now_str()
            
            # Obtener el log actual si existe
            cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
            row = cursor.fetchone()
            
            ultimo_exito = ahora if exito else (row[0] if row else None)
            estado = "OK" if exito else "ERROR"
            
            cursor.execute("""
                INSERT INTO scraper_logs 
                (fuente, ultimo_intento, ultimo_exito, estado, error, nuevos_registros)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT(fuente) DO UPDATE SET 
                    ultimo_intento=excluded.ultimo_intento,
                    ultimo_exito=excluded.ultimo_exito,
                    estado=excluded.estado,
                    error=excluded.error,
                    nuevos_registros=excluded.nuevos_registros
            """, (fuente, ahora, ultimo_exito, estado, error, nuevos))
            conn.commit()

    def get_scraper_logs(self):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM scraper_logs ORDER BY ultimo_intento DESC")
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_stats(self, table_name):
        with self.get_connection('bionews_legal_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            stats = {}
            
            # Verificar si la tabla existe
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s", (table_name,))
            if not cursor.fetchone():
                return None

            # Total count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            stats['total'] = cursor.fetchone()[0]
            
            if table_name == 'normativas':
                # Normativas por organismo
                cursor.execute("SELECT organismo, COUNT(*) as count FROM normativas WHERE organismo IS NOT NULL GROUP BY organismo ORDER BY count DESC LIMIT 15")
                stats['by_organismo'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]
                
                # Normativas por año y tipo
                cursor.execute("""
                    SELECT 
                        CASE 
                            WHEN fecha LIKE '____-__-__' THEN substr(fecha, 1, 4)
                            ELSE substr(fecha, -4)
                        END as anio, 
                        tipo_normativa, COUNT(*) as count 
                    FROM normativas 
                    WHERE (fecha LIKE '%-%-%' OR fecha LIKE '%/%/%')
                    GROUP BY anio, tipo_normativa
                    ORDER BY anio DESC
                """)
                rows = cursor.fetchall()
                stats['by_year_type'] = [dict(zip(['anio', 'tipo', 'count'], row)) for row in rows if row[0] and len(str(row[0])) == 4]

            elif table_name == 'fiscalizaciones':
                # Fiscalizaciones por region
                cursor.execute("SELECT region, COUNT(*) as count FROM fiscalizaciones WHERE region IS NOT NULL GROUP BY region ORDER BY count DESC")
                stats['by_region'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]
                
                # Fiscalizaciones por tipo (categoria)
                cursor.execute("SELECT categoria, COUNT(*) as count FROM fiscalizaciones WHERE categoria IS NOT NULL GROUP BY categoria ORDER BY count DESC")
                stats['by_tipo'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]

                # Fiscalizaciones por año
                cursor.execute("""
                    SELECT 
                        substr(expediente, instr(expediente, '-20') + 1, 4) as anio,
                        COUNT(*) as count
                    FROM fiscalizaciones
                    WHERE expediente LIKE '%-20__-%'
                    GROUP BY anio
                    ORDER BY anio DESC
                """)
                stats['by_year'] = [dict(zip(['anio', 'count'], row)) for row in cursor.fetchall()]

            elif table_name == 'medidas_provisionales':
                # Medidas por region
                cursor.execute("SELECT region, COUNT(*) as count FROM medidas_provisionales WHERE region IS NOT NULL GROUP BY region ORDER BY count DESC")
                stats['by_region'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]
                
                # Medidas por estado
                cursor.execute("SELECT estado, COUNT(*) as count FROM medidas_provisionales WHERE estado IS NOT NULL GROUP BY estado ORDER BY count DESC")
                stats['by_estado'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]

                # Medidas por año
                cursor.execute("""
                    SELECT 
                        substr(expediente, instr(expediente, '-20') + 1, 4) as anio,
                        COUNT(*) as count
                    FROM medidas_provisionales
                    WHERE expediente LIKE '%-20__-%'
                    GROUP BY anio
                    ORDER BY anio DESC
                """)
                stats['by_year'] = [dict(zip(['anio', 'count'], row)) for row in cursor.fetchall()]

            elif table_name == 'Tribunales':
                # Causas por tribunal
                cursor.execute("SELECT Tribunal, COUNT(*) as count FROM Tribunales WHERE Tribunal IS NOT NULL GROUP BY Tribunal ORDER BY count DESC")
                stats['by_tribunal'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]
                
                # Causas por año
                cursor.execute("""
                    SELECT 
                        CASE 
                            WHEN Fecha LIKE '____-__-__' THEN substr(Fecha, 1, 4)
                            ELSE substr(Fecha, -4)
                        END as anio, 
                        COUNT(*) as count 
                    FROM Tribunales 
                    WHERE Fecha IS NOT NULL
                    GROUP BY anio
                    ORDER BY anio DESC
                """)
                rows = cursor.fetchall()
                stats['by_year'] = [dict(zip(['anio', 'count'], row)) for row in rows if row[0] and len(str(row[0])) == 4]
                
                # Causas por tipo de procedimiento
                cursor.execute("SELECT Tipo_de_Procedimiento, COUNT(*) as count FROM Tribunales WHERE Tipo_de_Procedimiento IS NOT NULL GROUP BY Tipo_de_Procedimiento ORDER BY count DESC")
                stats['by_procedimiento'] = [dict(zip(['name', 'count'], row)) for row in cursor.fetchall()]

            return stats

    # ─── NOTIFICACIONES Y VISTOS ──────────────────────────────────────────────

    def update_category_exit(self, user_id, category_slug):
        """Actualiza el momento en que el usuario salió de una categoría."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                INSERT INTO user_category_views (user_id, category_slug, last_exit_at)
                VALUES (%s, %s, %s)
                ON CONFLICT(user_id, category_slug) DO UPDATE SET
                    last_exit_at = excluded.last_exit_at
            """, (user_id, category_slug, _now_str()))
            conn.commit()

    def mark_item_viewed(self, user_id, item_id_or_link, category_slug):
        """Marca un ítem específico como visto por el usuario."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                INSERT INTO user_item_views (user_id, item_id_or_link, category_slug, viewed_at)
                VALUES (%s, %s, %s, %s)
            """, (user_id, item_id_or_link, category_slug, _now_str()))
            conn.commit()

    def get_user_category_last_exit(self, user_id, category_slug):
        """Obtiene el timestamp de la última salida de una categoría."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT last_exit_at FROM user_category_views WHERE user_id = %s AND category_slug = %s", (user_id, category_slug))
            row = cursor.fetchone()
            return row[0] if row else None

    def get_viewed_items_ids(self, user_id, category_slug):
        """Obtiene la lista de IDs de ítems vistos en una categoría."""
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT item_id_or_link FROM user_item_views WHERE user_id = %s AND category_slug = %s", (user_id, category_slug))
            return [row[0] for row in cursor.fetchall()]

    def get_notification_status(self, user_id):
        """
        Calcula qué categorías tienen contenido nuevo para la sidebar.
        Regla: tiene contenido nuevo si hay algún ítem con created_at > last_exit_at
        y no está marcado como visto individualmente.
        """
        categories = [
            "noticias", "normativas", "pertinencias", "fiscalizaciones", 
            "sancionatorios", "registroSanciones", "programasDeCumplimiento", 
            "medidas_provisionales", "requerimientos", "Tribunales",
            "minsal_vigentes", "minsal_resultados", "mma", "dga", "sea_proyectos_evaluados"
        ]
        
        status = {}
        for cat in categories:
            has_new = self._check_if_category_has_new(user_id, cat)
            status[cat] = has_new
        return status

    def _check_if_category_has_new(self, user_id, category_slug):
        last_exit = self.get_user_category_last_exit(user_id, category_slug)
        viewed_ids = self.get_viewed_items_ids(user_id, category_slug)
        
        table_mapping = {
            "noticias": "noticias",
            "normativas": "normativas",
            "pertinencias": "pertinencias",
            "fiscalizaciones": "fiscalizaciones",
            "sancionatorios": "sancionatorios",
            "registroSanciones": "registroSanciones",
            "programasDeCumplimiento": "programasDeCumplimiento",
            "medidas_provisionales": "medidas_provisionales",
            "requerimientos": "requerimientos",
            "Tribunales": "Tribunales",
            "minsal_vigentes": "minsal_vigentes",
            "minsal_resultados": "minsal_resultados",
            "mma": ["mma_abiertas", "mma_cerradas"],
            "dga": "dga_consultas",
            "sea_proyectos_evaluados": "sea_proyectos_evaluados"
        }
        
        table = table_mapping.get(category_slug)
        if not table: return False
        
        # Obtener columna de fecha de creacion/scraping
        date_col = "fecha_scraping"
        if category_slug == "noticias":
            id_col = "link"
        elif category_slug in ["fiscalizaciones", "medidas_provisionales", "programasDeCumplimiento", "registroSanciones", "requerimientos", "sancionatorios"]:
            id_col = "expediente"
        elif category_slug == "pertinencias":
            id_col = "Expediente"
        elif category_slug == "Tribunales":
            id_col = "Accion"
        elif category_slug == "normativas":
            id_col = "accion"
        else:
            id_col = "id"
        
        
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            tables = table if isinstance(table, list) else [table]
            
            for t in tables:
                # Si last_exit es NULL, consideramos todo nuevo.
                if last_exit is None:
                    if viewed_ids:
                        placeholders = ', '.join(['%s'] * len(viewed_ids))
                        cursor.execute(f'SELECT 1 FROM "{t}" WHERE "{id_col}" NOT IN ({placeholders}) LIMIT 1', viewed_ids)
                    else:
                        cursor.execute(f'SELECT 1 FROM "{t}" LIMIT 1')
                else:
                    if viewed_ids:
                        placeholders = ', '.join(['%s'] * len(viewed_ids))
                        cursor.execute(f'SELECT 1 FROM "{t}" WHERE {date_col} > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1', (last_exit, *viewed_ids))
                    else:
                        cursor.execute(f'SELECT 1 FROM "{t}" WHERE {date_col} > %s LIMIT 1', (last_exit,))
                
                if cursor.fetchone():
                    return True
            
            return False

    def _normalize_date(self, date_val):
        """Normaliza una fecha a string ISO YYYY-MM-DD HH:MM:SS para comparación."""
        if not date_val: return ""
        str_val = str(date_val).strip()
        
        # Caso 1: DD/MM/YYYY o DD-MM-YYYY (con o sin hora)
        if "/" in str_val or ("-" in str_val and len(str_val.split("-")[0]) != 4):
            sep = "/" if "/" in str_val else "-"
            date_part = str_val.split(" ")[0]
            time_part = " ".join(str_val.split(" ")[1:]) if " " in str_val else ""
            parts = date_part.split(sep)
            if len(parts) == 3:
                try:
                    d, m, y = parts[0], parts[1], parts[2]
                    if len(y) == 2: y = "20" + y
                    result = f"{y}-{m.zfill(2)}-{d.zfill(2)}"
                    if time_part:
                        result += f" {time_part}"
                    return result
                except: pass
        
        # Caso 2: Ya es YYYY-MM-DD...
        return str_val

    def get_items_with_new_flag(self, user_id, category_slug, items):
        """Agrega el flag 'is_new' a cada ítem de la lista."""
        
        # Mapeo de subcategorías (tablas) a categorías principales para notificaciones
        # Esto permite que tablas como mma_abiertas y mma_cerradas compartan el mismo last_exit de 'mma'
        notification_mapping = {
            "mma_abiertas": "mma",
            "mma_cerradas": "mma",
            "dga_consultas": "dga"
        }
        notif_category = notification_mapping.get(category_slug, category_slug)

        last_exit = self.get_user_category_last_exit(user_id, notif_category)
        viewed_ids = set(self.get_viewed_items_ids(user_id, notif_category))
        
        if notif_category == "noticias":
            id_col = "link"
        elif notif_category in ["fiscalizaciones", "medidas_provisionales", "programasDeCumplimiento", "registroSanciones", "requerimientos", "sancionatorios"]:
            id_col = "expediente"
        elif notif_category == "pertinencias":
            id_col = "Expediente"
        elif notif_category == "Tribunales":
            id_col = "Accion"
        elif notif_category == "normativas":
            id_col = "accion"
        else:
            id_col = "id"
        
        date_col = "fecha_scraping"

        norm_last_exit = self._normalize_date(last_exit)
        # print(f"DEBUG: Category {category_slug}, User {user_id}, Last Exit: {norm_last_exit}")

        for item in items:
            item_id = str(item.get(id_col) or item.get("id_o_link") or "")
            
            # Si el ítem ya fue visto individualmente, no es nuevo
            if item_id in viewed_ids:
                item['is_new'] = False
                continue
                
            # Si el usuario nunca ha salido de la categoría, todo lo que tenga fecha es nuevo
            if last_exit is None:
                item['is_new'] = True
                continue

            # Priorizar fecha_scraping, luego Fecha/fecha del registro
            item_date = item.get(date_col) or item.get("Fecha") or item.get("fecha")
            
            if not item_date:
                item['is_new'] = False
            else:
                norm_item_date = self._normalize_date(item_date)
                is_new = norm_item_date > norm_last_exit
                item['is_new'] = is_new
        
        return items

    def get_consultation_documents(self, consulta_id, tipo_consulta):
        """Obtiene los documentos asociados a una consulta."""
        with self.get_connection('bionews_consultations_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT nombre_documento, link 
                FROM documentos 
                WHERE consulta_id = %s AND tipo_consulta = %s
            """, (consulta_id, tipo_consulta))
            rows = cursor.fetchall()
            return [{"nombre": row[0], "link": row[1]} for row in rows]

    # ─── BUG REPORTS ──────────────────────────────────────────────────────────
    def save_bug_report(self, user_id, titulo, descripcion, screenshot_path=None):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                INSERT INTO bug_reports (user_id, titulo, descripcion, screenshot_path, fecha_reporte, status)
                VALUES (%s, %s, %s, %s, %s, 'pendiente') RETURNING id""", (user_id, titulo, descripcion, screenshot_path, _now_str()))
            conn.commit()
            return cursor.fetchone()[0]

    def get_bug_reports(self, user_id=None):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            if user_id:
                cursor.execute("""
                    SELECT b.*, u.name as user_name 
                    FROM bug_reports b
                    JOIN users u ON b.user_id = u.id
                    WHERE b.user_id = %s
                    ORDER BY b.fecha_reporte DESC
                """, (user_id,))
            else:
                cursor.execute("""
                    SELECT b.*, u.name as user_name 
                    FROM bug_reports b
                    JOIN users u ON b.user_id = u.id
                    ORDER BY b.fecha_reporte DESC
                """)
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def update_bug_status(self, bug_id, status):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("UPDATE bug_reports SET status = %s WHERE id = %s", (status, bug_id))
            conn.commit()
            return cursor.rowcount > 0

    def get_bug_report(self, bug_id):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM bug_reports WHERE id = %s", (bug_id,))
            row = cursor.fetchone()
            if row:
                columns = [col[0] for col in cursor.description]
                return dict(zip(columns, row))
            return None

    def delete_bug_report(self, bug_id):
        with self.get_connection('bionews_users_db') as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("DELETE FROM bug_reports WHERE id = %s", (bug_id,))
            conn.commit()
            return cursor.rowcount > 0
