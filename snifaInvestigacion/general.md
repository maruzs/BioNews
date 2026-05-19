Actualmente las paginas del SMA/SNIFA se estaban obteniendo mediante el HTML, pero despues de haber investigado me di cuenta que es posible obtener los valores directamente en formato JSON mediante el uso de request para algunas de las categorias:

## Procedimientos Sancionatorios (src/scrapers/snifa.py y tabla registroSanciones):
Actualmente el scraper de snifa funcionaba usando beautifulSoup y requests, pero quiero implementarlo para que ahora funcione usando la API. Actualmente la BD ya esta construida por lo que de ahora en adelante siempre debera ejecutarse este post de abajo 
```js
curl.exe ^"https://snifa.sma.gob.cl/Sancionatorio/ObtenerResultadosGrid^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/x-www-form-urlencoded; charset=UTF-8^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Origin: https://snifa.sma.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://snifa.sma.gob.cl/Sancionatorio/Resultado^" ^
  -H ^"Cookie: _ga_H7DTM3S58G=GS2.1.s1779221598^$o30^$g1^$t1779223293^$j55^$l0^$h0; _ga=GA1.1.1117657353.1776648211; _ga_ET47766J7M=GS2.1.s1778165186^$o8^$g1^$t1778165201^$j45^$l0^$h0^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  --data-raw ^"draw=1^&columns^%^5B0^%^5D^%^5Bdata^%^5D=0^&columns^%^5B0^%^5D^%^5Bname^%^5D=^&columns^%^5B0^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B0^%^5D^%^5Borderable^%^5D=true^&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B1^%^5D^%^5Bdata^%^5D=1^&columns^%^5B1^%^5D^%^5Bname^%^5D=^&columns^%^5B1^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B1^%^5D^%^5Borderable^%^5D=true^&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B2^%^5D^%^5Bdata^%^5D=2^&columns^%^5B2^%^5D^%^5Bname^%^5D=^&columns^%^5B2^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B2^%^5D^%^5Borderable^%^5D=true^&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B3^%^5D^%^5Bdata^%^5D=3^&columns^%^5B3^%^5D^%^5Bname^%^5D=^&columns^%^5B3^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B3^%^5D^%^5Borderable^%^5D=true^&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B4^%^5D^%^5Bdata^%^5D=4^&columns^%^5B4^%^5D^%^5Bname^%^5D=^&columns^%^5B4^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B4^%^5D^%^5Borderable^%^5D=true^&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B5^%^5D^%^5Bdata^%^5D=5^&columns^%^5B5^%^5D^%^5Bname^%^5D=^&columns^%^5B5^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B5^%^5D^%^5Borderable^%^5D=true^&columns^%^5B5^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B5^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B6^%^5D^%^5Bdata^%^5D=6^&columns^%^5B6^%^5D^%^5Bname^%^5D=^&columns^%^5B6^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B6^%^5D^%^5Borderable^%^5D=true^&columns^%^5B6^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B6^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B7^%^5D^%^5Bdata^%^5D=7^&columns^%^5B7^%^5D^%^5Bname^%^5D=^&columns^%^5B7^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B7^%^5D^%^5Borderable^%^5D=true^&columns^%^5B7^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B7^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&order^%^5B0^%^5D^%^5Bcolumn^%^5D=0^&order^%^5B0^%^5D^%^5Bdir^%^5D=asc^&start=0^&length=10^&search^%^5Bvalue^%^5D=^&search^%^5Bregex^%^5D=false^&nombre=^&expediente=^&categoria=^&ddlRegion=^&ddlComuna=^"
```
Probando en POSTMAN ese cURL obtuve lo siguiente (Mostrare solo los primeros 3 registros, no los 10)
```json
{
    "draw": 1,
    "recordsTotal": 3358,
    "recordsFiltered": 3358,
    "data": [
        [
            "1",
            "D-078-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/24940' target='_blank'>Antros Rock Bar</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>EDUARDO CARTER GUIÑEZ</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Equipamiento</li></ul>",
            "<ul class='sin-orden'><li>Región de Los Lagos</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4501'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
        [
            "2",
            "F-016-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/16843' target='_blank'>ETFA 062-01 FISAM FISCALIZACIONES AMBIENTALES SPA</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>FISAM FISCALIZACIONES AMBIENTALES SPA</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>ETFA</li></ul>",
            "<ul class='sin-orden'><li>Región del Libertador General Bernardo O'Higgins</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4497'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
        [
            "3",
            "F-017-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/819' target='_blank'>TRANSPORTE DE RESIDUOS PELIGROSOS POR RUTAS DE LA REGION DE ANTOFAGASTA</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>LIMFOSEP S.A.</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Transportes y almacenajes</li></ul>",
            "<ul class='sin-orden'><li>Región de Antofagasta</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4496'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
```
Usando ese POST debera compararse la cantidad de registros que actualmente tengo en la tabla 'sancionatorios' en la bd con el valor que diga despues de "recordsTotal":
Si recordsTotal es mayor que la cantidad de registros que tengo, debera agregarse a la tabla aquellos que no existan previamente en la tabla siguiendo la idea del codigo snifa.py solo que ahora se hara con POST y no con el HTML.

