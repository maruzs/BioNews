## Ejemplo de curl para mostrar 10 primera pagina:
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
  -H ^"Referer: https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php?tipoPresentacion=Ambos^" ^
  -H ^"Cookie: miSeia=0; cookiesession1=678B286ED46FD8C3B43A4CD05B06F4B0; __utma=66077484.189921577.1776648208.1779292251.1779295196.18; __utmz=66077484.1776973710.3.2.utmcsr=sea.gob.cl^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; _ga_S1X3MHJQMV=GS2.1.s1779295062^$o25^$g1^$t1779296360^$j60^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1779210051^$o10^$g0^$t1779210071^$j40^$l0^$h0; _ga_BCSPV16K2P=GS2.1.s1779292063^$o16^$g1^$t1779292231^$j60^$l0^$h0; _gid=GA1.3.542971729.1779125527; SEIA_SERVER=seia.sea.gob.cl^%^3A443; PHPSESSID=ggt5h5mdkj5m2vbe7a9nf537ld; __utmc=66077484; __utmb=66077484.5.10.1779295196; __utmt=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"nombre=^&titular=^&folio=^&selectRegion=^&selectComuna=^&tipoPresentacion=Ambos^&projectStatus=^&PresentacionMin=^&PresentacionMax=^&CalificaMin=^&CalificaMax=^&sectores_economicos=^&razoningreso=^&id_tipoexpediente=^&offset=1^&limit=10^&orderColumn=FECHA_PRESENTACION^&orderDir=desc^"
Despues de --data-raw van los filtros, los que nos interesan son PresentacionMin y PresentacionMax
Normalmente con mostrar 10 elementos de la primera pagina basta ya que solo nos interesan los mas nuevos

## Analisis POST:
offset -> Paginacion, funciona distinto dependiendo del limit
limit -> Cantidad maxima de elementos a mostrar
Aqui abajo tienes ejemplos de los post que se usan 
### Mostrar 10

Mostrar 10
primera pagina:
```JS
  nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=1
limit=10
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 10
Segunda pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=2
limit=10
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 10
Tercera pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=3
limit=10
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

### Mostrar 100

Mostrar 100
Primera pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=1
limit=100
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 100
Segunda pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=11
limit=100
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 100
Tercera pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=21
limit=100
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

### Mostrar 50

Mostrar 50
Primera pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=1
limit=50
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 50:
Segunda pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=6
limit=50
orderColumn=FECHA_PRESENTACION
orderDir=desc
```

Mostrar 50
Tercera pagina:
```js
nombre
titular
folio
selectRegion
selectComuna
tipoPresentacion=Ambos
projectStatus
PresentacionMin
PresentacionMax
CalificaMin
CalificaMax
sectores_economicos
razoningreso
id_tipoexpediente
offset=11
limit=50
orderColumn=FECHA_PRESENTACION
orderDir=desc
```