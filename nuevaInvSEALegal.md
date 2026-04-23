# LINK
https://pertinencia.sea.gob.cl
# ANALISIS
Ahi se pueden ver todas las pertinencias, pero requiere un login (credenciales estaran en un .env pero no se como funciona si quiero distribuir esta app a otras personas)
1. Al ir al link te lleva a una pagina de login, hay que poner rut sin puntos y con guion, la clave y luego darle al boton de ingresar
2. Una vez dentro no hay que seleccionar nada mas que el boton 'Buscar', de manera que aparezcan TODAS las ultimas pertinencias
3. Al darle a 'Buscar' se genera una tabla, la cual obtiene informacion de un json, el problema es que es muy pesado y por ende utilizaria muchisimos recursos, por lo que me gustaria que haga una de las dos opciones (la que sea mas eficiente):
    * Descargue el JSON solo si al ver la tabla tenemos que hay una nueva pertinencia (si el primero de la tabla es diferente al anterior primero significa que hay algo nuevo).
    * Descargue el JSON de los ultimos 99 de ser posible

# INFO A OBTENER
Me interesa obtener lo siguiente de las pertinencias
nombre de pertinencia, ID de pertinencia (o el href que tiene nombre pertinencia si crees que es mas facil), Fecha de presentacion, Estado, Tipo de proyecto
# ESTRUCTURA PAGINA E INFORMACION

