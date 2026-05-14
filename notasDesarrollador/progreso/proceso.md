# Mejoras, cambios y actualizaciones por hacer

No todo se debe implementar ahora, estara marcado basado en prioridades

1. Alta
2. Media Alta
3. Media
4. Media Baja
5. Baja (Wishlist)
6. Ignorar por ahora (Saltar al siguiente punto)

## Funciones a implementar

### Mejoras scrapers

#### SEA - Pertinencias (4 - Media Baja)

Quiero que en la tabla tambien se guarde el tipo de proyecto, categoria economica y la region. Pero que no se muestren en la tabla, solo que se guarde en la BD y se pueda filtrar por ellos en el 'Desplegar filtros' de las pertinencias.
Hay que mapear las categorias economicas.
Habra que rellenar nuevamente la tabla de pertinencias para que se agreguen las columnas que nos interesan,

#### SNIFA/SMA - Todos (4 - Wishlist)

1. Si yo agrego un registro de alguna categoria del SNIFA quiero que la pagina haga seguimientos de los cambios DENTRO de ese expediente, es decir las fechas, nuevos documentos, etc.

   Para esto necesitamos que se guarde en la base de datos cierta informacion dentro del expediente, lo cual tomara bastante tiempo en construirse y en implementar. Recomiendo usar algo de IA para esto.

2. Que se pueda ordenar por fecha de manera descendente (De mas nueva a mas antigua) por defecto, para eso tambien necesitamos entrar en mas detalle en los expedientes. Por lo que necesito que se guarde en la base de datos cierta informacion dentro del expediente. Ademas no todas las categorias del SNIFA tienen fecha, pero como cada categoria del SNIFA tiene su propia tabla no sera complicado implementarlo.
3. Clasificar por estado (leve, grave, gravisima), esto requiere investigar internamente tambien (SANCIONATORIOS)

#### Tribunales (4 - Media Baja)

2. Que se pueda filtrar por categoria economica, deberan mapearse las categorias economicas, requiere investigacion y definicion de las categorias.

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

## Siguiente version/actualizacion

1. Mejorar Dashboards
2. Implementar DGA
3. Implementar consultas publicas
4. Auth para usuarios
5. Notificaciones
6. App movil
