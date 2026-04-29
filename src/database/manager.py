import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="data/bionews.db"):
        self.db_path = db_path
        # Asegurar que la carpeta data existe
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
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
            # Tabla para informacion legal (dashboard principal)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS legal (
                    link TEXT PRIMARY KEY,
                    nombre TEXT,
                    fecha TEXT,
                    estado TEXT,
                    tipo TEXT,
                    fuente TEXT,
                    fecha_scraping TIMESTAMP
                )
            """)
            # Tabla para favoritos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS favoritos (
                    id_o_link TEXT PRIMARY KEY,
                    fuente TEXT,
                    nombre TEXT,
                    fecha_agregado TIMESTAMP
                )
            """)
            conn.commit()

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
            # Ordenamos por la columna 'fecha' (formato YYYY-MM-DD) y luego por scraping
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

    def save_legal(self, legal_list):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            inserted_count = 0
            for item in legal_list:
                try:
                    cursor.execute("""
                        INSERT INTO legal 
                        (link, nombre, fecha, estado, tipo, fuente, fecha_scraping)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(link) DO UPDATE SET 
                            nombre=excluded.nombre,
                            estado=excluded.estado,
                            fecha_scraping=excluded.fecha_scraping
                        WHERE legal.estado != excluded.estado OR legal.nombre != excluded.nombre
                    """, (
                        item['link'], 
                        item['nombre'], 
                        item['fecha'], 
                        item['estado'], 
                        item['tipo'], 
                        item['fuente'],
                        datetime.now()
                    ))
                    if cursor.rowcount > 0:
                        inserted_count += 1
                except Exception as e:
                    print(f"Error al guardar dato legal: {e}")
            conn.commit()
            return inserted_count

    def get_all_legal(self, limit=50):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Ordenamos por fecha de actualizacion
            cursor.execute("SELECT * FROM legal ORDER BY fecha DESC LIMIT ?", (limit,))
            return cursor.fetchall()

    def get_last_by_source(self, fuente):
        """
        Obtiene el registro mas reciente de una fuente especifica
        para evitar colisiones entre scrapers.
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM legal WHERE fuente = ? ORDER BY fecha_scraping DESC LIMIT 1"
            cursor.execute(query, (fuente,))
            return cursor.fetchone()

    def add_favorite(self, id_o_link, fuente, nombre):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO favoritos 
                    (id_o_link, fuente, nombre, fecha_agregado)
                    VALUES (?, ?, ?, ?)
                """, (id_o_link, fuente, nombre, datetime.now()))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al guardar favorito: {e}")
                return False

    def remove_favorite(self, id_o_link):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM favoritos WHERE id_o_link = ?", (id_o_link,))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar favorito: {e}")
                return False

    def get_favorites(self, fuente=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if fuente:
                if fuente == "Tribunales":
                    cursor.execute("SELECT * FROM favoritos WHERE fuente LIKE '%TA%' OR fuente LIKE '%Tribunal%' OR fuente LIKE '%Corte%' ORDER BY fecha_agregado DESC")
                elif fuente == "SNIFA":
                    cursor.execute("SELECT * FROM favoritos WHERE fuente LIKE '%Fiscalizacion%' OR fuente LIKE '%Sancionatorio%' OR fuente LIKE '%Ingreso%' OR fuente LIKE '%SNIFA%' ORDER BY fecha_agregado DESC")
                else:
                    cursor.execute("SELECT * FROM favoritos WHERE fuente LIKE ? ORDER BY fecha_agregado DESC", (f"%{fuente}%",))
            else:
                cursor.execute("SELECT * FROM favoritos ORDER BY fecha_agregado DESC")
            return cursor.fetchall()

    def is_favorite(self, id_o_link):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM favoritos WHERE id_o_link = ?", (id_o_link,))
            return cursor.fetchone() is not None