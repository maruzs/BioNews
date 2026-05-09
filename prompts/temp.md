# IGNORAR ESTE DOCUMENTO, NO EJECUTAR NADA DE LO QUE SE VE AQUI, SON SOLO NOTAS PROPIAS QUE NO SON FINALES

## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.

### EXPLICACION

Los dashboards que tengo ahora estan horribles y funcionan mal, por lo que quiero hacerlos nuevamente y esta vez traigo una plantilla de ejemplo (dashboards/dashboardEjemplo.html y dashboards/dashboardEjemplo.css)

Para las siguientes categorias deberas implementar un apartado para dashboards:

#### Diario oficial - Normativas

Este es el mas diferente asi que esta especificado:

Cada tipo de normativa tiene sus propios colores, debe estar en la plantilla de ejemplo (General, Particular, Boletin Oficial Mineria)

Total Normativas a la fecha -> Tarjetas de KPI
Normativas por tipo -> Grafico de barras con Valor relativo por colores
Normativas por region -> Gráficos de Barras Agrupadas horizontales
Normativas por Año -> Gráficos de Barras Agrupadas verticales, una barra por tipo de normativa
Normativas por organismo -> Un grafico de barras horizontales por tipo de Normativa y una barra por suborganismo (si no tiene suborganismo en esa categoria usar el organismo)

SEA - Pertinencias

SEA - Proyectos evaluados

SNIFA/SMA - Fiscalizaciones

SNIFA/SMA - Sancionatorios

SNIFA/SMA - Sanciones

SNIFA/SMA - Programas de Cumplimiento

SNIFA/SMA - Medidas provisionales

SNIFA/SMA - Requerimientos de ingreso

Tribunales Ambientales

Consultas publicas - MMA

### INSTRUCCIONES

Proyectos evaluados debe tener tambien un dashboard, por lo que hay que implementarle un boton para que pueda acceder al dashboard de proyectos evaluados dentro de la interfaz de proyectos evaluados.

Quiero crear/implementar los dashboards para las categorias

### Indicaciones de formato:

Necesito que el dashboard soporte 'cross-filtering'. Si el usuario selecciona un segmento en el gráfico de barras (ej. una región o categoría), todos los demás componentes (KPIs, gráficos de líneas, mapas, etc) deben actualizar sus estados para reflejar solo los datos de esa selección.

Los dashboards deben estar claramente relacionados a las columnas de la tabla en la bd

- Tarjetas de KPI: Crea tarjetas de resumen en la parte superior con valores únicos.
- Grafico Circular -> Grafico circular (Vacio al centro) basado en porcentaje (cantidad estado/total registros)
- Grafico de barras con Valor relativo: Barras horizontales por tipo relativas al total, el total debe verse abajo y cada barra al final debe indicar su cantidad, al pasar el mouse por encima debera mostrar su porcentaje.
- Gráficos de Barras Agrupadas horizontales: Para rankings
- Graficos de Barras Agrupadas verticales: Para comparativas temporales por año
  Al final de cada barra debe indicarse la cantidad. Y al pasar el mouse por encima debera indicarse su total y su categoria (o el año)

Estos son los graficos generales que casi todas las categorias comparten:

Cantidad de registros -> Tarjetas de KPI
Registros por Categoria economica -> grafico de barras horizontal
Registros por Region -> Grafico de barras horizontal
Estado por registros -> Grafico circular con porcentajes por estado (basado en el total)
Registros por tipo -> Grafico de barras con valor relativo
Registros por Anio -> Grafico de barras vertical agrupadas (si hay tipos)

A veces ocurre que tipo o estado tienen cosas repetidas (archivada y archivadas, o suspendida y suspendidas), en ese caso se asume que son la misma categoria

Tambien ocurre que tienen filtros muy largos que incluyen '/' (ej. Agroindustrias / Forestal o Subsecretaría de Agricultura / Servicio Agrícola y Ganadero / Región de Atacama) en ese caso se toma hasta el primer '/' (ej. Agroindustrias / Forestal -> se considera que es Agroindustrias)

En general como dije debe estar basado en las columnas de las tablas y mas o menos esta seria la asociacion

Si es por anio -> Grafico de barras verticales
Si es por anio y hay distintas fuentes (Por ejemplo los 3 tribunales, Normas Generales, Normas particulares, Boletin Oficial mineria, ) -> Grafico de barras verticales agrupadas

Si es por tipo de documentos -> Grafico de barras con valor relativo
Si es por estado -> Grafico circular con porcentajes por estado (basado en el total), pero aqui hay que tener cuidado con casos raros como los siguientes ejemplos: archivada y archivadas (son lo mismo), Terminado - absolucion y terminado - Sancion (Son distintos, esto ocurre a veces en las tablas de SMA/SNIFA)

Si es por categoria economica -> Grafico de barras horizontal (cuidado con los que tienen '/', ocurre en algunas tablas de SMA/SNIFA)

etc.

Los graficos de los dashboards deben tener un boton para expandirse y al clickearlo mostrar un modal, ese modal debe mostrar el grafico mas grande y tener los siguientes botones:

1. Descargar (SVG o PNG, tu decides, no se deben guardar en la bd)
2. Ver en otra pagina -> Abre el grafico en otra pestana

Tambien la pestana de dashboard no debe abrir otra pestana, debe mostrarse en la misma pagina abajo de los botones de los filtros.
Sigue los colores y estetica de la pagina actualmente
Todo dentro de una categoria debe ser cross-filtering con todo

En resumen implementa un dashboard bonito basado en la informacion de las tablas

Usa la tecnologia mas rapida, moderna y bonita que puedas encontrar

Si necesitas inspiracion puedes revisar la carpeta dashboards/
