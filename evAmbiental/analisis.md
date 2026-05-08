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
   Por defecto se muestran 10 proyectos y usa paginacion, aqui tienes el html de ambos apartados:
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
