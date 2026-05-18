# Al logearme:

10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
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
bionews-auth-service | File "/app/src/database/manager.py", line 507, in \_check_if_category_has_new
bionews-auth-service | cursor.execute(f'SELECT 1 FROM "{t}" WHERE {date_col} > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1', (last_exit, *viewed_ids))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "noticias" does not exist
bionews-auth-service | LINE 1: SELECT 1 FROM "noticias" WHERE fecha_scraping > '2026-05-18T...
bionews-auth-service | ^
bionews-auth-service |
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:35:55 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 29 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:35:55 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 499 0 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.4:57076 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 OK
bionews-postgres | 2026-05-18 19:35:56.014 UTC [74] ERROR: relation "noticias" does not exist at character 15
bionews-postgres | 2026-05-18 19:35:56.014 UTC [74] STATEMENT: SELECT 1 FROM "noticias" WHERE fecha_scraping > '2026-05-18T13:32:34'::timestamp AND "link" NOT IN ('https://mma.gob.cl/establecimientos-educacionales-de-cabo-de-hornos-recibieron-certificacion-ambiental/') LIMIT 1
bionews-auth-service | INFO: 172.18.0.4:57086 - "GET /api/notifications/status HTTP/1.1" 500 Internal Server Error
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
bionews-auth-service | File "/app/src/database/manager.py", line 507, in \_check_if_category_has_new
bionews-auth-service | cursor.execute(f'SELECT 1 FROM "{t}" WHERE {date_col} > %s AND "{id_col}" NOT IN ({placeholders}) LIMIT 1', (last_exit, *viewed_ids))
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-auth-service | return super().execute(query, vars)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | psycopg2.errors.UndefinedTable: relation "noticias" does not exist
bionews-auth-service | LINE 1: SELECT 1 FROM "noticias" WHERE fecha_scraping > '2026-05-18T...
bionews-auth-service | ^
bionews-auth-service |
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:35:56 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:35:56 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"

# Al ir a las SMA - Sanciones:

