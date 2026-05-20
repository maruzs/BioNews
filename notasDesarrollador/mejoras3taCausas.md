Tengo el siguiente problema:

2026-05-20 13:36:10,155 [INFO] Procesando Tercer Tribunal...
bionews-api        | Ultima fecha registrada en BD: 18-05-2026
bionews-api        | Descargando registros desde la API del Tercer Tribunal...
bionews-api        | INFO:     127.0.0.1:47366 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | Error procesando los datos: cannot access local variable 'nuevos_registros' where it is not associated with a value
bionews-api        | 2026-05-20 13:36:14,012 [INFO] Tercer Tribunal: 0 nuevas causas.
bionews-api        | 2026-05-20 13:36:14,012 [INFO] --- SCRAPING TRIBUNALES FINALIZADO ---
bionews-api        | INFO:     127.0.0.1:48788 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | INFO:     127.0.0.1:54118 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | INFO:     127.0.0.1:50566 - "GET /api/health HTTP/1.1" 200 OK


Ademas de que para el 18 de mayo hubo una nueva causa que no esta guardada. 
Esta api funciona con un get, este es su cURL:
```js
curl.exe ^"https://causas.3ta.cl/api/v1/causes/?cause_state=ALL^&page=1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Referer: https://causas.3ta.cl/^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"XSRF-TOKEN: YAO9NBjjvzbaIKXjd-NCVN4nvhgDy0sllzrFn7wlL0gViUemmMa6V2HMIXKqMOAVLzaTDD0h8WKScT2e0uuS3w^" ^
  -H ^"If-Modified-Since: Mon, 26 Jul 1997 05:00:00 GMT^" ^
  -H ^"Authorization: Bearer undefined^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Cookie: _ga_5S7NDRMYL3=GS2.1.s1779298414^$o9^$g1^$t1779298425^$j49^$l0^$h0; _ga=GA1.2.1475686137.1776976762; _ga_3K21YKW97V=GS2.1.s1779298426^$o9^$g1^$t1779298596^$j60^$l0^$h0; _cause_management_session=KjrbXY^%^2BsEf4vYwFVWWqfU^%^2FvIwTEhd^%^2BbkVoO^%^2Bq1borenUUVKhCKiRmhDkf6mDhnf6ePdYNkPlhVYMVQoJwKwlAuF5tO^%^2BSNI8Qm5^%^2FXmujbY1Jb9pSPAuKlfObUCQau8ypL^%^2FFITiQ^%^2F0wJ13REiqLOy39ZFd3JZRihBQRroZpCBAYO2JIcS1zOl6C599DtTmvznjUxa1aXxOfCc^%^2Bf7MFDIxsfR5sYDa45wJmVAgtl7UmTXtueW45tIxtSVyE3HRPl13PdeXQMpsmOTRguYa0h7JO2KvpCD4yhelIXIY3Hu5buHho--79JDpbVc1Scfa6KW--PeMGNiNzfz77WlV1zfyeWg^%^3D^%^3D; _gid=GA1.2.1856819187.1779295345^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=4^" ^
  -H ^"Pragma: no-cache^" ^
  -H ^"Cache-Control: no-cache^" ^
  -H ^"TE: trailers^"
```

Al ingresar a `https://causas.3ta.cl/api/v1/causes/?cause_state=ALL^&page=1^` encontramos un json larguisimo con un monton de contenido inutil, la verdad el codigo que tenemos actualmente funciona casi perfecto, pero se me ocurrio una idea para mejorarlo. Al inicio del Json que se genera aparece lo siguiente:

```json
{
  "causes_ids": [
    5130,
    5129,
    5128,
    5127,
    5126,
    5125,
    5122,
    5121,
    5120,
    5115
  ],
```
Esos son las id de las causas que se muestran primero, es decir que si hubo una nueva aparecera ahi y si no existe deberia agregarse a la bd.
Eso si es importante notar que esta id  