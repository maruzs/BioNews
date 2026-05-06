Aqui se ve todo casi bien, solo tenemos el problema de que se muestran todas las noticias con la etiqueta 'Nuevo'

Cuando se actualizan las noticias me sale el punto rojo en las noticias (bien) pero me marca TODAS  

Horas de exitos y ejecuciones de los logs estan mal (Fue a las 13 y algo, sale que fue a las 17:23)

Barra de busqueda por palabra clave no funciona


Constantemente esta apareciendo esto, por que es? 
Si es porque cada x tiempo se estan actualizando las notificaciones, necesito que veas si es necesario, ya que lo que habiamos quedado previamente era que solo se actualizaran las notificaciones cuando un scraper hubiera encontrado algo nuevo, no en tiempo real ni cada cierta cantidad de tiempo.
Si esta funcionando de la manera deseada y es necesario lo de abajo de forma constante, dejalo
Si esta funcionando de la manera deseada y no es necesario lo de abajo de forma constante, desactivalo 
Si no esta funcionando de la manera deseada y no es necesario lo de abajo de forma constante, arregla lo de las notificaciones para que funcione de la manera deseada y luego desactiva lo de abajo de forma constante
```bash
INFO:     172.18.0.3:57684 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57696 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     172.18.0.3:57702 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57712 - "GET /api/notifications/status HTTP/1.1" 200 OK
INFO:     172.18.0.3:57716 - "GET /api/config/notifications HTTP/1.1" 200 OK
INFO:     172.18.0.3:57730 - "GET /api/notifications/status HTTP/1.1" 200 OK
```

Tengo las normativas repetidas muchas veces en la bd, por ejemplo
https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/06/44442/01/2803908.pdf
esta repetido 8 veces, revisa por que puede ser y arreglalo, son 584 registros para el dia 6 de mayo cuando deberian menos.
por ejemplo son unos 22 del tipo general y hay 176!