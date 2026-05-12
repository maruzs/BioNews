# Analisis correccion proyectos evaluados SEA

- Link principal -> https://seia.sea.gob.cl/busqueda/buscarProyecto.php

Correccion de paginacion e items mostrados:

1. En https://seia.sea.gob.cl/busqueda/buscarProyecto.php voy a buscar sin filtrar nada
2. En network puedo ver que se hizo una peticion POST que pesa 16.84kB (Aqui el cURL):

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
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778280728.1778597539.14; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778597539^$o21^$g1^$t1778600075^$j16^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778598472^$o9^$g0^$t1778599090^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778597549^$o13^$g1^$t1778598400^$j49^$l0^$h0; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=23976ef205bd29b9c283ca63607ef271b3a751a7bd418bba282eff27dc9d6a6c; __utmb=66077484.9.10.1778597539; __utmc=66077484; _gid=GA1.3.2118237672.1778597540; __utmt=1; _gat_gtag_UA_88214148_2=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=1^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"ss
```

3. Si yo bajo al apartado de paginacion y 'Mostrar' (es el html de aqui abajo):

```html
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
    Mostrando <strong>1 - 10 de 30.106</strong>
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
```

5. Y cambio la cantidad de items que se muestran de 10 a 100, se demora en cargar, pero veo que hace el siguiente POST que obtiene un file que pesa 164.95kB (aqui el cURL):

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
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778280728.1778597539.14; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778597539^$o21^$g1^$t1778600075^$j16^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778598472^$o9^$g0^$t1778599090^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778597549^$o13^$g1^$t1778598400^$j49^$l0^$h0; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=23976ef205bd29b9c283ca63607ef271b3a751a7bd418bba282eff27dc9d6a6c; __utmb=66077484.9.10.1778597539; __utmc=66077484; _gid=GA1.3.2118237672.1778597540; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=1^&limit=100^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
```

6. Pero si yo ahora cambio de pagina a la 2 ahora veo que se hace otro POST que obtiene un file que pesa 155.63kB (este es el cURL):

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
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778280728.1778597539.14; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778597539^$o21^$g1^$t1778600075^$j16^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778598472^$o9^$g0^$t1778599090^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778597549^$o13^$g1^$t1778598400^$j49^$l0^$h0; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=23976ef205bd29b9c283ca63607ef271b3a751a7bd418bba282eff27dc9d6a6c; __utmb=66077484.9.10.1778597539; __utmc=66077484; _gid=GA1.3.2118237672.1778597540; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=11^&limit=100^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
```

7. Y ahora paso a la pagina 3 con el POST obtenemos un file que pesa 155.31kB (este es su cURL):

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
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1778280728.1778597539.14; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1778597539^$o21^$g1^$t1778600075^$j16^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1778598472^$o9^$g0^$t1778599090^$j60^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1778597549^$o13^$g1^$t1778598400^$j49^$l0^$h0; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=23976ef205bd29b9c283ca63607ef271b3a751a7bd418bba282eff27dc9d6a6c; __utmb=66077484.9.10.1778597539; __utmc=66077484; _gid=GA1.3.2118237672.1778597540; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=21^&limit=100^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
```

8. Tal vez con eso puedas mejorar el scraper de SEA - Proyectos evaluados, ya que al ejecutarlo con una fecha mas temprana (que como muestra 10 proyectos requeriria cambiar de pagina) ocurre lo siguiente:

```bash
Iniciando scraping SEA Proyectos Evaluados. Modo diario.
Página 2 procesada. Nuevos registros: 5
Página 3 procesada. Nuevos registros: 5
API retorno status False o sin datos en offset 3
Scraping SEA Proyectos finalizado. Nuevos: 5
```
