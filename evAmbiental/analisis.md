Debemos implementar un apartado nuevo en lo que es el SEA, lo bueno es que la base de lo que es el login es la misma de las pertinencias, solo que ahora debemos ir a otra categoria.
Esto puede hacerse despues de que se hayan rescatado las pertinencias diarias.

De todas formas primero quiero rescatar TODOS los proyectos ingresados para la primera vez construir la tabla y de ahi en adelante solo sera filtar por el dia actual. Comienzo con el analisis.

## ANALISIS

1. Como dije, hay que acceder mediante login y es exactamente lo mismo que para obtener las pertinencias, puedes implementar que justo despues de investigar las pertinencias se pase a ver los proyectos.

Este es el link de la pagina de los proyectos:
https://seia.sea.gob.cl/busqueda/buscarProyecto.php

ahi dentro tendras un formulario (ver evAmbiental/formulario.html)

2. Ejecucion scraper (FORMULARIO):
   2.1 Primera ejecucion: Para la primera ejecucion del scraper cuando llenemos la tabla de datos no habra que poner nada en el formulario ya que queremos TODOS los datos, por lo que daremos directamente a buscar

   ```html
   <button
     type="submit"
     onclick="enviar_formulario()"
     class="btn btn-primary btn-lg sg-btnForm"
   >
     Buscar
   </button>
   ```

   2.2 Ejecucion posterior: Debera filtrar por el dia de hoy en el siguiente apartado:

   ```html
   <div
     role="wrapper"
     class="gj-datepicker gj-datepicker-bootstrap gj-unselectable input-group"
   >
     <input
       type="text"
       autocomplete="off"
       class="form-control"
       id="startDateFechaP"
       name="PresentacionMin"
       placeholder="dd/mm/aaaa"
       aria-describedby="btnToPresentationDate"
       data-type="datepicker"
       data-guid="1afe8da3-3371-492d-282e-ae28b31ff76f"
       data-datepicker="true"
       role="input"
     /><span class="input-group-append" role="right-icon"
       ><button class="btn btn-outline-secondary border-left-0" type="button">
         <i class="fa fa-calendar" aria-hidden="true"></i></button
     ></span>
   </div>
   ```

   y luego de poner la fecha de hoy le damos a buscar (mismo boton que en 2.1)

3. Analisis Developer tools>Network y paginacion despues de clickear 'Buscar':
   3.1 Network: al clickear 'Buscar', se genera una peticion POST, este es el cURL:

   ```bash
   curl.exe ^"https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php^" ^
   -X POST ^
   -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
   -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
   -H ^"Accept-Language: en-US,en;q=0.9^" ^
   -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
   -H ^"Content-Type: application/x-www-form-urlencoded^" ^
   -H ^"X-Requested-With: XMLHttpRequest^" ^
   -H ^"Origin: https://seia.sea.gob.cl^" ^
   -H ^"Connection: keep-alive^" ^
   -H ^"Referer: https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php^" ^
   -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778247389.1778256380.10; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778256379^$o13^$g0^$t1778256379^$j60^$l0^$h0; _ga=GA1.1.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778248248^$o8^$g0^$t1778248731^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778213014^$o11^$g1^$t1778213193^$j7^$l0^$h0; _gid=GA1.3.312106550.1778176199; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=210f31edf9963225bfbfc4f88d4d1aef92da152def7094c19cf373abe2fcd7b2; __utmc=66077484; __utmb=66077484.1.10.1778256380; __utmt=1^" ^
   -H ^"Sec-Fetch-Dest: empty^" ^
   -H ^"Sec-Fetch-Mode: cors^" ^
   -H ^"Sec-Fetch-Site: same-origin^" ^
   --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=1^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
   ```

   3.2 Paginacion:
   Por defecto se muestran 10 proyectos y usa paginacion, aqui tienes el html de ambos apartados (evAmbiental/paginacion.html):

   ```html
   <div class="dt-layout-row">
     <div class="dt-layout-cell dt-layout-start"></div>
     <div class="dt-layout-cell dt-layout-end">
       <div class="dt-length">
         <label for="dt-length-0">Mostrar &nbsp; </label
         ><select
           name="datatable-proyectos_length"
           aria-controls="datatable-proyectos"
           class="dt-input"
           id="dt-length-0"
         >
           <option value="10">10</option>
           <option value="20">20</option>
           <option value="50">50</option>
           <option value="100">100</option>
         </select>
       </div>
       <div
         class="dt-info"
         aria-live="polite"
         id="datatable-proyectos_info"
         role="status"
       >
         Mostrando <strong>1 - 10 de 30.104</strong>
       </div>
       <div class="dt-paging">
         <nav aria-label="pagination">
           <button
             class="dt-paging-button disabled first"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             aria-disabled="true"
             aria-label="First"
             data-dt-idx="first"
             tabindex="-1"
           >
             «</button
           ><button
             class="dt-paging-button disabled previous"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             aria-disabled="true"
             aria-label="Previous"
             data-dt-idx="previous"
             tabindex="-1"
           >
             ‹</button
           ><button
             class="dt-paging-button current"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             aria-current="page"
             data-dt-idx="0"
           >
             1</button
           ><button
             class="dt-paging-button"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             data-dt-idx="1"
           >
             2</button
           ><button
             class="dt-paging-button"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             data-dt-idx="2"
           >
             3</button
           ><span
             class="ellipsis"
             aria-controls="datatable-proyectos"
             aria-disabled="true"
             data-dt-idx="ellipsis"
             tabindex="-1"
             >…</span
           ><button
             class="dt-paging-button"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             data-dt-idx="3010"
           >
             3.011</button
           ><button
             class="dt-paging-button next"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             aria-label="Next"
             data-dt-idx="next"
           >
             ›</button
           ><button
             class="dt-paging-button last"
             role="link"
             type="button"
             aria-controls="datatable-proyectos"
             aria-label="Last"
             data-dt-idx="last"
           >
             »
           </button>
         </nav>
       </div>
     </div>
   </div>
   ```

   3.3 Si cambio a la pagina 2 se hace un nuevo post (leer ANALISIS CURLS PAGINACIONES)

