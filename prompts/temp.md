## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.

### EXPLICACION

Los dashboards que tengo ahora estan horribles y funcionan mal, por lo que quiero hacerlos nuevamente y esta vez traigo una plantilla de ejemplo (dashboards/dashboardEjemplo.html y dashboards/dashboardEjemplo.css)

Para las siguientes categorias deberas implementar un apartado para dashboards:

#### Diario oficial - Normativas

Cada tipo de normativa tiene sus propios colores, debe estar en la plantilla de ejemplo (General, Particular, Boletin Oficial Mineria)

Total Normativas a la fecha -> Tarjetas de KPI
Normativas por tipo -> Grafico de barras con Valor relativo por colores
Normativas por region -> Gráficos de Barras Agrupadas horizontales
Normativas por Año -> Gráficos de Barras Agrupadas verticales, una barra por tipo de normativa
Normativas por organismo -> Un grafico de barras horizontales por tipo de Normativa y una barra por suborganismo (si no tiene suborganismo en esa categoria usar el organismo)

#### SEA - Pertinencias

Cantidad de pertinencias -> Tarjeta de KPI
Pertinencias por region ->

#### SEA - Proyectos evaluados

Cantidad de proyectos -> Tarjeta de KPI
Proyectos por via de ingreso al año -> Grafico de barras agrupadas verticales con una barra por via de ingreso
Proyectos por razon de ingreso -> Grafico de barras horizontales por tipo de normativa con una barra por via de ingreso
Proyectos por estado -> Grafico de barras horizontal
Proyectos por categoria economica -> Grafico de barras horizontal

#### SNIFA/SMA - Fiscalizaciones

#### SNIFA/SMA - Sancionatorios

#### SNIFA/SMA - Sanciones

#### SNIFA/SMA - Programas de Cumplimiento

#### SNIFA/SMA - Medidas provisionales

#### SNIFA/SMA - Requerimientos de ingreso

#### Tribunales Ambientales

#### Consultas publicas - MMA

### INSTRUCCIONES

Proyectos evaluados debe tener tambien un dashboard, por lo que hay que implementarle un boton para que pueda acceder al dashboard de proyectos evaluados dentro de la interfaz de proyectos evaluados.

Quiero crear/implementar los dashboards para las categorias

### Indicaciones de formato:

Necesito que el dashboard soporte 'cross-filtering'. Si el usuario selecciona un segmento en el gráfico de barras (ej. una región o categoría), todos los demás componentes (KPIs, gráficos de líneas, mapas) deben actualizar sus estados para reflejar solo los datos de esa selección.

- Tarjetas de KPI: Crea tarjetas de resumen en la parte superior con valores únicos

- Graficos de barras:
  - Gráficos de Barras Agrupadas: Usa barras horizontales para rankings y barras verticales para comparativas temporales por año. Al final de cada barra debe indicarse la cantidad. Y al pasar el mouse por encima debera indicarse su total y su categoria (o el año)
  - Grafico de barras con Valor relativo: Barras horizontales por tipo relativas al total, el total debe verse abajo y cada barra al final debe indicar su cantidad, al pasar el mouse por encima debera mostrar su porcentaje.
