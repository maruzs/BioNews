## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

Estaba probando si funcionaba todo y decidi borrar el ultimo registro que habia en Fiscalizaciones (DFZ-2026-1585-X-NE) y si se borro, todo bien ahi. Pero luego le di al scraper manual de SNIFA y obtuve lo siguiente

```bash
bionews-api        | Registros actuales en BD: 3354
bionews-api        | Registros en la web: 0
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Fiscalizaciones (via Playwright)...
bionews-api        | Registros actuales en BD: 5181
bionews-api        | Navegando a https://snifa.sma.gob.cl/Fiscalizacion...
bionews-api        | Ingresando filtro: DFZ-2026
bionews-api        | Esperando resultados iniciales...
bionews-api        | Cambiando a mostrar todos los registros...
bionews-api        | Esperando que se carguen todos los registros...
bionews-db         | 2026-05-19 16:52:23.650 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-19 16:52:24.766 UTC [27] LOG:  checkpoint complete: wrote 11 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.017 s, sync=0.007 s, total=1.116 s; sync files=9, longest=0.005 s, average=0.001 s; distance=43 kB, estimate=180 kB; lsn=0/32FFA38, redo lsn=0/32FFA00
bionews-api        | Total registros en la web (año 2026): 10
bionews-api        | Encontrados 1 registros nuevos.
bionews-api        |   + DFZ-2026-1585-X-NE
bionews-api        | Scraper finalizado. Se agregaron 1 registros a Fiscalizaciones.
bionews-api        | Iniciando scraper de Requerimientos de Ingreso...
bionews-api        | Registros actuales en BD: 236
bionews-api        | Registros en la web: 236
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Medidas Provisionales...
bionews-api        | Registros actuales en BD: 492
bionews-api        | Registros en la web: 492
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Programas de Cumplimiento...
bionews-api        | Registros actuales en BD: 1410
bionews-api        | INFO:     127.0.0.1:40076 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | Registros en la web: 1410
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Registro Publico de Sanciones...
bionews-api        | Registros actuales en BD: 1022
bionews-api        | Registros en la web: 1114 (1021 unicos)
bionews-api        | No hay registros nuevos. La BD esta actualizada.
```

Se supone que si se agrego, verdad? Pero cuando voy a la pagina de fiscalizaciones no aparece el registro, solo tengo hasta 1584 y se supone que deberia tener hasta el 1585.
Tampoco aparece cuando le doy a buscar por palabra clave (DFZ-2026-1585-X-NE)
Pero si cambio de cuenta a la de algun usuario (estaba en administrador antes) si me aparece la notificacion de que hubo una nueva y me aparece en la tabla. Luego cuando volvi a iniciar sesion en la cuenta de administrador si me aparecio el registro DFZ-2026-1585-X-NE.

Ademas me di cuenta que si salgo de la categoria Fiscalizaciones (ahora que si me marco que hay una nueva) y vuelvo a entrar me sigue apareciendo la etiqueta 'Nueva' que ya no deberia aparecer. Lo mismo con SEA ahora que hice una nueva busqueda manual, me aparecieron los mismos que ya tenia antes (sin haber borrado nada) como nuevos y al salir no se quita la etiqueta de nueva.

Y por ejemplo habia 5 registros en las pertinencias hoy pero en la tabla se mostraban 3, por lo que hice un scrapeo manual y se mostraba que solo habia 3 nuevas, luego fui a borrar una en el panel de debug y fui a ver al panel y me aparecian 4 registros siendo que antes tenia 3 y en la web habia 5 y que aparentemente al descargar no habian aparecido las 2 nuevas, pero que al borrar la ultima si estaban las 2 mas nuevas y se borro una, dejandome con 4. Pero mas encima ahora me sale una de las de ayer con la etiqueta de 'Nueva', dejandome con 5 supuestamente nuevas cuando en realidad son 4.
Siento que estoy puede tener que ver con redis pero no estoy del todo seguro.
Ahora para probar lo que hice fue ejecutar nuevamente de forma manual el scraper del SEA:

```bash
bionews-api        | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-api        | Token CAS encontrado. Iniciando sesion...
bionews-api        | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-api        | 3. Consultando API para el rango: 2026-05-18 a 2026-05-19
bionews-api        | Se encontraron 15 registros en la API para hoy.
bionews-api        | 4. Guardando en base de datos...
bionews-api        | Proceso finalizado con exito. Se agregaron 1 registros nuevos.
bionews-api        | 5. Cerrando sesion...
bionews-api        | Iniciando scraping SEA Proyectos Evaluados. Modo diario.
bionews-api        | Offset 1 procesado. Registros nuevos hasta ahora: 0
bionews-api        | API retorno status False o sin datos en offset 101
bionews-api        | Scraping SEA Proyectos finalizado. Nuevos:
```

Le di f5 a la pagina (desde el panel de admin) y me aparecio el puntito rojo en la parte de SEA en el sidebar, pero al darle click ahi me seguian apareciendo 4 registros del 19 (hoy) y 1 de ayer con la etiqueta de nueva y no me aparecia el nuevo registro
Al cambiar de sesion a una de los usuarios de testeo que tengo si me aparece el nuevo registro, dejandome nuevamente con 5 del 19.
