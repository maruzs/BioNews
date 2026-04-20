# LINK
https://www.portaljudicial1ta.cl/sgc-web/consulta-causa.html
# ANALISIS
Carga con JS, hay un formulario donde no hay que seleccionar nada, solo darle a "buscar" para que se muestren todas las causas en una tabla, la primera siempre es la mas nueva.
La informacion de la tabla se obtiene de un json
## INFO A OBTENER
Tipo de causa, Rol, Fecha de ingreso, Caratula, Estado, Link (href en el rol)
# ESTRUCTURA PAGINA E INFORMACION
## Formulario y boton
```html
<a id="btnBuscar" class="btn btn-primary btn-buscar">buscar</a>
``` 
## Tabla de causas
```html
<table id="tabla-consulta-causa" class="table table-striped table-hover dataTable no-footer" role="grid" aria-describedby="tabla-consulta-causa_info">
<thead>
    <tr role="row"><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="Tipo de Causa: activate to sort column ascending">Tipo de Causa</th><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="ROL: activate to sort column ascending">ROL</th><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="Fecha ingreso: activate to sort column ascending">Fecha ingreso</th><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="Carátula: activate to sort column ascending">Carátula</th><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="Estado Subtipo: activate to sort column ascending">Estado Subtipo</th><th style="width: 0px;" class="sorting" tabindex="0" aria-controls="tabla-consulta-causa" rowspan="1" colspan="1" aria-label="Estado: activate to sort column ascending">Estado</th></tr>
    </thead>
``` 

## JSON GENERADO AL CLICKEAR BUSCAR
https://www.portaljudicial1ta.cl/sgc-ws/rest/consulta-causa/get-consulta-causa
El problema es que viene muy desordenado sin saltos, todo dentro de response 'JSON'
Ademas son todas las causas, no hay paginacion
```json
response	
'[{"caratula":"Comunidad Indígena Colla Tata Inti del Pueblo de Los Loros  con Servicio de Evaluación Ambiental ","estado":"En tramitación ( Espera de Informe) ","fechaCausa":"27-03-2026 03:00","idCausa":"a4f0c42b-a984-413c-9132-72ac14f22bec","idEstado":0,"idPendiente":0,"numeroRol":"R-156-2026","realizada":false,"subTipoCausa":"Espera de Informe","tipoCausa":"Reclamación"},{"caratula":"Comunidad Indígena Ancestral Wara QDA. Chañaral Alto y sus quebradas Copiapó-Diego de Almagro con Superintendencia del Medio Ambiente.","estado":"En tramitación ( Espera de Informe) ","fechaCausa":"23-03-2026 03:00","idCausa":"f3846c3e-d54e-4323-a55d-4204a5a3fc27","idEstado":0,"idPendiente":0,"numeroRol":"R-155-2026","realizada":false,"subTipoCausa":"Espera de Informe","tipoCausa":"Reclamación"},'
```