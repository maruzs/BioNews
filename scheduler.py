"""
scheduler.py  –  BioNews Automated Scraping Scheduler
======================================================
Corre los scrapers de manera secuencial cada hora entre las 07:00 y las 19:00
(hora local del servidor). Registra cada ejecución en logs/scheduler.log.

Uso:
    python scheduler.py

El proceso se puede correr en segundo plano con:
    Windows:  pythonw scheduler.py   (sin ventana de consola)
    Linux:    nohup python scheduler.py &
"""

import schedule
import time
import logging
import traceback
from datetime import datetime, time as dtime
from pathlib import Path

# ─── Logging ────────────────────────────────────────────────────────────────
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_DIR / "scheduler.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("bionews.scheduler")

# ─── Rango horario permitido (7am – 7pm) ────────────────────────────────────
HORA_INICIO = dtime(7, 0)
HORA_FIN    = dtime(19, 0)


def dentro_del_horario() -> bool:
    ahora = datetime.now().time()
    return HORA_INICIO <= ahora <= HORA_FIN


# ─── Job principal ───────────────────────────────────────────────────────────
def run_scrapers_job():
    """Ejecuta todos los scrapers de forma secuencial."""
    if not dentro_del_horario():
        log.info("Fuera del horario de ejecución (07:00–19:00). Se omite esta corrida.")
        return

    log.info("=" * 60)
    log.info("INICIANDO CICLO DE SCRAPING AUTOMÁTICO")
    log.info("=" * 60)

    # Importamos aquí para que errores de importación no maten el scheduler
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
        from src.database.manager import DatabaseManager
    except ImportError as e:
        log.error(f"Error de importación: {e}")
        return

    try:
        db = DatabaseManager()
        log.info("Base de datos conectada correctamente.")
    except Exception as e:
        log.error(f"Error al conectar con la base de datos: {e}")
        return

    # ── Scrapers legales ─────────────────────────────────────────────────────
    legales = [
        ("Primer Tribunal Ambiental",  PrimerTribunalScraper),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper),
        ("Tercer Tribunal Ambiental",  TercerTribunalScraperLegal),
        ("SEA Legal",                  SEALegalScraper),
        ("SNIFA Sancionatorios",       SnifaScraper),
        ("SNIFA Ingresos",             SnifaIngresoScraper),
        ("SNIFA Fiscalizaciones",      SnifaFiscalizacionScraper),
    ]

    log.info("--- INICIANDO SCRAPING LEGAL ---")
    for nombre, ScraperClass in legales:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            datos = scraper.get_legal_data()
            if datos:
                nuevos = db.save_legal(datos)
                log.info(f"  ✓ {nombre}: {nuevos} nuevos registros guardados.")
            else:
                log.info(f"  – {nombre}: sin registros nuevos.")
        except Exception:
            log.error(f"  ✗ Error en {nombre}:\n{traceback.format_exc()}")

    # ── Scrapers de noticias ──────────────────────────────────────────────────
    noticias = [
        ("Tercer Tribunal (Noticias)",   TercerTribunalScraper),
        ("Corte Suprema",                CorteSupremaScraper),
        ("SMA",                          SMAScraper),
        ("MMA",                          MMAScraper),
        ("SBAP",                         SBAPScraper),
        ("Diario Oficial",               DiarioOficialScraper),
        ("SEA Noticias",                 SEAScraper),
        ("Sernageomin",                  SernageominScraper),
        ("Tribunal Ambiental (Noticias)",TribunalScraper),
    ]

    log.info("--- INICIANDO SCRAPING DE NOTICIAS ---")
    for nombre, ScraperClass in noticias:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            items = scraper.get_latest_news()
            if items:
                nuevas = db.save_news(items)
                log.info(f"  ✓ {nombre}: {nuevas} nuevas noticias guardadas.")
            else:
                log.info(f"  – {nombre}: sin noticias nuevas.")
        except Exception:
            log.error(f"  ✗ Error en {nombre}:\n{traceback.format_exc()}")

    log.info("=" * 60)
    log.info("CICLO DE SCRAPING FINALIZADO")
    log.info("=" * 60)


# ─── Programación horaria ────────────────────────────────────────────────────
def main():
    log.info("BioNews Scheduler iniciado.")
    log.info(f"Los scrapers correrán cada hora entre {HORA_INICIO.strftime('%H:%M')} y {HORA_FIN.strftime('%H:%M')}.")

    # Corre cada hora en punto (ej: 07:00, 08:00, ... 19:00)
    schedule.every().hour.at(":00").do(run_scrapers_job)

    # Primera ejecución inmediata al arrancar (si es horario válido)
    log.info("Ejecutando primera pasada al arrancar el scheduler...")
    run_scrapers_job()

    while True:
        schedule.run_pending()
        time.sleep(30)   # revisa cada 30 segundos


if __name__ == "__main__":
    main()
