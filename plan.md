## Server side 
Actualmente se estan cargando las cosas server-side o sigue igual que antes?
Tu me dijiste esto sobre mi pregunta en el artefacto bionews_analisis_roadmaps

"Paginación Server-Side y Dashboards (3.1): Es perfectamente viable. Al paginar en el servidor, los DataGrids (tablas de datos) piden de 50 en 50 registros, agilizando la transferencia. Para los gráficos y estadísticas de los dashboards, el backend ejecuta consultas de agregación directa (como COUNT o GROUP BY) que se resuelven en milisegundos sobre la totalidad de la base de datos de Postgres y retornan un JSON consolidado muy liviano, de modo que tus métricas seguirán teniendo acceso al 100% de la información histórica real.

En caso de que no este implementado aun, puedes implementar todo lo que conversamos previamente aqui para que sea server side rendering sin afectar a la vista y uso de los dashboard, (que segun lo que me indicaste no deberia de haber problemas, verdad?)

Aun no me dices si esta funcionando server side o no!
Si ya esta funcionando con server side rendering hagamos lo siguiente:

## Nueva funcion:

Podriamos implementar el registro, login y cambio de contrasena mediante correo electronico (codigo/link)
Tienes libertad de accion pero cubre que no tenga o cause vulnerabilidades y que sea gratuito. Tu me indicas que debo hacer yo.

El login ahora debera ser con el correo electronico y la contrasena
La contrasena debe ser de 8 caracteres minimo
El administrador es el usuario con el correo marianoemunozr@gmail.com asignado (puedes crear un nuevo usuario si lo deseas, pero si lo haces hay que borrar administrador@bionews.cl)
Cada cierto tiempo de inactividad se debe cerrar la sesion de cualquier usuario.
Se puede tener la sesion abierta en mas de un dispositivo.
