# LINK
https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial
# ANALISIS
La pagina es estatica y no obtiene informacion de JSON ni ninguna api.
Hay que filtrar de la siguiente manera
Jurisdiccion -> Corte Suprema
Sala -> Tercera sala
Tipo noticia -> Todas
en titulo y fecha no debe haber nada
luego se le debe dar al boton 'filtrar'

Eso en network genera un POST llamado getNewsForFilters, que es un html Ajax/News con la informacion mas ordenada
## INFO A OBTENER
Nos interesa obtener Nombre, link al detalle, fecha, debera revisar todas las paginas dentro de la informacion filtrada
# ESTRUCTURA PAGINA E INFORMACION
## Pagina filtrado
```html
<form method="post" accept-charset="utf-8" name="form-filter" id="form-filter" class="col-12" action="/prensa-y-comunicaciones/noticias-del-poder-judicial"><div style="display:none;"><input type="hidden" name="_method" value="POST"><input type="hidden" name="_csrfToken" autocomplete="off" value="53d4b559e557ff83a1e50e7b748414d10553754d01a5e2b7054f7cbd9c8cdb13c2a64b03faf3d0a2826b5476eebfc5f0fc9ed4d617cc70739b43115af9ea3ab6"></div>
                    <div class="form-row">

                        <div class="form-group col-sm-12 col-lg-2">
                            <label for="jurisdiction_id">Jurisdicción</label>
                            <div class="input select"><select name="jurisdiction_id" class="form-control" id="jurisdiction-id"><option value="">Todas</option><option value="1">C.A de Arica</option><option value="4">C.A de Iquique</option><option value="5">C.A de Antofagasta</option><option value="6">C.A de Copiapó</option><option value="7">C.A de La Serena</option><option value="8">C.A de Valparaíso</option><option value="9">C.A de Santiago</option><option value="10">C.A de San Miguel</option><option value="11">C.A de Rancagua</option><option value="12">C.A de Talca</option><option value="13">C.A de Chillán</option><option value="14">C.A de Concepción</option><option value="15">C.A de Temuco</option><option value="16">C.A de Valdivia</option><option value="17">C.A de Puerto Montt</option><option value="18">C.A de Coyhaique</option><option value="19">C.A de Punta Arenas</option><option value="22">Corte Suprema</option></select></div>                        </div>
                        <div class="form-group col-sm-12 col-lg-2">
                            <label for="sala">Sala</label>
                            <div class="input select"><select name="sala" class="form-control" id="sala"><option value="">Seleccione...</option><option value="Primera sala">Primera sala</option><option value="Segunda sala">Segunda sala</option><option value="Tercera sala">Tercera sala</option><option value="Cuarta sala">Cuarta sala</option></select></div>                        </div>


                        <div class="form-group col-sm-12 col-lg-2">
                            <label for="new_type_id">Tipo noticia</label>
                            <div class="input select"><select name="new_type_id" class="form-control" id="new-type-id"><option value="">Todas</option><option value="2">Noticias de la Fiscalia Judicial</option><option value="4">Poder Judicial</option><option value="6">Emergencia Sanitaria</option><option value="21">Plan Estratégico</option><option value="22">Lenguaje Claro</option><option value="48">Noticias sobre fallos</option><option value="49">Noticias Fallos Corte Suprema</option></select></div>                        </div>

                        <div class="form-group col-sm-12 col-lg-2">
                            <label for="title">Título</label>
                            <input type="text" class="form-control" name="title" id="title">
                        </div>

                        <div class="form-group col-sm-12 col-lg-2">
                            <label for="advance_daterange">Fecha</label>
                            <input type="text" class="form-control" name="advance_daterange" id="advance-daterange" autocomplete="off">
                        </div>

                        <div class="form-group col-sm-12 col-lg-2 d-flex align-items-end">
                            <button type="button" id="btn-filter" name="inputZip" class="btn btn-primary btn-sm"> Filtrar </button>
                        </div>

                    </div>

                </form>
```

