## Docker compose logs -f
### Al ingresar a la pagina directamente
```bash
bionews-db         | 2026-05-20 16:27:56.092 UTC [40] ERROR:  function to_timestamp(timestamp without time zone, unknown) does not exist at character 60
bionews-db         | 2026-05-20 16:27:56.092 UTC [40] HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-db         | 2026-05-20 16:27:56.092 UTC [40] STATEMENT:  SELECT 1 FROM "noticias"
bionews-db         |                                WHERE TO_TIMESTAMP(fecha_scraping, 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                      > TO_TIMESTAMP('2026-05-20 12:25:08', 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                LIMIT 1
bionews-api        | INFO:     172.18.0.5:41796 - "GET /api/notifications/status HTTP/1.1" 500 Internal Server Error
bionews-web        | 172.20.0.4 - - [20/May/2026:16:27:56 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://impacts-gay-dans-connected.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | ERROR:    Exception in ASGI application
bionews-api        | Traceback (most recent call last):
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-api        |     result = await app(  # type: ignore[func-returns-value]
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
bionews-api        |     return await self.app(scope, receive, send)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in __call__
bionews-api        |     await super().__call__(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
bionews-api        |     await self.app(scope, receive, _send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 191, in __call__
bionews-api        |     with recv_stream, send_stream, collapse_excgroups():
bionews-api        |   File "/usr/local/lib/python3.11/contextlib.py", line 158, in __exit__
bionews-api        |     self.gen.throw(typ, value, traceback)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_utils.py", line 87, in collapse_excgroups
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 193, in __call__
bionews-api        |     response = await self.dispatch_func(request, call_next)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/slowapi/middleware.py", line 136, in dispatch
bionews-api        |     response = await call_next(request)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 168, in call_next
bionews-api        |     raise app_exc from app_exc.__cause__ or app_exc.__context__
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 144, in coro
bionews-api        |     await self.app(scope, receive_or_disconnect, send_no_error)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
bionews-api        |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-api        |     await route.handle(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-api        |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-api        |     response = await f(request)
bionews-api        |                ^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-api        |     raw_response = await run_endpoint_function(
bionews-api        |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-api        |     return await run_in_threadpool(dependant.call, **values)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-api        |     return await anyio.to_thread.run_sync(func)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-api        |     return await get_async_backend().run_sync_in_worker_thread(
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-api        |     return await future
bionews-api        |            ^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 1002, in run
bionews-api        |     result = context.run(func, *args)
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/server.py", line 707, in get_notification_status
bionews-api        |     return db.get_notification_status(user["sub"])
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/src/database/manager.py", line 478, in get_notification_status
bionews-api        |     result = {cat: self._check_if_category_has_new_fast(user_id, cat, exits) for cat in categories}
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/src/database/manager.py", line 478, in <dictcomp>
bionews-api        |     result = {cat: self._check_if_category_has_new_fast(user_id, cat, exits) for cat in categories}
bionews-api        |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/src/database/manager.py", line 509, in _check_if_category_has_new_fast
bionews-api        |     cur.execute(
bionews-api        | psycopg2.errors.UndefinedFunction: function to_timestamp(timestamp without time zone, unknown) does not exist
bionews-api        | LINE 2:                             WHERE TO_TIMESTAMP(fecha_scrapin...
bionews-api        |                                           ^
bionews-api        | HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-api        |
bionews-api        | INFO:     127.0.0.1:48282 - "GET /api/health HTTP/1.1" 200 OK
```

