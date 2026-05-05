"""
server.py  –  BioNews FastAPI Backend
======================================
Iniciar con:
    uvicorn server:app --host 0.0.0.0 --port 8000 --reload

Para producción (sin reload):
    uvicorn server:app --host 0.0.0.0 --port 8000
"""

import logging
import traceback
import json
import jwt
import datetime
import bcrypt
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException, status, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from src.database.manager import DatabaseManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("bionews.server")

app = FastAPI(title="BioNews API")

# ── CORS: permite el frontend Vite (dev) y cualquier origen Tailscale ────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En producción puedes limitar a la IP Tailscale del cliente
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()

# ─── AUTHENTICATION SETUP ───────────────────────────────────────────────────
SECRET_KEY = "bionews_super_secret_key_change_in_prod"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_default_admin():
    admin = db.get_user_by_email("administrador@bionews.cl")
    if not admin:
        hashed_pw = hash_password("#81680085pls")
        db.create_user("Administrador", "administrador@bionews.cl", hashed_pw, role="admin")

create_default_admin()

def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No token provided")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str = payload.get("sub")
        if user_id_str is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user_id = int(user_id_str)
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        # In a real app we might fetch user from DB here to check if blocked
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_admin(user = Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return user

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

@app.post("/api/auth/login")
def login(req: LoginRequest):
    user = db.get_user_by_email(req.email)
    if not user or not verify_password(req.password, user['password_hash']):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if user.get("blocked"):
        raise HTTPException(status_code=403, detail="Cuenta bloqueada")
        
    token_data = {"sub": str(user["id"]), "email": user["email"], "role": user["role"], "name": user["name"], "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "user": {"id": user["id"], "name": user["name"], "email": user["email"], "role": user["role"], "preferences": user["preferences"]}}

@app.post("/api/auth/register")
def register(req: RegisterRequest):
    if db.get_user_by_email(req.email):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    hashed_pw = hash_password(req.password)
    user_id = db.create_user(req.name, req.email, hashed_pw, role="user")
    if not user_id:
        raise HTTPException(status_code=500, detail="Error al crear usuario")
    
    token_data = {"sub": str(user_id), "email": req.email, "role": "user", "name": req.name, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "user": {"id": user_id, "name": req.name, "email": req.email, "role": "user", "preferences": "{}"}}

@app.get("/api/auth/me")
def get_me(user = Depends(get_current_user)):
    user_db = db.get_user_by_email(user["email"])
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    if user_db.get("blocked"):
        raise HTTPException(status_code=403, detail="Cuenta bloqueada")
    return {"id": user_db["id"], "name": user_db["name"], "email": user_db["email"], "role": user_db["role"], "preferences": user_db["preferences"]}

@app.put("/api/auth/preferences")
def update_preferences(req: dict, user = Depends(get_current_user)):
    # req is expected to be a dict of preferences
    prefs_str = json.dumps(req)
    db.update_user_preferences(user["sub"], prefs_str)
    return {"success": True}

# ─── ADMIN ENDPOINTS ────────────────────────────────────────────────────────
@app.get("/api/admin/users")
def admin_get_users(admin = Depends(get_current_admin)):
    return db.get_all_users()

@app.put("/api/admin/users/{user_id}/block")
def admin_block_user(user_id: int, req: dict, admin = Depends(get_current_admin)):
    blocked = req.get("blocked", 1)
    db.update_user_status(user_id, blocked)
    return {"success": True}

@app.delete("/api/admin/users/{user_id}")
def admin_delete_user(user_id: int, admin = Depends(get_current_admin)):
    db.delete_user(user_id)
    return {"success": True}

# ─── NEWS ─────────────────────────────────────────────────────────────────────
@app.get("/api/news")
def get_news():
    news = db.get_latest_news(limit=100)
    return [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news]

# ─── TABLAS ESPECIFICAS ─────────────────────────────────────────────────────
@app.get("/api/data/{table_name}")
def get_table_data(table_name: str, limit: int = 1000, user = Depends(get_current_user)):
    """Endpoint genérico para obtener datos de cualquier tabla permitida."""
    try:
        data = db.get_table_data(table_name, limit=limit)
        return data
    except ValueError as e:
        return {"error": str(e)}

@app.get("/api/data/{table_name}/count")
def get_table_count(table_name: str, user = Depends(get_current_user)):
    """Obtiene la cantidad de registros en una tabla."""
    try:
        count = db.get_table_count(table_name)
        return {"count": count}
    except ValueError as e:
        return {"error": str(e)}

@app.get("/api/options")
def get_options(user = Depends(get_current_user)):
    try:
        # Fetch a quick sample to get unique options. 
        # In a real app we would do SELECT DISTINCT.
        normativas = db.get_table_data("normativas", limit=5000)
        sma = db.get_table_data("fiscalizaciones", limit=5000)
        
        orgs = list(set(n.get("organismo") for n in normativas if n.get("organismo")))
        cats = list(set(s.get("categoria") for s in sma if s.get("categoria")))
        
        return {
            "normativas_organismos": orgs,
            "sma_categorias": cats
        }
    except Exception as e:
        return {"error": str(e)}

# ─── FAVORITES ───────────────────────────────────────────────────────────────
@app.get("/api/favorites")
def get_favorites(fuente: str = None, user = Depends(get_current_user)):
    favs = db.get_favorites(user_id=user["sub"], fuente=fuente)
    # user_id (0), id_o_link (1), fuente (2), nombre (3), fecha_agregado (4), accion (5)
    result = []
    for f in favs:
        accion = f[5] if len(f) > 5 else ""
        result.append({"id_o_link": f[1], "fuente": f[2], "nombre": f[3], "fecha_agregado": f[4], "accion": accion})
    return result

@app.post("/api/favorites")
def add_favorite(fav: dict, user = Depends(get_current_user)):
    accion = fav.get('accion', '')
    success = db.add_favorite(user["sub"], fav['id_o_link'], fav['fuente'], fav['nombre'], accion)
    return {"success": success}

@app.delete("/api/favorites/{id_o_link:path}")
def remove_favorite(id_o_link: str, user = Depends(get_current_user)):
    success = db.remove_favorite(user["sub"], id_o_link)
    return {"success": success}

# ─── LOGS ─────────────────────────────────────────────────────────────────────
@app.get("/api/logs")
def get_scraper_logs(user = Depends(get_current_user)):
    # Logs are requested by Sidebar for the red dots, so normal users need access to logs
    # We could restrict detailed logs to admin, but the simple ones are needed.
    return db.get_scraper_logs()

# ─── SCRAPING ENDPOINTS ───────────────────────────────────────────────────────
def _run_all_scrapers():
    """Función interna que corre todos los scrapers secuencialmente."""
    try:
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
    except ImportError as e:
        log.error(f"Error de importación al iniciar scrapers: {e}")
        return

    # ── Scrapers de datos (escriben directamente en sus tablas) ──────────────
    datos_scrapers = [
        ("Primer Tribunal Ambiental",  PrimerTribunalScraper),
        ("Segundo Tribunal Ambiental", SegundoTribunalScraper),
        ("Tercer Tribunal Ambiental",  TercerTribunalScraperLegal),
        ("Diario Oficial (Normativas)", DiarioOficialScraper),
        ("Pertinencias SEA",           PertinenciasScraper),
        ("SNIFA Sancionatorios",       SancionatoriosScraper),
        ("SNIFA Fiscalizaciones",      SnifaFiscalizacionScraper),
        ("SNIFA Requerimientos",       RequerimientosScraper),
        ("SNIFA Medidas Provisionales", MedidasProvisionalesScraper),
        ("SNIFA Programas de Cumplimiento", ProgramasCumplimientoScraper),
        ("SNIFA Registro Sanciones",   RegistroSancionesScraper),
    ]

    log.info("--- SCRAPING DATOS ---")
    for nombre, ScraperClass in datos_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            nuevos = scraper.run()
            db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
            log.info(f"{nombre}: {nuevos} nuevos registros.")
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    # ── Scrapers de noticias ─────────────────────────────────────────────────
    noticias_scrapers = [
        ("Tercer Tribunal (Noticias)",    TercerTribunalScraper),
        ("Corte Suprema",                 CorteSupremaScraper),
        ("SMA",                           SMAScraper),
        ("MMA",                           MMAScraper),
        ("SBAP",                          SBAPScraper),
        ("SEA Noticias",                  SEAScraper),
        ("Sernageomin",                   SernageominScraper),
        ("Tribunal Ambiental (Noticias)", TribunalScraper),
    ]

    log.info("--- SCRAPING NOTICIAS ---")
    for nombre, ScraperClass in noticias_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            items = ScraperClass().get_latest_news()
            if items:
                nuevas = db.save_news(items)
                db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                log.info(f"{nombre}: {nuevas} nuevas noticias.")
            else:
                db.log_scraper_run(nombre, exito=True, nuevos=0)
                log.info(f"{nombre}: sin noticias nuevas.")
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    log.info("--- SCRAPING FINALIZADO ---")

@app.post("/api/scrape/all")
def scrape_all(background_tasks: BackgroundTasks):
    background_tasks.add_task(_run_all_scrapers)
    return {"message": "Scraping iniciado en background."}

def _run_news_scrapers():
    """Función interna que corre solo los scrapers de noticias."""
    try:
        from src.scrapers.mma import MMAScraper
        from src.scrapers.sbap import SBAPScraper
        from src.scrapers.sea import SEAScraper
        from src.scrapers.sernageomin import SernageominScraper
        from src.scrapers.tribunal2 import TribunalScraper
        from src.scrapers.sma import SMAScraper
        from src.scrapers.corteSuprema import CorteSupremaScraper
        from src.scrapers.tribunal3 import TercerTribunalScraper
    except ImportError as e:
        log.error(f"Error de importación al iniciar scrapers: {e}")
        return

    noticias_scrapers = [
        ("Tercer Tribunal (Noticias)",    TercerTribunalScraper),
        ("Corte Suprema",                 CorteSupremaScraper),
        ("SMA",                           SMAScraper),
        ("MMA",                           MMAScraper),
        ("SBAP",                          SBAPScraper),
        ("SEA Noticias",                  SEAScraper),
        ("Sernageomin",                   SernageominScraper),
        ("Tribunal Ambiental (Noticias)", TribunalScraper),
    ]

    log.info("--- SCRAPING NOTICIAS MANUAL ---")
    for nombre, ScraperClass in noticias_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            items = ScraperClass().get_latest_news()
            if items:
                nuevas = db.save_news(items)
                db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                log.info(f"{nombre}: {nuevas} nuevas noticias.")
            else:
                db.log_scraper_run(nombre, exito=True, nuevos=0)
                log.info(f"{nombre}: sin noticias nuevas.")
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")
    log.info("--- SCRAPING NOTICIAS FINALIZADO ---")

@app.post("/api/scrape/news")
def scrape_news(background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    background_tasks.add_task(_run_news_scrapers)
    return {"message": "Scraping de noticias iniciado en background."}


# ─── Health check ──────────────────────────────────────────────────────────────
@app.get("/api/health")
def health():
    return {"status": "ok"}
