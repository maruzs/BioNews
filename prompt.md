# Mejoras, cambios y actualizaciones por hacer

No todo se debe implementar ahora, estara marcado basado en prioridades

1. Alta
2. Media Alta
3. Media
4. Media Baja
5. Baja (Wishlist)
6. Ignorar por ahora (Saltar al siguiente punto)

## Funciones a implementar

### Mejoras scrapers (3 - Media)

#### SEA - Pertinencias (3 - Media)

Quiero que en la tabla tambien se guarde el tipo de proyecto, categoria economica y la region. Pero que no se muestren en la tabla, solo que se guarde en la BD y se pueda filtrar por ellos en el 'Desplegar filtros' de las pertinencias.
Hay que mapear las categorias economicas.
Habra que rellenar nuevamente la tabla de pertinencias para que se agreguen las columnas que nos interesan,

#### SNIFA/SMA - Todos (3 - Media)

1. Si yo agrego un registro de alguna categoria del SNIFA quiero que la pagina haga seguimientos de los cambios DENTRO de ese expediente, es decir las fechas, nuevos documentos, etc.

   Para esto necesitamos que se guarde en la base de datos cierta informacion dentro del expediente, lo cual tomara bastante tiempo en construirse y en implementar. Recomiendo usar algo de IA para esto.

2. Que se pueda ordenar por fecha de manera descendente (De mas nueva a mas antigua) por defecto, para eso tambien necesitamos entrar en mas detalle en los expedientes. Por lo que necesito que se guarde en la base de datos cierta informacion dentro del expediente. Ademas no todas las categorias del SNIFA tienen fecha, pero como cada categoria del SNIFA tiene su propia tabla no sera complicado implementarlo.
3. Clasificar por estado (leve, grave, gravisima), esto requiere investigar internamente tambien (SANCIONATORIOS)

#### Tribunales (3 - Media)

1. Implementar filtro en Desplegar filtros para que se pueda filtrar por Tipo de Procedimiento
2. Que se pueda filtrar por categoria economica, deberan mapearse las categorias economicas, require investigacion y definicion de las categorias.

### Scrapers nuevos (3 - Media)

Quiero implementar nuevos scrapers pero requieren que investigue, se haran despues. No es necesario que investigues ahora sobre esto.

#### Nuevas fuentes de noticias: (3 - Media)

Hay que investigar las paginas para construir e implementar los scrapers. Se podrian agregar mas fuentes a futuro.

- Direccion General de Aguas (DGA) -> https://dga.mop.gob.cl/noticias/

#### Consultas Ciudadanas/Publicas: (3 - Media)

Recibe informacion de las siguientes fuentes:

- Ministerio de Salud (Minsal) -> https://www.minsal.cl/consultas-publicas-vigentes/
- Direccion General de Aguas (DGA) -> https://dga.mop.gob.cl/consulta-publica/
- Ministerio de Medio Ambiente (MMA) -> https://consultasciudadanas.mma.gob.cl/portal#consultas

Hay que analizar las paginas para construir e implementar los scrapers.
Se podrian agregar mas fuentesa futuro.
Debera ser una nueva pestana en la sidebar

### Dashboards (1 - Alta)

Hay ciertas condiciones generales para los graficos de los dashboards:

- Si las barras son demasiado pequenas se debera hacer que al clickear una barra o pasar el mouse por encima se agrande esa barra y se muestren las otras mas pequeñas. Ademas se deberia poder ver la informacion que contiene la barra pasando el mouse por encima.
- Todos los graficos (Los cuadrados de totales no) deben tener las siguientes opciones:
  1. Un boton/icono para poder expandir en pantalla (sin cambiar de pestana) -> Y un boton/icono para poder cerrar y volver a la vista normal, o al clickear fuera del grafico en el fondo de la pantalla, el fondo debe ser lo que habia ya previamente en la pantalla. Tambien debera tener el boton para abrir en una nueva pestana o para descargar (png o svg, lo que consideres mejor)
  2. Un boton/icono para descargar el grafico en png (o svg si lo consideras mejor)
  3. Un boton/icono para abrir el grafico en una nueva pestana del navegador
- Todos los graficos estan asociados entre si, es decir que si clickeo una barra, el resto de graficos mostraran como se hubiera filtrado por ese tipo. Y al des clickear una barra se debe volver a la vista normal.
  Por ejemplo si selecciono en el grafico de barras de pertinencias por region la barra de "region Metropolitana" las barras de los otros graficos deberan mostrar los datos filtrados por region metropolitana. O si clickeo una categoria economica, las otras barras deberan mostrar los datos filtrados por categoria economica.

