from .engine import ScrapingEngine
from ..utils.date_parser import parse_fecha
import sqlite3
import os

class DGAScraper:
    def __init__(self):
        self.url_home = "https://dga.mop.gob.cl/"
        self.url_noticias = "https://dga.mop.gob.cl/noticias/"
        self.engine = ScrapingEngine()

    def _get_last_scraped_link(self):
        """Obtiene el último link de noticia de DGA guardado en la base de datos."""
        try:
            # Buscamos la base de datos en la ruta esperada
            db_path = os.path.join("data", "data.db")
            if not os.path.exists(db_path):
                # Si no existe desde el CWD actual, intentamos subir niveles (por si se corre desde src o scrapers)
                db_path = os.path.join("..", "..", "data", "data.db")
                if not os.path.exists(db_path):
                    return None

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Buscamos la noticia más reciente de DGA
            cursor.execute("SELECT link FROM noticias WHERE fuente='DGA' ORDER BY fecha DESC, fecha_scraping DESC LIMIT 1")
            res = cursor.fetchone()
            conn.close()
            return res[0] if res else None
        except Exception as e:
            print(f"Error al obtener el último link de DGA: {e}", flush=True)
            return None

    def get_latest_news(self, pages=1):
        news_list = []
        last_link = self._get_last_scraped_link()
        found_last = False

        # 1. Scrapear página principal (3 noticias más nuevas con fecha)
        print(f"Iniciando scraping en DGA (Página Principal): {self.url_home}", flush=True)
        try:
            soup_home = self.engine.get_soup(self.url_home, wait_for_selector=".et_pb_blog_0")
            if soup_home:
                # El bloque de noticias en la home tiene la clase et_pb_blog_0
                articles = soup_home.select(".et_pb_blog_0 article.et_pb_post")
                for article in articles:
                    news_item = self._parse_article(article)
                    if news_item:
                        if last_link and news_item['link'] == last_link:
                            found_last = True
                            break
                        news_list.append(news_item)
        except Exception as e:
            print(f"Error en scraping de página principal DGA: {e}", flush=True)

        if found_last:
            print(f"Se encontraron {len(news_list)} noticias nuevas en DGA (página principal)", flush=True)
            return news_list

        # 2. Scrapear sección de noticias
        for p in range(1, pages + 1):
            url = self.url_noticias if p == 1 else f"{self.url_noticias}page/{p}/"
            print(f"Iniciando scraping en DGA (Sección Noticias, Página {p}): {url}", flush=True)
            try:
                soup = self.engine.get_soup(url, wait_for_selector=".et_pb_salvattore_content")
                
                if not soup:
                    break

                articles = soup.select(".et_pb_salvattore_content article.et_pb_post")
                if not articles:
                    break

                for article in articles:
                    news_item = self._parse_article(article)
                    if news_item:
                        # Evitar duplicados si ya la capturamos de la home
                        if any(item['link'] == news_item['link'] for item in news_list):
                            continue
                            
                        if last_link and news_item['link'] == last_link:
                            found_last = True
                            break
                        news_list.append(news_item)
                
                if found_last:
                    break
            except Exception as e:
                print(f"Error en scraping de sección noticias DGA (Página {p}): {e}", flush=True)
                break
        
        print(f"Se encontraron {len(news_list)} noticias nuevas en DGA", flush=True)
        return news_list

    def _parse_article(self, article):
        try:
            # Link y Título
            title_tag = article.select_one("h2.entry-title a")
            if not title_tag:
                return None
            
            title = title_tag.get_text(strip=True)
            link = title_tag["href"]
            
            # Fecha
            date_tag = article.select_one(".post-meta .published")
            fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
            if not fecha_raw:
                # Algunas veces el selector puede variar ligeramente en WordPress
                date_tag = article.select_one(".published")
                fecha_raw = date_tag.get_text(strip=True) if date_tag else ""
            
            if not fecha_raw:
                return None
            
            # Imagen
            img_tag = article.select_one(".et_pb_image_container img")
            img_url = ""
            if img_tag:
                # Priorizar data-src (lazy load) y luego src
                img_url = img_tag.get("data-src") or img_tag.get("src") or ""
            
            return {
                "titulo": title,
                "fecha": parse_fecha(fecha_raw),
                "link": link,
                "imagen": img_url,
                "fuente": "DGA"
            }
        except Exception as e:
            print(f"Error procesando un artículo de DGA: {e}", flush=True)
            return None
