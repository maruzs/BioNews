from src.scrapers.mma import MMAScraper

def test():
    scraper = MMAScraper()
    noticias = scraper.get_latest_news()
    
    print("\n--- RESULTADOS DE PRUEBA ---")
    for n in noticias[:3]: # Mostrar solo las primeras 3
        print(f"Titulo: {n['titulo']}")
        print(f"Fecha: {n['fecha']}")
        print(f"Link: {n['link']}")
        print(f"Imagen: {n['imagen']}")
        print("-" * 20)

if __name__ == "__main__":
    test()