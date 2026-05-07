# ANALISIS EJECUCION Y CORRECCIONES

## EJECUCION ULTIMO CODIGO DADO

Se muestran aun las etiquetas 'Nuevo'
No desaparecen todas al salir de la categoria, tampoco el punto rojo del menú lateral.
Ambos deben desaparecer al salir de la categoria (Puedes hacer si quieres que eso sea solo si pasa x tiempo fuera de la categoria, lo dejo a tu criterio)
Si desaparece la etiqueta 'Nuevo' del item si clickeo su accion
TODOS LOS REGISTROS DE LAS TABLAS TIENEN NUEVO

Si estoy en una categoria donde todos eran 'Nuevo' y doy F5 dejan de tener todos la etiqueta, eso esta bien, pero deberia ser tambien cuando salgo de la categoria.

Funciona el Marcar todo como leido

## ANALISIS

Apenas INGRESO a una categoria (ej: Normativas) me sale lo siguiente:

```bash
2026-05-07 18:02:16,896 [INFO] POST /api/notifications/exit: User 11 saliendo de normativas
2026-05-07 18:02:16,897 [INFO] POST /api/notifications/exit: User 11 saliendo de normativas
INFO: 127.0.0.1:58673 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO: 127.0.0.1:58681 - "GET /api/favorites HTTP/1.1" 200 OK
INFO: 127.0.0.1:58685 - "GET /api/favorites HTTP/1.1" 200 OK
INFO: 127.0.0.1:58682 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO: 127.0.0.1:58679 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO: 127.0.0.1:58688 - "GET /api/data/normativas?limit=5000 HTTP/1.1" 200 OK
INFO: 127.0.0.1:58691 - "GET /api/data/normativas?limit=5000 HTTP/1.1" 200 OK
INFO: 127.0.0.1:58694 - "GET /api/notifications/status/normativas HTTP/1.1" 200 OK
```

o cuando clickeo 'pertinencias' en la sidebar

```bash
2026-05-07 18:03:03,312 [INFO] POST /api/notifications/exit: User 11 saliendo de pertinencias
2026-05-07 18:03:03,312 [INFO] POST /api/notifications/exit: User 11 saliendo de pertinencias
```

## MODIFICACIONES A HACER

Puede que debido a que lo marca como salida apenas ingreso a una categoría, no se muestren las etiquetas 'nuevo' como debieran.
