# ERROR EN SEA

bionews-auth-service | INFO: 172.18.0.3:50308 - "POST /api/scrape/sea HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:32:05 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:32:05 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-auth-service | Token CAS encontrado. Iniciando sesion...
bionews-auth-service | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-auth-service | 3. Consultando API para el rango: 2026-05-18 a 2026-05-18
bionews-auth-service | Ocurrio un error general: Object of type date is not JSON serializable
bionews-auth-service | 5. Cerrando sesion...
bionews-postgres | 2026-05-18 20:32:08.441 UTC [220] ERROR: relation "sea*proyectos_evaluados" does not exist at character 22
bionews-postgres | 2026-05-18 20:32:08.441 UTC [220] STATEMENT: SELECT COUNT(*) FROM sea*proyectos_evaluados
bionews-auth-service | Error verificando DB: relation "sea_proyectos_evaluados" does not exist
bionews-auth-service | LINE 1: SELECT COUNT(*) FROM sea_proyectos_evaluados
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service | Iniciando scraping SEA Proyectos Evaluados. Modo completo.
bionews-auth-service | Error en scraping SEA Proyectos Evaluados: relation "sea_proyectos_evaluados" does not exist
bionews-auth-service | LINE 1: SELECT 1 FROM sea_proyectos_evaluados WHERE id = '2168353780...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service | Scraping SEA Proyectos finalizado. Nuevos: 0
bionews-postgres | 2026-05-18 20:32:31.921 UTC [221] ERROR: relation "sea_proyectos_evaluados" does not exist at character 15
bionews-postgres | 2026-05-18 20:32:31.921 UTC [221] STATEMENT: SELECT 1 FROM sea_proyectos_evaluados WHERE id = '2168353780'

# Error en consultas:

