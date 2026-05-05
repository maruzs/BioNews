"""
scheduler.py  –  BioNews Automated Scraping Scheduler
======================================================
Corre los scrapers según la programación definida:
- Diario Oficial: 1 vez al día (07:00)
- SNIFA/SMA: 2 veces al día (07:00 y 14:00)
- Pertinencias: cada 1 hora
- Noticias: cada 1 hora
- Todo lo demás (Tribunales): cada 1 hora
Nota: Las tareas de "cada 1 hora" solo se ejecutan entre las 07:00 y las 19:00.
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

def get_db():
    try:
        from src.database.manager import DatabaseManager
        return DatabaseManager()
    except Exception as e:
        log.error(f"Error al conectar con la base de datos: {e}")
        return None

def ejecutar_scrapers(scrapers_list, msg_inicio):
    """Ejecuta una lista de scrapers de datos"""
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
    """Ejecuta una lista de scrapers de noticias"""
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

# ─── TAREAS ESPECÍFICAS ──────────────────────────────────────────────────────

def run_diario_oficial():
    from src.scrapers.diario_oficial import DiarioOficialScraper
    ejecutar_scrapers([("Diario Oficial (Normativas)", DiarioOficialScraper)], "SCRAPING DIARIO OFICIAL (07:00)")

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
    ejecutar_scrapers([("Pertinencias SEA", PertinenciasScraper)], "SCRAPING PERTINENCIAS (CADA HORA)")

def run_tribunales():
    if not dentro_del_horario(): return
    from src.scrapers.primerTribunal import PrimerTribunalScraper
    from src.scrapers.segundoTribunal import SegundoTribunalScraper
    from src.scrapers.tercerTribunal import TercerTribunalScraperLegal
    lista = [
        ("Primer Tribunal Ambiental",  PrimerTribunalScraper),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper),
        ("Tercer Tribunal Ambiental",  TercerTribunalScraperLegal),
    ]
    ejecutar_scrapers(lista, "SCRAPING TRIBUNALES (CADA HORA)")

def run_noticias():
    if not dentro_del_horario(): return
    from src.scrapers.mma import MMAScraper
    from src.scrapers.sbap import SBAPScraper
    from src.scrapers.sea import SEAScraper
    from src.scrapers.sernageomin import SernageominScraper
    from src.scrapers.tribunal2 import TribunalScraper
    from src.scrapers.sma import SMAScraper
    from src.scrapers.corteSuprema import CorteSupremaScraper
    from src.scrapers.tribunal3 import TercerTribunalScraper
    lista = [
        ("Tercer Tribunal (Noticias)",   TercerTribunalScraper),
        ("Corte Suprema",                CorteSupremaScraper),
        ("SMA",                          SMAScraper),
        ("MMA",                          MMAScraper),
        ("SBAP",                         SBAPScraper),
        ("SEA Noticias",                 SEAScraper),
        ("Sernageomin",                  SernageominScraper),
        ("Tribunal Ambiental (Noticias)",TribunalScraper),
    ]
    ejecutar_noticias(lista, "SCRAPING NOTICIAS (CADA HORA)")

# ─── Programación horaria ────────────────────────────────────────────────────
def main():
    log.info("BioNews Scheduler iniciado.")
    
    # 1. Diario Oficial: 1 vez al día (07:00)
    schedule.every().day.at("07:00").do(run_diario_oficial)
    
    # 2. SNIFA/SMA: 2 veces al día (07:00 y 14:00)
    schedule.every().day.at("07:00").do(run_snifa)
    schedule.every().day.at("14:00").do(run_snifa)
    
    # 3. Pertinencias: cada hora (dentro del horario)
    schedule.every().hour.at(":05").do(run_pertinencias)
    
    # 4. Noticias: cada hora (dentro del horario)
    schedule.every().hour.at(":10").do(run_noticias)
    
    # 5. Todo lo demás (Tribunales): cada hora (dentro del horario)
    schedule.every().hour.at(":15").do(run_tribunales)

    log.info("Tareas programadas correctamente.")
    
    # Para la primera ejecución si es necesario, pero como ya están 
    # separados, mejor que corra la programación. Si se quiere forzar al arrancar:
    # Si la app se inicia en el día, para no esperar a la hora, se puede hacer:
    if dentro_del_horario():
        log.info("Ejecución inicial al arrancar...")
        run_pertinencias()
        run_tribunales()
        run_noticias()

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
