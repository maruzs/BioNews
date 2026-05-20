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


## Para implementar el server side rendering (con excepcion de los dashboards)
Esta pagina en general es una recreacion de una que ya existe, y estuve analizandola y esto es lo que note:
1. Las tablas las hacen con server side rendering y limits y paginacion
2. Cuando voy al apartado de Dashboards en la pestana Network de las herramientas de desarrollador se genera un GET que devuelve un archivo bastante pesado, por ejemplo https://beta.ecosinfoambiental.com/api-reports/vw-rca-dashboard/? devuelve un json de 17.07mb. Ellos logran hacer que su dashboard sea con cross filtering y el total de datos 
3. Para buscar por palabra clave ellos tambien lo hacen server side como el siguiente ejemplo:
   - Si yo pongo 'ampli' en el buscador por palabra clave (de una categoria, no el general ya que no tienen) se genera en semi tiempo real (se demora unos segundos cuando no estoy escribiendo) o al dar enter el siguiente GET -> `/api-reports/vw-rca-resumen/?__palabraclave=ampli^&page=1^&page_size=20`
   - Y luego despues de eso la tabla muestra los resultados 
4. Para los filtros avanzados ellos tambien lo hicieron server side de la siguiente manera:
   - Los filtros son dropdowns con todos los posibles registros (por ejemplo Titular es un dropdown con todos los titulares), pero en ese dropdown puede uno escribir y se va filtrando el dropdown a medida que vas escribiendo (no se si se entiende pero se empiezan a mostrar solo los que coinciden con lo que escribo)
   - Una vez seleccionados los respectivos filtros se le da a 'Aplicar filtros' y se construye una peticion GET con multiples parametros -> `api-reports/vw-rca-resumen/?categoria_economica=Agroindustrias^&razon_social=8i+S.A.^&page=1^&page_size=20`

   Eso lo tienen implementado para todas las categorias y los filtros avanzados son basados en las columnas que se muestran en las tablas (Aunque por ejemplo yo tengo para filtrar por anio los de SNIFA y el anio esta dentro del expediente). Todos los filtros que tengo actualmente deben mantenerse pero implementarse de esta manera