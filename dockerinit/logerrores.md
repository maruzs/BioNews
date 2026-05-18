maru@maru:/opt/BioNews$ docker compose logs -f
bionews-redis | 1:C 18 May 2026 19:14:48.995 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit*memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 18 May 2026 19:14:48.995 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 18 May 2026 19:14:48.995 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 18 May 2026 19:14:48.995 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 18 May 2026 19:14:48.996 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 18 May 2026 19:14:48.996 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 18 May 2026 19:14:48.997 _ Running mode=standalone, port=6379.
bionews-legal-service | INFO: Started server process [1]
bionews-redis | 1:M 18 May 2026 19:14:48.997 \_ Server initialized
bionews-redis | 1:M 18 May 2026 19:14:48.998 \* Ready to accept connections tcp
bionews-legal-service | INFO: Waiting for application startup.
bionews-legal-service | 2026-05-18 19:14:56,569 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-legal-service | INFO: Application startup complete.
bionews-legal-service | INFO: Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit)
bionews-consultations-service | INFO: Started server process [1]
bionews-consultations-service | INFO: Waiting for application startup.
bionews-consultations-service | 2026-05-18 19:14:56,578 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-consultations-service | INFO: Application startup complete.
bionews-consultations-service | INFO: Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)
bionews-news-service | INFO: Started server process [1]
bionews-news-service | INFO: Waiting for application startup.
bionews-news-service | 2026-05-18 19:14:56,569 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-news-service | INFO: Application startup complete.
bionews-news-service | INFO: Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
bionews-auth-service | INFO: Started server process [1]
bionews-auth-service | INFO: Waiting for application startup.
bionews-auth-service | 2026-05-18 19:14:56,578 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-auth-service | INFO: Application startup complete.
bionews-auth-service | INFO: Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
bionews-auth-service | 2026-05-18 19:14:56,581 [INFO] Suscrito a canal Redis: bionews_events
bionews-scheduler | 2026-05-18 15:14:55 [INFO] BioNews Scheduler iniciado.
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-scheduler | 2026-05-18 15:14:55 [INFO] Configurando scheduler con parametros: {'snifa_time_1': '16:12', 'snifa_time_2': '14:00', 'pertinencias_interval': '1', 'noticias_interval': 1, 'tribunales_interval': 1, 'notification_interval': 3, 'hora_inicio': '07:00', 'hora_fin': '19:00', 'test_time': '10:34', 'consultas_time_2': '15:50', 'consultas_time_1': '08:31'}
bionews-scheduler | 2026-05-18 15:15:25 [INFO] ========================================
bionews-scheduler | 2026-05-18 15:15:25 [INFO] SCRAPING NOTICIAS
bionews-scheduler | 2026-05-18 15:15:25 [INFO] ========================================
bionews-scheduler | Iniciando scraping en Tercer Tribunal Ambiental
bionews-scheduler | Consultando pagina 1 del Tercer Tribunal...
bionews-scheduler | 2026-05-18 15:15:26 [INFO] ▶ Procesando: Tercer Tribunal...
bionews-scheduler | Consultando pagina 2 del Tercer Tribunal...
bionews-scheduler | Consultando pagina 3 del Tercer Tribunal...
bionews-scheduler | Consultando pagina 4 del Tercer Tribunal...
bionews-scheduler | Consultando pagina 5 del Tercer Tribunal...
bionews-scheduler | Exito: Se encontraron 50 noticias en el Tercer Tribunal Ambiental
bionews-gateway | 2026/05/18 19:14:49 [emerg] 1#1: host not found in upstream "bionews-auth-service" in /etc/nginx/conf.d/default.conf:5
bionews-postgres |
bionews-gateway | nginx: [emerg] host not found in upstream "bionews-auth-service" in /etc/nginx/conf.d/default.conf:5
bionews-postgres | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-postgres |
bionews-postgres | 2026-05-18 19:14:49.101 UTC [1] LOG: starting PostgreSQL 15.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-postgres | 2026-05-18 19:14:49.101 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-postgres | 2026-05-18 19:14:49.101 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-postgres | 2026-05-18 19:14:49.105 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-postgres | 2026-05-18 19:14:49.111 UTC [30] LOG: database system was shut down at 2026-05-18 19:14:33 UTC
bionews-postgres | 2026-05-18 19:14:49.120 UTC [1] LOG: database system is ready to accept connections
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: using the "epoll" event method
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: nginx/1.31.0
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-scheduler | 2026-05-18 15:15:34 [INFO] ✓ Tercer Tribunal: 0 nuevas noticias guardadas.
bionews-scheduler | 2026-05-18 15:15:34 [INFO] ▶ Procesando: Corte Suprema...
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker processes
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 21
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 22
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 23
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 24
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 25
bionews-scheduler | Iniciando scraping en Corte Suprema: https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial
bionews-scheduler | Aplicando filtros de busqueda...
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 26
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 27
bionews-scheduler | Exito: Se encontraron 1 noticias medioambientales en la Corte Suprema
bionews-scheduler | 2026-05-18 15:15:46 [INFO] ✓ Corte Suprema: 0 nuevas noticias guardadas.
bionews-scheduler | 2026-05-18 15:15:46 [INFO] ▶ Procesando: SMA...
bionews-scheduler | Iniciando scraping en SMA (Pagina 1): https://portal.sma.gob.cl/index.php/sala-de-prensa/
bionews-scheduler | Iniciando scraping en SMA (Pagina 2): https://portal.sma.gob.cl/index.php/sala-de-prensa/page/2/
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | 2026/05/18 19:14:54 [notice] 1#1: start worker process 28
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: nginx/1.31.0
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker processes
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 29
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 30
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 31
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 32
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 33
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 34
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 35
bionews-web | 2026/05/18 19:14:49 [notice] 1#1: start worker process 36
bionews-scheduler | Iniciando scraping en SMA (Pagina 3): https://portal.sma.gob.cl/index.php/sala-de-prensa/page/3/
bionews-scheduler | Exito: Se encontraron 30 noticias en la SMA
bionews-scheduler | 2026-05-18 15:15:54 [INFO] ✓ SMA: 0 nuevas noticias guardadas.
bionews-scheduler | Iniciando scraping en MMA (Pagina 1): https://mma.gob.cl/noticias/
bionews-scheduler | 2026-05-18 15:15:54 [INFO] ▶ Procesando: MMA...

