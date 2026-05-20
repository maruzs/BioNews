## Docker compose logs -f
### DGA
Quiero que el scraper del DGA solo sea para https://dga.mop.gob.cl/noticias/, actualmente lo esta haciendo para
https://dga.mop.gob.cl/noticias/2, https://dga.mop.gob.cl/noticias/3, etc.
lo cual demora un monton y es innecesario.

### Scraping proyectos evaluados SEA
Ademas:
```bash
maru@maru:/opt/BioNews$ docker exec -it bionews-db psql -U bionews -d bionews -c "SELECT id, nombre, fecha_presentacion, fecha_scraping FROM sea_proyectos_evaluados ORDER BY fecha_scraping DESC LIMIT 10;"
ERROR:  relation "sea_proyectos_evaluados" does not exist
LINE 1: ..., nombre, fecha_presentacion, fecha_scraping FROM sea_proyec...
                                                             ^
maru@maru:/opt/BioNews$
```

Y sigue sin encontrar el registro, ademas lo que tu estas diciendo de que dice:
"Se encontraron 8 registros en la API para hoy.
Proceso finalizado con exito. Se agregaron 0 registros nuevos."
Eso es para las pertinencias, yo estoy hablando de los proyectos evaluados, los cuales no estan obteniendo un registro del dia de ayer 19/05/2026 que al parecer fue agregado despues de la ultima ejecucion del scraper sea (pertinencias y Proyectos evaluados) y como ahora solo revisa el dia actual no logra obtener el del dia de ayer.
el codigo de los proyectos evaluados del sea esta en sea_evaluados.py
```bash
bionews-api        | INFO:     172.18.0.5:35282 - "POST /api/scrape/sea/manual HTTP/1.1" 200 OK
bionews-web        | 172.20.0.4 - - [20/May/2026:16:52:13 +0000] "POST /api/scrape/sea/manual HTTP/1.1" 200 99 "https://impacts-gay-dans-connected.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | 1. Accediendo a la pagina de login (SSO CAS)...
bionews-api        | Token CAS encontrado. Iniciando sesion...
bionews-api        | 2. Accediendo a la app principal para obtener tokens de Laravel...
bionews-api        | 3. Consultando API para el rango: 2026-05-19 a 2026-05-20
bionews-api        | Se encontraron 8 registros en la API para hoy.
bionews-api        | 4. Guardando en base de datos...
bionews-api        | Proceso finalizado con exito. Se agregaron 0 registros nuevos.
bionews-api        | 5. Cerrando sesion...
bionews-api        | Iniciando scraping SEA Proyectos Evaluados. Modo diario.
bionews-api        | INFO:     127.0.0.1:43292 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | Offset 1 procesado. Registros nuevos hasta ahora: 0
bionews-api        | API retorno status False o sin datos en offset 101
bionews-api        | Scraping SEA Proyectos finalizado. Nuevos: 0
bionews-db         | 2026-05-20 16:52:24.852 UTC [27] LOG:  checkpoint starting: time
```

Hice nuevamente un pequeno analisis de como funciona la API de proyectos evaluados y esta todo en analisisPE.md