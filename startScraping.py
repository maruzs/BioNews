import traceback
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

def run_sync(log_callback):
    log_callback("Iniciando componentes del sistema...")
    
    try:
        db = DatabaseManager()
        log_callback("Base de datos conectada correctamente.")
    except Exception as e:
        log_callback(f"Error al conectar con la base de datos: {e}")
        return

    # 1. Sincronizacion de datos legales
    log_callback("--- INICIANDO SCRAPING LEGAL ---")
    legales = [
        ("Primer Tribunal Ambiental", PrimerTribunalScraper()),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper()),
        ("Tercer Tribunal Ambiental", TercerTribunalScraperLegal()),
        ("SEA Legal", SEALegalScraper()),
        ("SNIFA Sancionatorios", SnifaScraper()),
        ("SNIFA Ingresos", SnifaIngresoScraper()),
        ("SNIFA Fiscalizaciones", SnifaFiscalizacionScraper())
    ]
    
    for nombre, scraper in legales:
        log_callback(f"Procesando: {nombre}...")
        try:
            datos = scraper.get_legal_data()
            if datos:
                nuevos = db.save_legal(datos)
                log_callback(f"Exito: {nuevos} nuevos registros guardados.")
            else:
                log_callback("Sin registros nuevos encontrados.")
        except Exception as e:
            log_callback(f"Error en {nombre}: {str(e)}")

    # 2. Sincronizacion de noticias
    log_callback("\n--- INICIANDO SCRAPING DE NOTICIAS ---")
    noticias_scrapers = [
        ("Tercer Tribunal (Noticias)", TercerTribunalScraper()),
        ("Corte Suprema", CorteSupremaScraper()),
        ("SMA", SMAScraper()),
        ("MMA", MMAScraper()),
        ("SBAP", SBAPScraper()),
        ("Diario Oficial", DiarioOficialScraper()),
        ("SEA Noticias", SEAScraper()),
        ("Sernageomin", SernageominScraper()),
        ("Tribunal Ambiental (Noticias)", TribunalScraper())
    ]
    
    for nombre, scraper in noticias_scrapers:
        log_callback(f"Procesando: {nombre}...")
        try:
            # Llamamos a get_data() segun tu estructura original
            noticias = scraper.get_latest_news()
            if noticias:
                nuevas = db.save_news(noticias)
                log_callback(f"Exito: {nuevas} nuevas noticias guardadas.")
            else:
                log_callback("No se encontraron noticias nuevas.")
        except Exception as e:
            log_callback(f"Error inesperado en {nombre}: {str(e)}")

    log_callback("\n--- SINCRONIZACION FINALIZADA ---")