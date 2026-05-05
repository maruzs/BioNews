"""
scheduler.py  –  BioNews Automated Scraping Scheduler
======================================================
Corre los scrapers según la programación definida y configurable mediante data/scheduler.json.
"""

import schedule
import time
import logging
import traceback
import json
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

CONFIG_PATH = Path("data/scheduler.json")
DEFAULT_CONFIG = {
    "snifa_time_1": "07:00",
    "snifa_time_2": "14:00",
    "pertinencias_interval": 1,
    "noticias_interval": 1,
    "tribunales_interval": 1,
    "hora_inicio": "07:00",
    "hora_fin": "19:00"
}

def load_config():
    if not CONFIG_PATH.exists():
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG

def parse_time(time_str):
    try:
        h, m = map(int, time_str.split(':'))
        return dtime(h, m)
    except:
        return dtime(7, 0)

def dentro_del_horario() -> bool:
    config = load_config()
    ahora = datetime.now().time()
    inicio = parse_time(config.get("hora_inicio", "07:00"))
    fin = parse_time(config.get("hora_fin", "19:00"))
    return inicio <= ahora <= fin

def get_db():
    try:
        from src.database.manager import DatabaseManager
        return DatabaseManager()
    except Exception as e:
        log.error(f"Error al conectar con la base de datos: {e}")
        return None

def ejecutar_scrapers(scrapers_list, msg_inicio):
    log.info("=" * 40)
    log.info(msg_inicio)
    log.info("=" * 40)
    for nombre, ScraperClass in scrapers_list:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            nuevos = scraper.run()
            log.info(f"  ✓ {nombre}: {nuevos} nuevos registros guardados.")
        except Exception:
            log.error(f"  ✗ Error en {nombre}:\n{traceback.format_exc()}")
            
def ejecutar_noticias(scrapers_list, msg_inicio):
    log.info("=" * 40)
    log.info(msg_inicio)
    log.info("=" * 40)
    db = get_db()
    if not db: return
    for nombre, ScraperClass in scrapers_list:
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

def check_diario_oficial():
    # Only run between 7 and 19
    if not dentro_del_horario(): return
    weekday = datetime.now().weekday()
    if weekday == 6: # Sunday
        return
    today_str = datetime.now().strftime("%d-%m-%Y")
    db = get_db()
    if db:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT 1 FROM normativas WHERE fecha = ? LIMIT 1", (today_str,))
                if cursor.fetchone():
                    log.info("Diario Oficial ya tiene registros para hoy. Saltando...")
                    return
            except:
                pass
    from src.scrapers.diario_oficial import DiarioOficialScraper
    ejecutar_scrapers([("Diario Oficial (Normativas)", DiarioOficialScraper)], "SCRAPING DIARIO OFICIAL (DINAMICO)")

def run_snifa():
    from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
    from src.scrapers.reqSEIA import RequerimientosScraper
    from src.scrapers.snifa import SancionatoriosScraper
    from src.scrapers.medidas import MedidasProvisionalesScraper
    from src.scrapers.pdc import ProgramasCumplimientoScraper
    from src.scrapers.sanciones import RegistroSancionesScraper
    
    lista = [
        ("SNIFA Sancionatorios",            SancionatoriosScraper),
        ("SNIFA Fiscalizaciones",           SnifaFiscalizacionScraper),
        ("SNIFA Requerimientos",            RequerimientosScraper),
        ("SNIFA Medidas Provisionales",     MedidasProvisionalesScraper),
        ("SNIFA Programas de Cumplimiento", ProgramasCumplimientoScraper),
        ("SNIFA Registro Sanciones",        RegistroSancionesScraper),
    ]
    ejecutar_scrapers(lista, "SCRAPING SNIFA / SMA")

def run_pertinencias():
    if not dentro_del_horario(): return
    from src.scrapers.sea_legal import PertinenciasScraper
    ejecutar_scrapers([("Pertinencias SEA", PertinenciasScraper)], "SCRAPING PERTINENCIAS")

def run_tribunales():
    if not dentro_del_horario(): return
    from src.scrapers.primerTribunal import PrimerTribunalScraper
    from src.scrapers.segundoTribunal import SegundoTribunalScraper
    from src.scrapers.tercerTribunal import TercerTribunalScraper
    lista = [
        ("Primer Tribunal Ambiental",  PrimerTribunalScraper),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper),
        ("Tercer Tribunal Ambiental",  TercerTribunalScraper),
    ]
    ejecutar_scrapers(lista, "SCRAPING TRIBUNALES")

def run_noticias():
    if not dentro_del_horario(): return
    from src.scrapers.mma import MMAScraper
    from src.scrapers.sbap import SBAPScraper
    from src.scrapers.sea import SEAScraper
    from src.scrapers.sernageomin import SernageominScraper
    from src.scrapers.tribunal2 import TribunalScraper as SegundoTribunalNewsScraper
    from src.scrapers.sma import SMAScraper
    from src.scrapers.corteSuprema import CorteSupremaScraper
    from src.scrapers.tribunal3 import TercerTribunalNewsScraper
    lista = [
        ("Tercer Tribunal",              TercerTribunalNewsScraper),
        ("Corte Suprema",                CorteSupremaScraper),
        ("SMA",                          SMAScraper),
        ("MMA",                          MMAScraper),
        ("SBAP",                         SBAPScraper),
        ("SEA",                          SEAScraper),
        ("Sernageomin",                  SernageominScraper),
        ("Segundo Tribunal",             SegundoTribunalNewsScraper),
    ]
    ejecutar_noticias(lista, "SCRAPING NOTICIAS")

def setup_schedule():
    schedule.clear()
    config = load_config()
    log.info(f"Configurando scheduler con parametros: {config}")
    
    # Diario Oficial: every hour (check_diario_oficial checks if it's needed)
    schedule.every().hour.at(":05").do(check_diario_oficial)
    
    # SNIFA
    schedule.every().day.at(config.get("snifa_time_1", "07:00")).do(run_snifa)
    schedule.every().day.at(config.get("snifa_time_2", "14:00")).do(run_snifa)
    
    # The others
    p_interval = int(config.get("pertinencias_interval", 1))
    n_interval = int(config.get("noticias_interval", 1))
    t_interval = int(config.get("tribunales_interval", 1))
    
    schedule.every(p_interval).hours.at(":10").do(run_pertinencias)
    schedule.every(n_interval).hours.at(":15").do(run_noticias)
    schedule.every(t_interval).hours.at(":20").do(run_tribunales)

last_mtime = 0
def main():
    global last_mtime
    log.info("BioNews Scheduler iniciado.")
    
    setup_schedule()
    
    if CONFIG_PATH.exists():
        last_mtime = CONFIG_PATH.stat().st_mtime

    while True:
        try:
            mtime = CONFIG_PATH.stat().st_mtime if CONFIG_PATH.exists() else 0
            if mtime != last_mtime:
                last_mtime = mtime
                log.info("Detectado cambio en configuracion. Reconfigurando...")
                setup_schedule()
        except Exception as e:
            pass
            
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
