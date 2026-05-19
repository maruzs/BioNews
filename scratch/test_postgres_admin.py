import psycopg2

passwords = ["postgres", "admin", "changeme", "CambiameBionews2026!", "#81680085pls", ""]
users = ["postgres", "bionews"]

print("Trying connections with errors:")
for u in users:
    for p in passwords:
        try:
            conn = psycopg2.connect(
                host="127.0.0.1",
                port=5432,
                dbname="postgres" if u == "postgres" else "bionews",
                user=u,
                password=p,
                connect_timeout=3
            )
            print(f"SUCCESS: user={u}, password={p}")
            conn.close()
        except Exception as e:
            print(f"FAILED: user={u}, password={p} -> {type(e).__name__}: {e}")
