maru@maru:/opt/BioNews$ docker compose logs -f
bionews-scheduler | 2026-05-18 15:27:18 [INFO] BioNews Scheduler iniciado.
bionews-scheduler | 2026-05-18 15:27:18 [INFO] Configurando scheduler con parametros: {'snifa*time_1': '16:12', 'snifa_time_2': '14:00', 'pertinencias_interval': '1', 'noticias_interval': 1, 'tribunales_interval': 1, 'notification_interval': 3, 'hora_inicio': '07:00', 'hora_fin': '19:00', 'test_time': '10:34', 'consultas_time_2': '15:50', 'consultas_time_1': '08:31'}
bionews-postgres |
bionews-legal-service | INFO: Started server process [1]
bionews-postgres | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-legal-service | INFO: Waiting for application startup.
bionews-redis | 1:C 18 May 2026 19:27:12.043 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 18 May 2026 19:27:12.043 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 18 May 2026 19:27:12.043 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 18 May 2026 19:27:12.043 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 18 May 2026 19:27:12.044 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 18 May 2026 19:27:12.044 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 18 May 2026 19:27:12.046 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 18 May 2026 19:27:12.046 \_ Server initialized
bionews-redis | 1:M 18 May 2026 19:27:12.046 * Ready to accept connections tcp
bionews-consultations-service | INFO: Started server process [1]
bionews-consultations-service | INFO: Waiting for application startup.
bionews-news-service | INFO: Started server process [1]
bionews-auth-service | INFO: Started server process [1]
bionews-auth-service | INFO: Waiting for application startup.
bionews-auth-service | 2026-05-18 19:27:19,598 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-news-service | INFO: Waiting for application startup.
bionews-news-service | 2026-05-18 19:27:19,572 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-news-service | INFO: Application startup complete.
bionews-postgres |
bionews-postgres | 2026-05-18 19:27:12.051 UTC [1] LOG: starting PostgreSQL 15.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-postgres | 2026-05-18 19:27:12.051 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-postgres | 2026-05-18 19:27:12.051 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-postgres | 2026-05-18 19:27:12.057 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-postgres | 2026-05-18 19:27:12.065 UTC [29] LOG: database system was shut down at 2026-05-18 19:23:17 UTC
bionews-postgres | 2026-05-18 19:27:12.074 UTC [1] LOG: database system is ready to accept connections
bionews-legal-service | 2026-05-18 19:27:19,579 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-legal-service | INFO: Application startup complete.
bionews-legal-service | INFO: Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit)
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-news-service | INFO: Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: using the "epoll" event method
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: nginx/1.31.0
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker processes
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 21
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 22
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: nginx/1.31.0
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker processes
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 29
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 30
bionews-auth-service | INFO: Application startup complete.
bionews-auth-service | INFO: Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 31
bionews-auth-service | 2026-05-18 19:27:19,600 [INFO] Suscrito a canal Redis: bionews_events
bionews-consultations-service | 2026-05-18 19:27:19,620 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-consultations-service | INFO: Application startup complete.
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 23
bionews-consultations-service | INFO: Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 24
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 32
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 33
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 34
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 35
bionews-web | 2026/05/18 19:27:12 [notice] 1#1: start worker process 36
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 25
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 26
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 27
bionews-gateway | 2026/05/18 19:27:12 [notice] 1#1: start worker process 28
bionews-gateway | 2026/05/18 19:27:24 [error] 21#21: *1 open() "/etc/nginx/html/stub_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /stub_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:27:24 +0000] "GET /stub_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:27:24 [error] 22#22: *2 open() "/etc/nginx/html/basic_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /basic_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:27:24 +0000] "GET /basic_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:27:24 [error] 23#23: *3 open() "/etc/nginx/html/nginx_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /nginx_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:27:24 +0000] "GET /nginx_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:27:24 [error] 24#24: \*4 open() "/etc/nginx/html/status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:27:24 +0000] "GET /status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"

# AQUI ES CUANDO REINICIE LA PAGINA PARA LOGEARME

bionews-web | 172.20.0.2 - - [18/May/2026:19:27:53 +0000] "GET /login HTTP/1.1" 304 0 "http://192.168.1.35:81/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"

# Logre logearme pero no tengo absolutamente nada en las tablas

