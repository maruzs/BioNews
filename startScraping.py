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
from src.scrapers.engine import ScrapingEngine

def ejecutar_todo_el_scraping(log_callback):
    # log_callback reemplaza los print para enviar texto a la interfaz
    log_callback("Iniciando componentes del sistema...")

    db = DatabaseManager()
    log_callback("Base de datos conectada con exito")
    
    # 1. Sincronizacion de datos legales
    log_callback("--- INICIANDO SCRAPING LEGAL ---")
    legales = [
        ("Primer Tribunal Ambiental (1TA)", PrimerTribunalScraper()),
        ("Segundo Tribunal Ambiental (2TA)", SegundoTribunalScraper()),
        ("Tercer Tribunal Ambiental (3TA)", TercerTribunalScraperLegal()),
        ("SEA Legal", SEALegalScraper()),
        ("SNIFA Sancionatorios", SnifaScraper()),
        ("SNIFA Ingresos", SnifaIngresoScraper()),
        ("SNIFA Fiscalizaciones", SnifaFiscalizacionScraper())
    ]
    
    for nombre, s in legales:
        log_callback(f"Iniciando scraping legal en {nombre}")
        try:
            datos = s.get_legal_data()
            if datos:
                nuevos = db.save_legal(datos)
                log_callback(f"Guardados {nuevos} nuevos registros legales")
            else:
                log_callback(f"Sin registros nuevos para {nombre}")
        except Exception as e:
            log_callback(f"Error en {nombre}: {str(e)}")

    # 2. Sincronizacion de noticias
    log_callback("\n--- INICIANDO SCRAPING DE NOTICIAS ---")
    scrapers = [
        ("Tercer Tribunal", TercerTribunalScraper()),
        ("Corte Suprema", CorteSupremaScraper()),
        ("SMA", SMAScraper()),
        ("MMA", MMAScraper()),
        ("SBAP", SBAPScraper()),
        ("Diario Oficial", DiarioOficialScraper()),
        ("SEA Noticias", SEAScraper()),
        ("Sernageomin", SernageominScraper()),
        ("Tribunal Noticias", TribunalScraper())
    ]
    
    for nombre, s in scrapers:
        log_callback(f"Iniciando scraping en {nombre}")
        try:
            noticias = s.get_news()
            if noticias:
                nuevos = db.save_news(noticias)
                log_callback(f"Guardadas {nuevos} nuevas noticias de {nombre}")
            else:
                log_callback(f"Sin noticias nuevas para {nombre}")
        except Exception as e:
            log_callback(f"Error en {nombre}: {str(e)}")
            
    log_callback("\n--- PROCESO COMPLETADO ---")