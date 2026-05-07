## Notificaciones de items nuevos

Si hay cosas nuevas (ya sea por ejecucion programada o manual) solo se muestra el punto rojo cuando refresco la pagina con F5, adems las tablas no tienen etiqueta de 'nuevo', noticias tampoco. Deben aparecer apenas se detectan las novedades, ya sea desde la ejecucion programada o desde una ejecucion manual y deben desaperecer cuando salgo de la categoria (por ejemplo voy a otra pagina del navegador) o cuando salgo de la sesion (cierro sesion o cierro el navegador). La etiqueta de 'Nuevo' deben tenerla los items que recien fueron agregados a la bd, ademas de que deben tener un borde verde para las noticias. El 'Marcar todo como leido' debe funcionar igual, y tambien cuando doy click en la accion "Ver mas" de la noticia o en la columna 'Accion' de las tablas debera desaparecer la etiqueta de nuevo para ese item.

Paginación en Servidor: Actualmente el frontend carga todos los registros (hasta el límite de 1000). Para tablas muy grandes, se recomienda implementar paginación real desde la API.
Búsqueda Global: Implementar una barra de búsqueda que consulte todas las tablas simultáneamente desde el Home.

Borrar toda la tabla sanciones para descargarla completa nuevamente pero esta vez si con pago_multa

Normativas no debe estar ordenada por ficha_id, si no que por fecha de la mas nueva a la mas vieja
