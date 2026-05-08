# IGNORAR ESTE DOCUMENTO - NO LEER NO ES PARA DESARROLLAR ES SOLO PARA MI ANALISIS E INVESTIGACION

Deberemos descargar nuevamente las pertinencias ya que quiero que ahora la tabla de pertinencia incluyan la categoria economica (a-u) y el tipo de proyecto.

Recuerda que el mapeo de categoria economica es:
a -> Infraestructura Hidráulica
b -> Energía
c -> Energía
d -> Energía
e -> Infraestructura de Transporte
f -> Infraestructura Portuaria
g -> Inmobiliarios
h -> Inmobiliarios
h2 -> Instalaciones fabriles varias (tambien puede ser h.2 o h.2)
i1 -> Minería (tambien puede ser i.1)
j1 -> Energía (tambien puede ser j.1)
j3 -> Minería (tambien puede ser j.3 o j3)
j4 -> Otros (tambien puede ser j.4)
k -> Instalaciones fabriles varias
l -> Agropecuario
m -> Forestal
n -> Pesca y Acuicultura
ñ -> Otros
o -> Saneamiento Ambiental
p -> Otros
q -> Agropecuario
r -> Otros
s -> Otros
t -> Equipamiento
u -> Otros

Lo bueno es que puedo descargar un documento que tenga todas las pertinencias en formato JSON y solo deberemos crear un script para procesarlo.
Ejemplo JSON

```json
{
    "qidProcess": "B8145126-5510-4C23-8838-8518D2D26CF2",
    "name": "AUMENTO DE VIVIENDAS PARQUE BELLAVISTA CURICO",
    "presentationDate": "08-05-2026",
    "dateResponse": "",
    "correlativeId": "PERTI-2026-6193",
    "titularName": "Inmobiliaria Independencia SpA",
    "projectType": {
      "id": "",
      "valor": "Modificación con RCA"
    },
    "state": {
      "id": "",
      "valor": "En análisis"
    },
    "primaryTypologyName": "g.1) Proyectos de desarrollo urbano que contemplen obras de edificación y/o urbanización cuyo destino sea habitacional, industrial y/o de equipamiento de acuerdo a lo siguiente:",
    "regiones": [
      {
        "nombre": "Región del Maule",
        "codigo": "07",
        "orden": "10"
      }
    ],
    "comunas": [
      {
        "nombre": "Curicó",
        "codigo": "07301",
        "orden": "1"
      }
    ]
  },
```

Debemos tener la exacta misma tabla que actualmente (formato actual de las columnas) pero agregarle lo siguiente:
nueva columna 'tipo_proyecto' que se obtiene de este apartado de los JSON:

```json
tipo_proyecto -> "projectType": {
      "id": "",
      "valor": "Modificación con RCA"
    },
```

Donde el tipo_proyecto es lo que esta en "valor" del objeto "projectType", o null si no existe.

nueva columna 'categoria_economica' que se obtiene de este apartado de los JSON:

```json
"primaryTypologyName": "g.1) Proyectos de desarrollo urbano que contemplen obras de edificación y/o urbanización cuyo destino sea habitacional, industrial y/o de equipamiento de acuerdo a lo siguiente:",
```

De "primaryTypologyName": deberemos extraer la primera letra o subcategoria que esta antes del punto, osea en este caso 'g.1' y transformarlo a 'g', lo cual segun el mapeo significa 'Inmobiliarios'.

Hay casos como h que tiene h2 y son distintas categorias, en esos casos debera ver lo que esta despues del punto (ej. 'h.2') y transformarlo a 'h2', lo cual segun el mapeo significa 'Instalaciones fabriles varias'
