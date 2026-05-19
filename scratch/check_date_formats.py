import psycopg2

conn = psycopg2.connect(
    host="192.168.1.35",
    port=5432,
    dbname="bionews",
    user="bionews",
    password="changeme"
)

tables_dates = {
    'Tribunales': 'Fecha',
    'pertinencias': 'Fecha',
    'sea_proyectos_evaluados': 'fecha_presentacion',
    'minsal_vigentes': 'fecha_inicio',
    'mma_abiertas': 'fecha_inicio',
    'normativas': 'fecha',
    'noticias': 'fecha'
}

try:
    with conn.cursor() as cur:
        cur.execute("SET search_path TO scrapers, users, public;")
        for t, col in tables_dates.items():
            try:
                cur.execute(f'SELECT "{col}" FROM "{t}" WHERE "{col}" IS NOT NULL LIMIT 5')
                rows = cur.fetchall()
                print(f"Table: {t}, Column: {col}")
                print("  Sample values:", [r[0] for r in rows])
            except Exception as e:
                print(f"Table: {t}, Column: {col} -> Error: {e}")
                conn.rollback()
finally:
    conn.close()