bionews-auth-service | INFO: 172.18.0.2:40122 - "POST /api/auth/login HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:32 +0000] "POST /api/auth/login HTTP/1.1" 200 343 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:32 +0000] "POST /api/auth/login HTTP/1.1" 200 343 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:32 [error] 26#26: *8 open() "/etc/nginx/html/api/notifications/status" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/status HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:32 +0000] "GET /api/notifications/status HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:32 +0000] "GET /api/notifications/status HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:32 [error] 27#27: *9 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:32 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:32 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:32 [error] 28#28: *10 open() "/etc/nginx/html/api/logs" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/logs HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:32 +0000] "GET /api/logs HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:32 +0000] "GET /api/logs HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.2:40128 - "GET /api/auth/me HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:32 +0000] "GET /api/auth/me HTTP/1.1" 200 100 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:32 +0000] "GET /api/auth/me HTTP/1.1" 200 100 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:33 [error] 21#21: *14 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:33 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:33 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:33 [error] 21#21: *15 open() "/etc/nginx/html/api/notifications/status" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/status HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:33 +0000] "GET /api/notifications/status HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:33 +0000] "GET /api/notifications/status HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:37 [error] 21#21: *16 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:37 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:37 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:38 [error] 21#21: *17 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:38 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:38 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-news-service | INFO: 172.18.0.2:44464 - "GET /api/news HTTP/1.1" 500 Internal Server Error
bionews-news-service | ERROR: Exception in ASGI application
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-news-service | result = await app( # type: ignore[func-returns-value]
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-news-service | return await self.app(scope, receive, send)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-news-service | await super().**call**(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-news-service | await self.middleware_stack(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-news-service | raise exc
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-news-service | await self.app(scope, receive, \_send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-news-service | await self.app(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-news-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-news-service | raise exc
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-news-service | await app(scope, receive, sender)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-news-service | await self.app(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-news-service | await self.middleware_stack(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-news-service | await route.handle(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-news-service | await self.app(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-news-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-news-service | raise exc
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-news-service | await app(scope, receive, sender)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-news-service | response = await f(request)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-news-service | raw_response = await run_endpoint_function(
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-news-service | return await run_in_threadpool(dependant.call, \*\*values)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-news-service | return await anyio.to_thread.run_sync(func)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-news-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-news-service | return await future
bionews-news-service | ^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-news-service | result = context.run(func, *args)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/app/src/services/news/main.py", line 345, in get_news
bionews-news-service | news_dicts = [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news_rows]
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/app/src/services/news/main.py", line 345, in <listcomp>
bionews-news-service | news_dicts = [{"link": n[0], "titulo": n[1], "fecha": n[2], "imagen": n[3], "fuente": n[4], "fecha_scraping": n[5]} for n in news_rows]
bionews-news-service | ~^^^
bionews-news-service | KeyError: 0
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:40 +0000] "GET /api/news HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:40 +0000] "GET /api/news HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:28:43 [error] 21#21: *20 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:43 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:43 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:43 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:28:43 [error] 21#21: *21 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:43 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/noticias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.2:54936 - "GET /api/favorites HTTP/1.1" 500 Internal Server Error
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
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:44 +0000] "GET /api/favorites HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:44 +0000] "GET /api/favorites HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
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
bionews-auth-service | File "/app/src/services/auth/main.py", line 596, in get_favorites
bionews-auth-service | favs = db.get_favorites(user_id=user["sub"], fuente=fuente)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | AttributeError: 'DatabaseManager' object has no attribute 'get_favorites'
bionews-gateway | 2026/05/18 19:28:44 [error] 21#21: *24 open() "/etc/nginx/html/api/notifications/status/normativas" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/status/normativas HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:44 +0000] "GET /api/notifications/status/normativas HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:44 +0000] "GET /api/notifications/status/normativas HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:44 [error] 21#21: \*25 open() "/etc/nginx/html/api/notifications/exit" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "POST /api/notifications/exit HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:44 +0000] "POST /api/notifications/exit HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:44 +0000] "POST /api/notifications/exit HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.2:54950 - "GET /api/favorites HTTP/1.1" 500 Internal Server Error
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:46 +0000] "GET /api/favorites HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:46 +0000] "GET /api/favorites HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
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
bionews-auth-service | File "/app/src/services/auth/main.py", line 596, in get_favorites
bionews-auth-service | favs = db.get_favorites(user_id=user["sub"], fuente=fuente)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | AttributeError: 'DatabaseManager' object has no attribute 'get_favorites'
bionews-gateway | 2026/05/18 19:28:46 [error] 21#21: *28 open() "/etc/nginx/html/api/notifications/status/pertinencias" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/status/pertinencias HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:46 +0000] "GET /api/notifications/status/pertinencias HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:46 +0000] "GET /api/notifications/status/pertinencias HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:46 [error] 21#21: *29 open() "/etc/nginx/html/api/notifications/exit" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "POST /api/notifications/exit HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:46 +0000] "POST /api/notifications/exit HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:46 +0000] "POST /api/notifications/exit HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:48 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:48 [error] 21#21: *30 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:48 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:28:48 [error] 21#21: *31 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:48 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:48 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:53 [error] 22#22: *32 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:53 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:53 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:54 [error] 22#22: *33 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:54 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:54 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:59 [error] 22#22: *34 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:59 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:59 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 2026/05/18 19:28:59 [error] 22#22: \*35 open() "/etc/nginx/html/api/notifications/stream" failed (2: No such file or directory), client: 172.18.0.5, server: , request: "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:28:59 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:28:59 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDUxMn0.2Nus4ei0O7ajeDqJiDShG2sEsDGOOxl7dMbwLgfi_BM HTTP/1.1" 404 555 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"

# En el panel de admin si logro ver los usuarios logeados, pero en ninguna pestana (normativas, pertinencias, noticias, etc.) se muestra informacion, por ejemplo cuando le di click a pertinencias:

bionews-web | 172.20.0.2 - - [18/May/2026:19:29:44 +0000] "GET /api/favorites HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/pertinencias" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
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
bionews-auth-service | return await run_in_threadpool(dependant.call, \**values)
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
bionews-auth-service | File "/app/src/services/auth/main.py", line 596, in get_favorites
bionews-auth-service | favs = db.get_favorites(user_id=user["sub"], fuente=fuente)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | AttributeError: 'DatabaseManager' object has no attribute 'get_favorites'