Para cada apartado debemos tener un dashboard. Aqui te los explico:

#### Diario Oficial - Normativas (1 - Alta)

1. Total de normativas a la fecha -> Un cuadrado con los colores de la interfaz que diga el total de normativas
2. Normativas por organiso -> Un grafico de barras que muestre por organismos y suborganismos la cantidad de normativas por tipo (Generales, Particulares, Boletin Oficial Mineria).
3. Normativas por region -> Grafico de barras donde se muestre por regiones la cantidad de normativas.
4. Normativas por Año -> Grafico de barras con las normativas por año, pero cada año debe tener una barra por tipo de normativa (General, Particular, Boletin Oficial Mineria) con su color especifico indicado arriba. Cada barra debe indicar ademas de su color y tamaño la cantidad de normativas que hay por tipo al pasar el mouse por encima.

#### SEA - Pertinencias (2 - Media Alta)

1. Total de pertinencias -> Un cuadrado con los colores de la interfaz que diga el total de pertinencias
2. Pertinencias por Región -> Grafico de barras con cantidad de pertinencias por region
3. Pertinencias por categoria economica -> Grafico de barras con cantidad de pertinencias por categoria economica. (aun no implementable, deben agregarse las categorias economicas de las pertinencias)
4. Tipos de proyecto por año -> Grafico de barras con cantidad de pertinencias por tipo de proyecto por año, en cada ano debe haber una barra por tipo de proyecto con su color especifico indicado arriba. Cada barra debe indicar ademas de su color y tamaño la cantidad de pertinencias que hay por tipo al pasar el mouse por encima.

#### SNIFA/SMA - Fiscalizaciones (1 - Alta)

Los tipos de fiscalizacion estan al final de cada expediente despues de la region y el ultimo '-' (por ejemplo: RCA, PPDA, NE, Etc.)

1. Total de fiscalizaciones -> Un cuadrado con los colores de la interfaz que diga el total de fiscalizaciones
2. Fiscalizaciones por tipo -> Grafico por tipo pero que sea horizontal y se 'llene' del color dependiendo del porcentaje respecto al total de fiscalizaciones, por ejemplo si tengo que son 50k fiscalizaciones y tengo 36k NE y 14k RCA deberia verse tipo NE en 3/4 de la barra y RCA en 1/4 de la barra y que al final de la barra diga el total de fiscalizaciones que hay por tipo, los tipos estaran en vertical (uno arriba del otro) y al abajo al final debera verse el total de fiscalizaciones que hay.
3. Cantidad anual -> Grafico de barras con el total de fiscalizaciones por ano, sin categorizar por tipo de fiscalizacion (Como todos estan conectados al clickear un tipo de fiscalizacion se mostraran las que hubo de ese tipo en todos los anos, o si clickeo un ano se mostraran todas las fiscalizaciones que hubo de ese tipo en ese ano)
4. Fiscalizaciones por region -> Grafico de barras con cantidad de fiscalizaciones por region (Al igual que las pertinencias por region)
5. Fiscalizaciones por Categoria Economica -> Grafico de barras con cantidad de fiscalizaciones por categoria economica (Al igual que las pertinencias por categoria economica)

#### SNIFA/SMA - Sancionatorios (2 - Media Alta)

1. Cantidad de sancionatorios
2. Estados sancionatorios -> Grafico de barras horizontal
3. Sancionatorios por tipo de instrumento (NE, RCA,etc.) -> Grafico de barras horizontal basado en porcentaje y que abajo se vea el total.
4. Sancionatorios por categoria economica
5. Clasificar por gravedad (Leve, Grave, Gravisima), (Esto aun no se puede implementar, requiere crawlear los documentos)

#### SNIFA/SMA - Sanciones (2 - Media Alta)

1. Cantidad de sanciones
2. Multas Totales UTA
3. Multas por categoria economica
4. Clasificacion por Gravedad (Esto aun no se puede implementar, requiere crawlear los documentos)
5. Tabla de gravedades (Esto aun no se puede implementar, requiere crawlear los documentos)
6. Estado sancion actual (Esto aun no se puede implementar, requiere crawlear los documentos)

#### SNIFA/SMA - Programas de Cumplimiento (2 - Media Alta)

