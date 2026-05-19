## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

Tenemos los siguientes problemas/errores que corregir:

1. Las tablas que tengan la columna 'fecha' o similares deben siempre mostrarse ordenadas de mas nuevo a mas antiguo.
2. Las pertinencias son 25k registros, lo cual es un monton por lo que demora en cargar, debemos encontrar una solucion para que en el dashboard se hagan los calculos con el total de registros pero en la tabla se vayan cargando a medida que se van pidiendo pero aun asi muestre el total. (Esto debe ser para todas las tablas y dashboards). Que un dashboard tarde en cargar no es tan importante como que la tabla se demore en cargar.
3. El registro mas nuevo siempre debe tener el indice mas bajo, no el mas alto.

4. Etiqueta 'NUEVA' no desaparece en las noticias al clickear la pestana pero si desaparece el puntito rojo de notificacion.
   Al marcar todo como leido si desaparece la etiqueta de 'Nueva' hasta que vuelvo a entrar a la pestana y aparece nuevamente
   Al cerrar sesion y abrir nuevamente sigue apareciendo la etiqueta 'nueva'
   En general la etiqueta 'Nuevo' funciona raro, te definire nuevamente el comportamiento deseado para eso.

Comportamiento correcto etiqueta 'Nuevo' en todas las categorias
Si un scraper encontro algo nuevo y se agrego a su respectiva tabla

1. Debe aparecerle a todos los usuarios un punto rojo al lado de la pestana de esa categoria en el menu lateral.
2. Debe aparecer una etiqueta 'Nuevo' en la tabla en los registros que son nuevos.
   Si el usuario entra a la pestana de la categoria donde hubo algo nuevo debe ocurrir lo siguiente:
3. Debe poder ver la etiqueta 'Nuevo' en los registros nuevos.
4. Al clickear la accion del registro debe desaparecer la etiqueta para ese registro
5. Al salir de la categoria debe desaparecer el punto rojo del menu lateral, esto debe pasar cuando el usuario salga de la categoria (refrescar pagina, cerrar sesion, cerrar navegador, etc.).
6. Si el usuario salio de la categoria cuando vuelva a entrar ya no deben aparecer las etiquetas 'Nuevo' si no hubo cosas nuevas. Es decir que las cosas que ya fueron vistas por el usuario deben sermarcadas como vistas por el usuario y no deben aparecer con etiqueta 'Nuevo'.

Esto debe ser cross-device, es decir que si un usuario ve las cosas nuevas en el computador e ingresa al mismo tiempo desde el telefono no deberian aparecer las cosas con la etiqueta 'Nuevo'.

En resumen:
Si un scraper encuentra algo nuevo activa algun evento que hace que en el menu lateral (sidebar) se muestre un punto rojo al lado de la categoria correspondiente y que los elementos nuevos que no hayan sido vistos por el usuario aparezcan con la etiqueta 'Nuevo' en la tabla. (Esto debe ser para todos los usuarios de forma independiente)
Si un usuario ingresa a ver las cosas nuevas al salir de la categoria debera desaparecer el punto rojo y las etiquetas 'Nuevo' deberan desaparecer para ese usuario.
Cross-device: Si un usuario ve las cosas nuevas en el computador e ingresa al mismo tiempo desde el telefono no deberian aparecer las cosas con la etiqueta 'Nuevo'.