bionews-postgres | 2026-05-18 19:37:11.451 UTC [174] ERROR: relation "registrosanciones" does not exist at character 15
bionews-postgres | 2026-05-18 19:37:11.451 UTC [174] STATEMENT: SELECT * FROM registroSanciones LIMIT 5000
bionews-legal-service | INFO: 172.18.0.4:55546 - "GET /api/data/registroSanciones?limit=5000 HTTP/1.1" 500 Internal Server Error
bionews-legal-service | ERROR: Exception in ASGI application
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-legal-service | result = await app( # type: ignore[func-returns-value]
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-legal-service | return await self.app(scope, receive, send)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-legal-service | await super().**call**(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-legal-service | await self.app(scope, receive, \_send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-legal-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-legal-service | await route.handle(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-legal-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-legal-service | response = await f(request)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-legal-service | raw_response = await run_endpoint_function(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-legal-service | return await run_in_threadpool(dependant.call, \*\*values)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-legal-service | return await anyio.to_thread.run_sync(func)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-legal-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-legal-service | return await future
bionews-legal-service | ^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-legal-service | result = context.run(func, *args)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/services/legal/main.py", line 354, in get_table_data
bionews-legal-service | data = db.get_table_data(table_name, limit=limit)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/database/manager.py", line 114, in get_table_data
bionews-legal-service | cursor.execute(query, (limit,))
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-legal-service | return super().execute(query, vars)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | psycopg2.errors.UndefinedTable: relation "registrosanciones" does not exist
bionews-legal-service | LINE 1: SELECT \* FROM registroSanciones LIMIT 5000
bionews-legal-service | ^
bionews-legal-service |
bionews-web | 172.20.0.2 - - [18/May/2026:19:37:11 +0000] "GET /api/data/registroSanciones?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:37:11 +0000] "GET /api/data/registroSanciones?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | 2026-05-18 19:37:11,602 [INFO] POST /api/notifications/exit: User 4 saliendo de sancionatorios
bionews-auth-service | INFO: 172.18.0.4:42400 - "POST /api/notifications/exit HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:37:11 +0000] "POST /api/notifications/exit HTTP/1.1" 200 16 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:37:11 +0000] "POST /api/notifications/exit HTTP/1.1" 200 16 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-auth-service | INFO: 172.18.0.4:42412 - "GET /api/notifications/status/registroSanciones HTTP/1.1" 200 OK
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:37:12 +0000] "GET /api/notifications/status/registroSanciones HTTP/1.1" 200 48 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:37:12 +0000] "GET /api/notifications/status/registroSanciones HTTP/1.1" 200 48 "https://prairie-nissan-commonly-arabia.trycloudflare.com/sanciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:37:25 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 499 0 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:37:25 +0000] "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 68 "https://prairie-nissan-commonly-arabia.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-auth-service | INFO: 172.18.0.4:45248 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTcyNDk1NX0.s0ZVxLWqc00-H5IbbwNkJNCmQRrRb-76c8UjZAHdy4I HTTP/1.1" 200 OK

# Al ir a programas de cumplimiento:

bionews-postgres | 2026-05-18 19:38:09.605 UTC [241] ERROR: relation "programasdecumplimiento" does not exist at character 15
bionews-postgres | 2026-05-18 19:38:09.605 UTC [241] STATEMENT: SELECT * FROM programasDeCumplimiento LIMIT 5000
bionews-legal-service | INFO: 172.18.0.4:35406 - "GET /api/data/programasDeCumplimiento?limit=5000 HTTP/1.1" 500 Internal Server Error
bionews-legal-service | ERROR: Exception in ASGI application
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-legal-service | result = await app( # type: ignore[func-returns-value]
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-legal-service | return await self.app(scope, receive, send)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-legal-service | await super().**call**(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-legal-service | await self.app(scope, receive, \_send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-legal-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-legal-service | await route.handle(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-legal-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-web | 172.20.0.2 - - [18/May/2026:19:38:09 +0000] "GET /api/data/programasDeCumplimiento?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/programas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:38:09 +0000] "GET /api/data/programasDeCumplimiento?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/programas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-legal-service | response = await f(request)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-legal-service | raw_response = await run_endpoint_function(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-legal-service | return await run_in_threadpool(dependant.call, \*\*values)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-legal-service | return await anyio.to_thread.run_sync(func)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-legal-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-legal-service | return await future
bionews-legal-service | ^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-legal-service | result = context.run(func, *args)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/services/legal/main.py", line 354, in get_table_data
bionews-legal-service | data = db.get_table_data(table_name, limit=limit)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/database/manager.py", line 114, in get_table_data
bionews-legal-service | cursor.execute(query, (limit,))
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-legal-service | return super().execute(query, vars)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | psycopg2.errors.UndefinedTable: relation "programasdecumplimiento" does not exist
bionews-legal-service | LINE 1: SELECT \* FROM programasDeCumplimiento LIMIT 5000
bionews-legal-service | ^
bionews-legal-service |
bionews-auth-service | 2026-05-18 19:38:09,818 [INFO] POST /api/notifications/exit: User 4 saliendo de registroSanciones
bionews-auth-service | INFO: 172.18.0.4:33196 - "POST /api/notifications/exit HTTP/1.1" 200 OK

# Al ir a tribunales:

bionews-postgres | 2026-05-18 19:38:43.002 UTC [281] ERROR: relation "tribunales" does not exist at character 15
bionews-postgres | 2026-05-18 19:38:43.002 UTC [281] STATEMENT: SELECT * FROM Tribunales LIMIT 5000
bionews-legal-service | INFO: 172.18.0.4:48706 - "GET /api/data/Tribunales?limit=5000 HTTP/1.1" 500 Internal Server Error
bionews-web | 172.20.0.2 - - [18/May/2026:19:38:43 +0000] "GET /api/data/Tribunales?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/tribunales" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:38:43 +0000] "GET /api/data/Tribunales?limit=5000 HTTP/1.1" 500 21 "https://prairie-nissan-commonly-arabia.trycloudflare.com/tribunales" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-legal-service | ERROR: Exception in ASGI application
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-legal-service | result = await app( # type: ignore[func-returns-value]
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in **call**
bionews-legal-service | return await self.app(scope, receive, send)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in **call**
bionews-legal-service | await super().**call**(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in **call**
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in **call**
bionews-legal-service | await self.app(scope, receive, \_send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in **call**
bionews-legal-service | await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in **call**
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in **call**
bionews-legal-service | await self.middleware_stack(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-legal-service | await route.handle(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-legal-service | await self.app(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-legal-service | await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 53, in wrapped_app
bionews-legal-service | raise exc
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/\_exception_handler.py", line 42, in wrapped_app
bionews-legal-service | await app(scope, receive, sender)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-legal-service | response = await f(request)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-legal-service | raw_response = await run_endpoint_function(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-legal-service | return await run_in_threadpool(dependant.call, \*\*values)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-legal-service | return await anyio.to_thread.run_sync(func)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-legal-service | return await get_async_backend().run_sync_in_worker_thread(
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-legal-service | return await future
bionews-legal-service | ^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/anyio/\_backends/\_asyncio.py", line 1002, in run
bionews-legal-service | result = context.run(func, *args)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/services/legal/main.py", line 354, in get_table_data
bionews-legal-service | data = db.get_table_data(table_name, limit=limit)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/app/src/database/manager.py", line 114, in get_table_data
bionews-legal-service | cursor.execute(query, (limit,))
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/psycopg2/extras.py", line 236, in execute
bionews-legal-service | return super().execute(query, vars)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | psycopg2.errors.UndefinedTable: relation "tribunales" does not exist
bionews-legal-service | LINE 1: SELECT \* FROM Tribunales LIMIT 5000
bionews-legal-service | ^
bionews-legal-service |
