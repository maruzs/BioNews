# LINK
https://pertinencia.sea.gob.cl/api/public/buscador
# ANALISIS
Esta pagina obtiene un json directamente con la informacion
Dentro de ese json podemos ver las fechas e ID de pertinencia con la cual se puede acceder a los detalles
El json es muy pesado(en la fase de investigacion descargue uno y pesaba 23mb aprox)
## INFO A OBTENER
Nombre pertinencia, Fecha de generacion, Estado, Tipo proyecto, Region
# ESTRUCTURA PAGINA E INFORMACION
Es necesario un click en el boton buscar para que se genere el json con la informacion
## TABLA DE PERTINENCIAS
Boton buscar que carga json
```html
<button class="botonBuscar">Buscar </button>
```
La paginacion de la tabla no importa ya que el json obtiene toda la informacion

ejemplo de json (una pertinencia)
```json
[
  {
    "qidProcess": "18D2B89A-9403-4B79-8B35-C7E61C044AC9",
    "name": "PROYECTO INFINITO - VIÑA DEL MAR, VALPARAÍSO",
    "presentationDate": "20-04-2026",
    "dateResponse": "",
    "correlativeId": "PERTI-2026-5245",
    "titularName": "Sebastian Merfa",
    "projectType": {
      "id": "",
      "valor": "Proyecto nuevo"
    },
    "state": {
      "id": "",
      "valor": "En análisis"
    },
    "primaryTypologyName": "g.1) Proyectos de desarrollo urbano que contemplen obras de edificación y/o urbanización cuyo destino sea habitacional, industrial y/o de equipamiento de acuerdo a lo siguiente:",
    "regiones": [
      {
        "nombre": "Región de Valparaíso",
        "codigo": "05",
        "orden": "8"
      }
    ],
    "comunas": [
      {
        "nombre": "Viña del Mar",
        "codigo": "05109",
        "orden": "1"
      }
    ]
  },
```
## LINK DETALLE/EXPEDIENTE DE UNA PERTINENCIA
https://pertinencia.sea.gob.cl/api/public/expediente/{correlativeId}

https://pertinencia.sea.gob.cl/api/public/expediente/PERTI-2021-9316
ejemplo:
https://pertinencia.sea.gob.cl/api/public/expediente/PERTI-2026-5245