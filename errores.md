# BUGS Y ERRORES IDENTIFICADOS (v5)

## ERRORES, BUGS, PROBLEMAS Y CAMBIOS

El punto rojo de que hay algo nuevo no desaparece cuando salgo de la pestana.
Por ejemplo hay nuevas pertinencias y se muestra el punto rojo en la sidebar, ingreso y cuando salgo o voy a otra pestana (ejemplo Home) no desaparece el punto rojo, y deberia desaparecer hasta que haya nuevas pertinencias o noticias, etc

No esta implementado que las cosas nuevas se vean de un color diferente, esto debe ser para cada usuario, es decir desde la ultima vez que ingreso a la respectiva pestana. Las cosas nuevas deben tener alguna marca o algo que los distinga del resto, una vez que el usuario entra a la pestana se marcan como "vistos" (para ese usuario) y se quita el color diferente. Por ejemplo si hay 2 noticias nuevas, una vista y otra no, se muestra el distintivo en la no vista, y al entrar a la pestana se quita el color diferente de ambas.

Se sigue usando el 'scheduler.py' o ahora todo se hace desde server.py? Porque si se sigue usando me di cuenta que el codigo no esta actualizado (creo que solo el de los tribunales) con los nuevos nombres de las funciones y todo eso, revisalo ya que tal vez por eso no se estaba ejecutando cada una hora. Recuerda que cambiamos los nombres de los tribunales en ciertos archivos

## NUEVO

Dijiste que borraste referencia a archivos obsoletos como tribunal3.py, pero de ahi se obtienen las noticias del tercer tribunal, **revisar**

Tiene el mismo nombre la clase de tercerTribunal.py y tribunal3.py, pero uno es para noticias y el otro para las causa, revisar eso!
