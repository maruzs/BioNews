aru@maru:/opt/BioNews$ docker compose logs -f
bionews-auth-service | INFO: Started server process [1]
bionews-auth-service | INFO: Waiting for application startup.
bionews-auth-service | 2026-05-18 19:19:51,019 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-auth-service | INFO: Application startup complete.
bionews-auth-service | INFO: Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
bionews-auth-service | 2026-05-18 19:19:51,023 [INFO] Suscrito a canal Redis: bionews_events
bionews-scheduler | 2026-05-18 15:19:50 [INFO] BioNews Scheduler iniciado.
bionews-consultations-service | INFO: Started server process [1]
bionews-consultations-service | INFO: Waiting for application startup.
bionews-news-service | INFO: Started server process [1]
bionews-news-service | INFO: Waiting for application startup.
bionews-news-service | 2026-05-18 19:19:51,165 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-news-service | INFO: Application startup complete.
bionews-news-service | INFO: Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
bionews-consultations-service | 2026-05-18 19:19:51,030 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-consultations-service | INFO: Application startup complete.
bionews-consultations-service | INFO: Uvicorn running on http://0.0.0.0:8004 (Press CTRL+C to quit)
bionews-scheduler | 2026-05-18 15:19:50 [INFO] Configurando scheduler con parametros: {'snifa_time_1': '16:12', 'snifa_time_2': '14:00', 'pertinencias_interval': '1', 'noticias_interval': 1, 'tribunales_interval': 1, 'notification_interval': 3, 'hora_inicio': '07:00', 'hora_fin': '19:00', 'test_time': '10:34', 'consultas_time_2': '15:50', 'consultas_time_1': '08:31'}
bionews-scheduler | 2026-05-18 15:20:20 [INFO] ========================================
bionews-scheduler | 2026-05-18 15:20:20 [INFO] SCRAPING TRIBUNALESSCHEDULED
bionews-scheduler | 2026-05-18 15:20:20 [INFO] ========================================
bionews-scheduler | 2026-05-18 15:20:20 [INFO] ▶ Procesando: Primer Tribunal Ambiental...
bionews-scheduler | 2026-05-18 15:20:20 [ERROR] ✗ Error en Primer Tribunal Ambiental:
bionews-scheduler | Traceback (most recent call last):
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-scheduler | File "/app/src/scrapers/primerTribunal.py", line 20, in obtener_ultima_fecha
bionews-scheduler | cursor.execute("SELECT Fecha FROM Tribunales WHERE Tribunal = 'Primer Tribunal'")
bionews-scheduler | psycopg2.errors.UndefinedTable: relation "tribunales" does not exist
bionews-scheduler | LINE 1: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Primer Tribun...
bionews-scheduler | ^
bionews-scheduler |
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-scheduler |
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/src/scrapers/primerTribunal.py", line 152, in run
bionews-scheduler | ultima_fecha = obtener_ultima_fecha(conn)
bionews-scheduler | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/primerTribunal.py", line 44, in obtener_ultima_fecha
bionews-scheduler | except sqlite3.OperationalError:
bionews-scheduler | ^^^^^^^
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-scheduler |
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/scheduler.py", line 122, in ejecutar_scrapers
bionews-scheduler | nuevos = scraper.run()
bionews-scheduler | ^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/primerTribunal.py", line 169, in run
bionews-scheduler | except sqlite3.Error as e:
bionews-scheduler | ^^^^^^^
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |
bionews-scheduler | 2026-05-18 15:20:20 [INFO] ▶ Procesando: Segundo Tribunal Ambiental...
bionews-scheduler | 2026-05-18 15:20:20 [ERROR] ✗ Error en Segundo Tribunal Ambiental:
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/src/scrapers/segundoTribunal.py", line 19, in obtener_ultima_fecha
bionews-scheduler | cursor.execute("SELECT Fecha FROM Tribunales WHERE Tribunal = 'Segundo Tribunal'")
bionews-scheduler | psycopg2.errors.UndefinedTable: relation "tribunales" does not exist
bionews-scheduler | LINE 1: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Segundo Tribu...
bionews-scheduler | ^
bionews-scheduler |
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-legal-service | INFO: Started server process [1]
bionews-legal-service | INFO: Waiting for application startup.
bionews-legal-service | 2026-05-18 19:19:51,059 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-legal-service | INFO: Application startup complete.
bionews-legal-service | INFO: Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit)
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-postgres |
bionews-postgres | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-postgres |
bionews-postgres | 2026-05-18 19:19:43.649 UTC [1] LOG: starting PostgreSQL 15.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-postgres | 2026-05-18 19:19:43.649 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: using the "epoll" event method
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: nginx/1.31.0
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-scheduler |
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker processes
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 22
bionews-postgres | 2026-05-18 19:19:43.649 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-postgres | 2026-05-18 19:19:43.656 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-redis | 1:C 18 May 2026 19:19:43.525 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 18 May 2026 19:19:43.525 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 18 May 2026 19:19:43.525 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 18 May 2026 19:19:43.525 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 18 May 2026 19:19:43.526 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 18 May 2026 19:19:43.526 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 18 May 2026 19:19:43.527 _ Running mode=standalone, port=6379.
bionews-postgres | 2026-05-18 19:19:43.670 UTC [29] LOG: database system was shut down at 2026-05-18 19:19:19 UTC
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: nginx/1.31.0
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/src/scrapers/segundoTribunal.py", line 183, in run
bionews-scheduler | ultima_fecha = obtener_ultima_fecha(conn)
bionews-scheduler | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/segundoTribunal.py", line 43, in obtener_ultima_fecha
bionews-scheduler | except sqlite3.OperationalError:
bionews-scheduler | ^^^^^^^
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-scheduler |
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker processes
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 29
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 30
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 31
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 32
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 33
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 34
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 35
bionews-web | 2026/05/18 19:19:43 [notice] 1#1: start worker process 36
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 23
bionews-redis | 1:M 18 May 2026 19:19:43.527 _ Server initialized
bionews-redis | 1:M 18 May 2026 19:19:43.527 * Ready to accept connections tcp
bionews-postgres | 2026-05-18 19:19:43.679 UTC [1] LOG: database system is ready to accept connections
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 24
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/scheduler.py", line 122, in ejecutar_scrapers
bionews-scheduler | nuevos = scraper.run()
bionews-scheduler | ^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/segundoTribunal.py", line 201, in run
bionews-scheduler | except sqlite3.Error as e:
bionews-scheduler | ^^^^^^^
bionews-postgres | 2026-05-18 19:20:20.377 UTC [68] ERROR: relation "tribunales" does not exist at character 19
bionews-postgres | 2026-05-18 19:20:20.377 UTC [68] STATEMENT: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Primer Tribunal'
bionews-postgres | 2026-05-18 19:20:20.386 UTC [69] ERROR: relation "tribunales" does not exist at character 19
bionews-postgres | 2026-05-18 19:20:20.386 UTC [69] STATEMENT: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Segundo Tribunal'
bionews-postgres | 2026-05-18 19:20:20.395 UTC [70] ERROR: relation "tribunales" does not exist at character 19
bionews-postgres | 2026-05-18 19:20:20.395 UTC [70] STATEMENT: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Tercer Tribunal'
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 25
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 26
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 27
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 28
bionews-gateway | 2026/05/18 19:19:43 [notice] 1#1: start worker process 29
bionews-gateway | 2026/05/18 19:20:17 [error] 22#22: *1 open() "/etc/nginx/html/stub_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /stub_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:20:17 +0000] "GET /stub_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:20:17 [error] 23#23: *2 open() "/etc/nginx/html/basic_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /basic_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:20:17 +0000] "GET /basic_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:20:17 [error] 24#24: *3 open() "/etc/nginx/html/nginx_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /nginx_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:20:17 +0000] "GET /nginx_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |
bionews-scheduler | 2026-05-18 15:20:20 [INFO] ▶ Procesando: Tercer Tribunal Ambiental...
bionews-scheduler | 2026-05-18 15:20:20 [ERROR] ✗ Error en Tercer Tribunal Ambiental:
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/src/scrapers/tercerTribunal.py", line 36, in obtener_ultima_fecha
bionews-scheduler | cursor.execute("SELECT Fecha FROM Tribunales WHERE Tribunal = 'Tercer Tribunal'")
bionews-scheduler | psycopg2.errors.UndefinedTable: relation "tribunales" does not exist
bionews-scheduler | LINE 1: SELECT Fecha FROM Tribunales WHERE Tribunal = 'Tercer Tribun...
bionews-scheduler | ^
bionews-gateway | 2026/05/18 19:20:17 [error] 25#25: \*4 open() "/etc/nginx/html/status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:20:17 +0000] "GET /status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-scheduler |
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-scheduler |
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/src/scrapers/tercerTribunal.py", line 181, in run
bionews-scheduler | ultima_fecha = obtener_ultima_fecha(conn)
bionews-scheduler | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/tercerTribunal.py", line 60, in obtener_ultima_fecha
bionews-scheduler | except sqlite3.OperationalError:
bionews-scheduler | ^^^^^^^
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |
bionews-scheduler | During handling of the above exception, another exception occurred:
bionews-scheduler |
bionews-scheduler | Traceback (most recent call last):
bionews-scheduler | File "/app/scheduler.py", line 122, in ejecutar_scrapers
bionews-scheduler | nuevos = scraper.run()
bionews-scheduler | ^^^^^^^^^^^^^
bionews-scheduler | File "/app/src/scrapers/tercerTribunal.py", line 191, in run
bionews-scheduler | except sqlite3.Error as e:
bionews-scheduler | ^^^^^^^
bionews-scheduler | NameError: name 'sqlite3' is not defined
bionews-scheduler |

# AQUI FUI AL LOGIN (y obtuve Unexpected token 'I', "Internal S"... is not valid JSON)

bionews-auth-service | INFO: 172.18.0.4:37540 - "POST /api/auth/login HTTP/1.1" 500 Internal Server Error
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
bionews-auth-service | result = context.run(func, \*args)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 197, in login
bionews-auth-service | if not user or not verify_password(req.password, user['password_hash']):
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 151, in verify_password
bionews-auth-service | return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | ValueError: Invalid salt
bionews-web | 172.20.0.2 - - [18/May/2026:19:20:49 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:20:49 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:20:53 +0000] "GET /login HTTP/1.1" 304 0 "http://192.168.1.35:81/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.4:32978 - "POST /api/auth/login HTTP/1.1" 500 Internal Server Error
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
bionews-auth-service | result = context.run(func, \*args)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 197, in login
bionews-auth-service | if not user or not verify_password(req.password, user['password_hash']):
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/services/auth/main.py", line 151, in verify_password
bionews-auth-service | return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | ValueError: Invalid salt
bionews-web | 172.20.0.2 - - [18/May/2026:19:21:00 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:21:00 +0000] "POST /api/auth/login HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