4. Analisis del contenido de un formato.json (formatopag1.json y formatopag2.json son de las 2 primeras paginaciones con 10 registros cada una)
   4.1 Este es un registro completo:

   ```json
   {
     "EXPEDIENTE_ID": "2168003697",
     "EXPEDIENTE_NOMBRE": "PLAN DE REMEDIACI�N AMBIENTAL EN SITIO EX - CENTRAL DI�SEL IQUIQUE",
     "EXPEDIENTE_URL_PPAL": "https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168003697",
     "EXPEDIENTE_URL_FICHA": "https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168003697&modo=ficha",
     "WORKFLOW_DESCRIPCION": "DIA",
     "REGION_NOMBRE": "Regi�n de Tarapac�",
     "COMUNA_NOMBRE": "Iquique",
     "TIPO_PROYECTO": "o11",
     "RAZON_INGRESO": "Sentencia judicial",
     "TITULAR": "Engie Energ�a Chile S.A.",
     "INVERSION_MM": "6000000.0",
     "INVERSION_MM_FORMAT": "6,0000",
     "FECHA_PRESENTACION": "1778258184",
     "FECHA_PRESENTACION_FORMAT": "08/05/2026",
     "ESTADO_PROYECTO": "En Calificaci�n",
     "ENCARGADO": "",
     "ACTIVIDAD_ACTUAL": "",
     "FECHA_PLAZO": "",
     "FECHA_PLAZO_FORMAT": "",
     "ACCIONES": "",
     "LINK_MAPA": {
       "SHOW": true,
       "URL": "/mapa/visualizacion/PuntoRepresentativo/index.php?idExpediente=2168003697",
       "IMAGE": "map-invalid.jpg"
     },
     "DESCRIPCION_TIPOLOGIA": "Reparaci�n o recuperaci�n de �reas que contengan contaminantes, que abarquen, una superficie igual o mayor a 10.000 m2",
     "DIAS_LEGALES": "5",
     "SUSPENDIDO": "Activo",
     "VER_ACTIVIDAD": ""
   }
   ```

   4.2 Que obtener de cada registro:
   id -> EXPEDIENTE_ID (ej. 2168003697)
   nombre -> EXPEDIENTE_NOMBRE (ej. PLAN DE REMEDIACION AMBIENTAL EN SITIO EX - CENTRAL DIESEL IQUIQUE)
   url -> EXPEDIENTE_URL_PPAL (ej. https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168003697)
   titular -> TITULAR (ej. Engie Energia Chile S.A.)
   via_ingreso -> WORKFLOW_DESCRIPCION
   estado_proyecto -> ESTADO_PROYECTO
   razon_ingreso -> RAZON_INGRESO
   fecha_presentacion -> FECHA_PRESENTACION_FORMAT
   estado_proyecto -> ESTADO_PROYECTO
   subestado_proyecto -> SUSPENDIDO
   tipo_proyecto -> TIPO_PROYECTO

