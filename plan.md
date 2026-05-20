La secret key no deberia obtenerse directamente desde el .env? Por que esta escrito aqui?
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "Memr2026")

Investique y el segundo parametro de os.getenv es opcional si es que no se encuentra la key. Lo voy a poner en el .env y sacarla de ahi para ver si funciona

Cosas que veo en los docker compose logs -f:

```bash
bionews-db         | 2026-05-20 15:40:54.390 UTC [41] ERROR:  operator does not exist: text > timestamp without time zone at character 49
bionews-db         | 2026-05-20 15:40:54.390 UTC [41] HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-db         | 2026-05-20 15:40:54.390 UTC [41] STATEMENT:  SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-20T10:41:28'::timestamp LIMIT 1
bionews-api        | INFO:     172.18.0.5:59326 - "GET /api/notifications/status HTTP/1.1" 500 Internal Server Error
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
bionews-web        | 172.20.0.4 - - [20/May/2026:15:40:54 +0000] "GET /api/notifications/status HTTP/1.1" 500 21 "https://impacts-gay-dans-connected.trycloudflare.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
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
bionews-api        |   File "/app/src/database/manager.py", line 507, in _check_if_category_has_new_fast
bionews-api        |     cur.execute(f'SELECT 1 FROM "{t}" WHERE fecha_scraping > %s LIMIT 1', (last_exit,))
bionews-api        | psycopg2.errors.UndefinedFunction: operator does not exist: text > timestamp without time zone
bionews-api        | LINE 1: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-2...
bionews-api        |                                                         ^
bionews-api        | HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-api        |
bionews-api        | INFO:     127.0.0.1:58646 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | INFO:     127.0.0.1:43672 - "GET /api/health HTTP/1.1" 200 OK
```

Ahora hare pruebas del sistema

## Al ingresar a 'Normativas' 
No hay problemas en la interfaz aparentemente pero si en los logs me salio lo siguiente
```bash
bionews-web        | 172.20.0.4 - - [20/May/2026:15:43:58 +0000] "GET /api/data/normativas/count HTTP/1.1" 200 14 "https://impacts-gay-dans-connected.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | INFO:     172.18.0.5:44462 - "GET /api/data/normativas?limit=100 HTTP/1.1" 200 OK
bionews-web        | 172.20.0.4 - - [20/May/2026:15:43:59 +0000] "GET /api/data/normativas?limit=100 HTTP/1.1" 200 49276 "https://impacts-gay-dans-connected.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-db         | 2026-05-20 15:43:59.670 UTC [41] ERROR:  operator does not exist: text > timestamp without time zone at character 49
bionews-db         | 2026-05-20 15:43:59.670 UTC [41] HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-db         | 2026-05-20 15:43:59.670 UTC [41] STATEMENT:  SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-20T10:41:28'::timestamp LIMIT 1
bionews-api        | INFO:     172.18.0.5:44488 - "GET /api/notifications/status/normativas HTTP/1.1" 500 Internal Server Error
bionews-web        | 172.20.0.4 - - [20/May/2026:15:43:59 +0000] "GET /api/notifications/status/normativas HTTP/1.1" 500 21 "https://impacts-gay-dans-connected.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
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
bionews-api        |   File "/app/src/database/manager.py", line 540, in _check_if_category_has_new
bionews-api        |     cur.execute(f'SELECT 1 FROM "{t}" WHERE fecha_scraping > %s LIMIT 1', (last_exit,))
bionews-api        | psycopg2.errors.UndefinedFunction: operator does not exist: text > timestamp without time zone
bionews-api        | LINE 1: SELECT 1 FROM "normativas" WHERE fecha_scraping > '2026-05-2...
bionews-api        |                                                         ^
bionews-api        | HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
bionews-api        |
bionews-api        | INFO:     172.18.0.5:44476 - "GET /api/data/normativas?limit=-1 HTTP/1.1" 200 OK
bionews-web        | 2026/05/20 15:43:59 [warn] 29#29: *26 an upstream response is buffered to a temporary file /var/cache/nginx/proxy_temp/1/00/0000000001 while reading upstream, client: 172.20.0.4, server: _, request: "GET /api/data/normativas?limit=-1 HTTP/1.1", upstream: "http://172.18.0.4:8000/api/data/normativas?limit=-1", host: "impacts-gay-dans-connected.trycloudflare.com", referrer: "https://impacts-gay-dans-connected.trycloudflare.com/normativas"
bionews-web        | 172.20.0.4 - - [20/May/2026:15:43:59 +0000] "GET /api/data/normativas?limit=-1 HTTP/1.1" 200 501859 "https://impacts-gay-dans-connected.trycloudflare.com/normativas" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1
```

## Pertinencias nuevas:
La etiqueta de pertinencias 'Nueva' no desaparece una vez salgo de la pagina
Al parecer este es un problema general, la etiqueta de 'Nuevo' para los registros no desaparece una vez se sale de la categoria, tendra que ver con redis?

## Proyectos evaluados nuevos
Ocurre algo extrano, en los proyectos evaluados en la pagina oficial  hay 7 registros entre 19/05/2026 y 20/05/2026 (6 del 19 y 1 del 20) pero uno de los registros del 19 no se esta guardando ni mostrando. Intente con el boton de scraping SEA por fechas y el boton normal de scrapeo sea. 
Me di cuenta que en los logs cuando comienza el scraping de Proyectos Evaluados lo hace en 'Modo Diario', por lo que debe ser esa la razon por la que no encuentra el de ayer 19, se debio haber agregado despues de la ultima ejecucion que hice el 19 y como hoy ya es 20 y solo revisa por el dia de hoy no aparece nada, mira:
```bash
Iniciando scraping SEA Proyectos Evaluados. Modo diario.
bionews-api        | Offset 1 procesado. Registros nuevos hasta ahora: 0
bionews-api        | API retorno status False o sin datos en offset 101
bionews-api        | Scraping SEA Proyectos finalizado. Nuevos: 0
```

## Otro usuario
Antes estaba desde el perfil de administrador pero me cambie a uno de los usuarios de testing y no me aparecia ninguna categoria lateral con el punto rojo de 'notificacion'. Solo al ingresar a la categoria me aparece el punto rojo, el cual si desaparece cuando salgo de la categoria, pero si vuelvo a ingresar a la categoria despues de que desaparecio el puntito rojo me siguen saliendo las etiquetas de 'Nuevo' cuando deberian desaparecer una vez yo sali de la categoria.

Recuerda que el proceso de las notificaciones es el siguiente:

Scraper encuentra algo nuevo y lo agrega a su respectiva tabla -> Usuario ve punto rojo en la categoria en el sidebar -> Usuario ingresa a categoria y ve los nuevos registros con una etiqueta 'Nuevo' o algo similar -> Usuario sale de la categoria (o refresca pagina) y desaparece el punto rojo y la etiqueta 'Nuevo' (o 'Nueva') -> Usuario entra a la categoria nuevamente sin que haya habido nada nuevo y ya no existe la etiqueta 'Nuevo' para la categoria

Corrije todos estos errores, pero es prioridad el tema de las notificaciones