## cURL Archivo Networks
curl.exe ^"https://www.pjud.cl/ajax/news/getNewsForFilters^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0^" ^
  -H ^"Accept: */*^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Referer: https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----geckoformboundaryf50ef0100dccfcdc8a3fa04370eefbfa^" ^
  -H ^"Origin: https://www.pjud.cl^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Cookie: f5_cspm=1234; _ga_RNDXMD9BB1=GS2.1.s1776443190^$o1^$g1^$t1776443293^$j30^$l0^$h0; _ga=GA1.2.1833301768.1776443190; _ga_WKMRR3GSBD=GS2.1.s1776974741^$o2^$g1^$t1776975941^$j60^$l0^$h0; csrfToken=53d4b559e557ff83a1e50e7b748414d10553754d01a5e2b7054f7cbd9c8cdb13c2a64b03faf3d0a2826b5476eebfc5f0fc9ed4d617cc70739b43115af9ea3ab6; TS6add129e027=08a336eaa2ab20006bc0fa6b1feba1c970b785197f07605a2cc897f691b0da5d1ffbeaf7b4351ea1084bc7b0d4113000c3f0b9ea75cd1b0b5d38bd63b394190b23dbf09b5b0929225157bf5edb3b356bc219f703704b7dbdc81ceacdbdb1d986; _gid=GA1.2.937523187.1776974742; _gat_gtag_UA_179189041_1=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"Priority: u=0^" ^
  --data-binary ^
  ^"------geckoformboundaryf50ef0100dccfcdc8a3fa04370eefbfa^

Content-Disposition: form-data; name=^\^"id_jurisdiction^\^"^

^

22^

------geckoformboundaryf50ef0100dccfcdc8a3fa04370eefbfa^

Content-Disposition: form-data; name=^\^"sala^\^"^

^

Tercera sala^

------geckoformboundaryf50ef0100dccfcdc8a3fa04370eefbfa--^

^"

## HTML pagina Ajax generada mostrada en network
https://www.pjud.cl/ajax/news/getNewsForFilters
```html
<div class="container clearfix">
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/142664">
                        <h5>Corte Suprema fija el alcance del artículo 3°, letra d) del Decreto Ley N°211, que sanciona el tipo infraccional conocido como ‘interlocking horizontal directo’  &nbsp;</h5>
                        <small class="text-muted pull-right">02-03-2026 10:03</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/140986">
                        <h5>Corte Suprema acoge recurso de protección y ordena a Fonasa estudiar antecedentes de pareja del mismo sexo y decidir si procede ingreso al programa de fertilización asistida institucional</h5>
                        <small class="text-muted pull-right">03-02-2026 12:02</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/138356">
                        <h5>Corte Suprema rechaza recurso de protección contra Isapre por desafiliar a cotizante que viajó al extranjero mientras hacía uso de&nbsp; licencia médica</h5>
                        <small class="text-muted pull-right">19-12-2025 12:12</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/138076">
                        <h5>Corte Suprema rechaza recurso de protección de funcionario municipal destituido por hacer uso de licencia médica para viajar al extranjero</h5>
                        <small class="text-muted pull-right">17-12-2025 12:12</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/133057">
                        <h5>Corte Suprema acoge recurso de protección y ordena bloquear acceso a sitios web de apuestas deportivas ilegales</h5>
                        <small class="text-muted pull-right">30-09-2025 04:09</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/130188">
                        <h5>Corte Suprema acoge casación y ordena reparación de daño ambiental en humedal Teja Sur</h5>
                        <small class="text-muted pull-right">14-08-2025 12:08</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/127052">
                        <h5>Corte Suprema confirma multa aplicada por TLDC por entrega de información incompleta en fusión de empresas de producción audiovisual</h5>
                        <small class="text-muted pull-right">09-06-2025 01:06</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/126855">
                        <h5>Corte Suprema acoge queja y ordena a Ministerio Público entregar información solicitada por Ley de Transparencia</h5>
                        <small class="text-muted pull-right">05-06-2025 01:06</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/126292">
                        <h5>Corte Suprema acoge reclamación y ordena medidas de reparación por abuso de posición dominante de CDF</h5>
                        <small class="text-muted pull-right">27-05-2025 01:05</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/124697">
                        <h5>Corte Suprema acoge reclamo de ilegalidad por ampliación de helipuerto en la comuna de Huechuraba</h5>
                        <small class="text-muted pull-right">23-04-2025 12:04</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/122928">
                        <h5>Causas Tercera Sala de la Corte Suprema</h5>
                        <small class="text-muted pull-right">18-03-2025 09:03</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/121605">
                        <h5>Causas Tercera Sala de la Corte Suprema</h5>
                        <small class="text-muted pull-right">19-02-2025 09:02</small>
                    </a>
                    
                </div>
        
                <div class="row mb-2 col-12 jtpaginators jtpagitem_1 ">
                    <a class="col-12 jt-result-item" href="https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial/121585">
                        <h5>Causas Tercera Sala de la Corte Suprema</h5>
                        <small class="text-muted pull-right">18-02-2025 08:02</small>
                    </a>
                    
                </div>
        
        <div class="d-flex justify-content-center text-center">
            Página:
            <select id="paginanew">

                                <option value="1" selected="selected">
                        1</option>
                                    
            </select>
        </div>
    
<script type="text/javascript">
    $( "#paginanew" ).change(function() {
        jtpaginator($("#paginanew").val());
    });
</script>    </div>
```