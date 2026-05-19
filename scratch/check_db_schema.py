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
        # Get all columns for all tables in scrapers/users schemas
        cur.execute("""
            SELECT table_schema, table_name, column_name, data_type 
            FROM information_schema.columns 
            WHERE table_schema IN ('scrapers', 'users')
            ORDER BY table_name, ordinal_position;
        """)
        cols = cur.fetchall()
        
        tables = {}
        for schema, table, col, dtype in cols:
            if table not in tables:
                tables[table] = []
            tables[table].append((col, dtype))
            
        for t, columns in sorted(tables.items()):
            print(f"Table: {t}")
            date_cols = [c for c in columns if 'fecha' in c[0].lower() or 'date' in c[0].lower() or c[0] == 'Fecha']
            print(f"  All date-like columns: {date_cols}")
finally:
    conn.close()
