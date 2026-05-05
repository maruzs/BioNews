import traceback
# Scrapers de noticias
from src.scrapers.mma import MMAScraper
from src.scrapers.sbap import SBAPScraper
from src.scrapers.sea import SEAScraper 
from src.scrapers.sernageomin import SernageominScraper
from src.scrapers.tribunal2 import TribunalScraper
from src.scrapers.sma import SMAScraper
from src.scrapers.corteSuprema import CorteSupremaScraper
from src.scrapers.tribunal3 import TercerTribunalScraper
# Scrapers de datos (tablas especificas)
from src.scrapers.primerTribunal import PrimerTribunalScraper
from src.scrapers.segundoTribunal import SegundoTribunalScraper
from src.scrapers.tercerTribunal import TercerTribunalScraperLegal
from src.scrapers.diario_oficial import DiarioOficialScraper
from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
from src.scrapers.sea_legal import PertinenciasScraper
from src.scrapers.reqSEIA import RequerimientosScraper
from src.scrapers.snifa import SancionatoriosScraper
from src.scrapers.medidas import MedidasProvisionalesScraper
from src.scrapers.pdc import ProgramasCumplimientoScraper
from src.scrapers.sanciones import RegistroSancionesScraper
import sys
from src.database.manager import DatabaseManager

class PrintLogger:
    def __init__(self, callback, original_stdout):
        self.callback = callback
        self.original_stdout = original_stdout
        self.buffer = ""

    def write(self, message):
        self.original_stdout.write(message)
        self.buffer += message
        if '\n' in self.buffer:
            lines = self.buffer.split('\n')
            for line in lines[:-1]:
                line_str = line.strip()
                if line_str:
                    self.callback(line_str)
            self.buffer = lines[-1]

    def flush(self):
        self.original_stdout.flush()
        if self.buffer.strip():
            self.callback(self.buffer.strip())
            self.buffer = ""

def run_sync(log_callback, progress_callback=None):
    original_stdout = sys.stdout
    sys.stdout = PrintLogger(log_callback, original_stdout)
    
    try:
        log_callback("Iniciando componentes del sistema...")
        
        try:
            db = DatabaseManager()
            log_callback("Base de datos conectada correctamente.")
        except Exception as e:
            log_callback(f"Error al conectar con la base de datos: {e}")
            return

        # 1. Sincronizacion de datos (scrapers que escriben directamente en sus tablas)
        log_callback("--- INICIANDO SCRAPING DE DATOS ---")
        datos_scrapers = [
            ("Primer Tribunal Ambiental", PrimerTribunalScraper()),
            ("Segundo Tribunal Ambiental", SegundoTribunalScraper()),
            ("Tercer Tribunal Ambiental", TercerTribunalScraperLegal()),
            ("Diario Oficial (Normativas)", DiarioOficialScraper()),
            ("Pertinencias SEA", PertinenciasScraper()),
            ("SNIFA Sancionatorios", SancionatoriosScraper()),
            ("SNIFA Fiscalizaciones", SnifaFiscalizacionScraper()),
            ("SNIFA Requerimientos", RequerimientosScraper()),
            ("SNIFA Medidas Provisionales", MedidasProvisionalesScraper()),
            ("SNIFA Programas de Cumplimiento", ProgramasCumplimientoScraper()),
            ("SNIFA Registro Sanciones", RegistroSancionesScraper()),
        ]
        
        noticias_scrapers = [
            ("Tercer Tribunal (Noticias)", TercerTribunalScraper()),
            ("Corte Suprema", CorteSupremaScraper()),
            ("SMA", SMAScraper()),
            ("MMA", MMAScraper()),
            ("SBAP", SBAPScraper()),
            ("SEA Noticias", SEAScraper()),
            ("Sernageomin", SernageominScraper()),
            ("Tribunal Ambiental (Noticias)", TribunalScraper())
        ]
        
        total_scrapers = len(datos_scrapers) + len(noticias_scrapers)
        current_scraper = 0

        def step_progress():
            nonlocal current_scraper
            current_scraper += 1
            if progress_callback:
                progress_callback(current_scraper / total_scrapers)
                
        for nombre, scraper in datos_scrapers:
            log_callback(f"Procesando: {nombre}...")
            try:
                nuevos = scraper.run()
                db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
                log_callback(f"Exito: {nuevos} nuevos registros guardados.")
            except Exception as e:
                db.log_scraper_run(nombre, exito=False, error=str(e))
                log_callback(f"Error en {nombre}: {str(e)}")
            finally:
                step_progress()

        # 2. Sincronizacion de noticias
        log_callback("\n--- INICIANDO SCRAPING DE NOTICIAS ---")
        for nombre, scraper in noticias_scrapers:
            log_callback(f"Procesando: {nombre}...")
            try:
                noticias = scraper.get_latest_news()
                if noticias:
                    nuevas = db.save_news(noticias)
                    db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                    log_callback(f"Exito: {nuevas} nuevas noticias guardadas.")
                else:
                    db.log_scraper_run(nombre, exito=True, nuevos=0)
                    log_callback("No se encontraron noticias nuevas.")
            except Exception as e:
                db.log_scraper_run(nombre, exito=False, error=str(e))
                log_callback(f"Error inesperado en {nombre}: {str(e)}")
            finally:
                step_progress()

        log_callback("\n--- SINCRONIZACION FINALIZADA ---")
    finally:
        sys.stdout = original_stdout