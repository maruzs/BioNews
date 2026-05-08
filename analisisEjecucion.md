## SMA - FISCALIZACIONES

### LOGS - TERMINAL

Iniciando scraper de Fiscalizaciones (via Playwright)...
Registros actuales en BD: 5041
Navegando a https://snifa.sma.gob.cl/Fiscalizacion...
Ingresando filtro: DFZ-2026
Esperando resultados iniciales...
Sin filas aun, reintento 1/8...
Sin filas aun, reintento 2/8...
Sin filas aun, reintento 3/8...
Sin filas aun, reintento 4/8...
Sin filas aun, reintento 5/8...
Sin filas aun, reintento 6/8...
Sin filas aun, reintento 7/8...
Sin filas aun, reintento 8/8...
Cambiando a mostrar todos los registros...
Esperando que se carguen todos los registros...
Sin filas aun, reintento 1/10...
Sin filas aun, reintento 2/10...
Sin filas aun, reintento 3/10...
Sin filas aun, reintento 4/10...
Sin filas aun, reintento 5/10...
Sin filas aun, reintento 6/10...
Sin filas aun, reintento 7/10...
Sin filas aun, reintento 8/10...
Sin filas aun, reintento 9/10...
Sin filas aun, reintento 10/10...
No se encontraron registros en la web.

### PROBLEMA

No entiendo por que hizo eso, no cargo la pagina o algo? Es primera vez que me aparecen esos logs para 'Fiscalizaciones'.

## TRIBUNALES AMBIENTALES

### LOGS - TERMINAL

2026-05-08 11:45:22,283 [INFO] --- SCRAPING TRIBUNALES MANUAL ---
2026-05-08 11:45:22,298 [INFO] Procesando Primer Tribunal...
Ultima fecha registrada en BD: 05-05-2026
Buscando causas del ano 2026 en el Primer Tribunal...
Actualizacion completada. Se revisaron/guardaron 1 registros.
2026-05-08 11:45:23,282 [INFO] Primer Tribunal: 1 nuevas causas.
2026-05-08 11:45:23,284 [INFO] Procesando Segundo Tribunal...
Ultima fecha en BD para el Segundo Tribunal: 04-05-2026
Iniciando Chromium para buscar causas del ano 2026...
Navegando a la pagina principal...
Consultando categoria de tramite #1 de 12...
Consultando categoria de tramite #2 de 12...
Consultando categoria de tramite #3 de 12...
Consultando categoria de tramite #4 de 12...
Consultando categoria de tramite #5 de 12...
Consultando categoria de tramite #6 de 12...
Consultando categoria de tramite #7 de 12...
Consultando categoria de tramite #8 de 12...
Consultando categoria de tramite #9 de 12...
Consultando categoria de tramite #10 de 12...
Consultando categoria de tramite #11 de 12...
Consultando categoria de tramite #12 de 12...
Actualizacion completada. Se guardaron o actualizaron 1 registros.
2026-05-08 11:46:05,093 [INFO] Segundo Tribunal: 1 nuevas causas.
2026-05-08 11:46:05,093 [INFO] Procesando Tercer Tribunal...
Ultima fecha registrada en BD: 04-05-2026
Descargando registros desde la API del Tercer Tribunal...
Actualizacion completada. Se guardaron o actualizaron 1 registros.
2026-05-08 11:46:08,124 [INFO] Tercer Tribunal: 1 nuevas causas.
2026-05-08 11:46:08,126 [INFO] --- SCRAPING TRIBUNALES FINALIZADO --

### PROBLEMA

Las supuestas nuevas causas ya existian en la base de datos, no ha habido causas nuevas en ningun tribunal y aun asi las reconoce como nuevas

## GENERAL

Despues de haber ejecutado manualmente todos los scrapers no logro que funcione nada:
No carga el boton de refrescar logs
No me cargan las noticias al ir a verlas
No me cargan las normativas
Es como si se hubiera quedado pegado en alguna parte

Le di f5 a la pagina y se queda en 'Cargando...'

Creo que ya se que es:
Despues de ejecutar el scraper de consultas puedo ver lo siguiente en bash

```bash
Scraping MMA finalizado. Nuevos registros: 0
2026-05-08 11:50:30,454 [INFO] Procesando DGA Consultas...
Scrapeando consultas DGA: https://dga.mop.gob.cl/consulta-publica/
Scraping DGA finalizado. Nuevos registros: 0
```

Pero esa vez que no funcionaba nada no aparecio lo de la DGA hasta que hice ctrl+c

Ahora despues de haber reiniciado el servidor hice click nuevamente en 'Consultas' (scraper manual en panel admin) y si aparecio de inmediato lo de DGA y pude refrescar logs y cambiar de categoria, pero al momento de hacer ctrl+c en la consola uvicorn me salio esto:

```bash
INFO:     Shutting down
INFO:     Waiting for connections to close. (CTRL+C to force quit)
```

y se quedo ahi pegado y nuevamente no puedo hacer nada y la consola no muestra nada, ni siquiera me deja ahcer CTRL+C to force quit.

Tuve que abrir el panel de administrador y cerrar una cosa que decia algo de node (no lei bien todo) y se logro cerrar y esto salio en bash

```bash
INFO:     Waiting for connections to close. (CTRL+C to force quit)
INFO:     Finished server process [11588]
ERROR:    Traceback (most recent call last):
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 674, in run_until_complete
    self.run_forever()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 641, in run_forever
    self._run_once()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 1987, in _run_once
    handle._run()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\events.py", line 88, in _run
    self._context.run(self._callback, *self._args)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\server.py", line 78, in serve
    with self.capture_signals():
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\contextlib.py", line 144, in __exit__
    next(self.gen)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\server.py", line 339, in capture_signals
    signal.raise_signal(captured_signal)
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 157, in _on_sigint
    raise KeyboardInterrupt()
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\routing.py", line 645, in lifespan
    await receive()
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\lifespan\on.py", line 137, in receive
    return await self.receive_queue.get()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\queues.py", line 158, in get
    await getter
asyncio.exceptions.CancelledError

ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 674, in run_until_complete
    self.run_forever()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 641, in run_forever
    self._run_once()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\base_events.py", line 1987, in _run_once
    handle._run()
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\events.py", line 88, in _run
    self._context.run(self._callback, *self._args)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\server.py", line 78, in serve
    with self.capture_signals():
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\contextlib.py", line 144, in __exit__
    next(self.gen)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\server.py", line 339, in capture_signals
    signal.raise_signal(captured_signal)
  File "C:\Users\maria\AppData\Local\Programs\Python\Python312\Lib\asyncio\runners.py", line 157, in _on_sigint
    raise KeyboardInterrupt()
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 415, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\uvicorn\middleware\proxy_headers.py", line 56, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\fastapi\applications.py", line 1159, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\applications.py", line 90, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\middleware\errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\middleware\cors.py", line 88, in __call__
    await self.app(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\routing.py", line 660, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\routing.py", line 680, in app
    await route.handle(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\routing.py", line 276, in handle
    await self.app(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\fastapi\routing.py", line 134, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\fastapi\routing.py", line 121, in app
    await response(scope, receive, send)
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\starlette\responses.py", line 274, in __call__
    async with anyio.create_task_group() as task_group:
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\anyio\_backends\_asyncio.py", line 803, in __aexit__
    raise exc_val
  File "C:\Users\maria\Desktop\BioNews\.venv\Lib\site-packages\anyio\_backends\_asyncio.py", line 771, in __aexit__
    await self._on_completed_fut
asyncio.exceptions.CancelledError
INFO:     Stopping reloader process [20452]
```
