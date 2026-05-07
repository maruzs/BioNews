# Errores, correcciones y actualizaciones

## A implementar en el codigo

Implementar src/scrapers/scraper_dga.py para que funcione igual que el resto de scrapers de noticias.(Tambien debe ir a la tabla 'Noticias' y ejecutarse al mismo tiempo que los demas scrapers de noticias, tener su checkbox, etc. Todo igual ya que solo es una nueva fuente de noticias)

## Errores en el desarrollo

### Exceso de notificaciones en terminal

Ya sea al desplegarlo con docker en el servidor o desde mi desktop con la terminal de Antigravity me sigue saliendo esto

- servidor (docker compose logs -f)

```bash
bionews-web        | 172.18.0.1 - - [07/May/2026:13:20:27 +0000] "GET /api/config/notifications HTTP/1.1" 200 14 "https://warcraft-platforms-cache-later.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 OPR/130.0.0.0" "2803:c600:7115:a6b9:7cd5:334:10c:3acc"
bionews-api        | INFO:     172.18.0.4:47768 - "GET /api/config/notifications HTTP/1.1" 200 OK
bionews-web        | 172.18.0.1 - - [07/May/2026:13:20:27 +0000] "GET /api/config/notifications HTTP/1.1" 200 14 "https://warcraft-platforms-cache-later.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 OPR/130.0.0.0" "2803:c600:7115:a6b9:7cd5:334:10c:3acc"
bionews-api        | INFO:     172.18.0.4:47772 - "GET /api/notifications/status HTTP/1.1" 200 OK
bionews-web        | 172.18.0.1 - - [07/May/2026:13:20:27 +0000] "GET /api/notifications/status HTTP/1.1" 200 233 "https://warcraft-platforms-cache-later.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 OPR/130.0.0.0" "2803:c600:7115:a6b9:7cd5:334:10c:3acc"
bionews-api        | INFO:     172.18.0.4:47788 - "GET /api/notifications/status HTTP/1.1" 200 OK
bionews-web        | 172.18.0.1 - - [07/May/2026:13:20:27 +0000] "GET /api/notifications/status HTTP/1.1" 200 233 "https://warcraft-platforms-cache-later.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 OPR/130.0.0.0" "2803:c600:7115:a6b9:7cd5:334:10c:3acc"
```

- terminal antigravity

```bash
INFO:     127.0.0.1:52858 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:64487 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:65388 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:55189 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62548 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:56346 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:57790 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:53029 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:65363 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:53108 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60529 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:65411 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:52861 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:60943 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:57462 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     127.0.0.1:50062 - "GET /api/notifications/status HTTP/1.1" 200 OK
```

Constantemente esta apareciendo esto, por que es?
Si es porque cada x tiempo se estan actualizando las notificaciones, necesito que veas si es necesario, ya que lo que habiamos quedado previamente era que solo se actualizaran las notificaciones cuando un scraper hubiera encontrado algo nuevo, no en tiempo real ni cada cierta cantidad de tiempo.
Si esta funcionando de la manera deseada y es necesario lo de abajo de forma constante, dejalo
Si esta funcionando de la manera deseada y no es necesario lo de abajo de forma constante, desactivalo
Si no esta funcionando de la manera deseada y no es necesario lo de abajo de forma constante, arregla lo de las notificaciones para que funcione de la manera deseada y luego desactiva lo de abajo de forma constante

```bash
INFO:     172.18.0.3:57684 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57696 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     172.18.0.3:57702 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57712 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     172.18.0.3:57716 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57730 - "GET /api/notifications/status HTTP/1.1" 200 OK
```

La idea era/es que cuando un scraper haya obtenido algo nuevo se active ahi el punto y la etiquetas nuevas, no que cada x cantidad de tiempo (o en tiempo real) se esten actualizando las noticias.

Si resulta que ese metodo esta implementado revisa si es necesario que a cada rato se este consultando la API, si no es necesario quita esa consulta que se repite. Si es absolutamente necesario dejala.