### Al ir a proyectos evaluados
```bash
bionews-web        | 172.20.0.4 - - [20/May/2026:16:29:02 +0000] "GET /api/data/sea_proyectos_evaluados?limit=-1 HTTP/1.1" 200 705476 "https://impacts-gay-dans-connected.trycloudflare.com/sea-evaluados" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-db         | 2026-05-20 16:29:02.361 UTC [40] ERROR:  function to_timestamp(timestamp without time zone, unknown) does not exist at character 75
bionews-db         | 2026-05-20 16:29:02.361 UTC [40] HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-db         | 2026-05-20 16:29:02.361 UTC [40] STATEMENT:  SELECT 1 FROM "sea_proyectos_evaluados"
bionews-db         |                                WHERE TO_TIMESTAMP(fecha_scraping, 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                      > TO_TIMESTAMP('2026-05-20 12:25:04', 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                LIMIT 1
bionews-api        | INFO:     172.18.0.5:57066 - "GET /api/notifications/status/sea_proyectos_evaluados HTTP/1.1" 500 Internal Server Error
bionews-api        | ERROR:    Exception in ASGI application
bionews-api        | Traceback (most recent call last):
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-api        |     result = await app(  # type: ignore[func-returns-value]
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
bionews-api        |     return await self.app(scope, receive, send)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in __call__
bionews-api        |     await super().__call__(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
bionews-api        |     await self.app(scope, receive, _send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 191, in __call__
bionews-api        |     with recv_stream, send_stream, collapse_excgroups():
bionews-api        |   File "/usr/local/lib/python3.11/contextlib.py", line 158, in __exit__
bionews-api        |     self.gen.throw(typ, value, traceback)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_utils.py", line 87, in collapse_excgroups
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 193, in __call__
bionews-api        |     response = await self.dispatch_func(request, call_next)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/slowapi/middleware.py", line 136, in dispatch
bionews-api        |     response = await call_next(request)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 168, in call_next
bionews-api        |     raise app_exc from app_exc.__cause__ or app_exc.__context__
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 144, in coro
bionews-api        |     await self.app(scope, receive_or_disconnect, send_no_error)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
bionews-api        |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-api        |     await route.handle(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-api        |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-api        |     response = await f(request)
bionews-api        |                ^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-api        |     raw_response = await run_endpoint_function(
bionews-api        |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-api        |     return await run_in_threadpool(dependant.call, **values)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-api        |     return await anyio.to_thread.run_sync(func)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-api        |     return await get_async_backend().run_sync_in_worker_thread(
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-api        |     return await future
bionews-api        |            ^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 1002, in run
bionews-api        |     result = context.run(func, *args)
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/server.py", line 712, in get_notification_status_single
bionews-api        |     has_new = db._check_if_category_has_new(user["sub"], category)
bionews-api        |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/src/database/manager.py", line 550, in _check_if_category_has_new
bionews-api        |     cur.execute(
bionews-api        | psycopg2.errors.UndefinedFunction: function to_timestamp(timestamp without time zone, unknown) does not exist
bionews-api        | LINE 2:                             WHERE TO_TIMESTAMP(fecha_scrapin...
bionews-api        |                                           ^
bionews-api        | HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-api        |
bionews-web        | 172.20.0.4 - - [20/May/2026:16:29:02 +0000] "GET /api/notifications/status/sea_proyectos_evaluados HTTP/1.1" 500 21 "https://impacts-gay-dans-connected.trycloudflare.com/sea-evaluados" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | INFO:     127.0.0.1:54860 - "GET /api/health HTTP/1.1" 200 OK
```

### Al ir a fiscalizaciones, sancionatorios, Sanciones, Programas, Medidas, Requerimientos (El texto de abajo es el que dio al ir a fiscalizaciones pero ocurre para todos)

