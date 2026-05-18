import sys
import os
import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="bionews",
        user="bionews",
        password="changeme",
        options="-c client_encoding=UTF8 -c search_path=scrapers,users,public"
    )
    print("Connected successfully using password 'changeme'!")
    with conn.cursor() as cur:
        cur.execute("SELECT fecha_presentacion FROM sea_proyectos_evaluados LIMIT 15;")
        rows = cur.fetchall()
        print("Sample dates from database:")
        for r in rows:
            print(r)
    conn.close()
except Exception as e:
    print(f"Failed with 'changeme': {e}")
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            dbname="bionews",
            user="bionews",
            password="CambiameBionews2026!",
            options="-c client_encoding=UTF8 -c search_path=scrapers,users,public"
        )
        print("Connected successfully using password 'CambiameBionews2026!'!")
        with conn.cursor() as cur:
            cur.execute("SELECT fecha_presentacion FROM sea_proyectos_evaluados LIMIT 15;")
            rows = cur.fetchall()
            print("Sample dates from database:")
            for r in rows:
                print(r)
        conn.close()
    except Exception as e2:
        print(f"Failed with 'CambiameBionews2026!': {e2}")
