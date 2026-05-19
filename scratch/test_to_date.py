import psycopg2

conn = psycopg2.connect(
    host="192.168.1.35",
    port=5432,
    dbname="bionews",
    user="bionews",
    password="changeme"
)

try:
    with conn.cursor() as cur:
        cur.execute("SET search_path TO scrapers, users, public;")
        
        # Test sea_proyectos_evaluados
        try:
            cur.execute("""
                SELECT fecha_presentacion, to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') as parsed_date 
                FROM sea_proyectos_evaluados 
                ORDER BY to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC NULLS LAST
                LIMIT 5
            """)
            print("sea_proyectos_evaluados sorting success:", cur.fetchall())
        except Exception as e:
            print("sea_proyectos_evaluados sorting failed:", e)
            conn.rollback()

        # Test mma_abiertas
        try:
            cur.execute("""
                SELECT fecha_inicio, to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY') as parsed_date 
                FROM mma_abiertas 
                ORDER BY to_date(nullif(fecha_inicio, ''), 'MM/DD/YYYY') DESC NULLS LAST
                LIMIT 5
            """)
            print("mma_abiertas sorting success:", cur.fetchall())
        except Exception as e:
            print("mma_abiertas sorting failed:", e)
            conn.rollback()
            
finally:
    conn.close()
