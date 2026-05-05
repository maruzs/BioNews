# BUGS Y ERRORES IDENTIFICADOS

## Tabla normativas:

Si yo busco por palabra clave por ejemplo 'Certificado Tipos de cambio y paridades de monedas extranjeras para efectos que señala' que en la base de datos esta 2 veces (una para ayer 4 y otra para hoy 5) me aparecen ambos resultados, pero ambos con la fecha de 5/4/2026 y si luego clickeo donde dice 'Fecha' en la tabla y luego busco nuevamente por palabra clave el mismo titulo ahora me aparecen 3 registros con la fecha 5/4/2026.
Si luego quito el filtro por palabra y doy click varias veces a 'Fecha' (en la tabla) y luego busco por nombre ahora tengo muchos registros, antes todos tenian la id 2 y la fecha 5/4/2026, ahora tengo 3 con id 2 y fecha 5/4/2026 y 3 con id 108 y fecha 5/4/2026.

Ademas al ir bajando por la tabla se mueve todo muy raro, en general la tabla esta fallando mucho

Estaba revisando la tabla nuevamente ingresando desde 0 y me di cuenta que el orden va relativamente bien hasta que se encuentra con algo que ya existia el dia de ayer (Certificado de Tipos de cambio banco central de chile) y ahi falla y da el valor de lo del dia de ayer.
N | Fav | Fecha | Normativa | blablabla | Organismo
26 | | 5/5/2026 | decreto numero 21 | blablabla| Ministerio de ciencia
27 | | 5/5/2026 | decreto numero 22 | blablabla| Ministerio de ciencia
108| | 5/4/2026 | Certificado Tipos de cambio y paridades de monedas extranjeras para efectos que señala | blablabla| Ministerio de ciencia
29 | | 5/5/2026 | Extracto de resolucino | blablabla| Ministerio de hacienda

Al ordenar por fecha (desde la columna) con la flechita apuntando hacia arriba se comienza a comportar raro, la fecha mas arriba es 5/4/2026 y luego viene la 5/5/2026.
Ademas de que tengo el registro 108 como 7-8 veces y todas con fecha 5/4/2026.
En resumen en la interfaz la muestra de la tabla de normativas esta rara, ya que en la BD esta todo bien.
Si no selecciono nada en los nombres de las columnas de la tabla y no pongo filtros todo anda bien tambien moviendome por la paginacion.

## Noticias - SBAP

Hoy hubo una noticia en el SBAP y no aparece.
En los logs aparece que se encontro una nueva hoy (05/05/2026) a las 15:07 y en la tabla noticias en la bd aparece que fue scrapeada hoy a las 15:07, pero la fecha la pone como el 2026-01-05 cuando deberia ser 2026-05-05, de hecho en la pagina del SBAP el div corresponde a <div class="fecha">5 may. 2026</div>
En lo que respecta a la pagina web bionews no aparece ya que al ser de 'enero' no carga por la supuesta antiguedad.

## Pertinencias

No me aparece la tabla ordenada por fecha por defecto, debo clickear fecha para que se ordene por fecha. Deberia aparecer ordenada por fecha por defecto. Por lo demas esta perfecto con la excepcion de los filtros (revisar 'Todas las tablas' mas abajo)
Las fechas estan en formato month/day/year, y al ingresar a pertinencias el primer resultado que aparece es 12-31-2025 pero deberia ser la fecha mas reciente que en este caso es 5-5-2026.

## Todas las tablas

Tambien al desplegar filtros me pide que escriba para buscar por el filtro, deberia ser un dropdown con las opciones, esto es para TODAS las tablas
Por ejemplo en pertinencias dice 'Filtrar por Estado' deberia aparecer un desplegable con los estados, pero en cambio tengo que escribir yo.

## Preferencias de usuario

Estoy en un perfil temporal que hice aparte de Admin, luego hare otro para comprobar que no se mezclen las preferencias y favoritos de los usuarios.
Puede estar asociado al error de 'Todas las tablas'
Si yo selecciono en normativas la preferencia 'MINISTERIO DE CIENCIA, TECNOLOGÍA, CONOCIMIENTO E INNOVACIÓN' y y en 'SMA (Categorias)' 'Pesca y Acuicultura' y luego voy a 'Normativas' me aparecen todas las normativas, no solo las que yo seleccioné.
Lo mismo para SMA pero no tanto, aqui si aplica mas o menos ya que muestra principalmente Pesca y Acuicultura, pero se cuelan algunos de 'Transportes y Almacenaje'.

Probe con otro usuario a ver si las preferencias se estaban mezclando, este usuario no tiene ninguna preferencia seleccionada y no muestra solo Pesca y Acuicultura como si se estuvieran mezclando.

Al ese usuario le puse otras preferencias (instalacion fabril) y funciona bien, solo muestra las de instalacion fabril.
Le puse Pesca y acuicultura quitandole instalacion fabril y muestra Pesca y Acuicultura y algunas de Transporte y Almacenaje.
Con infraestructura (solo) muestra solo infraestructura.
Energia solo muestra Energia.
Infraetructura portuaria muestra Infraestructura portuaria e Infraestructura de Transporte
Forestal muestra solo forestal
Infraestructura de Transporte muestra Infraestructura de Transporte, Infraestructura portuaria, Transportes y almacenaje y Monitoreo de Calidad Ambiental.
Transportes y almacenaje muestra Transportes y almacenaje y Pesca y acuicultura
Minería muestra solo minería
vivienda e inmobiliarios muestra Mineria, equipamiento, Infraestructura Portuaria, Energia,
Y asi en general, la idea es que si yo aplico un filtro en mis preferencias solo muestre los registros que tengan esa categoria como preferencia, sin mezclarse con otros.
Tambien note que el Total de registros no tiene sentido, por ejemplo en fiscalizaciones para Vivienda e Inmobiliarios hay 197 registros en la tabla, pero me tira que hay 3620.
El total de registros sin filtros es de 5017 (En fiscalizaciones)

Las preferencias de normativas siguen sin funcionar correctamente.
