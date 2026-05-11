# Diario Oficial - Normativa

Dashboard:

- Normativas por Organismo -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de los organismos, ademas abajo dice 'count', no deberia decir nada

- Normativas por Año y Tipo -> Me gustaria que estuvieran desacopladas, no una arriba de la otra si no que una al lado de la otra.

- Total de Normativas -> Me gustaria que dijera 'Total Normativas' y luego el numero, no 'Count Normativas' y el numero

- Distribucion por Region -> Dice 'No especificado' y abajo dice Count. Esto es porque en la tabla no hay un apartado llamado Region, es en los organismos que podemos encontrar la region. Es por esto que haremos lo siguiente:

- En normativas por organismo no debera aparecer nada que sea Region (organismo) o Provincia (Suborganismo)
- En Distribucion por Region, deberian aparecer las regiones, es decir que todo lo que aparezca en la columna 'Organismo' en las normativas y sea 'Region' debera aparecer en las barras de esta grafica. Ademas no deberia decir 'Count'

# SEA - Pertinencias

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Borrar (Comentar) el grafico Pertinencias por Region ya que actualmente no tienen region
- Evolucion Anual por Tipo -> Preferiria que estuvieran desacopladas, no una arriba de la otra si no que una al lado de la otra.

# SEA - Proyectos Evaluados

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Tipo de presentacion -> No tenemos eso, deberia ser por razon_ingreso (en la tabla)
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count
- Estado de evaluacion -> Deberia ser basado en estado_proyecto (No el subestado)
- Presentaciones por Ano -> Actualmente lo hace por dia del mes (01-31) y deberia ser por anio (Actualmente solo tenemos de 2026, pero igualmente)

# SMA Fiscalizaciones

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada

# SMA - Sancionatorios

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada
- Evolucion anual -> El orden de los anios esta raro (2024,2025,2023,2022, etc. no estan ordenados), deberian estar ordenados cronologicamente (Antiguos -> actuales)

# SMA - Sanciones

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada
- No deberia ser Estado del Expediente, deberia ser Multas y ser en base a pago_multa
- Evolucion anual -> El orden de los anios esta raro (2024,2025,2023,2022, etc. no estan ordenados), deberian estar ordenados cronologicamente (Antiguos -> actuales)

# SMA - Programas de Cumplimiento (Programas)

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada
- No tenemos estado del expediente, no deberia estar este grafico
- Evolucion anual -> El orden de los anios esta raro (2024,2025,2023,2022, etc. no estan ordenados), deberian estar ordenados cronologicamente (Antiguos -> actuales)

# SMA - Medidas Provisionales

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada
- No tenemos estado del expediente, no deberia estar este grafico
- Evolucion anual -> El orden de los anios esta raro (2024,2025,2023,2022, etc. no estan ordenados), deberian estar ordenados cronologicamente (Antiguos -> actuales)

# SMA - Requerimientos de ingreso SEIA (Requerimientos)

Dashboard:

- Categoria economica -> Deberia ser barras horizontales ya que ahora mismo no se visualizan bien los nombres de las categorias economicas, ademas abajo dice 'count', no deberia decir nada
- Proyectos por region -> Deberian ser barras horizontales y abajo no deberia aparecer count, no deberia decir nada
- No tenemos estado del expediente, no deberia estar este grafico
- Evolucion anual -> El orden de los anios esta raro (2024,2025,2023,2022, etc. no estan ordenados), deberian estar ordenados cronologicamente (Antiguos -> actuales)

# Tribunales

Tipo de Procedimiento -> Separa 'Reclamación' y 'Reclamacion', tambien 'Solicitud' y 'Solicitud SMA', en ambos casos deberian ser lo mismo.
Tambien separa Demanda Ejecutiva pero ambas son iguales y solo tienen 1 (0.1%).
Ademas Tipo de Procedimiento deberia ser horizontal ya que los nombres son muy largos, ademas abajo dice 'count', no deberia decir nada
En 'Estado Procesal' En tramitacion y En tramitación deberian ser lo mismo pero actualmente estan separados, lo mismo con 'Terminada' y 'Terminadas', tambien 'En tramitacion' y 'Tramitacion'

Estos errores ocurren ya que entre los 3 tribunales no mantienen un mismo formato de nombres, pero esas son todas las opciones que hay que deberian juntarse

# Favoritos

No deberia tener panel dashboard, o a lo mas un dashboard basado en las fuentes de los favoritos.

## GENERAL

No deberia aparecer 'count' en ninguna grafica, eso es solo para los que tienen varios colores y requieren que se les ponga encima para saber que es cada uno.

El orden de los anios no esta ordenado cronologicamente.

Todo dropdown debera ser de esos que cuando tu empiezas a escribir empieza a mostrarse una lista de las opciones basandose en lo que vas escribiendo. De esa manera no habra que buscar uno por uno en el dropdown el que estoy buscando. Deben seguir siendo dropdown pero con esa caracteristica implementada.

Manten los formatos usados para los dashbboards
