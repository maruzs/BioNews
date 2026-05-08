Debemos implementar un apartado nuevo en lo que es el SEA, lo bueno es que la base de lo que es el login es la misma de las pertinencias, solo que ahora debemos ir a otra categoria.
Esto puede hacerse despues de que se hayan rescatado las pertinencias diarias.

De todas formas primero quiero rescatar TODOS los proyectos ingresados para la primera vez construir la tabla y de ahi en adelante solo sera filtar por el dia actual. Comienzo con el analisis.

## ANALISIS

1. Como dije, hay que acceder mediante login y es exactamente lo mismo que para obtener las pertinencias, puedes implementar que justo despues de investigar las pertinencias se pase a ver los proyectos.

Este es el link de la pagina de los proyectos:
https://seia.sea.gob.cl/busqueda/buscarProyecto.php

ahi dentro tendras un formulario (ver evAmbiental/formulario.html)

2. Ejecucion scraper (FORMULARIO):
   2.1 Primera ejecucion: Para la primera ejecucion del scraper cuando llenemos la tabla de datos no habra que poner nada en el formulario ya que queremos TODOS los datos, por lo que daremos directamente a buscar
   <button type="submit" onclick="enviar_formulario()" class="btn btn-primary btn-lg sg-btnForm">Buscar</button>
   2.2 Ejecucion posterior: Debera filtrar por el dia de hoy