Si no esta implementado te explico cual es la idea que hay que implementar:
Los scrapers se ejecutan cada cierto tiempo (asignado por el scheduler, el cual puede ser editado desde el panel de administrador)
Cuando un scraper encuentra algo nuevo (noticias, normativas, etc) ese contenido se agrega a la BD y se le asigna tambien una 'fecha_scraping'.
Si eso ocurre, debera aparecer en la sidebar para cada categoria (Noticias, Normativas, Pertinencias, Fiscalizaciones, Sancionatoris, Tribunales ambientales, Etc) un punto rojo que se mantiene hasta que el usuario ingrese a la categoria y luego salga. Adentro de la categoria debe verse un distintivo (etiqueta 'Nuevo' para las tablas al inicio y etiqueta nuevo y borde verde para las noticias nuevas) para los items nuevos. Esa etiqueta debera desaparecer si el usuario ve el item (en noticias 'Ver mas' y en las tablas sera el link que esta en la columna 'Accion' de cada registro) y tambien cuando sale de la categoria (Ya sea que se fue a otra categoria, reinicio la pagina, lo vio desde otro dispositivo, fue a su perfil, etc.)
Esto debe ser cross device, es decir que si el usuario (Admin tambien) tiene abierta su sesion en el telefono (por la web) y en la pc (por la web) y ve las noticias en el telefono, en el computador debera desaparecer el punto rojo de noticias y la etiqueta nuevo en cada noticia que haya visto, al igual que si se va a otra categoria. Debe ser como un "Visto para cada usuario". No tiene que ser necesariamente en tiempo real, puede ser dependiendo de los clicks, ahi tu ves como lo implementas.

La idea es evitar consultas tan seguidas a la API.

Ademas de que aunque haya visto por ejemplo las nuevas noticias y se desmarque el puntito rojo de notificaciones, me vuelve a aparecer al cabo de unos segundos. Tambien ocurre con la etiqueta de 'Nuevo' en noticias y normativas, que aunque haya clickeado 'Marcar todo como leido' desaparece la etiqueta 'Nuevo' pero al cabo de unos segundos vuelven a aparecer.

### Descarga repetida de normativas

Otro error que note fue que ayer (2026-05-06) se descargaron demasiados registros de Normativas, si revisas la bd veras que hay 846 registros para las normativas, lo cual no es normal. Por ejemplo ayer se tuvo 9 veces el mismo registro del banco central de chile, y tambien 9 veces la misma normativa del ministerio del interior "Decreto número 33, de 2026..."

Hoy se obtuvieron normalmente, tuve 74 lo cual es un numero razonable, pero para probar ejecute nuevamente desde el panel de administrador el scraper de normativas y se descargaron las mismas 74 nuevamente!
Ayer como ejecute varias veces el scraper de normativas debio haberse descargado 9 veces todo, hoy lo he ejecutado 2 veces y se descargaron 2 veces. Eso no debe ser, solo debe descargar lo nuevo y si no hubo cambios nada.
Esto puede ocurrir debido a que no hay Primary Key para las normativas, y revisando la tabla de normativas me di cuenta que el unico atributo que mantiene una constante diferencia entre si (aunque se repita la normativa en diferentes dias) es la url (Columna 'Accion') como puedes ver aqui abajo, las 4 son para la misma noticia 'Certificado Tipos de cambio y paridades de monedas extranjeras para efectos que señala' del Banco Central de Chile. Pero cada una tiene su propia fecha y su prop

https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/04/44440/01/2805795.pdf
https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/05/44441/01/2806374.pdf
https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/06/44442/01/2807185.pdf
https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/01/2807854.pdf

Despues de https://www.diariooficial.interior.gob.cl/publicaciones/ lo que vemos es lo siguiente:
/ano/mes/dia/numero_edicion/tipo_documento/numero_documento.pdf
El tipo de documento puede ser '01' (Normas Generales), '02' (Normas Particulares), '07' (Boletin Oficial Mineria), solo esos nos interesan
Cada URL es absolutamente unica ya sea por la fecha,numero de edicion y tipo de documento (que esos 3 los pueden compartir varios), pero principalmente por el numero_documento.pdf que es unico para cada normativa sin importar si al dia siguiente el mismo organismo repite la misma normativa.

Borra todos los que este repetidos en la tabla de normativas en la base de datos

### Barra de busqueda por palabra clave

Barra de 'Buscar por palabra clave' no esta funcionando activamente como antes, ahora solo funciona al hacer click en 'Aplicar filtro' dentro de 'Desplegar filtro'. Aqui tenemos 2 opciones

1. Que sea busqueda activa al mismo tiempo que se escribe en la barra de busqueda
2. Que haya un boton al lado de la barra de busqueda 'Aplicar busqueda' o que al presionar enter se active la busqueda.

Lo que sea mas optimo en lo que es rendimiento, experiencia de usuario y consumo de recursos.

### Fecha scraping

Todo registro en la base de datos que no tenga una fecha_scraping debera asignarsele como fecha_scraping la fecha 2026-05-04 23:59:59
Toda fecha_scraping que tenga yyyy-mm-dd hh:mm:ss.ssssss debera pasar al siguiente formato dd-mm-yyyy hh:mm:ss (quitar los microsegundos)
Toda fecha nueva que se guarde tampoco deberia tener microsegundos, hasta segundo basta y sobra.

