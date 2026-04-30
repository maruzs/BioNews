"""
server.py  –  BioNews FastAPI Backend
======================================
Iniciar con:
    uvicorn server:app --host 0.0.0.0 --port 8000 --reload

Para producción (sin reload):
    uvicorn server:app --host 0.0.0.0 --port 8000
"""

import logging
import traceback
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.database.manager import DatabaseManager
from src.scrapers.snifa import SnifaScraper
from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("bionews.server")

app = FastAPI(title="BioNews API")

# ── CORS: permite el frontend Vite (dev) y cualquier origen Tailscale ────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En producción puedes limitar a la IP Tailscale del cliente
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()

# ─── NEWS ─────────────────────────────────────────────────────────────────────
@app.get("/api/news")
def get_news():
    news = db.get_latest_news(limit=100)
    return [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news]

# ─── LEGAL ───────────────────────────────────────────────────────────────────
@app.get("/api/legal")
def get_legal():
    legal = db.get_all_legal(limit=1000)
    return [{"link": l[0], "nombre": l[1], "fecha": l[2], "estado": l[3], "tipo": l[4], "fuente": l[5], "fecha_scraping": l[6]} for l in legal]

# ─── FAVORITES ───────────────────────────────────────────────────────────────
@app.get("/api/favorites")
def get_favorites(fuente: str = None):
    favs = db.get_favorites(fuente=fuente)
    return [{"id_o_link": f[0], "fuente": f[1], "nombre": f[2], "fecha_agregado": f[3]} for f in favs]

@app.post("/api/favorites")
def add_favorite(fav: dict):
    success = db.add_favorite(fav['id_o_link'], fav['fuente'], fav['nombre'])
    return {"success": success}

@app.delete("/api/favorites/{id_o_link:path}")
def remove_favorite(id_o_link: str):
    success = db.remove_favorite(id_o_link)
    return {"success": success}

# ─── SCRAPING ENDPOINTS ───────────────────────────────────────────────────────
def _run_all_scrapers():
    """Función interna que corre todos los scrapers secuencialmente."""
    try:
        from src.scrapers.mma import MMAScraper
        from src.scrapers.sbap import SBAPScraper
        from src.scrapers.diario_oficial import DiarioOficialScraper
        from src.scrapers.sea import SEAScraper
        from src.scrapers.sernageomin import SernageominScraper
        from src.scrapers.tribunal2 import TribunalScraper
        from src.scrapers.sea_legal import SEALegalScraper
        from src.scrapers.snifa import SnifaScraper
        from src.scrapers.sma import SMAScraper
        from src.scrapers.corteSuprema import CorteSupremaScraper
        from src.scrapers.tribunal3 import TercerTribunalScraper
        from src.scrapers.primerTribunal import PrimerTribunalScraper
        from src.scrapers.segundoTribunal import SegundoTribunalScraper
        from src.scrapers.tercerTribunal import TercerTribunalScraperLegal
        from src.scrapers.reqSEIA import SnifaIngresoScraper
        from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
    except ImportError as e:
        log.error(f"Error de importación al iniciar scrapers: {e}")
        return

    legales = [
        ("Primer Tribunal Ambiental",  PrimerTribunalScraper),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper),
        ("Tercer Tribunal Ambiental",  TercerTribunalScraperLegal),
        ("SEA Legal",                  SEALegalScraper),
        ("SNIFA Sancionatorios",       SnifaScraper),
        ("SNIFA Ingresos",             SnifaIngresoScraper),
        ("SNIFA Fiscalizaciones",      SnifaFiscalizacionScraper),
    ]

    log.info("--- SCRAPING LEGAL ---")
    for nombre, ScraperClass in legales:
        log.info(f"Procesando: {nombre}...")
        try:
            datos = ScraperClass().get_legal_data()
            if datos:
                nuevos = db.save_legal(datos)
                log.info(f"{nombre}: {nuevos} nuevos registros.")
            else:
                log.info(f"{nombre}: sin registros nuevos.")
        except Exception:
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    noticias_scrapers = [
        ("Tercer Tribunal (Noticias)",    TercerTribunalScraper),
        ("Corte Suprema",                 CorteSupremaScraper),
        ("SMA",                           SMAScraper),
        ("MMA",                           MMAScraper),
        ("SBAP",                          SBAPScraper),
        ("Diario Oficial",                DiarioOficialScraper),
        ("SEA Noticias",                  SEAScraper),
        ("Sernageomin",                   SernageominScraper),
        ("Tribunal Ambiental (Noticias)", TribunalScraper),
    ]

    log.info("--- SCRAPING NOTICIAS ---")
    for nombre, ScraperClass in noticias_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            items = ScraperClass().get_latest_news()
            if items:
                nuevas = db.save_news(items)
                log.info(f"{nombre}: {nuevas} nuevas noticias.")
            else:
                log.info(f"{nombre}: sin noticias nuevas.")
        except Exception:
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    log.info("--- SCRAPING FINALIZADO ---")


@app.post("/api/scrape/all")
def scrape_all(background_tasks: BackgroundTasks):
    """Lanza todos los scrapers en segundo plano (ejecución secuencial)."""
    background_tasks.add_task(_run_all_scrapers)
    return {"status": "Scraping iniciado en segundo plano"}


@app.post("/api/scrape/snifa")
def scrape_snifa(background_tasks: BackgroundTasks):
    """Lanza solo el scraper de SNIFA en segundo plano."""
    def run():
        scraper = SnifaScraper()
        data = scraper.get_legal_data()
        db.save_legal(data)
    background_tasks.add_task(run)
    return {"status": "Scraping SNIFA iniciado en segundo plano"}


# ─── Health check ──────────────────────────────────────────────────────────────
@app.get("/api/health")
def health():
    return {"status": "ok"}
