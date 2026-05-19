import os
import psycopg2
from pathlib import Path

# Try passwords
passwords = ["CambiameBionews2026!", "changeme", "#81680085pls"]

# Try to find user from .env
user = "bionews"
env_path = Path(".") / ".env"
if env_path.exists():
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                if key.strip() == "DB_USER":
                    user = val.strip()
                elif key.strip() == "DB_PASS":
                    passwords.insert(0, val.strip())

working_pass = None
for p in list(set(passwords)):
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            dbname="bionews",
            user=user,
            password=p
        )
        conn.close()
        working_pass = p
        print(f"SUCCESS with password: {p}")
        break
    except Exception as e:
        print(f"Failed with password {p}: {e}")

if working_pass:
    # Set it in os.environ for manager
    os.environ["DB_HOST"] = "127.0.0.1"
    os.environ["DB_PORT"] = "5432"
    os.environ["DB_NAME"] = "bionews"
    os.environ["DB_USER"] = user
    os.environ["DB_PASS"] = working_pass

    from src.database.manager import DatabaseManager
    db = DatabaseManager()
    tables = [
        'fiscalizaciones', 'medidas_provisionales', 'normativas',
        'pertinencias', 'programasDeCumplimiento', 'registroSanciones',
        'requerimientos', 'sancionatorios', 'Tribunales', 'noticias',
        'minsal_vigentes', 'minsal_resultados', 'mma_abiertas', 'mma_cerradas',
        'dga_consultas', 'sea_proyectos_evaluados'
    ]
    print("\nTable Counts:")
    for t in tables:
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(f'SELECT COUNT(*) FROM "{t}"')
                    count = cur.fetchone()[0]
                    print(f"  {t}: {count}")
        except Exception as e:
            print(f"  {t}: Error: {e}")
else:
    print("Could not connect with any password.")
