import re

with open('src/services/auth/main.py', 'r', encoding='utf-8') as f:
    auth_content = f.read()

# 1. Add redis to the imports
auth_content = auth_content.replace('import asyncio', 'import asyncio\nimport redis.asyncio as redis\nimport os')

# 2. Redis Pub/Sub integration
redis_code = '''
# ─── REDIS PUB/SUB ───────────────────────────────────────────────────────────
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

async def redis_listener():
    """Escucha eventos de ingestión en Redis."""
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("bionews_events")
    log.info("Suscrito a canal Redis: bionews_events")
    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                data = json.loads(message["data"])
                if data.get("type") == "new_ingestion":
                    category = data.get("category")
                    timestamp = data.get("timestamp")
                    log.info(f"Nuevo evento de ingestión: {category} a las {timestamp}")
                    
                    # 1. Actualizar tabla global
                    db.update_category_last_update(category, timestamp)
                    
                    # 2. Transmitir vía SSE
                    await sse_manager.broadcast({
                        "type": "new_content",
                        "category": category,
                        "timestamp": timestamp
                    })
    except Exception as e:
        log.error(f"Error en redis_listener: {e}")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(redis_listener())

# ─── SSE NOTIFICATION MANAGER ───────────────────────────────────────────────
'''
auth_content = re.sub(r'# ─── SSE NOTIFICATION MANAGER ───────────────────────────────────────────────', redis_code, auth_content)

# 3. Modify /api/notifications/status
# Since we separated services, we need to update the status to use our fast check method
status_code = '''@app.get("/api/notifications/status/{category}")
def get_notification_status_single(category: str, user = Depends(get_current_user)):
    """Verifica si una categoría específica tiene ítems nuevos usando la lógica veloz."""
    has_new = db.check_category_has_new(user["sub"], category)
    return {"has_new": has_new, "category": category}'''

auth_content = re.sub(r'@app\.get\("/api/notifications/status/\{category\}"\)\ndef get_notification_status_single.*?return \{"has_new": has_new, "category": category\}', status_code, auth_content, flags=re.DOTALL)

with open('src/services/auth/main.py', 'w', encoding='utf-8') as f:
    f.write(auth_content)
print("Updated auth/main.py with Redis Pub/Sub")
