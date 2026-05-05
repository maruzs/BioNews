import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="data/data.db"):
        self.db_path = db_path
        # Asegurar que la carpeta data existe
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """Crea las tablas noticias y favoritos si no existen.
        Las demas tablas (fiscalizaciones, sancionatorios, etc.) ya existen en data.db
        y son gestionadas por sus scrapers respectivos."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Tabla para noticias
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS noticias (
                    link TEXT PRIMARY KEY,
                    titulo TEXT,
                    fecha TEXT,
                    imagen TEXT,
                    fuente TEXT,
                    fecha_scraping TIMESTAMP
                )
            """)
            # Tabla para favoritos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS favoritos (
                    user_id INTEGER,
                    id_o_link TEXT,
                    fuente TEXT,
                    nombre TEXT,
                    fecha_agregado TIMESTAMP,
                    accion TEXT,
                    PRIMARY KEY (user_id, id_o_link)
                )
            """)
            
            # Migración: Agregar user_id a favoritos si venimos de la versión antigua
            cursor.execute("PRAGMA table_info(favoritos)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'user_id' not in columns:
                cursor.execute("ALTER TABLE favoritos RENAME TO favoritos_old")
                cursor.execute("""
                    CREATE TABLE favoritos (
                        user_id INTEGER,
                        id_o_link TEXT,
                        fuente TEXT,
                        nombre TEXT,
                        fecha_agregado TIMESTAMP,
                        accion TEXT,
                        PRIMARY KEY (user_id, id_o_link)
                    )
                """)
                cursor.execute("""
                    INSERT INTO favoritos (user_id, id_o_link, fuente, nombre, fecha_agregado, accion)
                    SELECT 1, id_o_link, fuente, nombre, fecha_agregado, accion FROM favoritos_old
                """)
                cursor.execute("DROP TABLE favoritos_old")

            # Tabla para usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE,
                    password_hash TEXT,
                    role TEXT,
                    blocked INTEGER DEFAULT 0,
                    preferences TEXT
                )
            """)
                
            # Tabla para logs de scrapers
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scraper_logs (
                    fuente TEXT PRIMARY KEY,
                    ultimo_intento TIMESTAMP,
                    ultimo_exito TIMESTAMP,
                    estado TEXT,
                    error TEXT,
                    nuevos_registros INTEGER
                )
            """)
            conn.commit()

    # ─── NOTICIAS ────────────────────────────────────────────────────────────

    def save_news(self, news_list):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            inserted_count = 0
            for item in news_list:
                try:
                    cursor.execute("""
                        INSERT INTO noticias 
                        (link, titulo, fecha, imagen, fuente, fecha_scraping)
                        VALUES (?, ?, ?, ?, ?, ?)
                        ON CONFLICT(link) DO UPDATE SET 
                            titulo=excluded.titulo,
                            fecha_scraping=excluded.fecha_scraping
                        WHERE noticias.titulo != excluded.titulo
                    """, (
                        item['link'], 
                        item['titulo'], 
                        item['fecha'], 
                        item['imagen'], 
                        item['fuente'],
                        datetime.now()
                    ))
                    if cursor.rowcount > 0:
                        inserted_count += 1
                except Exception as e:
                    print(f"Error al guardar noticia: {e}")
            conn.commit()
            return inserted_count

    def get_latest_news(self, limit=100):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM noticias 
                ORDER BY fecha DESC, fecha_scraping DESC 
                LIMIT ?
            """, (limit,))
            return cursor.fetchall()

    def clean_old_data(self, days=10):
        # Implementacion opcional para tu regla de borrar lo antiguo
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM noticias 
                WHERE julianday('now') - julianday(fecha_scraping) > ?
            """, (days,))
            conn.commit()

    # ─── TABLAS ESPECIFICAS (lectura genérica) ────────────────────────────────

    def get_table_data(self, table_name, limit=1000):
        """Obtiene todos los registros de una tabla especifica."""
        # Whitelist de tablas permitidas para evitar SQL injection
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Obtener los nombres de columnas
            cursor.execute(f'PRAGMA table_info("{table_name}")')
            columns = [col[1] for col in cursor.fetchall()]
            
            cursor.execute(f'SELECT * FROM "{table_name}" LIMIT ?', (limit,))
            rows = cursor.fetchall()
            
            # Devolver como lista de diccionarios
            return [dict(zip(columns, row)) for row in rows]

    def get_table_count(self, table_name):
        """Obtiene la cantidad total de registros de una tabla."""
        allowed = {
            'fiscalizaciones', 'medidas_provisionales', 'normativas',
            'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
            'requerimientos', 'sancionatorios', 'Tribunales', 'noticias', 'favoritos'
        }
        if table_name not in allowed:
            raise ValueError(f"Tabla no permitida: {table_name}")
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')
            return cursor.fetchone()[0]

    # ─── FAVORITOS ────────────────────────────────────────────────────────────

    def add_favorite(self, user_id, id_o_link, fuente, nombre, accion=""):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO favoritos 
                    (user_id, id_o_link, fuente, nombre, fecha_agregado, accion)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(user_id, id_o_link) DO UPDATE SET
                        fuente=excluded.fuente,
                        nombre=excluded.nombre,
                        accion=excluded.accion
                """, (user_id, id_o_link, fuente, nombre, datetime.now(), accion))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al guardar favorito: {e}")
                return False

    def remove_favorite(self, user_id, id_o_link):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM favoritos WHERE user_id = ? AND id_o_link = ?", (user_id, id_o_link))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar favorito: {e}")
                return False

    def get_favorites(self, user_id, fuente=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if fuente:
                if fuente == "Tribunales":
                    cursor.execute("SELECT * FROM favoritos WHERE user_id = ? AND (fuente LIKE '%TA%' OR fuente LIKE '%Tribunal%' OR fuente LIKE '%Corte%') ORDER BY fecha_agregado DESC", (user_id,))
                elif fuente == "SNIFA":
                    cursor.execute("SELECT * FROM favoritos WHERE user_id = ? AND (fuente LIKE '%Fiscalizacion%' OR fuente LIKE '%Sancionatorio%' OR fuente LIKE '%Ingreso%' OR fuente LIKE '%SNIFA%') ORDER BY fecha_agregado DESC", (user_id,))
                else:
                    cursor.execute("SELECT * FROM favoritos WHERE user_id = ? AND fuente LIKE ? ORDER BY fecha_agregado DESC", (user_id, f"%{fuente}%"))
            else:
                cursor.execute("SELECT * FROM favoritos WHERE user_id = ? ORDER BY fecha_agregado DESC", (user_id,))
            return cursor.fetchall()

    def is_favorite(self, user_id, id_o_link):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM favoritos WHERE user_id = ? AND id_o_link = ?", (user_id, id_o_link))
            return cursor.fetchone() is not None

    # ─── USERS ────────────────────────────────────────────────────────────────
    def get_user_by_email(self, email):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            row = cursor.fetchone()
            if row:
                columns = [col[0] for col in cursor.description]
                return dict(zip(columns, row))
            return None

    def create_user(self, name, email, password_hash, role="user"):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO users (name, email, password_hash, role, blocked, preferences)
                    VALUES (?, ?, ?, ?, 0, '{}')
                """, (name, email, password_hash, role))
                conn.commit()
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                return None

    def get_all_users(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, role, blocked, preferences FROM users")
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def update_user_status(self, user_id, blocked):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET blocked = ? WHERE id = ?", (blocked, user_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0

    def update_user_preferences(self, user_id, preferences_json):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET preferences = ? WHERE id = ?", (preferences_json, user_id))
            conn.commit()
            return cursor.rowcount > 0

    # ─── LOGS DE SCRAPERS ──────────────────────────────────────────────────────

    def log_scraper_run(self, fuente, exito, error="", nuevos=0):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            ahora = datetime.now()
            
            # Obtener el log actual si existe
            cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = ?", (fuente,))
            row = cursor.fetchone()
            
            ultimo_exito = ahora if exito else (row[0] if row else None)
            estado = "OK" if exito else "ERROR"
            
            cursor.execute("""
                INSERT INTO scraper_logs 
                (fuente, ultimo_intento, ultimo_exito, estado, error, nuevos_registros)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(fuente) DO UPDATE SET 
                    ultimo_intento=excluded.ultimo_intento,
                    ultimo_exito=excluded.ultimo_exito,
                    estado=excluded.estado,
                    error=excluded.error,
                    nuevos_registros=excluded.nuevos_registros
            """, (fuente, ahora, ultimo_exito, estado, error, nuevos))
            conn.commit()

    def get_scraper_logs(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM scraper_logs ORDER BY ultimo_intento DESC")
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]