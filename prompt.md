Quiero agregar una nueva categoria que sean las consulta publicas, de momento estoy investigando la pagina de consultas publicas del MINSAL y puedes ver lo que llevo en investigacionConsultasPublicas/analisis.md

La nueva categoria se llamara Consultas Publicas y debe tener 3 subcategorias (Con la posibilidad de agregar mas en el futuro):

- MINSAL (Tiene subcategorias)
  - Consultas vigentes
  - Consultas resuelta
- DGA
- MMA

Esto debera verse en la sidebar como las otras categorias (Diario Oficial, SMA, etc). con sus respectivas subcategorias.

Partiremos con lo siguiente:

1. Implementar la interfaz para todas las categorias nuevas. (Las que no tengan nada deberan decir 'En proceso' en su pagina)

2. Implementar el scraper de las consultas publicas del minsal (por ahora esa mientras estudio las otras)
   **LEER investigacionConsultasPublicas/analisis.md para entender como funciona la pagina.**
   Para esta pagina deberemos crear las siguientes tablas en la BD data/data.db
   1. Consultas publicas vigentes
      La tabla se debera llamar minsal_vigentes y debera tener las columnas:
      - id (PK UNIQUE)
      - titulo (text)
      - fecha_inicio (text) -> Formato yyyy-mm-dd
      - periodo_consulta (text)
      - documentos (FK) -> Lista

   2. Resultados de consultas públicas
      La tabla se debera llamar minsal_resultados y debera tener las columnas:
      - id (PK UNIQUE)
      - titulo (text)
      - documentos (FK) -> Lista
   3. Documentos
      La tabla se debera llamar documentos y debera tener las columnas:
      - id (PK UNIQUE)
      - nombre_documento (text)
      - link (text)

   Y cada consulta tendra asociada una lista de documentos, pero cada documento esta asociado a una consulta (Creo, no estoy seguro por lo que lo dejaremos asi).

3. Implementar la interfaz para las consulta del Minsal.
   - Seran cards que muestren solo el titulo de la consulta y al hacer click se despliegue un modal para ver la informacion de la consulta, incluyendo los documentos con su boton de descarga.
4. En el panel de administrador debera agregarse un boton para scrapear las consultas publicas EN GENERAL (Por ahora solo va a poder scrapear el minsal ya que no tenemos otro creado)

   Una vez terminado eso veremos los siguientes scrapers y al final implementaremos una funcionalidad para que al igual que el resto de scrapers se puedan descargar todas las consultas publicas con un boton o con un horario especifico asignado.

El scraper la primera vez que se ejecute debera descargar todo, y las veces siguientes debera descargar solo las que no esten en la base de datos.