## Login (Usuario, clave y boton ingresar)
```html
<div class="ingreso">

<div id="login">
    <div class="login-header">
         <span class="fa-stack fa-2x hidden-xs">
          <i class="fa fa-circle fa-stack-2x"></i>
          <i class="fa fa-lock fa-stack-1x fa-inverse"></i>
        </span>
    </div>

    <form method="post" id="fm1">

        <section class="row">
             <div>
                <input class="required inputs autorut" id="username" size="25" tabindex="1" type="text" accesskey="u" autocomplete="off" placeholder="Usuario" name="username" value=""></div>
        </section>

        <section class="row">
          
            <div>
                <input class="required inputs" type="password" id="password" size="25" tabindex="2" accesskey="c" autocomplete="off" placeholder="Contraseña" name="password" value=""><span id="capslock-on" style="display:none;">
                    <p>
                        <i class="fa fa-exclamation-circle"></i>
                        <span>¡La tecla BLOQ MAYÚS está activada!</span>
                    </p>
                </span>
            </div>
        </section>
        <!--<section class="row check">
            <p th:if="${rememberMeAuthenticationEnabled}">
                <input type="checkbox" name="rememberMe" id="rememberMe" value="true" tabindex="5"  />
                <label for="rememberMe" th:text="#{screen.rememberme.checkbox.title}"/>
            </p>
        </section>
        
        <section class="row" th:if="${recaptchaSiteKey}">
            <div class="g-recaptcha" th:attr="data-sitekey=${recaptchaSiteKey}"/>
        </section> --><br><section class="sec_der">
            <input type="hidden" name="execution" value="090518d8-cb3d-4820-ab8d-681355aa2945_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuY1dWbVZVeHJlSEpCTXpWck1pdFVWazAyVkZGRGVIaG1WbUpVTUZCYVEwMUpMMHMxUkdOS01ISmlUSFVyWXpKQk4wWkJWbk5YVkZWMVNqRnFZeTlZUlV4dmJYUm1iMDVrVVdsWGJIWk1aRVY1TnpoaFZVTnpVVzkwVkZOUVpGWldURVp0YURVMU5XNUtOeTlaUlhCMmJtRjNNMmhPVVVGa1JtcGxOSFZtWVdsT1NUbFVTMlJHYXpCbGF6bDNiMjlDVkUxR2FscFFPRk5QTXk5bE9FZElWakEwYVd4aE9TOVNVMnBSYVcwM1NIRnFSRlpETjNsVVRqVXhMM2hhWW5aS2FEVnZUVlUxYUdoTEsyZHpVVmsyVmpWYWFuWllVakZyTkVoeVYxVnNWWEV3VEhwb2FYbHNlR3BpUkhoWVYxbHlNRzVzT1VaQ1FXTlVRa0YxUkZsQ01Ia3hkbXhUYjFKMWFrOWFlRGhVTjNoa1JXSjNNVVJVZVRJdksxTjRRak16WlRKUk1HOTRVSEF4TjBwR2EybHhVRE5oY2k5UmJYVjRjbWxxU0RrelRYZHVUa2R1Y2pRNGIwZElPRW95TlRoNlZHaENTR2RWUmxoMmRUaE1hRzFDVUdaNVFqRTVWMkZzY2tNNU5UWnpjMHA2VEc0NFZrRXdMelp5WmxoTWRHaE9jM3AxTlRZemVrWXJha2x1V1RsNVYxRk5lVUpNTHpCNFpUQnVjV2hhY0ZGd00wVkdaVmxQUlRFeWVUQXpOMVJuWlZWaFFuaHFUVXRwV0hZeWQzZHdTbFpvZW1sc1NIaGpUWGRoTlVReFluZ3ZjazF1UjBKdGEyVjJlVXRLZUROTWVFMUtRa2cwVERoR1l6VlZWMGRQWkRKUWNXaE1kbG95VFhCTmNHMVZTVVpPZUc5bE5raGxRbVowZVV4VVZERkpOa3hZTVhSUVpsSm5aalpWUTFGb1lrb3ZSR2hqUWpOd1UwRXdjVFp0Wmpoc2MzSm1aMlZzUjNsc2NVa3dhbFZxVUhaR2NtdzJSbVJ5Um5sUFJteDVTM2xhTW1aVVkzTnlLMGQ2Y21aeVRVRlhlSEJCTms5bVprUnRaVzFxYUhCUFJuRnZRMnd3VkdWa1JWZ3dhRnA0UjNvdmNuUmpWbGxtTldwb1FscDVlSEY2VFhWaVp6bFhUMGxYV2xwak1VSkRWRk4zTTNsVVRuZDBMMDg0ZG1KdVJYSTJja0ZPVURWWVlURkZTQzlTTDNabWFEZ3hjbXRwUzJVekwwMDBUMWRhVlhwYVpDdFdTazgzU2xkMlNYbGpaVUY1Wm5oTVduZFZTMnRSWkRSQ1RGUk5VekJ6WW01bU1XeHljWFZuYTNKWGVscGFTbEV3V1dKdlZ6RTVVRVIyU0dacFQwWnBVSEF3YkdKb1prNVlOV0k1VjBneFozaGFVbGQ1Umk5a1ZUWkVkekZFZWl0WldEWXhWR3RYZEdwWlpuWkJOREJsYmpNeU1URllRUzl4T1VWQ1IwSXpla2xKUkZKcU1tb3ZSVWd5WkdGSGRYTndNMHBYWmpGSlpFbHZkV2hrVDJGM05GTlphVlYyVUUxVWRXNU1ObVpZWTNoV1pVdEZURTVQUlhwUFJuWXphMHh1TDNwUlZreHJkamRVVWtkeFpGWlRaMGM0UlVjd2VrUktiRGRqVFdwM2FuZHdPSG8zVkRadE0zbEZiVmhWVlRNM1NHeG5SV1pQZW1sS01tZDRZVFo2TDBJeFdtSndkbEY1VG5oMFJYUmpPVmxEY2s1UFRGbGlTVWt4UjNsNWFHNXhjeXR4ZG5OUkwySkJaMUp2Y1V0MU5HeHlaSGhIT0hRdlJYZzBkMVpaVVhwVEt6Z3ZXbXgzU0VWNldHUjZablZYWkd4UGVGcDBURUpWVXpoMmIxbzBkRFJqTVhvMWNsVXhLMU5CYzJwM1ozRkRXR2xHTmpBcldFRnlhRXhXVDBWVFdGUjBLMGhETWtWc1JucGlPR0ZtUmxGTEwxRkJXVkpwV2l0RlVGUlFSaTlNYkRaeU0yd3JSSHB1VGs1eWQyVnpSVmg2WlZKSGIzVnNSbXRSZFVwbk1ucDNWR3BMSzB4V2VHeGtWRTl6ZFRKblFWTkVZWEl5ZDBnd2JGSlBaM0owUlRoWmQwaG9VSGN2YWpsRVFUVXhMMGRxZGxoUU0xQTRWRmxqTUdKUVJqSm9OMDlGUW1FdlZtMTNXbkpuYldaSWRteEhSa0UzU3pFelNVTnZkV0ZuZWpoV1JVbDFhRFpNZUdGclRVRnZUVTQzV2pCa01rNDNWVTAxUVRaUVV6VklSRGhEWjBadk5tMHhiRnBTWWsxYU1IY3lSa3QzYmxSTVFVSlZOeXN6WVhGc1pFUjRaMlZ4ZGtKWVQwVnhTblFyY2xOVloySmxOeTlaWmxodE9FWlFZMWhFY2psb2NrTjRjbkZFVGpFM1ExQkhjazExZERkV1RIbG5SWEpOTkRZNFRtcHNVa3h6SzNCbGEwaEtNVTh5TTFaSVdXTmFSR1I2VkhKTVoyNTNTRGhoUmpVek9GZHRSRE5GTWtSU2NuY3piRlF6VVdJME5WSllWeXRPS3pWdU4yeG9TRElyWkdWVkswMUxZa1J4TDNoaVREWnRTMFE1UWtrMU5XNWhTbG8zUlRGemJVWktkVkpVZGpCM05UWk1lRGRKTUVGV05FbFRRblp6VDNCWGNFOUlWa0ZrTUdaTU4zWTFiekZFYW5aTUsweEhka1pQVkZBeVNTc3diQzhyUlhndk9WZFpZMVJFVjFSTWFHcHBhbVIyVkhGd2RFaEdSRTFYYTBGeWVteGlNRnB0UlVOUlJYWnhTV05FZEVncldHRktaVEZpYW1SWk9FNTNkMlp3T1ZKM0sxWlJNSFl3WVV0RVpGWlpObmxGTTJKdFJUSTNMMHQzZVZsYVRteEJTMEZ1TTJFMVdXZE5jbVJpZFZWcVQxVnVkM0kwWXpGcWRGaElRVmRFTms5cE56aHFVRWdyTUZacWVGcFVjbHAyWldaV1dEUlBUV3QwTWxCdVlrbHJZMmhSWVZoRUsyZ3JUVVpMUTJZM2VFUTRORWw2ZERkcFEzVXpURmxwS3pCT1ptWndNV29yV0hkalpHZHFOMk55YURScGRrNVlVVkJUUWxkeFVWaEROVUZqU25FMk1WbzJhelJRTVV4VVZYbFNSbFZ4YURsSFMyUm9XSEJXUVdSTlFWZFZVR013YkdvclNuZElaWGR1TVRFNVNWQmxhRkJwYTBSQldHdFhURUoxVlV0aldpdDZUbXRFUVVoeVRHc3lURlU1TVc0ck1rRmtRek0xTm5wVGFUQlNLMWs0TUZCSU0wdDZiSFl3UlRFMVMyRnlXa2hMWm5kdFNIbFphbXBMUzJ0dVpEWklhRTFtYWxGU01tUkVOVTFKVUdkeE5YWXJXbk5yWm1WR1NYaE1aRVJHZERnek5VRnZZblpIUWtnMUwwcDFUelpuTDI1QmFWUjVWemgxVjIxemJuWXdZVTVrUldKVVNGQnZVVlZZYm5OVFJtTkVVWGx3Y1U1TVZqUnpNV01yVVVWVE9IZHhPRUUwWkRsbUwwMDRWSGxqZW5wSk4wMWhUbFJIYlVab1NVcDFaMU5SYjNoeFMwVnRVVUZ6Vms1MmVHbE5RMk16ZFVaNFNuTnlSamxKTUM5NGVGbDVVbkpyVlZrdllUYzJhamhCWm5RNFoyNXpNbXhKUTNkelNsRm5RMHhsWXpZMU0zRjBWRGR3TkRkTFFraFJhMnB5UlhFM2IzZGFUWGhqTkhGaVFYZERlUzlPWldsVVRHSnNRMVJYUldrNFJXWkxTSGsyYWxob1JGTnNUekJQTDJGaFQxYzVkRWt2V0U1UFJFTm1TbXhQZDBodlJTdDNOM1V5YjNSR1JqWm9OVlJMWVdSeFYyOWhjMVpTYjJNeVIyVjRSME55THk5MVZIWnBSa1p6UkZKMGNIQm5iVVJ2V1haNlRESjNWbEZCUlhoYWFXWlBkVkZJUzJWMGNVMUpSek5JWlhaV1EwVmlRMnhxYjBWbFQzSlhaRUp5UW5GSE9YaHdRekpaU1dJeGNqTXlObFY1VG5WelVUSlNjRGt5YzJJcmNUSlhRbVZFT1V4NVptMDFibmRNVEZSMWRWQnBiRkZQSzNSSVIxWXpUeXROS3pOdk5sQnpjR05PWmxCWFpsZGphbXhyWWxvMFJVTjVjRVpGU1dremVrVnlNR0YzUTI5VFdsUm5PVTFMTlVGakswMVNabkJTWkdRemVHUmhVVWhVV21KcmNXNWtOSHBMS3paUGJtNUJlRlF4Y1UxbU5YRlVibWxWYkUxdmMyaDFVSE5xYXpWQlEwaDBkakl2Y3paWFFWcFdUV01yTkhneEwxVjFUVmx2VlRkWk9VcEtPV3NyWW1ONVducEdWVXhQTWt4SE5VeGtaMmRVYVRGcloybHJSRkZDYzFOM2RsQkJTRXhEVVhGaWRtSjFjMUJoUkhwWllrMDFTblpJUVU5NFJFOUtRV1Y2UTFWa2RrdHRPVGRSZUhST05XUmtSRXRCZUhscVdYSk5ZV1JSUW1OTFVYcFpZVUpyVHpJNFZqVjVZMDFtUXpoWGJWZGpaVFZVVUdjM0syWkpRVVJoWTFSVFYyVlZXV1pHS3pkUk9VdFpNMjFqTlRGdFdDOWxkMmhLVGpoQ05XOXRNRmxhWTBkUmRucG9kaXRXTnpCWFJscHZURnBuVEVKcWFWZzVTbWhsYTNaMlVXOU9hRFo0VUhod1JGWk9lV3d6VDNkMEswTjZXSGRSVkVwTGQxUk9SVVkxUVRJcmNHZEZWV0V6VVRaeWRESnpPVE5DWVdaSU5HZE5PSEUzUlhwUk9UWnlTVGRyU0V0RGNrUkhTMjk0UVhKdVJ6WXhUekUzZW1sck1pdHZkV05qUnk5dk5VcFhNazlDTldwUlNVdG5SR2R1U2xacGVYZG5OVlprVlRBNU56VldRamhNVUhCeksyaGtjMjlHTDNrNU9XTmlWeXRVZVhaMFlUTldZa3BpY0dSVk5uUnlUVXRIV2pkaldsWm1ZaTlQTmpBMlNpdHdkMXA1VjNGWWR6bDVRWEZUT0VoNFR6RkhUbFppYVZwdmJXRnZURVp4YjFCUVUzUlphME01Tm5SMVJFNDNiRFU1ZG1zMlkycERVV3hLTlZNeFJDdFhOVGR2UjFwdVpHaHNaa0V2V21odVl6Z3lRVGhHY201Tk0yd3pUa2hrTjJad2FrYzNXWEJhZW10d1RrVnRaV3ByTVhCT2NuZHhTVU4wYW5oc1JGSmlUamhMUTNCMFJYZzVTaTl0TlVwS1FVcEVSMkV6ZDFJek1UZGxkMWw1Y0dOTkt6Y3hUbEpDV0dsSE1HZHlabGt6Ym5kblNrVlNPVEpDUkZOcE4waDFNekUwUlZkUldrTlZhVzB4UjNRcmFrZzJUWFJLU2pOMmJtOVdlR1Y1YkhsNGNtdHplamxKUjNGdlJVbGxkMVZ5Y0dJMldrbGFSSEIzUzNGbGRWbG5ka01yWXowLjBFN3VlOGY2ekRYZlZldGNadHo0THBKbFAwTEZpcFYtVlhWNlFad0F4OTJiU1BOcmdiMnQ5V0tZbVZlOGtNcEs1TDVIX0NQWTcyb1ZVbTNHLTFMN25R"><input type="hidden" name="_eventId" value="submit"><input type="hidden" name="geolocation"><input class="btn-ingresar" name="submit" accesskey="l" value="INICIAR SESIÓN" tabindex="6" type="submit"><!--div class="well well-lg hidden-xs" th:if="${pac4jUrls}">
    <div id="list-providers">
        <h4 id="medio2" class="titulo-login">También puedes iniciar sesión con:</h3>
            <div th:each="entry: ${pac4jUrls}" th:switch="${entry.type}">
                <a class="btn btn-block btn-social txt_info_cu" style="text-align:center"
                   th:classappend="'btn-' + ${entry.type}"
                   th:href="${entry.redirectUrl}"
                   th:inline="text"
                   th:title="${entry.name}">
					<span>INGRESAR con tu</span>
					<img src="/cas/images/logocu.png" style="height:40px" alt="ClaveUnica">
                    
                </a>
            </div>
       

    </div>
</div--></section>
    </form>
</div></div>
```

