from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.database.manager import DatabaseManager
from src.scrapers.snifa import SnifaScraper
from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
# Import other scrapers as needed

app = FastAPI(title="BioNews API")

# Allow CORS for the Vite React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()

@app.get("/api/news")
def get_news():
    news = db.get_latest_news(limit=100)
    # Convert tuples to list of dicts for JSON serialization
    return [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news]

@app.get("/api/legal")
def get_legal():
    legal = db.get_all_legal(limit=1000)
    return [{"link": l[0], "nombre": l[1], "fecha": l[2], "estado": l[3], "tipo": l[4], "fuente": l[5], "fecha_scraping": l[6]} for l in legal]

@app.get("/api/favorites")
def get_favorites(fuente: str = None):
    favs = db.get_favorites(fuente=fuente)
    return [{"id_o_link": f[0], "fuente": f[1], "nombre": f[2], "fecha_agregado": f[3]} for f in favs]

@app.post("/api/favorites")
def add_favorite(fav: dict):
    success = db.add_favorite(fav['id_o_link'], fav['fuente'], fav['nombre'])
    return {"success": success}

@app.delete("/api/favorites/{id_o_link:path}")
def remove_favorite(id_o_link: str):
    success = db.remove_favorite(id_o_link)
    return {"success": success}

# Example of running a scraper via API
@app.post("/api/scrape/snifa")
def scrape_snifa(background_tasks: BackgroundTasks):
    def run_scrapers():
        scraper = SnifaScraper()
        data = scraper.get_legal_data()
        db.save_legal(data)
    background_tasks.add_task(run_scrapers)
    return {"status": "Scraping started in background"}