# AQUI FUI AL LOGIN A INTENTAR INGRESAR

bionews-web | 172.20.0.2 - - [18/May/2026:19:16:15 +0000] "GET /login HTTP/1.1" 304 0 "http://192.168.1.35:81/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-scheduler | Iniciando scraping en SEA (Pagina 2): https://www.sea.gob.cl/noticias?page=2
bionews-scheduler | Se encontraron 27 noticias en SEA
bionews-scheduler | Iniciando scraping en Sernageomin (Pagina 1): https://www.sernageomin.cl/category/noticias/
bionews-scheduler | 2026-05-18 15:16:17 [INFO] ✓ SEA: 0 nuevas noticias guardadas.
bionews-scheduler | 2026-05-18 15:16:17 [INFO] ▶ Procesando: Sernageomin...
bionews-scheduler | Iniciando scraping en Sernageomin (Pagina 2): https://www.sernageomin.cl/category/noticias/page/2/
bionews-scheduler | Iniciando scraping en Sernageomin (Pagina 3): https://www.sernageomin.cl/category/noticias/page/3/
bionews-scheduler | Se encontraron 30 noticias en Sernageomin
bionews-scheduler | 2026-05-18 15:16:27 [INFO] ✓ Sernageomin: 1 nuevas noticias guardadas.
bionews-auth-service | 2026-05-18 19:16:27,048 [INFO] Nuevo evento de ingestión: noticias a las 2026-05-18T15:16:27.045047
bionews-scheduler | Iniciando scraping en Segundo Tribunal: https://tribunalambiental.cl/resumen-de-noticias/
bionews-scheduler | 2026-05-18 15:16:27 [INFO] ▶ Procesando: Segundo Tribunal...
bionews-auth-service | INFO: 172.18.0.4:57058 - "POST /api/auth/login HTTP/1.1" 500 Internal Server Error
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:16:27 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:16:27 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
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
bionews-auth-service | File "/app/src/services/auth/main.py", line 197, in login
bionews-auth-service | if not user or not verify_password(req.password, user['password_hash']):
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 151, in verify_password
bionews-auth-service | return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | ValueError: Invalid salt
bionews-scheduler | Se encontraron 6 noticias en Segundo Tribunal
bionews-scheduler | 2026-05-18 15:16:33 [INFO] ✓ Segundo Tribunal: 1 nuevas noticias guardadas.
bionews-auth-service | 2026-05-18 19:16:33,626 [INFO] Nuevo evento de ingestión: noticias a las 2026-05-18T15:16:33.625914
