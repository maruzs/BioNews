maru@maru:/opt/BioNews$ docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
bionews-auth-service bionews-auth-service "uvicorn src.service…" auth-service 46 seconds ago Restarting (1) 12 seconds ago
bionews-consultations-service bionews-consultations-service "uvicorn src.service…" consultations-service 46 seconds ago Restarting (1) 13 seconds ago
bionews-gateway nginx:alpine "/docker-entrypoint.…" api 48 seconds ago Up 39 seconds 80/tcp, 8000/tcp
bionews-legal-service bionews-legal-service "uvicorn src.service…" legal-service 46 seconds ago Restarting (1) 13 seconds ago
bionews-news-service bionews-news-service "uvicorn src.service…" news-service 46 seconds ago Restarting (1) 13 seconds ago
bionews-postgres postgres:15-alpine "docker-entrypoint.s…" postgres_db 48 seconds ago Up 45 seconds (healthy) 0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp
bionews-redis redis:7-alpine "docker-entrypoint.s…" redis_broker 48 seconds ago Up 45 seconds 0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp
bionews-scheduler bionews-scheduler "python scheduler.py" scheduler 46 seconds ago Up 39 seconds 8000/tcp
bionews-web bionews-web "/docker-entrypoint.…" web 46 seconds ago Up 45 seconds 80/tcp
