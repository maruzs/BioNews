# LINK
https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php
# ANALISIS
La tabla se carga de manera dinamica
La tabla se llena con informacion de un JSON
## INFO A OBTENER
Nombre del proyecto, Fecha de ingreso, Estado del proyecto, link a detalle
# ESTRUCTURA PAGINA E INFORMACION
## JSON
https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php
Ejemplo de una fila de la tabla
```json
{
  "status": true,
  "data": [
    {
      "EXPEDIENTE_ID": "2168238865",
      "EXPEDIENTE_NOMBRE": "Sistema de Generaci�n Solar Fotovoltaica Loma Verde",
      "EXPEDIENTE_URL_PPAL": "https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168238865",
      "EXPEDIENTE_URL_FICHA": "https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168238865&modo=ficha",
      "WORKFLOW_DESCRIPCION": "DIA",
      "REGION_NOMBRE": "Regi�n de Valpara�so",
      "COMUNA_NOMBRE": "Algarrobo",
      "TIPO_PROYECTO": "c",
      "RAZON_INGRESO": "Ingreso por tipolog�a (art. 3 del D.S. N�40)",
      "TITULAR": "KSR SEIS SpA",
      "INVERSION_MM": "1.3E+8",
      "INVERSION_MM_FORMAT": "130,0000",
      "FECHA_PRESENTACION": "1776462123",
      "FECHA_PRESENTACION_FORMAT": "17/04/2026",
      "ESTADO_PROYECTO": "En Admisi�n",
      "ENCARGADO": "",
      "ACTIVIDAD_ACTUAL": "",
      "FECHA_PLAZO": "",
      "FECHA_PLAZO_FORMAT": "",
      "ACCIONES": "",
      "LINK_MAPA": {
        "SHOW": true,
        "URL": "/mapa/visualizacion/PuntoRepresentativo/index.php?idExpediente=2168238865",
        "IMAGE": "map-invalid.jpg"
      },
      "DESCRIPCION_TIPOLOGIA": "Centrales generadoras de energ�a mayores a 3 MW",
      "DIAS_LEGALES": "1",
      "SUSPENDIDO": "Activo",
      "VER_ACTIVIDAD": ""
    },
```
## HTML
```html
<thead>
    <tr><th data-dt-column="0" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Nombre del Proyecto: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Nombre del Proyecto</span><span class="dt-column-order"></span></th><th data-dt-column="1" class="dt-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Tipo de Presentación: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Tipo de Presentación</span><span class="dt-column-order"></span></th><th data-dt-column="2" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Región: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Región</span><span class="dt-column-order"></span></th><th data-dt-column="3" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Comuna: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Comuna</span><span class="dt-column-order"></span></th><th data-dt-column="4" class="dt-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Tipo de Proyecto: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Tipo de Proyecto</span><span class="dt-column-order"></span></th><th data-dt-column="5" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Razón de Ingreso: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Razón de Ingreso</span><span class="dt-column-order"></span></th><th data-dt-column="6" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Titular: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Titular</span><span class="dt-column-order"></span></th><th data-dt-column="7" class="dt-head-center dt-body-right dt-orderable-asc dt-orderable-desc dt-type-numeric" rowspan="1" colspan="1" aria-label="Inversión (MMU$): Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Inversión (MMU$)</span><span class="dt-column-order"></span></th><th data-dt-column="8" class="dt-head-center dt-body-right dt-orderable-asc dt-orderable-desc dt-ordering-desc dt-type-numeric" rowspan="1" colspan="1" aria-sort="descending" aria-label="Fecha Presentación Fecha de Ingreso (1): Activate to remove sorting" tabindex="0"><span class="dt-column-title" role="button">Fecha Presentación Fecha de Ingreso (1)</span><span class="dt-column-order"></span></th><th data-dt-column="9" class="dt-head-center dt-body-right dt-orderable-none dt-type-numeric" rowspan="1" colspan="1" aria-label="Días Legales Transcurridos"><span class="dt-column-title">Días Legales Transcurridos</span><span class="dt-column-order"></span></th><th data-dt-column="10" class="dt-head-center dt-orderable-asc dt-orderable-desc" rowspan="1" colspan="1" aria-label="Estado del Proyecto: Activate to sort" tabindex="0"><span class="dt-column-title" role="button">Estado del Proyecto</span><span class="dt-column-order"></span></th><th data-dt-column="14" class="dt-head-center dt-orderable-none" rowspan="1" colspan="1" aria-label="Acciones"><span class="dt-column-title">Acciones</span><span class="dt-column-order"></span></th></tr></thead>
<tr><td class="dt-head-center"><a class="color-primary" href="https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168238865" target="_new">
                                        Sistema de Generación Solar Fotovoltaica Loma Verde
                                    </a></td><td class="dt-head-center dt-center">DIA</td><td class="dt-head-center">Región de Valparaíso</td><td class="dt-head-center">Algarrobo</td><td class="dt-head-center dt-center"><span data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Centrales generadoras de energía mayores a 3 MW">c</span></td><td class="dt-head-center">Ingreso por tipología (art. 3 del D.S. N°40)</td><td class="dt-head-center">KSR SEIS SpA</td><td class="dt-head-center dt-body-right dt-type-numeric">130,0000</td><td class="dt-head-center dt-body-right dt-type-numeric sorting_1">17/04/2026</td><td class="dt-head-center dt-body-right dt-type-numeric">1</td><td class="dt-head-center">En Admisión</td><td class="dt-head-center"><div class="sg-action-button d-flex">
    <button class="btn btn-primary sg-btn-table" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Ver Proyecto"><a href="https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2168238865" target="_blank"><img class="sg-icon" src="../img/icons/go_to_project.svg"></a></button><button class="btn sg-btn-table sg-icon-map" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Ver en Mapa" onclick="window.open('/mapa/visualizacion/PuntoRepresentativo/index.php?idExpediente=2168238865', 'mapa')"><img class="sg-icon" src="../template/default/images/html/map-invalid.jpg"></button>
</div></td></tr>
```