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
import asyncio
from asyncio import Queue
from typing import Optional, List
# pyrefly: ignore [missing-import]
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException, status, Header, Request, WebSocket, WebSocketDisconnect, File, UploadFile, Form
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
# pyrefly: ignore [missing-import]
from fastapi.responses import StreamingResponse
# pyrefly: ignore [missing-import]
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import shutil
import os
from src.database.manager import DatabaseManager
from src.database.cache import cache
from src.scrapers.sea_legal import PertinenciasScraper
from src.scrapers.sea_evaluados import SEAEvaluadosScraper

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("bionews.server")

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="BioNews API")
# Instrument API metrics under /api/metrics
Instrumentator().instrument(app).expose(app, endpoint="/api/metrics", include_in_schema=False)

# ── CORS: permite el frontend Vite (dev) y cualquier origen Tailscale ────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En producción puedes limitar a la IP Tailscale del cliente
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()

# Directorio para uploads
UPLOAD_DIR = "uploads/bugs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ─── SSE NOTIFICATION MANAGER ───────────────────────────────────────────────
class SSEManager:
    """Gestiona colas SSE por cliente. Cada cliente tiene su propia Queue."""
    def __init__(self):
        self._clients: List[Queue] = []

    def add_client(self) -> Queue:
        q: Queue = asyncio.Queue()
        self._clients.append(q)
        return q

    def remove_client(self, q: Queue):
        if q in self._clients:
            self._clients.remove(q)

    async def broadcast(self, data: dict):
        msg = f"data: {json.dumps(data)}\n\n"
        dead = []
        for q in self._clients:
            try:
                await q.put(msg)
            except Exception:
                dead.append(q)
        for q in dead:
            self.remove_client(q)

sse_manager = SSEManager()

# Mantener el ConnectionManager/WebSocket por compatibilidad (no se usa activamente)
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
    async def broadcast(self, message: dict):
        pass  # Deprecated: usar SSE
manager = ConnectionManager()

async def notify_new_content(category_slug: str, item_id: str = None):
    """Notifica a los clientes vía SSE cuando hay contenido nuevo."""
    await sse_manager.broadcast({
        "type": "new_content",
        "category": category_slug,
        "timestamp": datetime.datetime.now().isoformat()
    })

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
        
    db.update_user_last_login(user["id"])
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

@app.get("/api/admin/scheduler")
def get_scheduler_config(admin = Depends(get_current_admin)):
    import json
    from pathlib import Path
    config_path = Path("data/scheduler.json")
    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)
    return {
        "snifa_time_1": "07:00",
        "snifa_time_2": "14:00",
        "pertinencias_interval": 1,
        "noticias_interval": 1,
        "tribunales_interval": 1,
        "hora_inicio": "07:00",
        "hora_fin": "19:00"
    }

@app.post("/api/admin/scheduler")
def update_scheduler_config(req: dict, admin = Depends(get_current_admin)):
    import json
    from pathlib import Path
    config_path = Path("data/scheduler.json")
    with open(config_path, "w") as f:
        json.dump(req, f)
    return {"success": True}

@app.get("/api/config/notifications")
def get_notifications_config():
    from pathlib import Path
    import json
    config_path = Path("data/scheduler.json")
    if config_path.exists():
        with open(config_path, "r") as f:
            config = json.load(f)
            return {"interval": config.get("notification_interval", 15)}
    return {"interval": 15}

# ─── BUG REPORTS ────────────────────────────────────────────────────────────
@app.post("/api/bugs")
async def report_bug(
    titulo: str = Form(...),
    descripcion: str = Form(...),
    screenshot: UploadFile = File(None),
    user = Depends(get_current_user)
):
    screenshot_path = None
    if screenshot:
        # Validar tamaño (5MB)
        contents = await screenshot.read()
        if len(contents) > 5 * 1024 * 1024:
             raise HTTPException(status_code=400, detail="El archivo es demasiado grande (máximo 5MB)")
        await screenshot.seek(0)
        
        # Guardar archivo
        file_ext = screenshot.filename.split(".")[-1] if "." in screenshot.filename else "png"
        filename = f"bug_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{user['sub']}.{file_ext}"
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(screenshot.file, buffer)
        screenshot_path = f"/uploads/bugs/{filename}"

    db.save_bug_report(user["sub"], titulo, descripcion, screenshot_path)
    return {"success": True}

@app.get("/api/admin/bugs")
def get_admin_bugs(admin = Depends(get_current_admin)):
    return db.get_bug_reports()

@app.get("/api/bugs/my")
def get_my_bugs(user = Depends(get_current_user)):
    return db.get_bug_reports(user_id=user["sub"])