1. Total de PdC (Programas de Cumplimiento)
2. Programas de cumplimiento anuales
3. Tipo de Programa de Cumplimiento -> Grafico basado en porcentaje
4. Programas de cumplimiento por estado (No se puede implementar aun, requiere crawlear los documentos)
5. Programa de cumplimiento por region
6. Programas de cumplimiento por categoria economica

#### SNIFA/SMA - Medidas Provisionales (1 - Alta)

1. Numero de expedientes
2. Medidas provisionales anuales
3. Medidas provisionales por region
4. Medidas provisionales por categoria economica
5. Medidas provisionales por estado -> Basado en porcentajes y total (con sancionatorio o sin sancionatorio)

#### SNIFA/SMA - Requerimientos (2 - Media Alta)

1. Numero de expedientes
2. Requerimientos de ingreso anuales
3. Requerimientos de ingreso por region
4. Requerimientos de ingreso por categoria economica
5. Requerimientos de ingreso por Tipo de documento (no se puede aun, requiere crawlear los documentos)

#### Tribunales Ambientales (1 - Alta)

1. Numero de causas/procedimientos
2. Numero de causas/procedimientos anual por tribunal -> Grafico de barras con barras por tribunal por ano ( Cada barra debe indicar ademas del color y tamaño la cantidad de causas/procedimientos que hay por tipo al pasar el mouse por encima.)
3. Procedimientos por Estado Procesal
4. Procedimientos por tipo por tribunal -> Grafico de barras por tribunales con barras por tipo de procedimiento con colores diferentes e indicados.
5. Procedimientos totales por tribunal ambiental -> Grafico basado en porcentaje
6. Procedimientos por categoria economica (No se puede aun)

### Alertas (3 - Media)

1. Quiero que se envie todos los dias un correo tipo 10 am con la informacion nueva del dia, habra que disenar el correo de como se quiere ver.
2. Debe haber una campana (notificaciones) en la interfaz que muestre la cantidad de cosas nuevas que hay por categoria. No es necesario que las muestre todas, puede tener abajo un boton de ver mas y que solo cargue 4. O que por categoria diga cuantas cosas nuevas hubo, y al pasar el mouse por encima se muestre la lista de cosas nuevas. Esta campana de notificaciones debe estar en la barra superior al lado del icono de usuario.
3. Historial de notificaciones, aqui es donde debe llevar el 'ver mas' donde se puede desplegar filtros, marcar todo como leido y se ven las notificaciones basado en los favoritos del usuario o por temas que el usuario desee seguir. Que se pueda seleccionar que tipo de notificaciones quiere recibir (por ejemplo: solo sma, solo tribunales, etc) y que por defecto esten todos seleccionados. Y que se pueda limpiar el historial de notificaciones.
4. Que los filtros de las notificaciones sean los mismos que los filtros de las tablas (Expedientes e IDs no), por ejemplo para sancionatorios deberia poder filtrarse en el 'Desplegar filtros' por Expediente, Unidad Fiscalizable, Categoria, Region y Estado (Expediente no)
5. Los filtros deben aplicarse en tiempo real.

### Autenticacion de usuarios (Con mail) (3 - Media)

Los usuarios al registrarse en la pagina con su correo deben recibir un correo de confirmacion con un codigo o link de validacion para poder acceder a la pagina. Este correo debe ser enviado por el servidor y no puede ser enviado desde el frontend.

### Home (5 - Ignorar)

Aun no defino que tendra el Home, pero actualmente quiero que solo diga "Home en proceso" y que este vacio. (solo con la sidebar y perfil)

### Landing Page (5 - Ignorar)

Todo igual por ahora, no cambiar nada

### Interfaz - Visual (3 - Media)

1. Actualmente la pagina es una copia de otra llamada Ecosinfoambiental, quiero cambiar la interfaz para que sea propia de BioNews. Pero todas las funcionalidades y arquitectura deben ser las mismas, solo la estetica y diseno debe cambiar, eso lo dejo a libre disposicion.

### App mobil (4 - Wishlist, apartado grande, dejar para el final)

Quiero crear una app mobil que sea lo mas parecida a la pagina web, con las mismas funcionalidades, etc. Esta app sera utilizada en un celular android, por lo que me interesa que se pueda utilizar de manera offline (es decir, que se pueda ver la informacion sin internet) y que se actualice automaticamente cuando haya internet.
