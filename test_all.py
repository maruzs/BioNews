from src.scrapers.mma import MMAScraper
from src.scrapers.sbap import SBAPScraper
from src.scrapers.diario_oficial import DiarioOficialScraper
from src.scrapers.sea import SEAScraper 
from src.database.manager import DatabaseManager

def run_sync():
    db = DatabaseManager()
    
    # Lista de scrapers a ejecutar
    scrapers = [
        MMAScraper(),
        SBAPScraper(),
        DiarioOficialScraper(),
        SEAScraper()
    ]
    
    total_nuevos = 0
    
    for s in scrapers:
        noticias = s.get_latest_news()
        if noticias:
            cantidad = db.save_news(noticias)
            total_nuevos += cantidad
            print(f"Guardadas {cantidad} nuevas noticias de {noticias[0]['fuente']}")

    print(f"\nSincronizacion terminada. Total nuevos registros: {total_nuevos}")

    # Verificacion rapida
    print("\nUltimos registros en base de datos:")
    for n in db.get_latest_news(limit=10):
        print(f"[{n[4]}] - {n[1]} ({n[2]})")

if __name__ == "__main__":
    run_sync()