bionews-auth-service | 2026-05-18 20:36:51,401 [INFO] Procesando MINSAL Consultas...
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:36:51 +0000] "POST /api/scrape/consultas HTTP/1.1" 200 69 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:36:51 +0000] "POST /api/scrape/consultas HTTP/1.1" 200 69 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | MINSAL: 37 consultas analizadas, 0 nuevas.
bionews-auth-service | 2026-05-18 20:36:52,250 [INFO] Procesando MMA Consultas...
bionews-auth-service | Scrapeando consultas MMA Abiertas...
bionews-auth-service | Detalle: https://consultasciudadanas.mma.gob.cl/portal/consulta/226
bionews-auth-service | Detalle: https://consultasciudadanas.mma.gob.cl/portal/consulta/227
bionews-auth-service | Detalle: https://consultasciudadanas.mma.gob.cl/portal/consulta/224
bionews-auth-service | Detalle: https://consultasciudadanas.mma.gob.cl/portal/consulta/221
bionews-auth-service | Scrapeando consultas MMA Cerradas...
bionews-auth-service | Pestaña: Planes
bionews-auth-service | Aviso: La pestaña Planes no cambió de clase, continuando...
bionews-auth-service | Encontrados 56 registros en Planes
bionews-auth-service | Pestaña: Normas
bionews-auth-service | Aviso: La pestaña Normas no cambió de clase, continuando...
bionews-auth-service | Encontrados 47 registros en Normas
bionews-auth-service | Pestaña: Otros
bionews-auth-service | Aviso: La pestaña Otros no cambió de clase, continuando...
bionews-auth-service | Encontrados 76 registros en Otros
bionews-auth-service | Pestaña: Especies
bionews-auth-service | Aviso: La pestaña Especies no cambió de clase, continuando...
bionews-auth-service | Encontrados 8 registros en Especies
bionews-auth-service | ERROR: Exception in ASGI application
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/app/src/services/auth/main.py", line 1081, in \_run_consultas_scrapers
bionews-auth-service | nuevos_mma = await asyncio.to_thread(scraper_inst.run)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/threads.py", line 25, in to_thread
bionews-auth-service | return await loop.run_in_executor(None, func_call)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/concurrent/futures/thread.py", line 58, in run
bionews-auth-service | result = self.fn(*self.args, \*\*self.kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/scrapers/mma_consultas.py", line 311, in run
bionews-auth-service | nuevos = self.save_results(abiertas, cerradas)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/scrapers/mma_consultas.py", line 246, in save_results
bionews-auth-service | conn = self.\_get_connection()
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/app/src/scrapers/mma_consultas.py", line 19, in \_get_connection
bionews-auth-service | return sqlite3.connect(DB_PATH)
bionews-auth-service | ^^^^^^^
bionews-auth-service | NameError: name 'sqlite3' is not defined
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
bionews-auth-service | await self.func(*self.args, \*\*self.kwargs)
bionews-auth-service | File "/app/src/services/auth/main.py", line 1086, in \_run_consultas_scrapers
bionews-auth-service | db.log_scraper_run("MMA Consultas", exito=False, error=str(e))
bionews-auth-service | File "/app/src/database/manager.py", line 242, in log_scraper_run
bionews-auth-service | ultimo_exito = ahora if exito else (row[0] if row else None)
bionews-auth-service | ~~~^^^
bionews-auth-service | KeyError: 0
bionews-web | 172.20.0.2 - - [18/May/2026:20:37:24 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNzAzNH0.0rh6AochPy9gu6wqLsTcogQOvJVq50K_kiKwt6ub6-I HTTP/1.1" 499 0 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:37:24 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNzAzNH0.0rh6AochPy9gu6wqLsTcogQOvJVq50K_kiKwt6ub6-I HTTP/1.1" 200 68 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | INFO: 172.18.0.3:44160 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNzAzNH0.0rh6AochPy9gu6wqLsTcogQOvJVq50K_kiKwt6ub6-I HTTP/1.1" 200 OK

# Nota

Para probar que realmente estuviera funcionando fui al panel de depuracionque tiene el administrador y borre la ultima pertinencia, aparentemente si se borro, pero al intentar descargar con el boton de admin no aparecio en los logs de docker compose logs -f que si se haya descargado, ademas no se por que dice algo de proyectos finalizados si JAMAS ha existido un apartado para eso, solo pertinencias y proyectos evaluados (SEA)

bionews-legal-service | INFO: 172.18.0.3:39572 - "DELETE /api/admin/debug/delete-latest/pertinencias HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:38:16 +0000] "DELETE /api/admin/debug/delete-latest/pertinencias HTTP/1.1" 200 50 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:38:16 +0000] "DELETE /api/admin/debug/delete-latest/pertinencias HTTP/1.1" 200 50 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.3:57646 - "POST /api/scrape/sea HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:20:38:23 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:20:38:23 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://prairie-nissan-commonly-arabia.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-auth-service | Token CAS encontrado. Iniciando sesion...
bionews-auth-service | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-auth-service | 3. Consultando API para el rango: 2026-05-18 a 2026-05-18
bionews-auth-service | Ocurrio un error general: Object of type date is not JSON serializable
bionews-auth-service | 5. Cerrando sesion...
bionews-postgres | 2026-05-18 20:38:25.691 UTC [539] ERROR: relation "sea_proyectos_evaluados" does not exist at character 22
bionews-postgres | 2026-05-18 20:38:25.691 UTC [539] STATEMENT: SELECT COUNT(_) FROM sea_proyectos_evaluados
bionews-auth-service | Error verificando DB: relation "sea_proyectos_evaluados" does not exist
bionews-auth-service | LINE 1: SELECT COUNT(_) FROM sea_proyectos_evaluados
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service | Iniciando scraping SEA Proyectos Evaluados. Modo completo.
bionews-postgres | 2026-05-18 20:38:44.079 UTC [546] ERROR: relation "sea_proyectos_evaluados" does not exist at character 15
bionews-postgres | 2026-05-18 20:38:44.079 UTC [546] STATEMENT: SELECT 1 FROM sea_proyectos_evaluados WHERE id = '2168353780'
bionews-auth-service | Error en scraping SEA Proyectos Evaluados: relation "sea_proyectos_evaluados" does not exist
bionews-auth-service | LINE 1: SELECT 1 FROM sea_proyectos_evaluados WHERE id = '2168353780...
bionews-auth-service | ^
bionews-auth-service |
bionews-auth-service | Scraping SEA Proyectos finalizado. Nuevos: 0
