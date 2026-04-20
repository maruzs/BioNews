# Quiero crear una especie de newsletter medioambiental chileno.
El software debe scrapear ciertas paginas de enfoque medioambiental e informarme de los cambios que haya encontrado, es decir noticias nuevas (ultimos 3 dias), nuevas pertinencias, nuevos sancionatorios, e ingresos en admisibilidad.

# Las paginas son las siguientes
## Servicio de biodiversidad y areas protegidas (Noticias)
https://sbap.gob.cl/sala-de-prensa/noticias-y-comunicados
## Diario oficial (Noticias)
https://www.diariooficial.interior.gob.cl/edicionelectronica
## Servicio nacional de geologia y mineria (Noticias)
https://www.sernageomin.cl/
## Servicio de Evaluacion Ambiental (Noticias y pertinencias)
https://www.sea.gob.cl/noticias
https://seia.sea.gob.cl/busqueda/buscarProyectoResumen.php

## Sistema Nacional de Informacion de Fiscalizacion Ambiental (Noticias y Procedimientos Sancionatorios y Fiscalizaciones)
https://snifa.sma.gob.cl/Sancionatorio

## Tribunales ambientales (Noticias, Causas y expediente electronico)
https://tribunalambiental.cl/

El software se ejecutara de manera local, con una interfaz que muestre toda la informacion actualizada y que cuando se le de click a 'Actualizar' se ponga a buscar en las paginas indicadas si hay nueva informacion e informar en la interefaz, ademas dando un link a la informacion para poder ir e investigar mas a fondo.

En la interfaz se debera mostrar la informacion de los ultimos 3 dias y cada vez que se actualice se borrara el dia mas antiguo y mostrara lo mas nuevo si es que existe.

La interfaz tendra un apartado general donde se muestra la ultima informacion, pero tendra pestanas dedicadas para cada una de las paginas


# Investigacion de funcionamiento de las paginas
* SBAP -> sbap.md
*


# Diseno basico de la interfaz

Quiero que sea una desktop app que me muestre como una tabla con la siguiente informacion
1. De donde la obtuvo
2. Nombre 
3. Fecha
4. Link

Y que arriba de la tabla tenga pestanas que muestren 
Inicial (donde esta la tabla general)
Noticias (Solo noticias)
Y una pestana por pagina de informacion (SBAP, SEA, TEA, etc)

Que en algun lado haya un boton que comience el scrapeo de las paginas, de manera que solo se actualice la informacion cuando se clickee ese boton.