## TABLA

La tabla tendra las siguientes columnas:

- id (Text PK Unique)
- nombre (Text)
- titular (Text)
- via_ingreso (Text)
- estado_proyecto (Text)
- razon_ingreso (Text)
- fecha_presentacion (Text)
- estado_proyecto + (subestado_proyecto) (Text) -> subestado debe estar entre parentesis
- tipo_proyecto (Text)
- url (Text URL)

## INTERFAZ

Debera estar en la categoria SEA en la subcategoria
Proyectos Evaluados
Es decir sea quedar asi:
SEA

- Pertinencias
- Proyectos Evaluados
  Estaba pensando hacerlo como tabla pero tal vez con cards sea mas bonito, pero la verdad la prioridad no es la estetica si no que sea lo mas funcional posible. Asi que tu decide si con cards o con tabla.

### TABLA

Quiero que sea una tabla que muestre la siguiente informacion
numero (como todas las tablas)
corazon (para agregar a favoritos, como todas las tablas)
etiqueta nuevo (si es nuevo, como todas las tablas)
nombre
titular
fecha presentacion
estado_proyecto + (subestado_proyecto)
razon ingreso
tipo_proyecto

- ver ficha -> Es un url que lleva a la ficha

### CARDS

Quiero que sean cards que muestren la siguiente informacion:
Estado (subestado)
nombre
fecha presentacion
corazon (para agregar a favoritos)
etiqueta nuevo (si es nuevo)
ver detalles -> Esto despliega un modal que muestra la siguiente informacion:

- nombre
- id
- titular
- fecha presentacion
- razon ingreso
- estado_proyecto + (subestado_proyecto)
- tipo_proyecto

- ver ficha -> Es un url que lleva a la ficha

### ANALISIS CURLS PAGINACIONES

Pagina 1:

- Peso -> 17.07 kb
- primer registro -> 2168003697
- cURL:

```js
curl.exe ^"https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/x-www-form-urlencoded^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Origin: https://seia.sea.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php^" ^
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778256380.1778260225.11; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778260224^$o14^$g0^$t1778260224^$j60^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778248248^$o8^$g0^$t1778248731^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778213014^$o11^$g1^$t1778213193^$j7^$l0^$h0; _gid=GA1.3.312106550.1778176199; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=210f31edf9963225bfbfc4f88d4d1aef92da152def7094c19cf373abe2fcd7b2; __utmc=66077484; __utmb=66077484.1.10.1778260225; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=1^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
```

Pagina 2:

- peso -> 17.43kb
- primer registro -> 2168129124
- cURL:

```js
curl.exe ^"https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/x-www-form-urlencoded^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Origin: https://seia.sea.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php^" ^
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778256380.1778260225.11; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778260224^$o14^$g1^$t1778260224^$j60^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778248248^$o8^$g0^$t1778248731^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778213014^$o11^$g1^$t1778213193^$j7^$l0^$h0; _gid=GA1.3.312106550.1778176199; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=210f31edf9963225bfbfc4f88d4d1aef92da152def7094c19cf373abe2fcd7b2; __utmc=66077484; __utmb=66077484.1.10.1778260225; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=2^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
```

pagina 3:

- peso -> 16.49kb
- primer registro -> 2168275602
- cURL:

```js
curl.exe ^"https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/x-www-form-urlencoded^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Origin: https://seia.sea.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php^" ^
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778256380.1778260225.11; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778260224^$o14^$g1^$t1778260224^$j60^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778248248^$o8^$g0^$t1778248731^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778213014^$o11^$g1^$t1778213193^$j7^$l0^$h0; _gid=GA1.3.312106550.1778176199; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=210f31edf9963225bfbfc4f88d4d1aef92da152def7094c19cf373abe2fcd7b2; __utmc=66077484; __utmb=66077484.1.10.1778260225; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=2^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"s
```
