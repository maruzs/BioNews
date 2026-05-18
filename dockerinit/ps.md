maru@maru:/opt/BioNews$ docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
bionews-auth-service bionews-auth-service "uvicorn src.service…" auth-service 19 seconds ago Up 13 seconds 8000/tcp
bionews-consultations-service bionews-consultations-service "uvicorn src.service…" consultations-service 19 seconds ago Up 13 seconds 8000/tcp
bionews-gateway nginx:alpine "/docker-entrypoint.…" api 20 seconds ago Up 18 seconds 80/tcp, 8000/tcp
bionews-legal-service bionews-legal-service "uvicorn src.service…" legal-service 19 seconds ago Up 13 seconds 8000/tcp
bionews-news-service bionews-news-service "uvicorn src.service…" news-service 19 seconds ago Up 13 seconds 8000/tcp
bionews-postgres postgres:15-alpine "docker-entrypoint.s…" postgres_db 20 seconds ago Up 18 seconds (healthy) 0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp
bionews-redis redis:7-alpine "docker-entrypoint.s…" redis_broker 20 seconds ago Up 18 seconds 0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp
bionews-scheduler bionews-scheduler "python scheduler.py" scheduler 19 seconds ago Up 13 seconds 8000/tcp
bionews-web bionews-web "/docker-entrypoint.…" web 19 seconds ago Up 18 seconds 80/tcp

maru@maru:/opt/BioNews$ docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
9434380345d2 bionews-news-service "uvicorn src.service…" 26 seconds ago Up 20 seconds 8000/tcp bionews-news-service
0d0750dcded8 bionews-auth-service "uvicorn src.service…" 26 seconds ago Up 20 seconds 8000/tcp bionews-auth-service
e23e910954c0 bionews-legal-service "uvicorn src.service…" 26 seconds ago Up 20 seconds 8000/tcp bionews-legal-service
0fb3c9cd2211 bionews-consultations-service "uvicorn src.service…" 26 seconds ago Up 20 seconds 8000/tcp bionews-consultations-service
19fb2a6e2c26 bionews-scheduler "python scheduler.py" 26 seconds ago Up 20 seconds 8000/tcp bionews-scheduler
9820895c9f3e bionews-web "/docker-entrypoint.…" 26 seconds ago Up 25 seconds 80/tcp bionews-web
0e0561c4f054 postgres:15-alpine "docker-entrypoint.s…" 27 seconds ago Up 26 seconds (healthy) 0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp bionews-postgres
0e87d212e459 nginx:alpine "/docker-entrypoint.…" 27 seconds ago Up 26 seconds 80/tcp, 8000/tcp bionews-gateway
c5f5da2c07f5 redis:7-alpine "docker-entrypoint.s…" 27 seconds ago Up 26 seconds 0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp bionews-redis
8ecbb58704b1 netdata/netdata:latest "/usr/sbin/run.sh" 3 days ago Up 3 days (healthy) 0.0.0.0:19999->19999/tcp, [::]:19999->19999/tcp netdata
540fd5be59a6 amir20/dozzle:latest "/dozzle" 3 days ago Up 3 days 0.0.0.0:8888->8080/tcp, [::]:8888->8080/tcp dozzle
ecf8acc7f60e jc21/nginx-proxy-manager:latest "/init" 3 days ago Up 3 days 0.0.0.0:80-81->80-81/tcp, [::]:80-81->80-81/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp nginx-proxy-app-1