@app.put("/api/admin/bugs/{bug_id}/resolve")
def resolve_bug(bug_id: int, admin = Depends(get_current_admin)):
    from pathlib import Path
    bug = db.get_bug_report(bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug no encontrado")
    
    # Borrar imagen asociada si existe
    if bug["screenshot_path"]:
        filename = bug["screenshot_path"].split("/")[-1]
        file_path = Path("uploads/bugs") / filename
        if file_path.exists():
            file_path.unlink()
    
    db.update_bug_status(bug_id, "resuelto")
    return {"message": "Bug marcado como resuelto y captura eliminada."}

@app.delete("/api/admin/bugs/{bug_id}")
def delete_bug_admin(bug_id: int, admin = Depends(get_current_admin)):
    from pathlib import Path
    bug = db.get_bug_report(bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug no encontrado")
    
    # Solo se pueden borrar si están resueltos
    if bug["status"] != "resuelto":
         raise HTTPException(status_code=400, detail="Solo se pueden borrar reportes resueltos")

    if bug["screenshot_path"]:
        filename = bug["screenshot_path"].split("/")[-1]
        file_path = Path("uploads/bugs") / filename
        if file_path.exists():
            file_path.unlink()
            
    db.delete_bug_report(bug_id)
    return {"message": "Reporte eliminado permanentemente."}

@app.delete("/api/bugs/{bug_id}")
def delete_bug_user(bug_id: int, user = Depends(get_current_user)):
    from pathlib import Path
    bug = db.get_bug_report(bug_id)
    if not bug or bug["user_id"] != int(user["sub"]):
        raise HTTPException(status_code=404, detail="Bug no encontrado o no pertenece al usuario")
    
    if bug["screenshot_path"]:
        filename = bug["screenshot_path"].split("/")[-1]
        file_path = Path("uploads/bugs") / filename
        if file_path.exists():
            file_path.unlink()
            
    db.delete_bug_report(bug_id)
    return {"message": "Reporte eliminado permanentemente."}

# ─── NEWS ─────────────────────────────────────────────────────────────────────
@app.get("/api/news")
def get_news(user = Depends(get_current_user)):
    cache_key = "news:latest:100"
    cached_dicts = cache.get(cache_key)
    if cached_dicts is not None:
        news_dicts = cached_dicts
    else:
        news_rows = db.get_latest_news(limit=100)
        # Convertir a dicts
        news_dicts = [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news_rows]
        cache.set(cache_key, news_dicts, expire_seconds=300)
    # Agregar flag is_new
    return db.get_items_with_new_flag(user["sub"], "noticias", news_dicts)

# ─── TABLAS ESPECIFICAS ─────────────────────────────────────────────────────
@app.get("/api/data/{table_name}")
def get_table_data(table_name: str, limit: int = 1000, user = Depends(get_current_user)):
    """Endpoint genérico para obtener datos de cualquier tabla permitida."""
    try:
        cache_key = f"table_data:{table_name}:{limit}"
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            data = cached_data
        else:
            data = db.get_table_data(table_name, limit=limit)
            cache.set(cache_key, data, expire_seconds=300)
            
        category_slug = table_name
        return db.get_items_with_new_flag(user["sub"], category_slug, data)
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

@app.get("/api/consultas/documentos/{consulta_id}")
def get_consultation_docs(consulta_id: str, tipo: str, user = Depends(get_current_user)):
    """Obtiene los documentos asociados a una consulta pública."""
    return db.get_consultation_documents(consulta_id, tipo)

@app.get("/api/minsal/documents/{consulta_id}")
def get_minsal_docs_alias(consulta_id: str, type: str, user = Depends(get_current_user)):
    """Alias para el endpoint de documentos de MINSAL con mapeo de tipos."""
    mapped_type = f"minsal_{type}" if not type.startswith("minsal_") else type
    return db.get_consultation_documents(consulta_id, mapped_type)

@app.delete("/api/admin/debug/delete-latest/{category}")
def delete_latest_record(category: str, admin = Depends(get_current_admin)):
    """Endpoint de depuración para borrar el registro más reciente basado en fecha."""
    table_mapping = {
        "mma_abiertas": "mma_abiertas",
        "mma_cerradas": "mma_cerradas",
        "minsal_vigentes": "minsal_vigentes",
        "sea_evaluados": "sea_proyectos_evaluados",
        "pertinencias": "pertinencias",
        "fiscalizaciones": "fiscalizaciones",
        "sancionatorios": "sancionatorios",
        "sanciones": "registroSanciones",
        "programas": "programasDeCumplimiento",
        "medidas": "medidas_provisionales",
        "requerimientos": "requerimientos",
    }
    
    table = table_mapping.get(category)
    if not table and category not in ["tribunal_1", "tribunal_2", "tribunal_3"]:
        raise HTTPException(status_code=400, detail="Categoría inválida")
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        try:
            if category.startswith("tribunal_"):
                trib_id = category.split("_")[1]
                trib_names = {"1": "Primer Tribunal", "2": "Segundo Tribunal", "3": "Tercer Tribunal"}
                trib_name = trib_names.get(trib_id)
                # En Postgres la tabla es "Tribunales" y la PK es "Rol". Usamos %s en psycopg2.
                cursor.execute('DELETE FROM "Tribunales" WHERE "Rol" = (SELECT "Rol" FROM "Tribunales" WHERE "Tribunal" = %s ORDER BY fecha_scraping DESC, "Fecha" DESC, "Rol" DESC LIMIT 1)', (trib_name,))
                deleted = cursor.rowcount
            
            elif category in ["mma_abiertas", "mma_cerradas"]:
                # MMA format: dd-mm-yyyy. La PK es id.
                cursor.execute(f"""
                    DELETE FROM "{table}" 
                    WHERE id = (
                        SELECT id FROM "{table}" 
                        ORDER BY substr(fecha_inicio, 7, 4) || '-' || substr(fecha_inicio, 4, 2) || '-' || substr(fecha_inicio, 1, 2) DESC, id DESC 
                        LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "minsal_vigentes":
                # MINSAL format: yyyy-mm-dd. La PK es id.
                cursor.execute(f"""
                    DELETE FROM "{table}" 
                    WHERE id = (
                        SELECT id FROM "{table}" 
                        ORDER BY fecha_inicio DESC, id DESC 
                        LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "sea_evaluados":
                # SEA format: dd/mm/yyyy. La PK es id.
                cursor.execute(f"""
                    DELETE FROM "{table}" 
                    WHERE id = (
                        SELECT id FROM "{table}" 
                        ORDER BY substr(fecha_presentacion, 7, 4) || '-' || substr(fecha_presentacion, 4, 2) || '-' || substr(fecha_presentacion, 1, 2) DESC, id DESC 
                        LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "pertinencias":
                # Pertinencias format: yyyy-mm-dd. La PK es "Expediente".
                cursor.execute(f"""
                    DELETE FROM "{table}" 
                    WHERE "Expediente" = (
                        SELECT "Expediente" FROM "{table}" 
                        ORDER BY "Fecha" DESC, "Expediente" DESC 
                        LIMIT 1
                    )
                """)
                deleted = cursor.rowcount

            elif category in ["fiscalizaciones", "sancionatorios", "sanciones", "programas", "medidas", "requerimientos"]:
                # Las tablas de la SMA usan ficha_id.
                cursor.execute(f'DELETE FROM "{table}" WHERE ficha_id = (SELECT MAX(ficha_id) FROM "{table}")')
                deleted = cursor.rowcount
            else:
                # Fallback genérico para Postgres
                try:
                    cursor.execute(f'DELETE FROM "{table}" WHERE id = (SELECT id FROM "{table}" ORDER BY id DESC LIMIT 1)')
                    deleted = cursor.rowcount
                except Exception:
                    cursor.execute(f'DELETE FROM "{table}" WHERE "Expediente" = (SELECT "Expediente" FROM "{table}" ORDER BY "Expediente" DESC LIMIT 1)')
                    deleted = cursor.rowcount
            
            conn.commit()
            
            try:
                cache.invalidate_pattern("table_data:*")
                cache.invalidate_pattern("news:*")
            except Exception:
                pass
                
            return {"status": "ok", "deleted": deleted, "table": table or "Tribunales"}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))

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

@app.get("/api/search")
def global_search(q: str = "", user = Depends(get_current_user)):
    """Búsqueda global en todas las tablas."""
    if not q or len(q.strip()) < 2:
        return {"results": {}, "total": 0}
    
    q = q.strip()
    results = {}
    total = 0
    LIMIT_PER_TABLE = 50
    
    # Configuración de cada tabla: (nombre_tabla, campos_a_buscar, campo_titulo, campo_id, campo_accion)
    search_config = [
        ("fiscalizaciones",       ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("sancionatorios",        ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("registroSanciones",     ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("programasDeCumplimiento",["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("medidas_provisionales", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("requerimientos",        ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("normativas",            ["normativa", "organismo", "suborganismo"], "normativa", "accion", "accion"),
        ("noticias",              ["titulo", "fuente"], "titulo", "link", "link"),
        ("Tribunales",            ["Rol", "Caratula"], "Caratula", "Rol", "Accion"),
        ("pertinencias",          ["Expediente", "Nombre_de_Proyecto", "Proponente", "tipo_proyecto", "categoria_economica"], "Nombre_de_Proyecto", "Expediente", "Accion"),
        ("sea_proyectos_evaluados", ["nombre", "titular", "via_ingreso", "estado_proyecto", "tipo_proyecto", "categoria_economica"], "nombre", "id", "url"),
    ]
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        for table, fields, title_field, id_field, action_field in search_config:
            try:
                where_clauses = " OR ".join([f'LOWER("{f}") LIKE %s' for f in fields])
                params = [f'%{q.lower()}%'] * len(fields)
                cursor.execute(
                    f'SELECT * FROM "{table}" WHERE {where_clauses} LIMIT {LIMIT_PER_TABLE}',
                    params
                )
                rows = cursor.fetchall()
                if not rows:
                    continue
                # Obtener nombres de columnas
                col_names = [desc[0] for desc in cursor.description]
                table_results = []
                for row in rows:
                    d = dict(zip(col_names, row))
                    table_results.append({
                        "id": str(d.get(id_field, "")),
                        "titulo": str(d.get(title_field, ""))[:120],
                        "accion": d.get(action_field, ""),
                        "extra": d.get("expediente") or d.get("Expediente") or d.get("fecha") or d.get("Fecha") or "",
                        "_raw": d
                    })
                if table_results:
                    results[table] = table_results
                    total += len(table_results)
            except Exception:
                pass  # Tabla sin datos o error, ignorar
    
    return {"results": results, "total": total, "query": q}

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

@app.get("/api/stats/{table_name}")
def get_stats(table_name: str, user = Depends(get_current_user)):
    stats = db.get_stats(table_name)
    if not stats:
        return {"error": "Tabla no encontrada o sin estadísticas"}
    return stats

# ─── NOTIFICATIONS ───────────────────────────────────────────────────────────
@app.get("/api/notifications/status")
def get_notification_status(user = Depends(get_current_user)):
    return db.get_notification_status(user["sub"])

@app.get("/api/notifications/status/{category}")
def get_notification_status_single(category: str, user = Depends(get_current_user)):
    """Verifica si una categoría específica tiene ítems nuevos."""
    has_new = db._check_if_category_has_new(user["sub"], category)
    return {"has_new": has_new, "category": category}

@app.post("/api/notifications/exit")
def post_notification_exit(req: dict, user = Depends(get_current_user)):
    category = req.get("category")
    if not category:
        raise HTTPException(status_code=400, detail="Category is required")
    log.info(f"POST /api/notifications/exit: User {user['sub']} saliendo de {category}")
    db.update_category_exit(user["sub"], category)
    return {"success": True}

@app.delete("/api/notifications/reset")
def reset_notification_history(user = Depends(get_current_user)):
    """Borra el historial de last_exit_at del usuario → todo vuelve a aparecer como 'nuevo'."""
    with db.get_users_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM user_category_views WHERE user_id = %s", (user["sub"],))
            cur.execute("DELETE FROM user_item_views WHERE user_id = %s", (user["sub"],))
            conn.commit()
    return {"success": True, "message": "Historial de notificaciones reseteado"}

@app.post("/api/notifications/view-item")
def post_notification_view_item(req: dict, user = Depends(get_current_user)):
    category = req.get("category")
    item_id = req.get("item_id")
    if not category or not item_id:
        raise HTTPException(status_code=400, detail="Category and item_id are required")
    db.mark_item_viewed(user["sub"], item_id, category)
    return {"success": True}

@app.get("/api/notifications/stream")
async def notification_stream(request: Request, token: str = ""):
    """SSE stream: el cliente se conecta una vez y recibe eventos push cuando hay contenido nuevo."""
    if not token:
        raise HTTPException(status_code=401, detail="No token")
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    q = sse_manager.add_client()

    async def event_generator():
        try:
            # Enviar keepalive inicial
            yield f"data: {json.dumps({'type': 'connected'})}\n\n"
            while True:
                # Esperar evento o keepalive cada 25 segundos
                try:
                    msg = await asyncio.wait_for(q.get(), timeout=25.0)
                    yield msg
                except asyncio.TimeoutError:
                    # keepalive para mantener la conexión
                    yield ": keepalive\n\n"
                if await request.is_disconnected():
                    break
        finally:
            sse_manager.remove_client(q)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

# ─── SCRAPING ENDPOINTS ───────────────────────────────────────────────────────
async def _run_all_scrapers():
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
        from src.scrapers.tribunal3 import TercerTribunalNewsScraper
        from src.scrapers.scraper_dga import DGAScraper
        # Scrapers de datos (tablas especificas)
        from src.scrapers.primerTribunal import PrimerTribunalScraper
        from src.scrapers.segundoTribunal import SegundoTribunalScraper
        from src.scrapers.tercerTribunal import TercerTribunalScraper
        from src.scrapers.diario_oficial import DiarioOficialScraper
        from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
        from src.scrapers.sea_legal import PertinenciasScraper
        from src.scrapers.reqSEIA import RequerimientosScraper
        from src.scrapers.snifa import SancionatoriosScraper
        from src.scrapers.medidas import MedidasProvisionalesScraper
        from src.scrapers.pdc import ProgramasCumplimientoScraper
        from src.scrapers.sanciones import RegistroSancionesScraper
        from src.scrapers.minsal import MINSALScraper
        from src.scrapers.mma_consultas import MMAConsultasScraper
        from src.scrapers.dga_consultas import DGAConsultasScraper
    except ImportError as e:
        log.error(f"Error de importación al iniciar scrapers: {e}")
        return

    # ── Scrapers de datos (escriben directamente en sus tablas) ──────────────
    datos_scrapers = [
        ("Primer Tribunal",            PrimerTribunalScraper),
        ("Segundo Tribunal",           SegundoTribunalScraper),
        ("Tercer Tribunal",            TercerTribunalScraper),
        ("Diario Oficial (Normativas)", DiarioOficialScraper),
        ("Pertinencias SEA",           PertinenciasScraper),
        ("SNIFA Sancionatorios",       SancionatoriosScraper),
        ("SNIFA Fiscalizaciones",      SnifaFiscalizacionScraper),
        ("SNIFA Requerimientos",       RequerimientosScraper),
        ("SNIFA Medidas Provisionales", MedidasProvisionalesScraper),
        ("SNIFA Programas de Cumplimiento", ProgramasCumplimientoScraper),
        ("SNIFA Registro Sanciones",   RegistroSancionesScraper),
        ("MINSAL Consultas",           MINSALScraper),
        ("MMA Consultas",              MMAConsultasScraper),
        ("DGA Consultas",              DGAConsultasScraper),
    ]

    log.info("--- SCRAPING DATOS ---")
    mapping = {
        "Primer Tribunal": "Tribunales",
        "Segundo Tribunal": "Tribunales",
        "Tercer Tribunal": "Tribunales",
        "Diario Oficial (Normativas)": "normativas",
        "Pertinencias SEA": "pertinencias",
        "SNIFA Sancionatorios": "sancionatorios",
        "SNIFA Fiscalizaciones": "fiscalizaciones",
        "SNIFA Requerimientos": "requerimientos",
        "SNIFA Medidas Provisionales": "medidas_provisionales",
        "SNIFA Registro Sanciones": "registroSanciones",
        "MINSAL Consultas": "minsal_vigentes",
        "MMA Consultas": "mma",
        "DGA Consultas": "dga",
    }
    for nombre, ScraperClass in datos_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            scraper_inst = ScraperClass()
            nuevos = await asyncio.to_thread(scraper_inst.run)
            db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
            log.info(f"{nombre}: {nuevos} nuevos registros.")
            if nuevos > 0:
                cat = mapping.get(nombre)
                if cat:
                    await notify_new_content(cat)
                    if nombre == "MINSAL Consultas":
                        await notify_new_content("minsal_resultados")
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    # ── Scrapers de noticias ─────────────────────────────────────────────────
    noticias_scrapers = [
        ("Tercer Tribunal",               TercerTribunalNewsScraper),
        ("Corte Suprema",                 CorteSupremaScraper),
        ("SMA",                           SMAScraper),
        ("MMA",                           MMAScraper),
        ("SBAP",                          SBAPScraper),
        ("SEA",                           SEAScraper),
        ("Sernageomin",                   SernageominScraper),
        ("Segundo Tribunal",              TribunalScraper),
        ("DGA",                           DGAScraper),
    ]

    log.info("--- SCRAPING NOTICIAS ---")
    for nombre, ScraperClass in noticias_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            scraper_inst = ScraperClass()
            items = await asyncio.to_thread(scraper_inst.get_latest_news)
            if items:
                nuevas = db.save_news(items)
                db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                log.info(f"{nombre}: {nuevas} nuevas noticias.")
                if nuevas > 0:
                    await notify_new_content("noticias")
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

@app.post("/api/scrape/tribunales")
def scrape_tribunales(background_tasks: BackgroundTasks):
    background_tasks.add_task(_run_tribunales_scrapers)
    return {"message": "Scraping de tribunales iniciado."}

async def _run_tribunales_scrapers():
    """Función interna que corre solo los scrapers de tribunales legales."""
    log.info("--- SCRAPING TRIBUNALES MANUAL ---")
    
    # 2. Ejecutar scrapers
    try:
        from src.scrapers.primerTribunal import PrimerTribunalScraper
        from src.scrapers.segundoTribunal import SegundoTribunalScraper
        from src.scrapers.tercerTribunal import TercerTribunalScraper
    except ImportError as e:
        log.error(f"Error de importación en scrapers tribunales: {e}")
        return

    scrapers = [
        ("Primer Tribunal", PrimerTribunalScraper),
        ("Segundo Tribunal", SegundoTribunalScraper),
        ("Tercer Tribunal", TercerTribunalScraper),
    ]

    for nombre, ScraperClass in scrapers:
        log.info(f"Procesando {nombre}...")
        try:
            scraper_inst = ScraperClass()
            nuevos = await asyncio.to_thread(scraper_inst.run)
            db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
            log.info(f"{nombre}: {nuevos} nuevas causas.")
            if nuevos > 0:
                await notify_new_content("Tribunales")
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))
            log.error(f"Error en {nombre}:\n{traceback.format_exc()}")

    log.info("--- SCRAPING TRIBUNALES FINALIZADO ---")

async def _run_news_scrapers():
    """Función interna que corre solo los scrapers de noticias."""
    try:
        from src.scrapers.mma import MMAScraper
        from src.scrapers.sbap import SBAPScraper
        from src.scrapers.sea import SEAScraper
        from src.scrapers.sernageomin import SernageominScraper
        from src.scrapers.tribunal2 import TribunalScraper
        from src.scrapers.sma import SMAScraper
        from src.scrapers.corteSuprema import CorteSupremaScraper
        from src.scrapers.tribunal3 import TercerTribunalNewsScraper as TercerTribunalScraper
        from src.scrapers.scraper_dga import DGAScraper
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
        ("Segundo Tribunal",              TribunalScraper),
        ("DGA",                           DGAScraper),
    ]

    log.info("--- SCRAPING NOTICIAS MANUAL ---")
    for nombre, ScraperClass in noticias_scrapers:
        log.info(f"Procesando: {nombre}...")
        try:
            # Ejecutamos el scraper (síncrono) en un hilo para no bloquear el loop principal
            scraper_inst = ScraperClass()
            items = await asyncio.to_thread(scraper_inst.get_latest_news)
            
            if items:
                nuevas = db.save_news(items)
                db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
                log.info(f"{nombre}: {nuevas} nuevas noticias.")
                if nuevas > 0:
                    await notify_new_content("noticias")
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

async def _run_sea_scrapers():
    # 1. Pertinencias
    try:
        scraper_pert = PertinenciasScraper()
        nuevos_pert = await asyncio.to_thread(scraper_pert.run)
        db.log_scraper_run("Pertinencias SEA", exito=True, nuevos=nuevos_pert)
        if nuevos_pert > 0:
            await notify_new_content("pertinencias")
    except Exception as e:
        db.log_scraper_run("Pertinencias SEA", exito=False, error=str(e))

    # 2. Proyectos Evaluados
    try:
        scraper_eval = SEAEvaluadosScraper()
        nuevos_eval = await asyncio.to_thread(scraper_eval.run)
        db.log_scraper_run("Proyectos Evaluados SEA", exito=True, nuevos=nuevos_eval)
        if nuevos_eval > 0:
            await notify_new_content("sea_proyectos_evaluados")
    except Exception as e:
        db.log_scraper_run("Proyectos Evaluados SEA", exito=False, error=str(e))

@app.post("/api/scrape/sea")
def scrape_sea(background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    background_tasks.add_task(_run_sea_scrapers)
    return {"message": "Scraping de SEA iniciado en background."}

class SEAManualRequest(BaseModel):
    start_date: str
    end_date: str

async def _run_sea_scrapers_manual(start_date: str, end_date: str):
    # 1. Pertinencias
    try:
        scraper_pert = PertinenciasScraper()
        nuevos_pert = await asyncio.to_thread(scraper_pert.run, start_date, end_date)
        db.log_scraper_run("Pertinencias SEA (Manual)", exito=True, nuevos=nuevos_pert)
        if nuevos_pert > 0:
            await notify_new_content("pertinencias")
    except Exception as e:
        db.log_scraper_run("Pertinencias SEA (Manual)", exito=False, error=str(e))

    # 2. Proyectos Evaluados
    try:
        scraper_eval = SEAEvaluadosScraper()
        nuevos_eval = await asyncio.to_thread(scraper_eval.run, start_date, end_date)
        db.log_scraper_run("Proyectos Evaluados SEA (Manual)", exito=True, nuevos=nuevos_eval)
        if nuevos_eval > 0:
            await notify_new_content("sea_proyectos_evaluados")
    except Exception as e:
        db.log_scraper_run("Proyectos Evaluados SEA (Manual)", exito=False, error=str(e))

@app.post("/api/scrape/sea/manual")
def scrape_sea_manual(req: SEAManualRequest, background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    if not req.start_date or not req.end_date:
        raise HTTPException(status_code=400, detail="start_date and end_date are required")
    background_tasks.add_task(_run_sea_scrapers_manual, req.start_date, req.end_date)
    return {"message": f"Scraping manual de SEA iniciado en background para el rango {req.start_date} al {req.end_date}."}

async def _run_snifa_scrapers():
    from src.scrapers.fiscalizaciones import SnifaFiscalizacionScraper
    from src.scrapers.reqSEIA import RequerimientosScraper
    from src.scrapers.snifa import SancionatoriosScraper
    from src.scrapers.medidas import MedidasProvisionalesScraper
    from src.scrapers.pdc import ProgramasCumplimientoScraper
    from src.scrapers.sanciones import RegistroSancionesScraper
    log.info("MANUAL")
    scrapers = [
        ("SNIFA Sancionatorios", SancionatoriosScraper),
        ("SNIFA Fiscalizaciones", SnifaFiscalizacionScraper),
        ("SNIFA Requerimientos", RequerimientosScraper),
        ("SNIFA Medidas Provisionales", MedidasProvisionalesScraper),
        ("SNIFA Programas de Cumplimiento", ProgramasCumplimientoScraper),
        ("SNIFA Registro Sanciones", RegistroSancionesScraper)
    ]
    mapping = {
        "SNIFA Sancionatorios": "sancionatorios",
        "SNIFA Fiscalizaciones": "fiscalizaciones",
        "SNIFA Requerimientos": "requerimientos",
        "SNIFA Medidas Provisionales": "medidas_provisionales",
        "SNIFA Programas de Cumplimiento": "programasDeCumplimiento",
        "SNIFA Registro Sanciones": "registroSanciones"
    }
    for nombre, ScraperClass in scrapers:
        try:
            scraper_inst = ScraperClass()
            nuevos = await asyncio.to_thread(scraper_inst.run)
            db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
            if nuevos > 0:
                cat = mapping.get(nombre)
                if cat:
                    await notify_new_content(cat)
        except Exception as e:
            db.log_scraper_run(nombre, exito=False, error=str(e))

@app.post("/api/scrape/snifa")
def scrape_snifa(background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    background_tasks.add_task(_run_snifa_scrapers)
    return {"message": "Scraping de SNIFA iniciado en background."}

async def _run_normativas_scrapers():
    from src.scrapers.diario_oficial import DiarioOficialScraper
    try:
        scraper_inst = DiarioOficialScraper()
        nuevos = await asyncio.to_thread(scraper_inst.run)
        db.log_scraper_run("Diario Oficial (Normativas)", exito=True, nuevos=nuevos)
        if nuevos > 0:
            await notify_new_content("normativas")
    except Exception as e:
        db.log_scraper_run("Diario Oficial (Normativas)", exito=False, error=str(e))

@app.post("/api/scrape/normativas")
def scrape_normativas(background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    background_tasks.add_task(_run_normativas_scrapers)
    return {"message": "Scraping de Normativas iniciado en background."}

class NormativasManualRequest(BaseModel):
    start_date: str
    end_date: str

async def _run_normativas_scrapers_manual(start_date: str, end_date: str):
    from src.scrapers.diario_oficial import DiarioOficialScraper
    try:
        scraper_inst = DiarioOficialScraper()
        nuevos = await asyncio.to_thread(scraper_inst.run, start_date, end_date)
        db.log_scraper_run("Diario Oficial (Normativas) (Manual)", exito=True, nuevos=nuevos)
        if nuevos > 0:
            await notify_new_content("normativas")
    except Exception as e:
        db.log_scraper_run("Diario Oficial (Normativas) (Manual)", exito=False, error=str(e))

@app.post("/api/scrape/normativas/manual")
def scrape_normativas_manual(req: NormativasManualRequest, background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    if not req.start_date or not req.end_date:
        raise HTTPException(status_code=400, detail="start_date and end_date are required")
    background_tasks.add_task(_run_normativas_scrapers_manual, req.start_date, req.end_date)
    return {"message": f"Scraping manual de Normativas iniciado en background para el rango {req.start_date} al {req.end_date}."}

async def _run_consultas_scrapers():
    from src.scrapers.minsal import MINSALScraper
    from src.scrapers.mma_consultas import MMAConsultasScraper
    from src.scrapers.dga_consultas import DGAConsultasScraper
    # MINSAL
    try:
        log.info("Procesando MINSAL Consultas...")
        scraper_inst = MINSALScraper()
        nuevos_minsal = await asyncio.to_thread(scraper_inst.run)
        db.log_scraper_run("MINSAL Consultas", exito=True, nuevos=nuevos_minsal)
        if nuevos_minsal > 0:
            await notify_new_content("minsal_vigentes")
            await notify_new_content("minsal_resultados")
    except Exception as e:
        db.log_scraper_run("MINSAL Consultas", exito=False, error=str(e))
        log.error(f"Error en MINSAL Consultas: {e}")

    # MMA
    try:
        log.info("Procesando MMA Consultas...")
        scraper_inst = MMAConsultasScraper()
        nuevos_mma = await asyncio.to_thread(scraper_inst.run)
        db.log_scraper_run("MMA Consultas", exito=True, nuevos=nuevos_mma)
        if nuevos_mma > 0:
            await notify_new_content("mma")
    except Exception as e:
        db.log_scraper_run("MMA Consultas", exito=False, error=str(e))
        log.error(f"Error en MMA Consultas: {e}")
        
    # DGA
    try:
        log.info("Procesando DGA Consultas...")
        scraper_inst = DGAConsultasScraper()
        nuevos_dga = await asyncio.to_thread(scraper_inst.run)
        db.log_scraper_run("DGA Consultas", exito=True, nuevos=nuevos_dga)
        if nuevos_dga > 0:
            await notify_new_content("dga")
    except Exception as e:
        db.log_scraper_run("DGA Consultas", exito=False, error=str(e))
        log.error(f"Error en DGA Consultas: {e}")

@app.post("/api/scrape/consultas")
def scrape_consultas(background_tasks: BackgroundTasks, admin = Depends(get_current_admin)):
    background_tasks.add_task(_run_consultas_scrapers)
    return {"message": "Scraping de Consultas Públicas iniciado en background."}


# ─── Health check ──────────────────────────────────────────────────────────────
@app.get("/api/health")
def health():
    return {"status": "ok"}

# ─── BACKGROUND SCHEDULER MONITOR ─────────────────────────────────────────────
running_scrapers = set()

async def scheduler_monitor():
    """Tarea que monitorea el scheduler.json y ejecuta tareas programadas."""
    last_checked_minute = ""
    while True:
        try:
            from pathlib import Path
            import json
            config_path = Path("data/scheduler.json")
            if config_path.exists():
                with open(config_path, "r") as f:
                    config = json.load(f)
                
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                
                # 1. Ejecuciones por HORARIO FIJO (Consultas y SNIFA)
                if current_time != last_checked_minute:
                    # Consultas Públicas
                    if current_time == config.get("consultas_time_1") or current_time == config.get("consultas_time_2"):
                        if "consultas" not in running_scrapers:
                            log.info(f"ALERTA: Iniciando scrapeo programado de Consultas Públicas a las {current_time}")
                            running_scrapers.add("consultas")
                            asyncio.create_task(run_with_lock("consultas", _run_consultas_scrapers()))
                    
                    # SNIFA
                    if current_time == config.get("snifa_time_1") or current_time == config.get("snifa_time_2"):
                        if "snifa" not in running_scrapers:
                            log.info(f"ALERTA: Iniciando scrapeo programado de SNIFA a las {current_time}")
                            running_scrapers.add("snifa")
                            asyncio.create_task(run_with_lock("snifa", _run_snifa_scrapers()))

                    # Hora de testeo
                    if current_time == config.get("test_time"):
                        log.info(f"Testeo ejecutado a las {current_time}")
                    
                    last_checked_minute = current_time

                # 2. Ejecuciones por INTERVALO (SEA, Noticias, Tribunales)
                hora_inicio = config.get("hora_inicio", "07:00")
                hora_fin = config.get("hora_fin", "19:00")
                
                if hora_inicio <= current_time <= hora_fin:
                    logs = db.get_scraper_logs()
                    
                    def should_run(fuente_name, interval_hours, task_id):
                        if not interval_hours or task_id in running_scrapers: 
                            return False
                        log_entry = next((l for l in logs if l['fuente'] == fuente_name), None)
                        if not log_entry: return True
                        
                        ultimo_intento = datetime.datetime.fromisoformat(log_entry['ultimo_intento'])
                        diff = now - ultimo_intento
                        return diff.total_seconds() >= int(interval_hours) * 3600

                    if should_run("Pertinencias SEA", config.get("pertinencias_interval"), "sea"):
                        log.info(f"Iniciando scrapeo programado de SEA por intervalo ({config.get('pertinencias_interval')}h)")
                        running_scrapers.add("sea")
                        asyncio.create_task(run_with_lock("sea", _run_sea_scrapers()))
                    
                    if should_run("Noticias", config.get("noticias_interval"), "news"):
                        log.info(f"Iniciando scrapeo programado de Noticias por intervalo ({config.get('noticias_interval')}h)")
                        running_scrapers.add("news")
                        asyncio.create_task(run_with_lock("news", _run_news_scrapers()))

                    if should_run("Tribunales Ambientales", config.get("tribunales_interval"), "tribunales"):
                        log.info(f"Iniciando scrapeo programado de Tribunales por intervalo ({config.get('tribunales_interval')}h)")
                        running_scrapers.add("tribunales")
                        asyncio.create_task(run_with_lock("tribunales", _run_tribunales_scrapers()))

        except Exception as e:
            log.error(f"Error en scheduler_monitor: {e}")
        
        # El usuario pidió ver cada 40 minutos (2400 segundos) para evitar spam
        await asyncio.sleep(2400)

async def run_with_lock(task_id, coro):
    try:
        await coro
    finally:
        if task_id in running_scrapers:
            running_scrapers.remove(task_id)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(scheduler_monitor())
    log.info("BioNews Backend Started. Scheduler monitor active.")
