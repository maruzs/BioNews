1. Si el servidor estuvo apagado o no se han ejecutado los scrapers por mas de un dia no se obtendrian todos los ultimos registros de SEA por ejemplo, ya que lo tenemos filtrado para que obtenga los del dia actual, debemos corregir eso para que basado en la ultima fecha de scrapeo se haga bien el filtro, es decir no obtener solo las del dia de hoy, si no que obtener las de los ultimos dias desde que no se hizo. Por ejemplo:

La ultima vez que se hizo el scrapeo fue el 06-05-2026, y he tenido el servidor apagado desde entonces, al encenderlo hoy 12-05-2026, solo obtendria los registros del dia de hoy, cuando deberia obtener los de los ultimos dias desde el 06-05-2026.

El problema esta en que al encender el servidor inmediatamente se ejecuta el scrapeo y si se obtiene algo ya no aparecera que el ultimo scrapeo fue el 06-05-2026, si no que el dia de hoy cuando se encendio el servidor, tendremos tres opciones:

1. Revisar la ultima vez que se hizo el scrapeo y obtener los registros desde ese dia hasta el dia actual antes que se haga el scrapeo del dia de hoy
2. Que si ya se hizo el scrapeo del dia de hoy sin haber hecho este cambio revise cuantos dias hay entre el dia actual y el ultimo dia que se hizo el scrapeo y haga el scrapeo de esos dias de diferencia. (Lo que me acaba de pasar al ejecutar el proyecto sin darme cuenta de este error)
3. Que en el panel de administrador tenga un boton para ejecutar el scrapeo manualmente pero de todo el ultimo mes (y que se agreguen los que no esten claramente, evitando duplicados), seria genial que pudiera yo marcar la fecha de inicio y final del scrapeo manual por rango, por ejemplo del 01-05-2026 al 05-05-2026 y se ejecutara el scrapeo solo de ese rango de fechas. (Esto es opcional pero estaria muy bien)

Actualmente estoy en produccion y al haber ejecutado el codigo (uvicorn y npm) se hicieron los scrapers del dia de hoy, asi que no tengo registros de varios dias, por lo que no tengo registros de esos dias.

Esto es solo para el SEA (Pertinencias y proyectos evaluados).