### Correccion scrapers noticias

Me di cuenta que ciertos scrapers marcan como que encontraron algo nuevo y en realidad era algo que ya estaba en la bd. Por ejemplo mira esto que note en la BD para un registro especifico:

Link (PK):
https://mma.gob.cl/seremi-del-medio-ambiente-informa-constante-monitoreo-de-calidad-del-aire-en-puchuncavi-y-quintero-y-pide-reforzar-limpieza-de-alcantarillados-de-establecimientos-educacionales/
Titulo:
Seremi del Medio Ambiente informa constante monitoreo de calidad del aire en Puchuncaví y Quintero y pide reforzar limpieza de alcantarillados de establecimientos educacionales
Fecha:
2026-05-04
Imagen:
https://mma.gob.cl/wp-content/uploads/2026/05/xQuintero-680x424.jpeg.pagespeed.ic.qA85Zt5fwp.webp
Fuente:
MMA
Fecha_scraping
2026-05-07 13:16:24.557715

Si te das cuenta ahi dice que la fecha de la noticia es 2026-05-04 pero la fecha de scraping es 2026-05-07, esa noticia yo se que la extraje el 4 de mayo, pero igualmente aparece que se extrajo el 7 de mayo. Como se puede solucionar eso?
Esto ocurre para TODAS las noticias que estan en la base de datos, todas tienen fecha de scraping 'actualizada' de la ultima vez que se ejecuto el scraper, no de cuando realmente se extrajo la noticia. Es decir que cada vez que se ejecuta el scraper la fecha_scraping se cambia para cosas que relmente no son nuevas, si no que ya estaban en la base de datos desde antes. Puede ser que por lo mismo se marquen como nuevas y aparezcan con el puntito rojo de notificaciones.

### SMA/SNIFA

Aqui el problema es que no se muestran las cosas mas nuevas, esto ocurre para cualquier subcategoria de SMA/SNIFA (fiscalizaciones, sancionatorios, requerimientos de ingreso, etc.)
Por ejemplo (esto lo hice ayer):
Se supone que se encontraron los siguientes registros en fiscalizaciones
Expedientes:

- DFZ-2026-614-XIV-PC
- DFZ-2026-758-IX-PC
- DFZ-2026-795-XIII-PC
  Y no aparecen en la pagina de fiscalizaciones

Los problemas que veo son:

- Estan en la BD pero no aparecen al buscar en la pagina (con cualquier filtro)
- Debe ser por el limite de 5000, pero las mas nuevas siempre deben estar primero
- Ademas me gustaria que se pudiera filtrar las fiscalizaciones por ano (esta en el expediente)

* Formato expediente:
  DFZ-ANO-NUMERO-REGION-TIPO (A veces despues de tipo hay TIPO FISCALIZACION y pueden ser -IA o -EI o no tener nada pero eso no lo tomamos en cuenta por ahora) y esto es lo que puede ser:
  - DFZ -> Valor general, se repite para todas las fiscalizaciones
  - ANO -> Ano en que se creo el expediente
    NUMERO -> Numero del expediente
    REGION -> Numero de la region (I a XIV)
    TIPO -> Tipo de documento:
  * RCA (Resolucion de Clasificacion Ambiental)
  * PC (Programa de Cumplimiento)
  * PPDA (Plan de Prevención y Descontaminación Ambiental)
  * NE (Norma de Emisión)
  * LEY (Ley Ambiental)

  * MP (Medidas Provisionales)
  * NC (Norma de Calidad)
  * SRCA (Sistema de Resoluciones de Clasificacion Ambiental)

  Si hay algo despues de TIPO es el TIPO FISCALIZACION
  - IA -> Inspeccion Ambiental
  - EI -> Examen de Informacion

- Las fiscalizaciones mas nuevas estan basadas en la url, mira el formato:
  https://snifa.sma.gob.cl/Fiscalizacion/Ficha/{numero_ficha}
  Mira los ejemplos que te dare aqui abajo (La primera es la mas nueva de todas, la ultima la mas antigua de todas, las del medio son al azar pero en orden descendente)

https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1075741 (Mas nueva)
https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1075735
https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1075730
https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1075720
y asi hasta llegar a la mas antigua (la tabla que tengo es hasta 2024, despues tendre hasta 2014 pero ahora no importa eso)
https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1004507 (Mas antigua)

- La tabla debe estar ordenada de mas nueva a mas antigua y que siempre en la interfaz las mas nuevas esten primero, no las ultimas obtenidas.

Tienes permiso para hacer todos los cambios que consideres pertinentes al proyecto ya que hare una nueva rama para esto
