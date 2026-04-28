# BioNews v1.2.1 -> v1.2.2

## Correcciones y mejoras proxima version:

[X] Para SNIFA se guarda el expediente, pero me interesa que tambien muestre la empresa relacionada
[X] Poder guardar en favoritos las cosas que se les quiera hacer seguimiento
[ ] Revision de html/json solo si existen nuevas instancias o cambios con el fin de optimizar y apurar el proceso de scrapeo
[ ] Color picker para la interfaz
[ ] Descarga directa de PDFs con posibilidad de verlo en la misma app, o link directo al documento
[ ] Ejecucion paralela de scrapers
[ ] Pagina web
[ ] Informe mensual
[ ] Informe trimestral
[ ] Informe anual
[ ] Graficos
[ ] Resumen de nuevos cambios y documentos con IA
[ ] Mostrar avances de scrapeo en 'Registro de actividad'
[X] Barra de busqueda para SNIFA
[X] Checkboxes para filtrar por Categoria y Estado en SNIFA
[ ] Orden de Fiscalizaciones en SNIFA esta raro por la ausencia de fechas
[ ] Otras entidades diario oficial que contengan temas medioambientales
[ ] Informacion mas detallada dentro de las tarjetas del diario oficial
[ ] Agregar categoria 'Equipamiento', 'Infrastructura de Transporte'
[ ] En favoritos no se muestra nada al filtrar por SNIFA ni Tribunales, solo SEA

## Posibles vulnerabilidades que arreglar

[X] Desactivacion de verificacion de SSL (Usar certificados validos)
[ ] Inyeccion de SQL
[ ] Ejecucion de binarios externos (reemplazo de chromium)
[ ] Sandboxing en scraping, actualizar pw-browser

## Otras cosas que revisar

[X] Eliminar librerias y dependencias no utilizadas
[ ] Hacer que se pueda expandir la pantalla con F11
[X] No muestra noticias corte suprema pero se supone que si las obtiene
[X] Checkbox noticias sernageomin
[ ] Fotos noticias sernageomin
[X] Logo diario oficial
[ ] Cambiar logo de flet en la app

## WIP - Seguimiento favoritos:

1. Investigacion:
   [X] Sea
   [ ] SNIFA
   [ ] Tribunales
2. Desarrollo codigo:
   [ ] Codigo sea
   [ ] Codigo SNIFA
   [ ] Codigo tribunales

[X]Barra de busqueda para favoritos

[X]Agregar pertinencias, sancionatorios y fiscalizaciones antiguas para hacerle seguimiento

Implementar en SNIFA:
[] Medidas provisionales
[] Programas de cumplimiento
[] Informes de seguimiento ambiental

"


# NO COMMIT

## Cosas a imitar de ecosinfoambiental
Watchlist

## SEA:
Proyectos evaluados
Pertinencias
Participacion ciudadana

## SMA:
Fiscalizaciones:
   * Reporte de fiscalizacion:
      - Listado de fiscalizaciones
   * Dashboard
      - Fiscalizaciones
      - Unidades fiscalizables
      - Fiscalizaciones por tipo 
      - Cantidad de expediente anual (grafico)
      - Fiscalizaciones por region 
      - Fiscalizacion por Categoria Economica

Sancionatorios:
   * Documentos sancionatorios:
      - Listado de procedimientos sancionatorios
   * Dashboard:
      - Cantidad de hechos 
      - Cantidad de procedimientos
      - Estados sancionatorios
      - Procedimientos sancionatorios por tipo de instrumento
      - Distribucion de Categorias Economicas por Numero de Procedimientos
      - Clasificacion por gravedad
      - Clasificacion por estado

Sanciones:
   * Registro de sanciones:
      - Listado de procedimiento de sanciones 
   * Dashboard:
      - Cantidad de hechos
      - Multas Totales UTA
      - Estado de sancion anual
      - Multas por categoria economica en UTA
      - Clasificacion por gravedad infraccion Art. 36
      - Estados

Seguimiento Ambiental:
   * Registro de seguimiento ambiental:
      - Listado de seguimiento ambiental
   * Dashboard:
      - Numero de expedientes
      - Seguimiento ambiental por categoria
      - Seguimiento ambiental anual
      - Seguimiento ambiental por region
      - Seguimiento por Componente Ambiental

Programa de cumplimiento:
   * Reporte por programa de cumplimiento
      - Listado de programa de cumplimiento
   * Dashboard:
      - Total PdC
      - Programa de cumplimiento anual
      - Tipo de programa de cumplimiento
      - PdC por estado 
      - PdC por region
      - PdC por categoria economica

Medidas Provisionales:
   * Registro de medidas provisionales
      - Listado de medidas provisionales
   * Dashboard:
      - Numero de expedientes
      - Medidas provisionales por categoria
      - Medidas provisionales anual
      - Medidas provisionales por region
      - Medidas provisionales por estado

Requerimiento de ingreso:
   * Registro de requerimiento de ingreso:
      - Listado de requerimiento de ingreso
   * Dashboard:
      - Numero de expedientes
      - Requerimiento de ingreso por categoria
      - Requerimiento de ingreso anual
      - Requerimiento de ingreso por region
      - Requerimiento de ingreso por tipo de documento 

## Tribunales Ambientales:
   * Reporte tribunales ambientales:
      - Listado de tribunales ambientales
   * Dashboard:
      - Numero de procedimientos 
      - Procedimientos por ano
      - Procedimientos por estado procesal
      - Procedimientos por tipo
      - Procedimientos totales por tribunal ambiental
      - Procedimientos por categoria economica
      - Procedimientos por region

## SEA

Proyectos evaluados:
   * Registro de proyectos evaluados:
      - Listado de proyectos evaluados
   * Dashboard:
      - Cantidad de proyectos
      - Cantidad de RCA
      - Estados de proyectos
      - Evolución Temporal de EIA y DIA de RCA Aprobadas
      - Proyectos Aprobados con RCA por Región y Categoría Económica



Pertinencias:
   * Registro de pertinencias:
      - Listado de pertinencias
   * Dashboard:
      - Pertinencias por region
      - Pertinencias por categoria economica
      - Estado de sacion anual 

Participacion ciudadana:
   * Registro de participacion ciudadana:
      - Listado de participacion ciudadana
   * Dashboard:
      - Total de proyectos con PAC 
      - Proceso PAC a la fecha (DIA)
      - Proceso PAC a la fecha (EIA)
      - Participación Ciudadana por Región
      - Participación Ciudadana por Tipo de Presentación y Estado de Proyecto
      - Participación Ciudadana Anual

## DIARIO OFICIAL

Normativas:
   * Reporte de Normativas:
      - Listado de normativas
   * Dashboard:
      - Cantidad de normativas
      - Normativas por ano
      - Normativas por organismo
      - Normativas por region
      - Subsecretaria por Organismo

