# PROYECTO
Programa web de scraping de informacion medioambiental desde paginas oficiales

# IDEA GENERAL
Un programa desktop que muestre un dashboard principal con la ultima informacion sobre causas, pertinencias, sancionatorios, fiscalizaciones, ingresos en admisibilidad y noticias.

El dashboard principal debe mostrar solo informacion sobre temas legales, no noticias, esas se encontraran en otra pestana.

## PESTANAS

1. Pagina principal
Aqui se mostrara todo lo ultimo (Excepcion de las noticias) en una tabla que muestre lo siguiente
Nombre, estado, fecha de actualizacion, link al detalle
2. Noticias
Noticias de los ultimos 3 dias de diversas fuentes en un formato de tarjetas con
imagen, fecha, nombre y que al clickear permita ir al link de detalles de la noticia
3. Por pagina
Cada pagina de informacion legal tendra su apartado donde se pueda ver la informacion de los ultimos x dias

## Funcionamiento
La informacion se actualizara cada vez que se inicie la pagina o se clickee el boton "Actualizar".
La actualizacion consiste en la activacion de scrapers de ciertas paginas, que revisen si hubo cambios desde la ultima actualizacion, y en caso de existir se debera obtener la nueva informacion, en caso de que no, todo se mantendra igual.

### No definido aun
Sobre la informacion antigua tengo 2 opciones, que solo se borre lo que ya fue revisado y lo que no haya sido revisado en los ultimos X dias. (por ejemplo 10 dias).

Que cada vez que se actualice se borre la instancia de informacion mas antigua, por ejemplo:
tenemos un maximo 3 dias [lunes, martes, miercoles], cada uno con su informacion y noticias, y yo el jueves abro el programa o actualizo y ahora seria asi [martes, miercoles, jueves], si actualizo mas de una vez al dia no cambia nada.

El problema recae en las pertinencias/sancionatorios/causas que estan activas, pero como siempre se estara comparando la informacion nueva con la ya existente, si solo desaparece una antigua que se haya actualizado no deberian de encontrarse errores.

# INTERFAZ

Me gustaria una interfaz resizeable, con colores "Medioambientes" y/o "Ecologicos" (verdes, blancos, etc.)

* El apartado de noticias mostrara tarjetas con la imagen, fecha, nombre y que al clickearla nos lleve a la pagina de detalles.
La cantidad de tarjetas que se muestran debera depender del ancho de la pagina (aumenta o disminuye al ser resizeable)
* El dashboard general debera tener una tabla con la informacion, clasificandola por tipo, es decir 
Nombre|Fecha|Estado|Tipo|Fuente|Detalle

Donde en tipo debera decir si es causa, pertinencia, sancionatorio, fiscalizacion, ingreso de admisibilidad, etc.
Fuente
Estado dependera de lo que diga en cada fuente (en curso, ingresada, en admision, etc.) 

Para acceder a las diversas pestanas (general, noticias, por pagina) tenemos dos opciones
1. Burger menu arriba a la izquierda que muestre las opciones
2. Barra superior con los nombres de las pestanas

# ANALISIS
El analisis de cada pagina se hara en documentos propios

# Arquitectura
Todo se debe hacer en el computador del cliente, el scraping debe ser headless, uno por pagina y ejecutados de manera que no usen tantos recursos al usuario y vuelva lento su computador para otras funciones (secuencial o paralelo)
Debera ser un programa ejecutable

# PAGINAS A INVESTIGAR
## Servicio de biodiversidad y areas protegidas (Noticias)
https://sbap.gob.cl/sala-de-prensa/noticias-y-comunicados
mas info en sbap.md
## Diario oficial (Noticias)
https://www.diariooficial.interior.gob.cl/edicionelectronica
mas info en diOf.md
## Servicio nacional de geologia y mineria (Noticias)
https://www.sernageomin.cl/
mas info en snagemi.md
## Servicio de Evaluacion Ambiental (Noticias y pertinencias)
https://www.sea.gob.cl/noticias
https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php
mas info en sea.md

## Sistema Nacional de Informacion de Fiscalizacion Ambiental (Noticias y Procedimientos Sancionatorios y Fiscalizaciones)
https://snifa.sma.gob.cl/Sancionatorio
mas info en snifa.md
## Tribunales ambientales (Noticias, Causas y expediente electronico)
https://tribunalambiental.cl/


# Estructura
BioNews/
├── analisis/               # Documentacion y reportes de investigacion (ya existente)
├── assets/                 # Iconos, logos e imagenes de la app
├── data/                   # Almacenamiento de la base de datos SQLite
├── src/                    # Codigo fuente principal
│   ├── main.py             # Punto de entrada (inicializa la app Flet)
│   ├── config.py           # Configuracion global (URLs, tiempos de espera, colores)
│   ├── database/           # Gestion de persistencia
│   │   ├── __init__.py
│   │   └── manager.py      # Operaciones CRUD para noticias y casos legales
│   ├── scrapers/           # Motores de extraccion (Playwright + BS4)
│   │   ├── __init__.py
│   │   ├── engine.py       # Logica base y manejo de navegadores headless
│   │   ├── sea.py          # Scraper especifico para SEA
│   │   └── snifa.py        # Scraper especifico para SNIFA
│   ├── ui/                 # Componentes de la interfaz de usuario
│   │   ├── __init__.py
│   │   ├── dashboard.py    # Vista de la tabla principal
│   │   ├── news.py         # Vista de tarjetas de noticias
│   │   ├── settings.py     # Vista de configuracion por pagina
│   │   └── styles.py       # Definicion de colores "ecologicos" y temas
│   └── utils/              # Funciones auxiliares (formateo de fechas, logs)
├── .gitignore              # Archivos a ignorar (venv, __pycache__, .db)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Instrucciones de instalacion y uso