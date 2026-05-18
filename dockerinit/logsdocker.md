(.venv) maru@maru:/opt/BioNews$ docker compose logs -f
bionews-legal-service | INFO: Started server process [1]
bionews-legal-service | INFO: Waiting for application startup.
bionews-legal-service | 2026-05-18 19:56:13,849 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-legal-service | INFO: Application startup complete.
bionews-legal-service | INFO: Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit)
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-postgres |
bionews-postgres | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-postgres |
bionews-postgres | 2026-05-18 19:56:06.107 UTC [1] LOG: starting PostgreSQL 15.18 on x86*64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-postgres | 2026-05-18 19:56:06.107 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-postgres | 2026-05-18 19:56:06.107 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-postgres | 2026-05-18 19:56:06.112 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-postgres | 2026-05-18 19:56:06.119 UTC [29] LOG: database system was shut down at 2026-05-18 19:55:28 UTC
bionews-postgres | 2026-05-18 19:56:06.128 UTC [1] LOG: database system is ready to accept connections
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: using the "epoll" event method
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: nginx/1.31.0
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker processes
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 21
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 22
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 23
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 24
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 25
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 26
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 27
bionews-gateway | 2026/05/18 19:56:06 [notice] 1#1: start worker process 28
bionews-gateway | 2026/05/18 19:56:09 [error] 21#21: \_1 bionews-auth-service could not be resolved (2: Server failure), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/tribunales"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:56:09 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/tribunales" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:56:14 +0000] "POST /api/notifications/exit HTTP/1.1" 200 16 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-news-service | INFO: Started server process [1]
bionews-news-service | INFO: Waiting for application startup.
bionews-news-service | 2026-05-18 19:56:13,790 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-news-service | INFO: Application startup complete.
bionews-news-service | INFO: Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
bionews-consultations-service | INFO: Started server process [1]
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: nginx/1.31.0
bionews-auth-service | INFO: Started server process [1]
bionews-auth-service | INFO: Waiting for application startup.
bionews-auth-service | 2026-05-18 19:56:13,930 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-redis | 1:C 18 May 2026 19:56:06.086 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 18 May 2026 19:56:06.086 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 18 May 2026 19:56:06.086 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 18 May 2026 19:56:06.086 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 18 May 2026 19:56:06.087 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 18 May 2026 19:56:06.087 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 18 May 2026 19:56:06.088 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 18 May 2026 19:56:06.088 _ Server initialized
bionews-redis | 1:M 18 May 2026 19:56:06.088 _ Ready to accept connections tcp
bionews-auth-service | INFO: Application startup complete.
bionews-auth-service | INFO: Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
bionews-auth-service | 2026-05-18 19:56:13,932 [INFO] Suscrito a canal Redis: bionews_events
bionews-auth-service | 2026-05-18 19:56:14,468 [INFO] POST /api/notifications/exit: User 4 saliendo de Tribunales
bionews-auth-service | INFO: 172.18.0.2:39926 - "POST /api/notifications/exit HTTP/1.1" 200 OK
bionews-auth-service | INFO: 172.18.0.2:39928 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 OK
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-consultations-service | INFO: Waiting for application startup.
bionews-consultations-service | 2026-05-18 19:56:13,871 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-consultations-service | INFO: Application startup complete.
bionews-scheduler | 2026-05-18 15:56:12 [INFO] BioNews Scheduler iniciado.
bionews-scheduler | 2026-05-18 15:56:12 [INFO] Configurando scheduler con parametros: {'snifa_time_1': '16:12', 'snifa_time_2': '14:00', 'pertinencias_interval': '1', 'noticias_interval': 1, 'tribunales_interval': 1, 'notification_interval': 3, 'hora_inicio': '07:00', 'hora_fin': '19:00', 'test_time': '10:34', 'consultas_time_2': '15:50', 'consultas_time_1': '08:31'}
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker processes
bionews-consultations-service | INFO: Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 29
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 30
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 31
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 32
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 33
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 34
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 35
bionews-web | 2026/05/18 19:56:06 [notice] 1#1: start worker process 36
bionews-web | 172.20.0.2 - - [18/May/2026:19:56:09 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/tribunales" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:56:14 +0000] "POST /api/notifications/exit HTTP/1.1" 200 16 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"

# LOS DE ARRIBA SON LOS LOGS ANTES DE QUE INICE SESION, AQUI ABAJO ES LO QUE VA SALIENDO CUANDO VOY PROBANDO COSAS

bionews-web | 172.20.0.2 - - [18/May/2026:19:56:14 +0000] "POST /api/notifications/exit HTTP/1.1" 200 16 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.2:38152 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:24 +0000] "POST /api/auth/login HTTP/1.1" 401 36 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:24 +0000] "POST /api/auth/login HTTP/1.1" 401 36 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.2:38160 - "POST /api/auth/login HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:32 +0000] "POST /api/auth/login HTTP/1.1" 200 343 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:32 +0000] "POST /api/auth/login HTTP/1.1" 200 343 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:32 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 499 0 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:32 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 68 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | INFO: 172.18.0.2:60994 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNjI1Mn0.n5mcDobjlFjdJ0G_8c9xgLmtBlxDhlmdsU_dDSueEJs HTTP/1.1" 200 OK
bionews-auth-service | INFO: 172.18.0.2:32770 - "GET /api/auth/me HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:32 +0000] "GET /api/auth/me HTTP/1.1" 200 100 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:32 +0000] "GET /api/auth/me HTTP/1.1" 200 100 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-postgres | 2026-05-18 19:57:32.883 UTC [117] ERROR: operator does not exist: text > timestamp without time zone at character 49
bionews-postgres | 2026-05-18 19:57:32.883 UTC [117] HINT: No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-postgres | 2026-05-18 19:57:32.883 UTC [117] STATEMENT: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-18T19:36:51'::timestamp AND "accion" NOT IN ('http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/02/2806276.pdf', 'http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/07/2805674.pdf') LIMIT 1
bionews-auth-service | INFO: 172.18.0.2:32768 - "GET /api/notifications/status HTTP/1.1" 500 Internal Server Error
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:32 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:32 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-auth-service | response = await f(request)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-auth-service | raw_response = await run_endpoint_function(
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-auth-service | return await run_in_threadpool(dependant.call, **values)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-auth-service | return await anyio.to_thread.run_sync(func)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-auth-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-auth-service | return await future
bionews-auth-service | ^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-auth-service | result = context.run(func, *args)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 632, in get_notification_status
bionews-auth-service | return db.get_notification_status(user["sub"])
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/database/manager.py", line 446, in get_notification_status
bionews-auth-service | has_new = self.\_check_if_category_has_new(user_id, cat)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/database/manager.py", line 513, in \_check_if_category_has_new
bionews-auth-service | cursor.execute(f'SELECT 1 FROM "{t_lower}" WHERE {date_col} > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1', (last_exit, *viewed_ids))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedFunction: operator does not exist: text > timestamp without time zone
bionews-auth-service | LINE 1: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-1...
bionews-auth-service | ^
bionews-auth-service | HINT: No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-auth-service |
bionews-gateway | 2026/05/18 19:57:33 [error] 21#21: \*24 open() "/etc/nginx/html/api/logs" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/logs HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:33 +0000] "GET /api/logs HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:33 +0000] "GET /api/logs HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:33 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNjI1Mn0.n5mcDobjlFjdJ0G_8c9xgLmtBlxDhlmdsU_dDSueEJs HTTP/1.1" 499 0 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:33 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNjI1Mn0.n5mcDobjlFjdJ0G_8c9xgLmtBlxDhlmdsU_dDSueEJs HTTP/1.1" 200 29 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | INFO: 172.18.0.2:32780 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNjI1Mn0.n5mcDobjlFjdJ0G_8c9xgLmtBlxDhlmdsU_dDSueEJs HTTP/1.1" 200 OK
bionews-postgres | 2026-05-18 19:57:33.483 UTC [123] ERROR: operator does not exist: text > timestamp without time zone at character 49
bionews-postgres | 2026-05-18 19:57:33.483 UTC [123] HINT: No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-postgres | 2026-05-18 19:57:33.483 UTC [123] STATEMENT: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-18T19:36:51'::timestamp AND "accion" NOT IN ('http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/02/2806276.pdf', 'http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/07/2805674.pdf') LIMIT 1
bionews-auth-service | INFO: 172.18.0.2:32788 - "GET /api/notifications/status HTTP/1.1" 500 Internal Server Error
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:57:33 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:57:33 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-auth-service | response = await f(request)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-auth-service | raw_response = await run_endpoint_function(
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-auth-service | return await run_in_threadpool(dependant.call, **values)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-auth-service | return await anyio.to_thread.run_sync(func)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-auth-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-auth-service | return await future
bionews-auth-service | ^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-auth-service | result = context.run(func, *args)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 632, in get_notification_status
bionews-auth-service | return db.get_notification_status(user["sub"])
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/database/manager.py", line 446, in get_notification_status
bionews-auth-service | has_new = self.\_check_if_category_has_new(user_id, cat)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/database/manager.py", line 513, in \_check_if_category_has_new
bionews-auth-service | cursor.execute(f'SELECT 1 FROM "{t_lower}" WHERE {date_col} > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1', (last_exit, *viewed_ids))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedFunction: operator does not exist: text > timestamp without time zone
bionews-auth-service | LINE 1: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-1...
bionews-auth-service | ^
bionews-auth-service | HINT: No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-auth-service |

# ESO DE ARRIBA FUE APENAS ME LOGEE (me equivoque en mi clave la primera vez si), ESTO DE ABAJO SON LAS PRUEBAS QUE HE IDO HACIENDO

## TODO ESTABA BIEN ASI QUE FUI A PROBAR LOS SCRAPERS EN EL PANEL DE ADMIN

### PARA EL SEA

bionews-gateway | 172.18.0.5 - - [18/May/2026:20:00:39 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:00:39 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-auth-service | Token CAS encontrado. Iniciando sesion...
bionews-auth-service | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-auth-service | 3. Consultando API para el rango: 2026-05-18 a 2026-05-18
bionews-auth-service | Ocurrio un error general: Object of type date is not JSON serializable
bionews-auth-service | 5. Cerrando sesion...
bionews-postgres | 2026-05-18 20:00:42.575 UTC [318] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:00:42.575 UTC [318] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Pertinencias SEA'
bionews-postgres | 2026-05-18 20:00:42.599 UTC [319] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:00:42.599 UTC [319] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Pertinencias SEA'
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 928, in \_run_sea_scrapers
bionews-auth-service | db.log_scraper_run("Pertinencias SEA", exito=True, nuevos=nuevos_pert)
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Pertin...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service |
bionews-auth-service | During handling of the above exception, another exception occurred:
bionews-auth-service |
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 96, in **call**
bionews-auth-service | await self.simple_response(scope, receive, send, request_headers=headers)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 154, in simple_response
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 121, in app
bionews-auth-service | await response(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/responses.py", line 170, in **call**
bionews-auth-service | await self.background()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 36, in **call**
bionews-auth-service | await task()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 21, in **call**
bionews-auth-service | await self.func(\*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 932, in \_run_sea_scrapers
bionews-auth-service | db.log_scraper_run("Pertinencias SEA", exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Pertin...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service | INFO: 172.18.0.2:32796 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNjI1Mn0.n5mcDobjlFjdJ0G_8c9xgLmtBlxDhlmdsU_dDSueEJs HTTP/1.1" 200 OK

### NOTICIAS

bionews-auth-service | INFO: 172.18.0.2:33154 - "POST /api/scrape/news HTTP/1.1" 200 OK
bionews-auth-service | 2026-05-18 20:01:40,486 [INFO] --- SCRAPING NOTICIAS MANUAL ---
bionews-auth-service | 2026-05-18 20:01:40,486 [INFO] Procesando: Tercer Tribunal (Noticias)...
bionews-auth-service | Iniciando scraping en Tercer Tribunal Ambiental
bionews-auth-service | Consultando pagina 1 del Tercer Tribunal...
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:01:40 +0000] "POST /api/scrape/news HTTP/1.1" 200 58 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:01:40 +0000] "POST /api/scrape/news HTTP/1.1" 200 58 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | Consultando pagina 2 del Tercer Tribunal...
bionews-auth-service | Consultando pagina 3 del Tercer Tribunal...
bionews-auth-service | Consultando pagina 4 del Tercer Tribunal...
bionews-auth-service | Consultando pagina 5 del Tercer Tribunal...
bionews-auth-service | Exito: Se encontraron 50 noticias en el Tercer Tribunal Ambiental
bionews-postgres | 2026-05-18 20:01:51.993 UTC [375] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:01:51.993 UTC [375] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Tercer Tribunal (Noticias)'
bionews-postgres | 2026-05-18 20:01:52.001 UTC [376] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:01:52.001 UTC [376] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Tercer Tribunal (Noticias)'
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 906, in \_run_news_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=True, nuevos=nuevas)
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Tercer...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service |
bionews-auth-service | During handling of the above exception, another exception occurred:
bionews-auth-service |
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 96, in **call**
bionews-auth-service | await self.simple_response(scope, receive, send, request_headers=headers)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 154, in simple_response
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 121, in app
bionews-auth-service | await response(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/responses.py", line 170, in **call**
bionews-auth-service | await self.background()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 36, in **call**
bionews-auth-service | await task()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 21, in **call**
bionews-auth-service | await self.func(\*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 914, in \_run_news_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Tercer...
bionews-auth-service | ^
bionews-auth-service |

### SNIFA

bionews-auth-service | INFO: 172.18.0.2:46712 - "POST /api/scrape/snifa HTTP/1.1" 200 OK
bionews-auth-service | 2026-05-18 20:02:25,934 [INFO] MANUAL
bionews-auth-service | Iniciando scraper de Procedimientos Sancionatorios...
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:02:25 +0000] "POST /api/scrape/snifa HTTP/1.1" 200 55 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:02:25 +0000] "POST /api/scrape/snifa HTTP/1.1" 200 55 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | Registros actuales en BD: 3354
bionews-auth-service | Registros en la web: 0
bionews-auth-service | No hay registros nuevos. La BD esta actualizada.
bionews-postgres | 2026-05-18 20:02:26.244 UTC [409] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:02:26.244 UTC [409] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'SNIFA Sancionatorios'
bionews-postgres | 2026-05-18 20:02:26.252 UTC [410] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:02:26.252 UTC [410] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'SNIFA Sancionatorios'
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 1009, in \_run_snifa_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'SNIFA ...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service |
bionews-auth-service | During handling of the above exception, another exception occurred:
bionews-auth-service |
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 96, in **call**
bionews-auth-service | await self.simple_response(scope, receive, send, request_headers=headers)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 154, in simple_response
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 121, in app
bionews-auth-service | await response(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/responses.py", line 170, in **call**
bionews-auth-service | await self.background()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 36, in **call**
bionews-auth-service | await task()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 21, in **call**
bionews-auth-service | await self.func(\*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 1015, in \_run_snifa_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'SNIFA ...
bionews-auth-service | ^
bionews-auth-service |

### NORMATIVAS

bionews-auth-service | INFO: 172.18.0.2:35294 - "POST /api/scrape/normativas HTTP/1.1" 200 OK
bionews-web | 172.20.0.2 - - [18/May/2026:20:02:49 +0000] "POST /api/scrape/normativas HTTP/1.1" 200 60 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | Iniciando extraccion para 1 dia(s)...
bionews-auth-service | Buscando informacion para la fecha: 18-05-2026
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:02:49 +0000] "POST /api/scrape/normativas HTTP/1.1" 200 60 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-postgres | 2026-05-18 20:02:49.653 UTC [427] ERROR: syntax error at or near "PRAGMA" at character 1
bionews-postgres | 2026-05-18 20:02:49.653 UTC [427] STATEMENT: PRAGMA table_info(normativas)
bionews-postgres | 2026-05-18 20:02:51.656 UTC [427] ERROR: duplicate key value violates unique constraint "normativas_pkey"
bionews-postgres | 2026-05-18 20:02:51.656 UTC [427] DETAIL: Key (accion)=(https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/18/44452/01/2809092.pdf) already exists.
bionews-postgres | 2026-05-18 20:02:51.656 UTC [427] STATEMENT:
bionews-postgres | INSERT INTO normativas (fecha, normativa, tipo_normativa, organismo, suborganismo, accion, fecha_scraping, ficha_id)
bionews-postgres | VALUES ('2026-05-18', 'Resolución exenta número 319, de 2026.- Establece sujetos pasivos que señala, conforme a la ley Nº 20.730, que regula el lobby y las gestiones que representen intereses particulares ante las autoridades y funcionarios, y deja sin efecto resolución Nº 579 exenta, de 2025', 'Normas Generales', 'MINISTERIO DE HACIENDA', NULL, 'https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/18/44452/01/2809092.pdf', '2026-05-18 20:02:51', 2809092)
bionews-postgres |
bionews-auth-service | Error procesando seccion Normas Generales para la fecha 18-05-2026: duplicate key value violates unique constraint "normativas_pkey"
bionews-auth-service | DETAIL: Key (accion)=(https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/18/44452/01/2809092.pdf) already exists.
bionews-auth-service |
bionews-auth-service | Error procesando seccion Normas Particulares para la fecha 18-05-2026: current transaction is aborted, commands ignored until end of transaction block
bionews-auth-service |
bionews-postgres | 2026-05-18 20:02:52.404 UTC [427] ERROR: current transaction is aborted, commands ignored until end of transaction block
bionews-postgres | 2026-05-18 20:02:52.404 UTC [427] STATEMENT:
bionews-postgres | INSERT INTO normativas (fecha, normativa, tipo_normativa, organismo, suborganismo, accion, fecha_scraping, ficha_id)
bionews-postgres | VALUES ('2026-05-18', 'Resolución exenta número 34, de 2026.- Rechaza recursos de reposición interpuestos en contra de la resolución N° 9 exenta, de 2026', 'Normas Particulares', 'MINISTERIO DE ENERGÍA', NULL, 'http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/18/44452/02/2810014.pdf', '2026-05-18 20:02:52', 2810014)
bionews-postgres |
bionews-postgres | 2026-05-18 20:02:53.171 UTC [427] ERROR: current transaction is aborted, commands ignored until end of transaction block
bionews-postgres | 2026-05-18 20:02:53.171 UTC [427] STATEMENT:
bionews-postgres | INSERT INTO normativas (fecha, normativa, tipo_normativa, organismo, suborganismo, accion, fecha_scraping, ficha_id)
bionews-postgres | VALUES ('2026-05-18', 'VAR 13 / Vargas Díaz Rafael Alejandro', 'Boletin Oficial Mineria', 'REGIÓN DE TARAPACÁ', 'Provincia del Tamarugal', 'http://www.diariooficial.interior.gob.cl/publicaciones/2026/05/18/44452/07/2810526.pdf', '2026-05-18 20:02:53', 2810526)
bionews-postgres |
bionews-auth-service | Error procesando seccion Boletin Oficial Mineria para la fecha 18-05-2026: current transaction is aborted, commands ignored until end of transaction block
bionews-auth-service |
bionews-auth-service | El proceso de extraccion ha finalizado. 0 registros nuevos.
bionews-postgres | 2026-05-18 20:02:53.185 UTC [428] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:02:53.185 UTC [428] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Diario Oficial (Normativas)'
bionews-postgres | 2026-05-18 20:02:53.192 UTC [429] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:02:53.192 UTC [429] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Diario Oficial (Normativas)'
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 1027, in \_run_normativas_scrapers
bionews-auth-service | db.log_scraper_run("Diario Oficial (Normativas)", exito=True, nuevos=nuevos)
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Diario...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service |
bionews-auth-service | During handling of the above exception, another exception occurred:
bionews-auth-service |
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 96, in **call**
bionews-auth-service | await self.simple_response(scope, receive, send, request_headers=headers)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 154, in simple_response
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 121, in app
bionews-auth-service | await response(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/responses.py", line 170, in **call**
bionews-auth-service | await self.background()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 36, in **call**
bionews-auth-service | await task()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 21, in **call**
bionews-auth-service | await self.func(\*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 1031, in \_run_normativas_scrapers
bionews-auth-service | db.log_scraper_run("Diario Oficial (Normativas)", exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Diario...
bionews-auth-service | ^
bionews-auth-service |

### TRIBUNALES

bionews-auth-service | INFO: 172.18.0.2:51914 - "POST /api/scrape/tribunales HTTP/1.1" 200 OK
bionews-auth-service | 2026-05-18 20:03:18,230 [INFO] --- SCRAPING TRIBUNALES MANUAL ---
bionews-auth-service | 2026-05-18 20:03:18,234 [INFO] Procesando Primer Tribunal...
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:03:18 +0000] "POST /api/scrape/tribunales HTTP/1.1" 200 46 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:03:18 +0000] "POST /api/scrape/tribunales HTTP/1.1" 200 46 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | Ultima fecha registrada en BD: 15-05-2026
bionews-auth-service | Buscando causas del ano 2026 en el Primer Tribunal...
bionews-auth-service | Actualizacion completada. Se revisaron/guardaron 1 registros.
bionews-postgres | 2026-05-18 20:03:18.905 UTC [456] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:03:18.905 UTC [456] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Primer Tribunal'
bionews-postgres | 2026-05-18 20:03:18.915 UTC [457] ERROR: relation "scraper_logs" does not exist at character 26
bionews-postgres | 2026-05-18 20:03:18.915 UTC [457] STATEMENT: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Primer Tribunal'
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 858, in \_run_tribunales_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=True, nuevos=nuevos)
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Primer...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service |
bionews-auth-service | During handling of the above exception, another exception occurred:
bionews-auth-service |
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-auth-service | result = await app( # type: ignore[func-returns-value]
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-auth-service | return await self.app(scope, receive, send)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-auth-service | await super().**call**(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-auth-service | await self.app(scope, receive, \_send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 96, in **call**
bionews-auth-service | await self.simple_response(scope, receive, send, request_headers=headers)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 154, in simple_response
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-auth-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-auth-service | await self.middleware_stack(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-auth-service | await route.handle(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-auth-service | await self.app(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-auth-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-auth-service | raise exc
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-auth-service | await app(scope, receive, sender)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 121, in app
bionews-auth-service | await response(scope, receive, send)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/responses.py", line 170, in **call**
bionews-auth-service | await self.background()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 36, in **call**
bionews-auth-service | await task()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/background.py", line 21, in **call**
bionews-auth-service | await self.func(\*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 863, in \_run_tribunales_scrapers
bionews-auth-service | db.log_scraper_run(nombre, exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 239, in log_scraper_run
bionews-auth-service | cursor.execute("SELECT ultimo_exito FROM scraper_logs WHERE fuente = %s", (fuente,))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "scraper_logs" does not exist
bionews-auth-service | LINE 1: SELECT ultimo_exito FROM scraper_logs WHERE fuente = 'Primer...
bionews-auth-service | ^
bionews-auth-service |
