# BUGS Y ERRORES IDENTIFICADOS (v4)

Ok, los scrapers estan funcionando perfectamente.
Al menos en la pestana de administrador todo va bien de manera manual, asumire que funcionan tambien con el scheduler.

## ERRORES, BUGS, PROBLEMAS Y CAMBIOS

Aun no se si esta implementado el tema de que las noticias nuevas tengan un color diferente hasta que se salga de la pestana de noticias. (Despues de escribir eso cambie a un usuario normal y no, no esta implementado lo de los colores nuevos)

1. Que cuando hay noticias nuevas aparte de tener el puntito rojo en la sidebar las ultimas noticias agregadas tengan un color diferente al resto hasta que se salga de la pestana de noticias, en cuyo caso se va a considerar que ya fueron "revisadas" las nuevas.
2. Lo mismo para las pertinencias y todo lo del SMA

## Tribunales

En la pestana Tribunales al desplegar filtros, 'Filtrar por Tipo' no es un dropdown, hay que escribir ahi, eso hay que arreglarlo

## Panel de administrador

Implementar un boton en el panel de administrador para comenzar el scrapeo de los tribunales, ya que estaba revisandolos manualmente y en el primer y segundo tribunal no hay causas nuevas, pero en el tercer tribunal si y no se han actualizado (hay una del 4 de mayo pero las ultimas registradas son del 1 de mayo) y necesito ver si es porque no se ha ejecutado el scraper de tribunales o esta fallando, por lo que quiero borrar el ultimo registro de cada uno de los tres tribunales y ejecutar el scraper de tribunales manualmente desde el panel de administrador para ver si se obtienen las causas nuevas correctamente

## Noticias

El filtro por fecha de Noticias requiere que se escriba manualmente (con '/' incluso), quiero que vuelva a ser un calendario, todo lo demas esta perfecto en cuanto a noticias

## Normativas

En normativas al desplegar filtro, el 'Filtrar por Tipo' sigue siendo un cuadro de texto en lugar de un dropdown con los posibles tipos (Normas Generales, Normas Particulares y Boletin Oficial Mineria). Lo mismo para los suborganismos, deberia ser un dropdown con los suborganismos que existen. Por lo demas, todo perfecto en normativas

## SEA - Pertinencias

En los filtros desplegados al escribir por ejemplo en 'Filtrar por Proponente' se demora bastante en escribir cada letra, me imagino que tiene que ver con la enorme cantidad de registros, pero a la vez no tiene mucho sentido ya que solo al clickear 'Aplicar Filtro' deberia ejecutarse la busqueda y no mientras se escribe. (revisar 'Todos los filtros desplegables' para mas detalle de lo que quiero que pase)

## Todos los filtros desplegables

En los filtros desplegados al escribir por ejemplo en 'Filtrar por Proponente' se demora bastante en escribir cada letra, me imagino que tiene que ver con la enorme cantidad de registros, pero a la vez no tiene mucho sentido ya que solo al clickear 'Aplicar Filtro' deberia ejecutarse la busqueda y no mientras se escribe.
Esto ocurre en todos los filtros desplegables que tienen para escribir texto, me gustaria que solo cuando se apriete 'Enter' o 'Aplicar Filtro' se ejecute la busqueda de manera que la escritura sea mas fluida y no se tenga que esperar a que se escriba cada letra.
