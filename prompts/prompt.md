## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

1. Se logro que se muestre lo mas nuevo primero en Pertinencias
2. En las categorias de SMA/SNIFA debemos hacer las siguientes correcciones:

- La fiscalizacion mas nueva es la que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.
- El Sancionatorio mas nuevo es el que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.
- La sancion mas nueva (registro sanciones) es la que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.
- El programa de cumplimiento mas nuevo es el que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.
- La medida provisional mas nueva es la que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.
- El requerimiento de ingreso mas nuevo es el que tiene el numero de ficha mas alto, ese numero de ficha se puede encontrar en la url que tienen todos los registros de las categorias de SMA/SNIFA.

Me di cuenta que en general las etiquetas de nuevo estan fallando demasiado por lo que se me ocurrio que podria hacerse de la siguiente manera

Si un usuario ingresa a una categoria se guarda la ultima vez que ingreso a esa categoria y se compara con la ultima hora de scraping de esa categoria y si resulta que ingreso antes del ultimo scraping y si se encontraron cosas nuevas en esa categoria entonces se muestra la etiqueta de nuevo y si no no se muestra.
Quitaremos la funcionalidad de que al clickear la accion de un nuevo registro se quite la etiqueta de "Nuevo" de ese registro.
De esta manera dependera solamente del usuario si las cosas son nuevas o no y podra mantenerse un estandar general simplemente comparando la hora de ingreso a la categoria con la fecha de scraping del registro.

Por ejemplo el usuario A tendria una parte donde esten las ultimas veces que visito una categoria (Ej. Normativas: 19/05/2026 11:39, Fiscalizaciones 19/05/2026 11:35, etc.)
Y si hubo alguna ejecucion de un scraper (ya sea por programacion horaria o manual) en la que se agregaron nuevos registros a la tabla correspondiente (ej. nueva fiscalizacion a la tabla fiscalizaciones el 19/05/2026 12:00) debera compararse con la fecha de la ultima visita de ese usuario a esa categoria (en este ejemplo 19/05/2026 11:35 ultima visita vs 19/05/2026 12:00 nuevo registro en el scraper).
No es necesario que sea en tiempo real, no tiene mucho sentido y es mejor funcionar con 'flags'.
Ademas es mejor centrar todo al usuario y no en las tablas, de esa manera funcionara para todos correctamente ya que pensando a futuro si tengo 1000 usuarios por ejemplo cada registro de cada tabla debera tener una forma de ver si el usuario X lo vio o no. Al dejarlo con banderas por usuario es mas eficiente y escalable.
