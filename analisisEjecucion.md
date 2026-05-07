## Notificaciones de items nuevos

Si hay cosas nuevas (ya sea por ejecucion programada o manual) solo se muestra el punto rojo cuando refresco la pagina con F5, adems las tablas no tienen etiqueta de 'nuevo', noticias tampoco. Deben aparecer apenas se detectan las novedades, ya sea desde la ejecucion programada o desde una ejecucion manual y deben desaperecer cuando salgo de la categoria (por ejemplo voy a otra pagina del navegador) o cuando salgo de la sesion (cierro sesion o cierro el navegador). La etiqueta de 'Nuevo' deben tenerla los items que recien fueron agregados a la bd, ademas de que deben tener un borde verde para las noticias. El 'Marcar todo como leido' debe funcionar igual, y tambien cuando doy click en la accion "Ver mas" de la noticia o en la columna 'Accion' de las tablas debera desaparecer la etiqueta de nuevo para ese item.
Las notificaciones no son en tiempo real, son basadas en si los scrapers obtuvieron algo nuevo.

## Otros

Paginación en Servidor: Actualmente el frontend carga todos los registros (hasta el límite de 1000). Para tablas muy grandes, se recomienda implementar paginación real desde la API.

Búsqueda Global: Implementar una barra de búsqueda que consulte todas las tablas simultáneamente desde el Home.

Borrar toda la tabla sanciones para descargarla completa nuevamente pero esta vez si con pago_multa

Normativas no debe estar ordenada por ficha_id, si no que por fecha de la mas nueva a la mas vieja

Eliminación de Polling: Migrar la lógica de NotificationsContext.tsx para evitar llamadas constantes a la API. Implementar una carga bajo demanda cuando el usuario cambia de categoría o una actualización manual.

Persistencia de "Visto": Asegurar que las etiquetas "Nuevo" y el punto rojo desaparezcan de forma persistente no solo en la sesión actual, sino entre dispositivos del mismo usuario.