## Buscar todas las pertinencias
```html
<button class="boton-buscar" type="submit"><span class="boton-buscar__text">Buscar</span></button>
```

## JSON rellenado tabla (Es muy grande eso si)
**https://pertinencia.sea.gob.cl/api/proceso/buscarcp**
### FORMATO INFORMACION DEL JSON
```json
[
  {
    "qidProcess": "1F8DEDDD-2046-4A80-8E6D-00D81F5B335A",
    "name": "PROYECTO DE REUTILIZACIÓN DE RILES EN RIEGO DE CAMINOS INTERNOS",
    "presentationDate": "23-04-2026",
    "dateResponse": "",
    "correlativeId": "PERTI-2026-5399",
    "titularName": "HIF CHILE 1 SpA",
    "projectType": {
      "id": "",
      "valor": "Modificación con RCA"
    },
    "state": {
      "id": "",
      "valor": "En análisis"
    },
    "primaryTypologyName": "k.1) Instalaciones fabriles sobre 2.000 KVA",
    "regiones": [
      {
        "nombre": "Región de Magallanes y Antártica Chilena",
        "codigo": "12",
        "orden": "17"
      }
    ],
    "comunas": [
      {
        "nombre": "Punta Arenas",
        "codigo": "12101",
        "orden": "1"
      }
    ]
  },
  {
    "qidProcess": "0D1A7CA8-7A31-4FFD-BD75-CBD88CBB746A",
    "name": "Stripcenter y Bodegas Cosmito",
    "presentationDate": "23-04-2026",
    "dateResponse": "",
    "correlativeId": "PERTI-2026-5362",
    "titularName": "Joaquín Horacio Herrera Villagrán",
    "projectType": {
      "id": "",
      "valor": "Proyecto nuevo"
    },
    "state": {
      "id": "",
      "valor": "En análisis"
    },
    "primaryTypologyName": "e.6) Estaciones de servicio cuya capacidad de almacenamiento sea igual o superior a 850.000 L.",
    "regiones": [
      {
        "nombre": "Región del Biobío",
        "codigo": "08",
        "orden": "12"
      }
    ],
    "comunas": [
      {
        "nombre": "Penco",
        "codigo": "08107",
        "orden": "1"
      }
    ]
  },
```
### CURL
curl.exe ^"https://pertinencia.sea.gob.cl/api/proceso/buscarcp^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-CSRF-TOKEN: lbrHoyiwvByir8fevStVXzGF7ZNlxNKoCsta4BWl^" ^
  -H ^"X-XSRF-TOKEN: eyJpdiI6IlVHOXBoNHBBWk1ENG9oVTBGNDZJR1E9PSIsInZhbHVlIjoieWd0NVI4QThlZkVITjhvOXR2M0J3TlBHczZ6ZFVXYTFxbWFyaG9QQzh2RThIcFJ2LzZOc3hGV1VZZkMwRDdxVXI1dWRYVTRscHROMU12akMwbnllSFVBRFVXNExrS08wdXY5RzU4OTRGYXNvaWFXVi9GWW9KWjRQVjJoUUNtQmQiLCJtYWMiOiIwMGM4NzVjOTllMGI4N2RkYWE1N2VlMWYwNTE5Y2NlZDQ1ZDlhNzI5ZDM5Mzg2MmIyZDc4ZmVjOTIxM2NlMzA4IiwidGFnIjoiIn0=^" ^
  -H ^"Origin: https://pertinencia.sea.gob.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://pertinencia.sea.gob.cl/^" ^
  -H ^"Cookie: _ga_S1X3MHJQMV=GS2.1.s1776656394^$o2^$g1^$t1776658301^$j60^$l0^$h0; _ga=GA1.3.1088673434.1776648208; _ga_V50KN47LXK=GS2.1.s1776656441^$o1^$g0^$t1776656443^$j58^$l0^$h0; CASAuth=be91f21d6412b08404f86ce33c1371ce; cookiesession1=678B2891A24B83087510548C378EE18A; XSRF-TOKEN=eyJpdiI6IlVHOXBoNHBBWk1ENG9oVTBGNDZJR1E9PSIsInZhbHVlIjoieWd0NVI4QThlZkVITjhvOXR2M0J3TlBHczZ6ZFVXYTFxbWFyaG9QQzh2RThIcFJ2LzZOc3hGV1VZZkMwRDdxVXI1dWRYVTRscHROMU12akMwbnllSFVBRFVXNExrS08wdXY5RzU4OTRGYXNvaWFXVi9GWW9KWjRQVjJoUUNtQmQiLCJtYWMiOiIwMGM4NzVjOTllMGI4N2RkYWE1N2VlMWYwNTE5Y2NlZDQ1ZDlhNzI5ZDM5Mzg2MmIyZDc4ZmVjOTIxM2NlMzA4IiwidGFnIjoiIn0^%^3D; sistema_consulta_de_pertinencia_session=T4WkAtdQUzcJjaeYZiravZvXOAU3eM5IwK6hE0Nm; _ga_BCSPV16K2P=GS2.1.s1776956989^$o1^$g1^$t1776957068^$j59^$l0^$h0; _gid=GA1.3.1850045353.1776956990^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"^{^\^"pertinenciaFilter^\^":^{^\^"estado^\^":^\^"^\^",^\^"fechaPresentacionDesde^\^":^\^"^\^",^\^"fechaPresentacionHasta^\^":^\^"^\^",^\^"fechaRespuestaDesde^\^":^\^"^\^",^\^"fechaRespuestaHasta^\^":^\^"^\^",^\^"id^\^":^\^"^\^",^\^"idLocalidades^\^":^[^],^\^"idTipologias^\^":^[^],^\^"nombre^\^":^\^"^\^",^\^"tipoProyecto^\^":^\^"^\^",^\^"titular^\^":^\^"^\^",^\^"regiones^\^":^[^],^\^"comunas^\^":^[^],^\^"excelFull^\^":false,^\^"activarFiltrosAvanzados^\^":false,^\^"mainRowHeight^\^":84,^\^"advancedRow1Height^\^":72,^\^"advancedRow3Height^\^":72^}^}^"