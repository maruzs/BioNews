from src.scrapers.mma import MMAScraper
from src.scrapers.sbap import SBAPScraper
from src.scrapers.diario_oficial import DiarioOficialScraper
from src.scrapers.sea import SEAScraper 
from src.scrapers.sernageomin import SernageominScraper
from src.scrapers.tribunal2 import TribunalScraper #Noticias
from src.scrapers.sea_legal import SEALegalScraper
from src.scrapers.snifa import SnifaScraper # Nueva importacion
from src.scrapers.sma import SMAScraper
from src.scrapers.corteSuprema import CorteSupremaScraper
from src.scrapers.tribunal3 import TercerTribunalScraper #Noticias
from src.scrapers.primerTribunal import PrimerTribunalScraper #Legal
from src.scrapers.segundoTribunal import SegundoTribunalScraper #Legal
from src.scrapers.tercerTribunal import TercerTribunalScraperLegal #Legal
from src.scrapers.reqSEIA import SnifaIngresoScraper # Nueva importacion
from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper # Nueva importacion
from src.database.manager import DatabaseManager
from src.scrapers.engine import ScrapingEngine

def run_sync():
    print("INGRESA 1")

    db = DatabaseManager()
    print("INGRESA 2")
    # 1. Sincronizacion de datos legales (Dashboard Principal)
    print("--- INICIANDO SCRAPING LEGAL ---")
    legales = [
        PrimerTribunalScraper(),
        SegundoTribunalScraper(),
        TercerTribunalScraperLegal(),
        SEALegalScraper(),
        SnifaScraper(),
        SnifaIngresoScraper(),
        SnifaFiscalizacionScraper()
    ]
    
    for s in legales:
        datos = s.get_legal_data()
        if datos:
            nuevos = db.save_legal(datos)
            print(f"Guardados {nuevos} nuevos registros legales")

    # 2. Sincronizacion de noticias
    print("\n--- INICIANDO SCRAPING DE NOTICIAS ---")
    scrapers = [
        TercerTribunalScraper(),
        CorteSupremaScraper(),
        SMAScraper(),
        MMAScraper(),
        SBAPScraper(),
        DiarioOficialScraper(),
        SEAScraper(),
        SernageominScraper(),
        TribunalScraper()
    ]
    
    total_noticias = 0
    for s in scrapers:
        noticias = s.get_latest_news()
        if noticias:
            cantidad = db.save_news(noticias)
            total_noticias += cantidad
            print(f"Guardadas {cantidad} nuevas noticias de {noticias[0]['fuente']}")

    print(f"\nSincronizacion terminada. Total noticias nuevas: {total_noticias}")

if __name__ == "__main__":
    run_sync()