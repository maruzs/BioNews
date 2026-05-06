## Proceso actual

Ahora si se muestra en las tablas un distintivo 'nuevo' pero esta fallando, esto es lo que ocurre:

Yo ingreso a mi cuenta y hay nuevas normativas, entonces el punto rojo me informa de eso y al entrar a normativas no me aparece el distintivo verde que dice 'nuevo' al lado de las nuevas normativas pero si se logra quitar el puntito rojo.
Ahora resulta que yo voy a 'Home' y vuelvo a 'Normativas', no tiene el puntito rojo pero al entrar si me aparece el distintivo verde de 'nuevo' y se supone que ya lo vi porque me quito el punto rojo de 'Home'.
Ahora luego de ver ese distintivo vuelvo a 'Home' y luego a normativas y el distintivo verde sigue ahi cuando ya debio desaparecer la ultima vez que ingrese a normativas. Al cerrar sesion y volver a entrar en el mismo dispositivo ya no aparece el puntito rojo, pero sigue apareciendo el distintivo 'nuevo' en las normativas de la tabla.
Eso ocurre con todas las categorias (noticias, normativas, pertinencias, tribunales, y todo lo del SMA)

## Proceso deseado

Este es el proceso real que deberia verse y debe ser cross device.

Yo ingreso a mi cuenta con mis credenciales desde mi computadora y veo que hay nuevas noticias y nuevas normativas ya que en la sidebar puedo ver un puntito rojo al lado de cada una de esas categorias.
Yo entro a ver las noticias a ver si hay algo que me interese y veo que hay 3 noticias nuevas que no he visto, por lo que se muestra un distintivo verde en esas noticias (para las noticias es un borde verde con una etiqueta que dice "Nuevo"), ademas que el puntito rojo de las noticias desaparecio. Luego de terminar de ver si habia alguna noticia interesante paso a ver las nuevas normativas que siguen con el puntito rojo y al entrar desaparece su puntito rojo y veo que hay nuevas normativas ya que tienen una etiqueta que dice 'nuevo' entre el la columna 'Nº' y 'Fav' para las filas de normativas que no he visto aun, una vez termino de ver las cosas nuevas (ya sea por encima o entrando a cada una de ellas) voy a home ya que he terminado de revisar cualquier cosa nueva y no aparece ningun puntito rojo.
Luego sin haber salido de la sesion decido volver a las noticias porque hubo una que queria leer y no lo hice y al volver al apartado de noticias no deberia aparecer el distintivo verde porque ya vi todas las ultimas noticias y no ha habido nuevas desde entonces. Lo mismo para las normativas y todas las demas categorias.
Ademas si yo por ejemplo clickeo en 'Leer mas' de una noticia tambien debe desaparecer el distintivo 'Nuevo' pero solo de la noticia que vi. Es decir si hay 3 noticias nuevas y veo una el distintivo se quita solo de esa noticia, y las otras 2 siguen con el distintivo 'Nuevo'. Si vuelvo a entrar a la lista de noticias las 2 que faltan deberian seguir con el distintivo 'Nuevo' y la que ya vi no deberia tenerlo. (Lo mismo para las otras categorias pero con el boton de 'Accion')

Luego yo salgo de sesion en mi computadora (o la apago sin salir de la sesion) y vuelvo a entrar desde mi celular, al yo ingresar no deberia ver puntitos rojos si no hay cosas nuevas, es decir que si ya revise la categoria desde otro dispositivo/buscador no deberia aparecer el puntito rojo en esta sesion que acabo de iniciar en el celular. Lo mismo con los distintivos 'Nuevo' de cada categoria.

Si hay normativas nuevas pero no entro a verlas pero si las noticias por ejemplo, no deberia aparecer el puntito rojo en normativas pero si en noticias (en cualquier dispositivo/buscador).
Si luego de un tiempo sale una nueva normativa y la veo pero no entro a ver las noticias que salieron en ese lapso de tiempo, entonces deveria aparecer el distintivo verde en las noticias pero no en normativas.

Cada vez que haya una nueva noticia (o cualquier categoria) deberia aparecerle un punto rojo sin necesidad de que reinicie la pagina (es decir en tiempo real), lo mismo con la etiqueta 'Nuevo' de cada categoria. Por ejemplo, si hay 2 noticias nuevas, al mismo tiempo que sale la primera deberia aparecer el puntito rojo y la etiqueta 'Nuevo', y lo mismo para la segunda. Es decir, deberian aparecer en el mismo momento en que se agregan a la db.

Si por ejemplo no me meti en mas de un dia (ejemplo 3 dias) y hubo nuevo contenido esos 3 dias, todos deberian aparecer con el distintivo verde y deberia quitarse solo cuando yo entre a cada una de las categorias.

Solo para que sepas las categorias son las siguientes pero la idea debe aplicar para TODAS las categorias que hay en la sidebar.

Noticias
Diario Oficial - Normativas
SEA - Pertinencias
SMA - Fiscalizaciones
SMA - Sancionatorios
SMA - Sanciones
SMA - Programas
SMA - Medidas
SMA - Requerimientos
Tribunales Ambientales - Tribunales

No se si puedes entender diagramas UML directamente por codigo (plantUML) pero te lo adjunto de todas formas, esta en @notasDesarrollador/flujoNotificaciones.puml

Es una idea general que debes implementar al codigo actual que tenemos, haz los cambios que consideres necesarios (idealmente que no haya que migrar ninguna tabla existente)

Este es un documento de referencia para que entiendas el contexto.
