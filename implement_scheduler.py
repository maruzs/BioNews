import re

with open('scheduler.py', 'r', encoding='utf-8') as f:
    sched_content = f.read()

redis_import = '''import json
import os
import redis
from datetime import datetime, time as dtime

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

CATEGORY_MAP = {
    "Primer Tribunal Ambiental": "Tribunales",
    "Segundo Tribunal Ambiental": "Tribunales",
    "Tercer Tribunal Ambiental": "Tribunales",
    "Diario Oficial (Normativas)": "normativas",
    "Pertinencias SEA": "pertinencias",
    "SNIFA Sancionatorios": "sancionatorios",
    "SNIFA Fiscalizaciones": "fiscalizaciones",
    "SNIFA Requerimientos": "requerimientos",
    "SNIFA Medidas Provisionales": "medidas_provisionales",
    "SNIFA Programas de Cumplimiento": "programasDeCumplimiento",
    "SNIFA Registro Sanciones": "registroSanciones",
    "MINSAL Consultas": "minsal_vigentes",
    "MMA Consultas": "mma",
    "DGA Consultas": "dga",
}

def publish_event(category_slug):
    try:
        if not category_slug: return
        msg = {
            "type": "new_ingestion",
            "category": category_slug,
            "timestamp": datetime.now().isoformat()
        }
        redis_client.publish("bionews_events", json.dumps(msg))
        if category_slug == "minsal_vigentes":
            msg["category"] = "minsal_resultados"
            redis_client.publish("bionews_events", json.dumps(msg))
    except Exception as e:
        log.error(f"Error publishing to Redis: {e}")
'''

sched_content = re.sub(r'import json\nfrom datetime import datetime, time as dtime', redis_import, sched_content)

# Update ejecutar_scrapers
new_ejecutar = '''def ejecutar_scrapers(scrapers_list, msg_inicio):
    log.info("=" * 40)
    log.info(msg_inicio + "SCHEDULED")
    log.info("=" * 40)
    for nombre, ScraperClass in scrapers_list:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            nuevos = scraper.run()
            log.info(f"  ✓ {nombre}: {nuevos} nuevos registros guardados.")
            if nuevos > 0:
                cat = CATEGORY_MAP.get(nombre)
                if cat:
                    publish_event(cat)
        except Exception:
            log.error(f"  ✗ Error en {nombre}:\\n{traceback.format_exc()}")'''

sched_content = re.sub(r'def ejecutar_scrapers.*?log\.error\(f"  ✗ Error en \{nombre\}:\\n\{traceback\.format_exc\(\)\}"\)', new_ejecutar, sched_content, flags=re.DOTALL)

# Update ejecutar_noticias
new_noticias = '''def ejecutar_noticias(scrapers_list, msg_inicio):
    log.info("=" * 40)
    log.info(msg_inicio)
    log.info("=" * 40)
    db = get_db()
    if not db: return
    for nombre, ScraperClass in scrapers_list:
        log.info(f"  ▶ Procesando: {nombre}...")
        try:
            scraper = ScraperClass()
            items = scraper.get_latest_news()
            if items:
                nuevas = db.save_news(items)
                log.info(f"  ✓ {nombre}: {nuevas} nuevas noticias guardadas.")
                if nuevas > 0:
                    publish_event("noticias")
            else:
                log.info(f"  – {nombre}: sin noticias nuevas.")
        except Exception:
            log.error(f"  ✗ Error en {nombre}:\\n{traceback.format_exc()}")'''

sched_content = re.sub(r'def ejecutar_noticias.*?log\.error\(f"  ✗ Error en \{nombre\}:\\n\{traceback\.format_exc\(\)\}"\)', new_noticias, sched_content, flags=re.DOTALL)

with open('scheduler.py', 'w', encoding='utf-8') as f:
    f.write(sched_content)
print("Updated scheduler.py")
