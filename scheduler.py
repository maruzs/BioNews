"""
scheduler.py  –  BioNews Automated Scraping Scheduler (Optimizado)
==================================================================
Corre los scrapers según la programación definida y configurable mediante data/scheduler.json.
Guarda los logs de ejecución en base de datos y notifica los cambios en tiempo real vía SSE a la API.
"""

import schedule
import time
import logging
import traceback
import json
import requests
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
    "consultas_time_1": "08:30",
    "consultas_time_2": "15:30",
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

def notify_new_content_external(category):
    """Envía una petición al endpoint interno de la API para gatillar la notificación SSE."""
    try:
        url = "http://api:8000/api/internal/notify-new"
        res = requests.post(url, json={"category": category}, timeout=5)
        if res.status_code == 200:
            log.info(f"  ✓ Notificación SSE enviada externamente para: {category}")
        else:
            log.warning(f"  ✗ API retornó status {res.status_code} al notificar SSE.")
    except Exception as e:
        log.warning(f"  ✗ No se pudo notificar SSE de forma externa para {category}: {e}")

def ejecutar_scrapers(scrapers_list, msg_inicio, category_override=None):
    log.info("=" * 40)
    log.info(msg_inicio + " (SCHEDULED)")
    log.info("=" * 40)
    db = get_db()
    any_success = False
    
    for nombre, ScraperClass in scrapers_list:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            # Ejecución del scraper (síncrona)
            nuevos = scraper.run()
            log.info(f"  ✓ {nombre}: {nuevos} nuevos registros guardados.")
            
            # Registrar éxito en la base de datos
            if db:
                db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
            
            if nuevos > 0:
                any_success = True
                # Resolver categoría para enviar notificación SSE
                cat = category_override
                if not cat:
                    # Mapping por defecto para SNIFA
                    snifa_mapping = {
                        "SNIFA Sancionatorios": "sancionatorios",
                        "SNIFA Fiscalizaciones": "fiscalizaciones",
                        "SNIFA Requerimientos": "requerimientos",
                        "SNIFA Medidas Provisionales": "medidas_provisionales",
                        "SNIFA Programas de Cumplimiento": "programasDeCumplimiento",
                        "SNIFA Registro Sanciones": "registroSanciones"
                    }
                    cat = snifa_mapping.get(nombre)
                
                # Emitir notificación SSE
                if cat:
                    if isinstance(cat, list):
                        for c in cat:
                            notify_new_content_external(c)
                    else:
                        notify_new_content_external(cat)
                        
        except Exception as e:
            err_str = traceback.format_exc()
            log.error(f"  ✗ Error en {nombre}:\n{err_str}")
            # Registrar error en la base de datos
            if db:
                db.log_scraper_run(nombre, exito=False, error=str(e))
            
    if any_success:
        try:
            from src.database.cache import cache
            cache.invalidate_pattern("table_data:*")
            cache.invalidate_pattern("notif_status:*")
            log.info("  ✓ Caché de Redis invalidada.")
        except Exception as e:
            log.warning(f"  ✗ No se pudo invalidar la caché de Redis: {e}")

def ejecutar_noticias(scrapers_list, msg_inicio):
    log.info("=" * 40)
    log.info(msg_inicio + " (SCHEDULED)")
    log.info("=" * 40)
    db = get_db()
    if not db: return
    any_success = False
    
    for nombre, ScraperClass in scrapers_list:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            items = scraper.get_latest_news()
            if items:
                nuevas = db.save_news(items)
                db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                log.info(f"  ✓ {nombre}: {nuevas} nuevas noticias guardadas.")
                if nuevas > 0:
                    any_success = True
            else:
                db.log_scraper_run(nombre, exito=True, nuevos=0)
                log.info(f"  – {nombre}: sin noticias nuevas.")
        except Exception as e:
            err_str = traceback.format_exc()
            log.error(f"  ✗ Error en {nombre}:\n{err_str}")
            db.log_scraper_run(nombre, exito=False, error=str(e))

    if any_success:
        notify_new_content_external("noticias")
        try:
            from src.database.cache import cache
            cache.invalidate_pattern("table_data:*")
            cache.invalidate_pattern("news:*")
            log.info("  ✓ Caché de Redis invalidada.")
        except Exception as e:
            log.warning(f"  ✗ No se pudo invalidar la caché de Redis: {e}")