## Fiscalizaciones (src/scrapers/fiscalizaciones.py y tabla fiscalizaciones)
Actualmente Fiscalizaciones requiere que usando playwright pasemos por los filtros de la pagina snifa.sma.gob.cl/Fiscalizacion ya que si vamos directamente a snifa.sma.gob.cl/Fiscalizacion/Resultado no cargaba nunca por la enorme cantidad de registros que existen. El codigo esta en src/scrapers/fiscalizaciones.py y debe extraerse lo mismo y funcionar casi identico, con la excepcion de que ahora usaremos POST como el cURL que tenemos aca abajo

```js
curl.exe ^"https://snifa.sma.gob.cl/Fiscalizacion/ObtenerResultadosGrid^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/javascript, */*; q=0.01^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/x-www-form-urlencoded; charset=UTF-8^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Origin: https://snifa.sma.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://snifa.sma.gob.cl/Fiscalizacion/Resultado^" ^
  -H ^"Cookie: _ga_H7DTM3S58G=GS2.1.s1779221598^$o30^$g1^$t1779224068^$j55^$l0^$h0; _ga=GA1.1.1117657353.1776648211; _ga_ET47766J7M=GS2.1.s1778165186^$o8^$g1^$t1778165201^$j45^$l0^$h0^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  --data-raw ^"draw=1^&columns^%^5B0^%^5D^%^5Bdata^%^5D=0^&columns^%^5B0^%^5D^%^5Bname^%^5D=^&columns^%^5B0^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B0^%^5D^%^5Borderable^%^5D=true^&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B1^%^5D^%^5Bdata^%^5D=1^&columns^%^5B1^%^5D^%^5Bname^%^5D=^&columns^%^5B1^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B1^%^5D^%^5Borderable^%^5D=true^&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B2^%^5D^%^5Bdata^%^5D=2^&columns^%^5B2^%^5D^%^5Bname^%^5D=^&columns^%^5B2^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B2^%^5D^%^5Borderable^%^5D=true^&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B3^%^5D^%^5Bdata^%^5D=3^&columns^%^5B3^%^5D^%^5Bname^%^5D=^&columns^%^5B3^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B3^%^5D^%^5Borderable^%^5D=true^&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B4^%^5D^%^5Bdata^%^5D=4^&columns^%^5B4^%^5D^%^5Bname^%^5D=^&columns^%^5B4^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B4^%^5D^%^5Borderable^%^5D=true^&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B5^%^5D^%^5Bdata^%^5D=5^&columns^%^5B5^%^5D^%^5Bname^%^5D=^&columns^%^5B5^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B5^%^5D^%^5Borderable^%^5D=true^&columns^%^5B5^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B5^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B6^%^5D^%^5Bdata^%^5D=6^&columns^%^5B6^%^5D^%^5Bname^%^5D=^&columns^%^5B6^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B6^%^5D^%^5Borderable^%^5D=true^&columns^%^5B6^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B6^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B7^%^5D^%^5Bdata^%^5D=7^&columns^%^5B7^%^5D^%^5Bname^%^5D=^&columns^%^5B7^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B7^%^5D^%^5Borderable^%^5D=true^&columns^%^5B7^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B7^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&columns^%^5B8^%^5D^%^5Bdata^%^5D=8^&columns^%^5B8^%^5D^%^5Bname^%^5D=^&columns^%^5B8^%^5D^%^5Bsearchable^%^5D=true^&columns^%^5B8^%^5D^%^5Borderable^%^5D=true^&columns^%^5B8^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=^&columns^%^5B8^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false^&order^%^5B0^%^5D^%^5Bcolumn^%^5D=0^&order^%^5B0^%^5D^%^5Bdir^%^5D=asc^&start=0^&length=10^&search^%^5Bvalue^%^5D=^&search^%^5Bregex^%^5D=false^&nombre=^&expediente=DFZ^&categoria=^&ddlRegion=^&ddlComuna=^"
```
Es importante poner el filtro DFZ en la categoria y
eso nos da el siguiente json (Mostrare solo los primeros 3 registros, no los 10)
```json
{
    "draw": 1,
    "recordsTotal": 49961,
    "recordsFiltered": 49961,
    "data": [
        [
            "1",
            "DFZ-2013-400-IX-RCA-IA",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>FRIGORIFICO TEMUCO S.A.</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Agroindustrias</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/2457' target='_blank'>FRIGORIFICO TEMUCO</a></li></ul>",
            "<ul class='sin-orden'><li>Región de la Araucanía</li></ul>",
            "<ul class='sin-orden'><li>Temuco</li></ul>",
            "En SNIFA",
            "<span></span><a href='/Fiscalizacion/Ficha/4040706'><i class='fa fa-plus-circle'></i> Ver detalle</a>"
        ],
        [
            "2",
            "DFZ-2013-152-XIV-RCA-IA",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>GRANJA MARINA TORNAGALEONES S.A.</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Pesca y Acuicultura</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/2562' target='_blank'>TORNAGALEONES</a></li></ul>",
            "<ul class='sin-orden'><li>Región de Los Ríos</li></ul>",
            "<ul class='sin-orden'><li>Corral</li></ul>",
            "En SNIFA",
            "<span></span><a href='/Fiscalizacion/Ficha/4040705'><i class='fa fa-plus-circle'></i> Ver detalle</a>"
        ],
        [
            "3",
            "DFZ-2013-623-III-RCA-IA",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>COMPAÑIA CONTRACTUAL MINERA CANDELARIA</li><li><i class='fa-li fa fa-user'></i>COMPAÑIA CONTRACTUAL MINERA OJOS DEL SALADO                                                         </li><li><i class='fa-li fa fa-user'></i>TRANSNET S.A.                                                                                       </li><li><i class='fa-li fa fa-user'></i>COMPAÑIA GENERAL DE ELECTRICIDAD S.A.</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Minería</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/10295' target='_blank'>CANDELARIA</a></li></ul>",
            "<ul class='sin-orden'><li>Región de Atacama</li></ul>",
            "<ul class='sin-orden'><li>Tierra Amarilla</li></ul>",
            "En SNIFA",
            "<span></span><a href='/Fiscalizacion/Ficha/4040704'><i class='fa fa-plus-circle'></i> Ver detalle</a>"
        ],
```

De ahi todo debe ser identico a lo que funciona ahora, solo que el contenido se obtiene desde ahora usando el cURL y playwright ya no es necesario. Para la primera ejecucion habra que construir la bd para los +49k registros, pero de ahi en adelante siempre sera necesario obtener solo los 10 mas nuevos y ver si estan en la bd o no.

