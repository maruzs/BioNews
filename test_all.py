from src.scrapers.mma import MMAScraper
from src.scrapers.sbap import SBAPScraper
from src.scrapers.diario_oficial import DiarioOficialScraper
from src.scrapers.sea import SEAScraper 
from src.scrapers.sernageomin import SernageominScraper
from src.scrapers.tribunal2 import TribunalScraper
from src.scrapers.sea_legal import SEALegalScraper
from src.scrapers.snifa import SNIFAScraper # Nueva importacion
from src.database.manager import DatabaseManager

def run_sync():
    db = DatabaseManager()
    
    # 1. Sincronizacion de datos legales (Dashboard Principal)
    print("--- INICIANDO SCRAPING LEGAL ---")
    legales = [
        SEALegalScraper(),
        SNIFAScraper()
    ]
    
    for s in legales:
        datos = s.get_legal_data()
        if datos:
            nuevos = db.save_legal(datos)
            print(f"Guardados {nuevos} nuevos registros legales")

    # 2. Sincronizacion de noticias
    print("\n--- INICIANDO SCRAPING DE NOTICIAS ---")
    scrapers = [
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