def check_diario_oficial():
    # Solo correr en horario diurno
    if not dentro_del_horario(): return
    weekday = datetime.now().weekday()
    if weekday == 6: # Domingo no hay diario oficial
        return
    today_str = datetime.now().strftime("%d-%m-%Y")
    db = get_db()
    if db:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT 1 FROM normativas WHERE fecha = %s LIMIT 1", (today_str,))
                if cursor.fetchone():
                    log.info("Diario Oficial ya tiene registros para hoy. Saltando...")
                    return
            except:
                pass
    from src.scrapers.diario_oficial import DiarioOficialScraper
    ejecutar_scrapers([("Diario Oficial (Normativas)", DiarioOficialScraper)], "SCRAPING DIARIO OFICIAL (DINAMICO)", "normativas")

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

def run_sea():
    if not dentro_del_horario(): return
    from src.scrapers.sea_legal import PertinenciasScraper
    from src.scrapers.sea_evaluados import SEAEvaluadosScraper
    
    # 1. Pertinencias
    ejecutar_scrapers([("Pertinencias SEA", PertinenciasScraper)], "SCRAPING PERTINENCIAS", "pertinencias")
    # 2. Proyectos Evaluados
    ejecutar_scrapers([("Proyectos Evaluados SEA", SEAEvaluadosScraper)], "SCRAPING PROYECTOS EVALUADOS", "sea_proyectos_evaluados")

def run_tribunales():
    if not dentro_del_horario(): return
    from src.scrapers.primerTribunal import PrimerTribunalScraper
    from src.scrapers.segundoTribunal import SegundoTribunalScraper
    from src.scrapers.tercerTribunal import TercerTribunalScraper
    lista = [
        ("Primer Tribunal",  PrimerTribunalScraper),
        ("Segundo Tribunal", SegundoTribunalScraper),
        ("Tercer Tribunal",  TercerTribunalScraper),
    ]
    ejecutar_scrapers(lista, "SCRAPING TRIBUNALES", "Tribunales")

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
    from src.scrapers.scraper_dga import DGAScraper
    
    lista = [
        ("Tercer Tribunal (Noticias)",  TercerTribunalNewsScraper),
        ("Corte Suprema",               CorteSupremaScraper),
        ("SMA",                         SMAScraper),
        ("MMA",                         MMAScraper),
        ("SBAP",                        SBAPScraper),
        ("SEA Noticias",                SEAScraper),
        ("Sernageomin",                 SernageominScraper),
        ("Segundo Tribunal (Noticias)", SegundoTribunalNewsScraper),
        ("DGA",                         DGAScraper),
    ]
    ejecutar_noticias(lista, "SCRAPING NOTICIAS")
    
def run_consultas():
    from src.scrapers.minsal import MINSALScraper
    from src.scrapers.mma_consultas import MMAConsultasScraper
    from src.scrapers.dga_consultas import DGAConsultasScraper
    
    # MINSAL (Afecta tanto vigentes como resultados)
    ejecutar_scrapers([("MINSAL Consultas", MINSALScraper)], "SCRAPING MINSAL CONSULTAS", ["minsal_vigentes", "minsal_resultados"])
    # MMA
    ejecutar_scrapers([("MMA Consultas", MMAConsultasScraper)], "SCRAPING MMA CONSULTAS", "mma")
    # DGA
    ejecutar_scrapers([("DGA Consultas", DGAConsultasScraper)], "SCRAPING DGA CONSULTAS", "dga")

def setup_schedule():
    schedule.clear()
    config = load_config()
    log.info(f"Configurando scheduler con parametros: {config}")
    
    # Diario Oficial: cada hora
    #schedule.every().hour.at(":05").do(check_diario_oficial)
    schedule.every().day.at("07:00").do(check_diario_oficial)
    
    # SNIFA (Horarios fijos)
    schedule.every().day.at(config.get("snifa_time_1", "07:00")).do(run_snifa)
    schedule.every().day.at(config.get("snifa_time_2", "14:00")).do(run_snifa)
    
    # Intervalos (SEA, Noticias, Tribunales)
    p_interval = int(config.get("pertinencias_interval", 1))
    n_interval = int(config.get("noticias_interval", 1))
    t_interval = int(config.get("tribunales_interval", 1))
    
    schedule.every(p_interval).hours.at(":10").do(run_sea)
    schedule.every(n_interval).hours.at(":15").do(run_noticias)
    schedule.every(t_interval).hours.at(":20").do(run_tribunales)
    
    # Consultas Públicas (Horarios fijos)
    schedule.every().day.at(config.get("consultas_time_1", "08:30")).do(run_consultas)
    schedule.every().day.at(config.get("consultas_time_2", "15:30")).do(run_consultas)

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
