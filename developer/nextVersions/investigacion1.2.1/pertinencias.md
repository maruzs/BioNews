# Link todas las pertinencias
https://pertinencia.sea.gob.cl/
Es dinamica pero la informacion se obtiene desde un json
https://pertinencia.sea.gob.cl/api/proceso/buscarcp
Que tiene las pertinencias en el siguiente formato
```json
[
  {
    "qidProcess": "75A63D22-613F-495E-9EC9-B4C5ABE5C394",
    "name": "CARTA DE PERTINENCIA SEIA",
    "presentationDate": "25-04-2026",
    "dateResponse": "",
    "correlativeId": "PERTI-2026-5549",
    "titularName": "Luis Alberto Hernández Hormazábal",
    "projectType": {
      "id": "",
      "valor": "Proyecto nuevo"
    },
    "state": {
      "id": "",
      "valor": "En análisis"
    },
    "primaryTypologyName": "g.2) Proyecto de desarrollo turístico (destinados en forma permanente al uso habitacional y/o de equipamiento para fines turísticos) que contemplen al menos una de las siguientes características:",
    "regiones": [
      {
        "nombre": "Región de La Araucanía",
        "codigo": "09",
        "orden": "13"
      }
    ],
    "comunas": [
      {
        "nombre": "Angol",
        "codigo": "09201",
        "orden": "1"
      }
    ]
  },
```
# Formato link detalles pertinencias
https://pertinencia.sea.gob.cl/api/public/expediente/{correlativeId}
* ejemplos:
    https://pertinencia.sea.gob.cl/api/public/expediente/PERTI-2026-5549

Ese es el link oficial, pero cada uno de esos tiene tambien un JSON que se obtiene de aqui
https://pertinencia.sea.gob.cl/api/proceso/obtener-pertinencia/{correlativeId}
* Ejemplo
    https://pertinencia.sea.gob.cl/api/proceso/obtener-pertinencia/PERTI-2026-5549

Este seria el json de esa pertinencia

```json
{
  "cp_nombre": "CARTA DE PERTINENCIA SEIA",
  "cp_descripcion": "DETERMINAR LA NO IMPLICANCIA DE INGRESO OBLIGATORIO AL SEIA",
  "nombre_titular": "Luis Alberto Hernández Hormazábal",
  "id_project_type": "A47D5714-C6E7-7D74-E053-FA000F0A3F38",
  "project_type": "Proyecto nuevo",
  "folioExpediente": "2026-09-114",
  "estado": "En análisis",
  "qid_process": "75A63D22-613F-495E-9EC9-B4C5ABE5C394",
  "user": "2166940487",
  "qidRecord": "FB537320-E536-4756-B420-A4B003F671C9",
  "extended": [
    {
      "label": "location",
      "value": "LT.C LOS CONFINESLTB-4 EX.PC10 .PTE"
    },
    {
      "label": "attendantId",
      "value": "2159860335"
    },
    {
      "label": "antiguedadRCA",
      "value": "false"
    },
    {
      "label": "titularCoincideRepLegal",
      "value": "true"
    },
    {
      "label": "mapPoints",
      "value": ""
    },
    {
      "label": "montoInversion",
      "value": "876.649"
    },
    {
      "label": "hasFisicalDocument",
      "value": "false"
    },
    {
      "label": "modifyCpId",
      "value": "5EC4C4B5-4449-4B0E-BF37-DAAEA36A9DD8"
    },
    {
      "label": "workPartDescription",
      "value": "Proyecto contempla cierres provisorios perimetrales, posterior movimiento de tierra para escarpes y mejoramiento de suelo, luego se ejecutan fundaciones de H.A. y estructura soportante de acero y metalcon, a continuación se procede a cerrar los muros y cubiertas de cada unidad junto con sus cierres interiores, finalmente se ejecutan las instalaciones, artefactos y terminaciones, por último se hace limpieza a obra y retiro de escombros, para recepción final de obras ante la direcciones obras municipales correspondiente.-"
    },
    {
      "label": "pertinenciaAsociada",
      "value": "false"
    },
    {
      "label": "idSignature",
      "value": "2142639017.0000"
    },
    {
      "label": "attendantName",
      "value": "Doris Ubilla Saldías"
    }
  ],
  "roles": [
    {
      "idPerfil": "2166940487",
      "idRol": "5",
      "nombrePerfil": "Titular"
    }
  ],
  "tipologias": [
    {
      "codigoTipologia": "502",
      "esPrimaria": 1,
      "nombreTipologia": "Proyecto de desarrollo turístico (destinados en forma permanente al uso habitacional y/o de equipamiento para fines turísticos) que contemplen al menos una de las siguientes características:"
    }
  ],
  "regiones": [
    {
      "codigo": "09",
      "nombre": "Región de La Araucanía",
      "orden": "13"
    }
  ]
}
```

Y de ese json nos interesaria obtener lo siguiente
1. Estado
2. qidProcess

Con el qidProcess podemos ir a lo siguiente
https://pertinencia.sea.gob.cl/api/documentos/getExpedienteFirmado/{qidProcess}
y de ahi obtener lo siguiente
https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId={docId}
ejemplo:
    <a href=https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId=2026/04/25/4214-1dfc-4a16-a02e-8e70f9e5695b target=\"_blank\"> Consulta de Pertinencia </a>
docId no existe, es solo una generalizacion, pero lo que importa es todo el href

Ese  link nos lleva directo al documento de la pertinencia

Entonces en la interfaz de favoritos deberiamos hacer lo siguiente
1. Dividirlo en pertinencias y SNIFA
en pertinencias debemos mostrar las filas con la siguiente informacion, de la mas nueva a la mas vieja
Nombre ("cp_nombre")
Estado ("estado")
Ver PDF (https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId={docId})
Ver Expediente (https://pertinencia.sea.gob.cl/api/proceso/obtener-pertinencia/{correlativeId})
