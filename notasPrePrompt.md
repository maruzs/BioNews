## Perfil de administrador

Ahora en todas las categorias (menos noticias) me aparecen TODOS los items como 'Nuevos', por ejemplo para las pertinencias, las 25744 publicaciones estan todas como 'Nuevos', cuando deberian haber solo 1 nueva (ejecute de manera manual el scraper de pertinencias recien)
De hecho me aparecen TODAS como nuevas, menos la que es nueva
Y tampoco se van cuando salgo de la categoria y vuelvo a entrar.
Tampoco desaparecen cuando le doy click a la accion (correspondiente)
Tal vez se podria implementar un boton en cada categoria que diga 'Marcar todas como leidas' y otro que diga 'Marcar todas como no leidas' para cada categoria y eso sea mas sencillo de usar, pero de todas formas me gustaria mas que fuera que al salir de una categoria se desmarque tanto el punto rojo como las etiquetas de 'Nuevo' (si, ahora para coordinarlo mejor el punto rojo se ira solo al salir de la categoria al igual que las etiquetas de 'Nuevo' )
Tambien cuando le di al boton para scrapear noticias me dio lo siguiente en la consola:

```bash
INFO:     127.0.0.1:59357 - "POST /api/scrape/news HTTP/1.1" 200 OK
2026-05-06 09:00:01,829 [ERROR] Error de importación al iniciar scrapers: cannot import name 'TercerTribunalScraper' from 'src.scrapers.tribunal3' (C:\Users\maria\Desktop\BioNews\src\scrapers\tribunal3.py)
```

Fui a ver las pertinencias para ver si me aparecia la nueva como nueva y no, me aparecen todas menos esa, y para peor en la consola note que esta constantemente con esto:

```bash
INFO:     127.0.0.1:50533 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50536 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50539 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50542 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50545 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50548 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50551 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50554 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50557 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50560 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50563 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50566 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50569 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50572 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50575 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50578 - "POST /api/notifications/exit HTTP/1.1" 200 OK
INFO:     127.0.0.1:50581 - "POST /api/notifications/exit HTTP/1.1" 200 OK
```

Y asi 'Infinitamente' para todas las categorias, solo si voy a 'Home' dejan de aparecer nuevas.
Si eso ocurre por estar en tiempo real me gustaria que ya no sea en tiempo real y que fuera cada 15 segundos (Que ese tiempo pueda ser cambiable desde el panel de administrador, por defecto 15 segundos)

## Problemas que noto y solucionaremos despues cuando ya este terminado el proyecto de forma correcta

El buscador (firefox, opera, chrome) esta usando cantidades obscenas de ram, sin estar en bionews (con la ip http://192.168.1.24:5173/ hosteada por terminal en el desktop) tiene aprox 550 MB, cuando abro la pagina en firefox sube a 750 Mb que es normal, pero cuando entro por ejemplo a normativas ya subio a 862Mb y en segundos siguio subiendo a 980 Mb hasta que volvi al 'Home'.
Eso es cuando se usa desde el mismo PC hosteado por terminal, pero tambien creo que aumenta el uso de ram si accedo desde el servidor (Todo esto del uso de recursos lo veremos despues)

Al final si lo piensas las notificaciones deberian salir solo despues de que se haya ejecutado el scraper correspondiente y no cada 15 segundos ya que los scrapers son los que traen la informacion, entonces avisar cada 15 segundos o tiempo real no tiene sentido.

Proceso:
(Usare las normativas como ejemplo pero es para todas las categorias, normativas se scrapea a las 7am si o si)
Yo como usuario ingrese ayer antes de irme a dormir para ver si habia alguna normativa nueva, vi que no, entonces sali de la pagina.

Al dia siguiente ingreso a las 10am a la pagina y por temas del scheduler deberian haberse ejecutado varios scrapers, entre esas normativas, es decir que deberian haber normativas nuevas, por lo que deberia aparecer la notificacion con el punto rojo en la sidebar para la categoria normativas (Normativas es un ejemplo aqui, debe ser para todas las categorias), yo entonces ingreso a la categoria de normativas y veo que solo las cosas nuevas tienen la etiqueta de 'Nuevo' (para cada usuario independiente basado en la ultima vez que ingreso y la ultima vez que el scraper obtuvo algo nuevo). Si yo clickeo la accion de cada item nuevo (Por ejemplo: En normativas el icono de verPDF , en pertinencias ver el PDF, en jurisprudencia ver el link, etc) solo el item que clickee deberia perder el estado de 'Nuevo'. Si yo cambio de categoria o voy al 'Home' recien ahi el punto rojo de la categoria normativas deberia desaparecer, y tambien TODAS las etiquetas de 'Nuevo' de los items de esa categoria deberian desaparecer.

Entonces como funcionaria:

1. Se ejecutan los scrapers a su hora acordada
2. Si algun scraper guardo cosas nuevas a la base de datos (es decir que encontro cosas nuevas en la fuente que estaba scraping) al usuario debera aparecerle un punto rojo en la categoria correspondiente en la sidebar (Independiente para cada usuario)
3. Yo como usuario entro a la categoria
4. Basado en la ultima vez que ingrese a la categoria y la ultima vez que el scraper obtuvo algo nuevo, deberan aparecer etiquetas de 'Nuevo' en los items que sean nuevos para mi.
5. Yo clickeo la accion de cada item nuevo y ese item pierde la etiqueta de 'Nuevo' (y solo ese)
6. Si salgo de la categoria o voy al home, el punto rojo de la categoria desaparece y TODAS las etiquetas de 'Nuevo' de los items de esa categoria desaparecen. Y por ende se debe atualizar la fecha de la ultima vez que ingrese a la categoria para ese usuario.

Tambien note 2 cosas que quiero corregir:

1. En normativas si le doy click a un corazon de una fila se marcan visualmente todos los corazones de todas las filas, pero si voy a favoritos solo aparece marcado el que clickee. Pero si yo le doy corazon a otra fila cuando ya habia dado corazon a otra previamente (y estando visualmente todas marcadas) se desmarcan todas en vez de agregar un nuevo favorito, y en la tabla de favorito desaparece la anterior y no aparece la nueva.

Normativas:

1. Clickeo corazon de fila X -> Se marcan visualmente todos los corazones de TODAS las filas y la fila X aparece en la tabla de favoritos
2. Clickeo corazon de fila Y (Visualmente estaban todos marcados) -> Se desmarcan TODAS las filas y no tengo nada en la tabla de favoritos, ni la nueva ni la anterior.

Desde Admin -> Vi que se actualizaron las noticias por el puntito rojo en el sidebar, pero al entrar no tenia la etiqueta 'Nuevo' ni un borde verde (en la card)
Desde el perfil de prueba: decidi ir a ver si ahi si aparecia y tampoco
