import re

with open('server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. ThreadPoolExecutor for /api/search
search_code = '''from concurrent.futures import ThreadPoolExecutor

@app.get("/api/search")
def global_search(q: str = "", user = Depends(get_current_user)):
    """Búsqueda global concurrente en todas las bases de datos."""
    if not q or len(q.strip()) < 2:
        return {"results": {}, "total": 0}
    
    q = q.strip()
    results = {}
    LIMIT_PER_TABLE = 50
    
    search_config = [
        ("bionews_legal_db", "fiscalizaciones", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "sancionatorios", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "registroSanciones", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "programasDeCumplimiento", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "medidas_provisionales", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "requerimientos", ["expediente", "nombre_razon_social", "unidad_fiscalizable"], "unidad_fiscalizable", "expediente", "detalle_link"),
        ("bionews_legal_db", "normativas", ["normativa", "organismo", "suborganismo"], "normativa", "accion", "accion"),
        ("bionews_news_db", "noticias", ["titulo", "fuente"], "titulo", "link", "link"),
        ("bionews_legal_db", "Tribunales", ["Rol", "Caratula"], "Caratula", "Rol", "Accion"),
        ("bionews_legal_db", "pertinencias", ["Expediente", "Nombre_de_Proyecto", "Proponente", "tipo_proyecto", "categoria_economica"], "Nombre_de_Proyecto", "Expediente", "Accion"),
        ("bionews_legal_db", "sea_proyectos_evaluados", ["nombre", "titular", "via_ingreso", "estado_proyecto", "tipo_proyecto", "categoria_economica"], "nombre", "id", "url"),
    ]
    
    def search_table(conf):
        db_name, table, fields, title_field, id_field, action_field = conf
        try:
            with db.get_connection(db_name) as conn:
                from psycopg2.extras import RealDictCursor
                cursor = conn.cursor(cursor_factory=RealDictCursor)
                where_clauses = " OR ".join([f'"{f}" ILIKE %s' for f in fields])
                params = [f'%{q}%'] * len(fields)
                cursor.execute(f'SELECT * FROM "{table}" WHERE {where_clauses} LIMIT {LIMIT_PER_TABLE}', params)
                rows = cursor.fetchall()
                
                table_results = []
                for d in rows:
                    table_results.append({
                        "id": str(d.get(id_field, "")),
                        "titulo": str(d.get(title_field, ""))[:120],
                        "accion": d.get(action_field, ""),
                        "extra": d.get("expediente") or d.get("Expediente") or d.get("fecha") or d.get("Fecha") or "",
                        "_raw": dict(d)
                    })
                return table, table_results
        except Exception as e:
            return table, []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(search_table, conf) for conf in search_config]
        for future in futures:
            table, table_results = future.result()
            if table_results:
                results[table] = table_results

    total = sum(len(r) for r in results.values())
    return {"results": results, "total": total, "query": q}'''

content = re.sub(r'@app\.get\("/api/search"\)\ndef global_search.*?return \{"results": results, "total": total, "query": q\}', search_code, content, flags=re.DOTALL)

# 2. Fix delete_latest_record
delete_code = '''@app.delete("/api/admin/debug/delete-latest/{category}")
def delete_latest_record(category: str, admin = Depends(get_current_admin)):
    """Endpoint de depuración para borrar el registro más reciente basado en fecha o ID serial."""
    table_mapping = {
        "mma_abiertas": ("mma_abiertas", "bionews_consultations_db"),
        "mma_cerradas": ("mma_cerradas", "bionews_consultations_db"),
        "minsal_vigentes": ("minsal_vigentes", "bionews_consultations_db"),
        "sea_evaluados": ("sea_proyectos_evaluados", "bionews_legal_db"),
        "pertinencias": ("pertinencias", "bionews_legal_db"),
        "fiscalizaciones": ("fiscalizaciones", "bionews_legal_db"),
        "sancionatorios": ("sancionatorios", "bionews_legal_db"),
        "sanciones": ("registroSanciones", "bionews_legal_db"),
        "programas": ("programasDeCumplimiento", "bionews_legal_db"),
        "medidas": ("medidas_provisionales", "bionews_legal_db"),
        "requerimientos": ("requerimientos", "bionews_legal_db"),
        "tribunal_1": ("Tribunales", "bionews_legal_db"),
        "tribunal_2": ("Tribunales", "bionews_legal_db"),
        "tribunal_3": ("Tribunales", "bionews_legal_db")
    }
    
    if category not in table_mapping:
        raise HTTPException(status_code=400, detail="Categoría inválida")
        
    table, db_name = table_mapping[category]
    
    with db.get_connection(db_name) as conn:
        cursor = conn.cursor()
        try:
            if category.startswith("tribunal_"):
                trib_id = category.split("_")[1]
                trib_names = {"1": "Primer Tribunal", "2": "Segundo Tribunal", "3": "Tercer Tribunal"}
                trib_name = trib_names.get(trib_id)
                # PostgreSQL doesn't have rowid. Use ctid or id if there's a primary key.
                # In our schema Tribunales uses Rol as PK, but there's no serial ID? Wait, fecha_scraping can be used
                cursor.execute("""
                    DELETE FROM Tribunales 
                    WHERE ctid IN (
                        SELECT ctid FROM Tribunales 
                        WHERE Tribunal = %s 
                        ORDER BY fecha_scraping DESC LIMIT 1
                    )
                """, (trib_name,))
                deleted = cursor.rowcount
            
            elif category in ["mma_abiertas", "mma_cerradas"]:
                cursor.execute(f"""
                    DELETE FROM {table} 
                    WHERE ctid IN (
                        SELECT ctid FROM {table} 
                        ORDER BY fecha_scraping DESC LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "minsal_vigentes":
                cursor.execute(f"""
                    DELETE FROM {table} 
                    WHERE ctid IN (
                        SELECT ctid FROM {table} 
                        ORDER BY fecha_scraping DESC LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "sea_evaluados":
                cursor.execute(f"""
                    DELETE FROM {table} 
                    WHERE ctid IN (
                        SELECT ctid FROM {table} 
                        ORDER BY fecha_scraping DESC LIMIT 1
                    )
                """)
                deleted = cursor.rowcount
                
            elif category == "pertinencias":
                cursor.execute(f"""
                    DELETE FROM {table} 
                    WHERE ctid IN (
                        SELECT ctid FROM {table} 
                        ORDER BY fecha_scraping DESC LIMIT 1
                    )
                """)
                deleted = cursor.rowcount

            elif category in ["fiscalizaciones", "sancionatorios", "sanciones", "programas", "medidas", "requerimientos"]:
                cursor.execute(f"DELETE FROM {table} WHERE ficha_id = (SELECT MAX(ficha_id) FROM {table})")
                deleted = cursor.rowcount
            else:
                cursor.execute(f"DELETE FROM {table} WHERE ctid IN (SELECT ctid FROM {table} ORDER BY fecha_scraping DESC LIMIT 1)")
                deleted = cursor.rowcount
            
            conn.commit()
            return {"status": "ok", "deleted": deleted, "table": table}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))'''

content = re.sub(r'@app\.delete\("/api/admin/debug/delete-latest/\{category\}"\)\ndef delete_latest_record.*?raise HTTPException\(status_code=500, detail=str\(e\)\)', delete_code, content, flags=re.DOTALL)

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("server.py updated for Phase 3")
