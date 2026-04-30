# MEJORAS

# Punto 1 - Tablas y base de datos

Quiero que cada fuente tenga su propia tabla en la base de datos, por ejemplo :

- El SNIFA/SMA tendria:

* Fiscalizaciones -> N°,Favorito,Expediente,Razón Social,Unidad Fiscalizable,Categoría Económica,Región,Estado,Acción
* Sancionatorios -> N°,Favorito,Expediente,Fecha Inicio,Razón Social,Unidad Fiscalizable,Categoría Económica,Estado,Acción
* Sanciones\* -> N°,Favorito,Expediente,Fecha Inicio,Razón Social,Categoría Económica,Estado,Cant. Hecho Infraccional,Multa Total (UTA),Acción
* Seguimiento Ambiental\* -> N°,Favorito,Expediente,Fecha Informe,Razón Social,Nombre Seguimiento,Unidad Fiscalizable,Categoría Económica,Región,Acción
* Programa de Cumplimiento\* -> N°,Favorito,Expediente,Fecha de Ingreso,Fecha de Termino,Razón Social,Unidad Fiscalizable,Categoría Económica,Región,Acción
* Medidas Provisionales\* -> N°,Favorito,Expediente,Razón Social,Unidad Fiscalizable,Categoría,Estado,Acción
* Requerimiento de Ingreso -> N°,Favorito,Expediente,Año,Razón Social,Unidad Fiscalizable,Categoría Economica,Región,Acción

- El SEA tendria:

* Proyectos Evaluados\* -> N°
  Favorito,N° RCA,Año RCA,Titular,Nombre del Proyecto,Unidad Fiscalizable,Via de Ingreso,Categoría Económica,Acción
* Pertinencias -> N°,Favorito,Expediente,Nombre de Proyecto,Proponente,Categoría Económica,Estado,Acción
* Participacion ciudadana\* -> N°,Favorito,Fecha Presentación,Inicio Part. Ciudadana,Término Part. Ciudadana,Titular,Nombre Proyecto,Tipo Presentación (Vía de Ingreso),Región,Inversión (MMU$),Estado,Acción
* Noticias -> Iria a la tabla general de noticias

- Tribunales Ambientales tendria todos los tribunales en una misma tabla con las siguientes columnas:
  N°,Favorito,Rol,Fecha,Carátula,Tribunal,Tipo de Procedimiento,Estado Procesal,Acción

- El diario oficial ahora no sera solo de temas medioambientales, sera con todos los temas y en el perfil se elegiran las categorias de organismo y subsecretarias que interesan, la tabla sera para la siguiente categoria:

* Normativas\* -> N°,Favorito,Fecha,Normativa,Tipo de Normativa,Organismo,Subsecretaria,Acción
  (En el diario oficial debemos obtener normas generales, normas particulares y Boletin oficial de Mineria)

- Y lo que no caiga en ninguna categoria serian las noticias en una tabla llamada Noticias que tendria las siguientes columnas

* Fecha
* Titulo
* Enlace
* Fuente

Generalmente la columna de Accion sera un boton que lleva al documento original o al expediente. De momento en el diario oficial llevara al diario oficial del dia de hoy, proximamente llevara al documento original. Para los apartados que tengan fichas o expedientes por ahora se hara llevando directamente al link, a futuro se implementara que la informacion que se ve en el link del detalle (ficha/expediente) se muestre en la misma app.

Esto se debe a que tengo que hacer una investigacion mas detallada de eso.

# Punto 2 - Scrapeo paralelo

Ahora lo que me interesa hacer es que los scrapers se ejecuten de forma paralela, de 2 en 2 o de 3 en 3 para optimizar el tiempo.asdasd

# Investigacion

Hay varios apartados que debo investigar para poder implementar las mejoras.

Lo que en el punto 1 tiene un asterisco (\*) tengo que investigarlo