```bash
bionews-web        | 172.20.0.4 - - [20/May/2026:16:30:04 +0000] "GET /api/data/fiscalizaciones?limit=100 HTTP/1.1" 200 37078 "https://impacts-gay-dans-connected.trycloudflare.com/fiscalizaciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-db         | 2026-05-20 16:30:05.382 UTC [39] ERROR:  function to_timestamp(timestamp without time zone, unknown) does not exist at character 67
bionews-db         | 2026-05-20 16:30:05.382 UTC [39] HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-db         | 2026-05-20 16:30:05.382 UTC [39] STATEMENT:  SELECT 1 FROM "fiscalizaciones"
bionews-db         |                                WHERE TO_TIMESTAMP(fecha_scraping, 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                      > TO_TIMESTAMP('2026-05-20 12:06:07', 'YYYY-MM-DD HH24:MI:SS')
bionews-db         |                                LIMIT 1
bionews-api        | INFO:     172.18.0.5:60886 - "GET /api/notifications/status/fiscalizaciones HTTP/1.1" 500 Internal Server Error
bionews-api        | ERROR:    Exception in ASGI application
bionews-web        | 172.20.0.4 - - [20/May/2026:16:30:05 +0000] "GET /api/notifications/status/fiscalizaciones HTTP/1.1" 500 21 "https://impacts-gay-dans-connected.trycloudflare.com/fiscalizaciones" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | Traceback (most recent call last):
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
bionews-api        |     result = await app(  # type: ignore[func-returns-value]
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
bionews-api        |     return await self.app(scope, receive, send)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1159, in __call__
bionews-api        |     await super().__call__(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 90, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
bionews-api        |     await self.app(scope, receive, _send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 88, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 191, in __call__
bionews-api        |     with recv_stream, send_stream, collapse_excgroups():
bionews-api        |   File "/usr/local/lib/python3.11/contextlib.py", line 158, in __exit__
bionews-api        |     self.gen.throw(typ, value, traceback)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_utils.py", line 87, in collapse_excgroups
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 193, in __call__
bionews-api        |     response = await self.dispatch_func(request, call_next)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/slowapi/middleware.py", line 136, in dispatch
bionews-api        |     response = await call_next(request)
bionews-api        |                ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 168, in call_next
bionews-api        |     raise app_exc from app_exc.__cause__ or app_exc.__context__
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/base.py", line 144, in coro
bionews-api        |     await self.app(scope, receive_or_disconnect, send_no_error)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
bionews-api        |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 660, in __call__
bionews-api        |     await self.middleware_stack(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 680, in app
bionews-api        |     await route.handle(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
bionews-api        |     await self.app(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 134, in app
bionews-api        |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
bionews-api        |     raise exc
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
bionews-api        |     await app(scope, receive, sender)
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 120, in app
bionews-api        |     response = await f(request)
bionews-api        |                ^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 674, in app
bionews-api        |     raw_response = await run_endpoint_function(
bionews-api        |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 330, in run_endpoint_function
bionews-api        |     return await run_in_threadpool(dependant.call, **values)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
bionews-api        |     return await anyio.to_thread.run_sync(func)
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/to_thread.py", line 63, in run_sync
bionews-api        |     return await get_async_backend().run_sync_in_worker_thread(
bionews-api        |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2518, in run_sync_in_worker_thread
bionews-api        |     return await future
bionews-api        |            ^^^^^^^^^^^^
bionews-api        |   File "/usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 1002, in run
bionews-api        |     result = context.run(func, *args)
bionews-api        |              ^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/server.py", line 712, in get_notification_status_single
bionews-api        |     has_new = db._check_if_category_has_new(user["sub"], category)
bionews-api        |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-api        |   File "/app/src/database/manager.py", line 550, in _check_if_category_has_new
bionews-api        |     cur.execute(
bionews-api        | psycopg2.errors.UndefinedFunction: function to_timestamp(timestamp without time zone, unknown) does not exist
bionews-api        | LINE 2:                             WHERE TO_TIMESTAMP(fecha_scrapin...
bionews-api        |                                           ^
bionews-api        | HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
bionews-api        |
bionews-api        | INFO:     172.18.0.5:60870 - "GET /api/data/fiscalizaciones?limit=-1 HTTP/1.1" 200 OK
bionews-web        | 2026/05/20 16:30:05 [warn] 29#29: *44 an upstream response is buffered to a temporary file /var/cache/nginx/proxy_temp/3/00/0000000003 while reading upstream, client: 172.20.0.4, server: _, request: "GET /api/data/fiscalizaciones?limit=-1 HTTP/1.1", upstream: "http://172.18.0.4:8000/api/data/fiscalizaciones?limit=-1", host: "impacts-gay-dans-connected.trycloudflare.com", referrer: "https://impacts-gay-dans-connected.trycloudflare.com/fiscalizaciones"
```

Al ir a tribunales, Consultas publicas y pertinencias tambien ocurre, pero en Normativas no ocurre ese error. En resumen ocurre en todas las categorias menos en Normativas


Y por ultimo, al ejecutar scraper de SEA (manual o por fechas) sigue sin encontrar el proyecto que faltaba:
```bash
bionews-web        | 172.20.0.4 - - [20/May/2026:16:33:30 +0000] "POST /api/scrape/sea HTTP/1.1" 200 53 "https://impacts-gay-dans-connected.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-api        | Token CAS encontrado. Iniciando sesion...
bionews-api        | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-api        | 3. Consultando API para el rango: 2026-05-19 a 2026-05-20
bionews-api        | Se encontraron 8 registros en la API para hoy.
bionews-api        | 4. Guardando en base de datos...
bionews-api        | Proceso finalizado con exito. Se agregaron 0 registros nuevos.
bionews-api        | 5. Cerrando sesion...
bionews-api        | Iniciando scraping SEA Proyectos Evaluados. Modo diario.
bionews-api        | Offset 1 procesado. Registros nuevos hasta ahora: 0
bionews-api        | API retorno status False o sin datos en offset 101
bionews-api        | Scraping SEA Proyectos finalizado. Nuevos: 0
bionews-api        | INFO:     127.0.0.1:44792 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | INFO:     172.18.0.5:56980 - "POST /api/scrape/sea/manual HTTP/1.1" 200 OK
bionews-web        | 172.20.0.4 - - [20/May/2026:16:33:53 +0000] "POST /api/scrape/sea/manual HTTP/1.1" 200 99 "https://impacts-gay-dans-connected.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-api        | Token CAS encontrado. Iniciando sesion...
bionews-api        | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-api        | 3. Consultando API para el rango: 2026-05-19 a 2026-05-20
bionews-api        | Se encontraron 8 registros en la API para hoy.
bionews-api        | 4. Guardando en base de datos...
bionews-api        | Proceso finalizado con exito. Se agregaron 0 registros nuevos.
bionews-api        | 5. Cerrando sesion...
bionews-api        | Iniciando scraping SEA Proyectos Evaluados. Modo diario.
bionews-api        | Offset 1 procesado. Registros nuevos hasta ahora: 0
bionews-api        | API retorno status False o sin datos en offset 101
bionews-api        | Scraping SEA Proyectos finalizado. Nuevos: 0
```