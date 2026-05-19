import os
import psycopg2

passwords = ["CambiameBionews2026!", "changeme", "#81680085pls", "Memr2026.", "postgres"]
users = ["bionews", "postgres"]

for u in users:
    for p in passwords:
        try:
            conn = psycopg2.connect(
                host="192.168.1.35",
                port=5432,
                dbname="postgres" if u == "postgres" else "bionews",
                user=u,
                password=p,
                connect_timeout=3
            )
            print(f"SUCCESS CONNECTING: user={u}, password={p}")
            with conn.cursor() as cur:
                cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema IN ('scrapers', 'users')")
                tables = cur.fetchall()
                print("Tables:", [t[0] for t in tables])
            conn.close()
            break
        except Exception as e:
            print(f"FAILED user={u}, password={p}: {e}")
