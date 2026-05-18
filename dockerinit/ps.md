maru@maru:/opt/BioNews$ docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
bionews-auth-service bionews-auth-service "uvicorn src.service…" auth-service 20 seconds ago Up 13 seconds 8000/tcp
bionews-consultations-service bionews-consultations-service "uvicorn src.service…" consultations-service 20 seconds ago Up 13 seconds 8000/tcp
bionews-gateway nginx:alpine "/docker-entrypoint.…" api 20 seconds ago Up 13 seconds 80/tcp, 8000/tcp
bionews-legal-service bionews-legal-service "uvicorn src.service…" legal-service 20 seconds ago Up 13 seconds 8000/tcp
bionews-news-service bionews-news-service "uvicorn src.service…" news-service 20 seconds ago Up 13 seconds 8000/tcp
bionews-postgres postgres:15-alpine "docker-entrypoint.s…" postgres_db 20 seconds ago Up 19 seconds (healthy) 0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp
bionews-redis redis:7-alpine "docker-entrypoint.s…" redis_broker 20 seconds ago Up 19 seconds 0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp
bionews-scheduler bionews-scheduler "python scheduler.py" scheduler 20 seconds ago Up 13 seconds 8000/tcp
bionews-web bionews-web "/docker-entrypoint.…" web 20 seconds ago Up 19 seconds 80/tcp
