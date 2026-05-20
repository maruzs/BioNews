## Docker compose logs -f (errores.md)
Revisa los logs que te di, pero note este error:
```bash
ionews-db         | 2026-05-20 19:33:29.383 UTC [6023] ERROR:  functions in index expression must be marked IMMUTABLE
bionews-db         | 2026-05-20 19:33:29.383 UTC [6023] STATEMENT:  CREATE INDEX IF NOT EXISTS idx_sea_fecha_presentacion_date ON sea_proyectos_evaluados (to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC);
```

ademas, no deberia usarse UTC, deberia usarse la hora chilena (TZ=America/Santiago)?

## Server side 
Actualmente se estan cargando las cosas server-side o sigue igual que antes?
Tu me dijiste esto sobre mi pregunta en el artefacto bionews_analisis_roadmaps

"Paginación Server-Side y Dashboards (3.1): Es perfectamente viable. Al paginar en el servidor, los DataGrids (tablas de datos) piden de 50 en 50 registros, agilizando la transferencia. Para los gráficos y estadísticas de los dashboards, el backend ejecuta consultas de agregación directa (como COUNT o GROUP BY) que se resuelven en milisegundos sobre la totalidad de la base de datos de Postgres y retornan un JSON consolidado muy liviano, de modo que tus métricas seguirán teniendo acceso al 100% de la información histórica real.

En caso de que no este implementado aun, puedes implementar todo lo que conversamos previamente aqui, ya que segun lo que me indicaste no deberia de haber problemas, verdad?

## SNIFA CON REQUESTS (fiscalizaciones y procedimientos sancionatorios)

tengo el siguiente error al scrapear SNIFA:

```bash
bionews-api        | INFO:     172.18.0.5:58856 - "POST /api/scrape/snifa HTTP/1.1" 200 OK
bionews-web        | 172.20.0.4 - - [20/May/2026:20:30:42 +0000] "POST /api/scrape/snifa HTTP/1.1" 200 55 "https://impacts-gay-dans-connected.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:44f4:a278:b94b:f23c, 172.20.0.1"
bionews-api        | 2026-05-20 16:30:42,402 [INFO] MANUAL
bionews-api        | Iniciando scraper de Procedimientos Sancionatorios para el año 2026 (via HTTP POST)...
bionews-api        | Registros del año 2026 en BD: 81
bionews-api        | Total registros del año 2026 en la web (recordsTotal): 82
bionews-api        | No hay registros nuevos en el lote de los 10 mas recientes.
bionews-api        | Iniciando scraper de Fiscalizaciones para el año 2026 (via HTTP POST)...
bionews-api        | Registros del año 2026 en BD: 726
bionews-api        | Total registros del año 2026 en la web (recordsTotal): 743
bionews-api        | INFO:     127.0.0.1:38458 - "GET /api/health HTTP/1.1" 200 OK
bionews-api        | No hay registros nuevos en el lote de los 10 mas recientes.
bionews-api        | Iniciando scraper de Requerimientos de Ingreso...
bionews-api        | Registros actuales en BD: 236
bionews-api        | Registros en la web: 236
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Medidas Provisionales...
bionews-api        | Registros actuales en BD: 492
bionews-api        | Registros en la web: 492
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Programas de Cumplimiento...
bionews-api        | Registros actuales en BD: 1410
bionews-api        | Registros en la web: 1410
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | Iniciando scraper de Registro Publico de Sanciones...
bionews-api        | Registros actuales en BD: 1022
bionews-api        | Registros en la web: 1114 (1021 unicos)
bionews-api        | No hay registros nuevos. La BD esta actualizada.
bionews-api        | INFO:     127.0.0.1:34486 - "GET /api/health HTTP/1.1" 200 OK
```

Aparte de que ahora hay mas registros yo borre uno antes de iniciar para ver si funcionaba
En fiscalizaciones, en la pagina oficial al menos los primeros 20-30 son nuevos.

Deberia revisarse


Este es el ejemplo de lo que devuelve el POST

```js
{
    "draw": 1,
    "recordsTotal": 743,
    "recordsFiltered": 743,
    "data": [
        [
            "1",
            "DFZ-2026-1644-XIII-NE",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/25264\u0027 target=\u0027_blank\u0027\u003eGimansio Zona Fit - Ñuñoa\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión Metropolitana\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eÑuñoa\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1076000\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
        [
            "2",
            "DFZ-2026-1643-VII-PPDA",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/25263\u0027 target=\u0027_blank\u0027\u003eLEÑA MARCELO VERA\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión del Maule\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eSagrada Familia\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075999\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
        [
            "3",
            "DFZ-2026-1642-VII-PPDA",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/25262\u0027 target=\u0027_blank\u0027\u003eLEÑA LUIS RAMIREZ\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión del Maule\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eSagrada Familia\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075998\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
        [
            "4",
            "DFZ-2026-1641-VII-PPDA",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/25261\u0027 target=\u0027_blank\u0027\u003eSUPERMERCADO DE LA LEÑA SAGRADA FAMILIA\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión del Maule\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eSagrada Familia\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075997\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
        [
            "5",
            "DFZ-2026-1640-VII-PPDA",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/17418\u0027 target=\u0027_blank\u0027\u003eLEÑERÍA ÓSCAR GONZÁLEZ\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión del Maule\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRomeral\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075996\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
        [
            "6",
            "DFZ-2026-1638-VII-PPDA",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003eEquipamiento\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/17417\u0027 target=\u0027_blank\u0027\u003eSUPERMERCADO DE LA LEÑA\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión del Maule\u003c/li\u003e\u003c/ul\u003e",
            "\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRomeral\u003c/li\u003e\u003c/ul\u003e",
            "En SNIFA",
            "\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075995\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
        ],
```

El error puede ser porque hace la extraccion de la ficha con `extract_ficha_id(url)` pero ahora ya no lo hacemos usando la URL, lo hacemos obteniendo el json, el cual tiene el siguiente formato:
```js
[
"12",
"DFZ-2026-1585-X-NE",

"\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-user\u0027\u003e\u003c/i\u003ePRODUCTOS DEL SUR LTDA.\u003c/li\u003e\u003c/ul\u003e",

"\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-angle-right\u0027\u003e\u003c/i\u003ePesca y Acuicultura\u003c/li\u003e\u003c/ul\u003e",

"\u003cul class=\u0027fa-ul\u0027\u003e\u003cli\u003e\u003ci class=\u0027fa-li fa fa-building\u0027\u003e\u003c/i\u003e\u003ca href=\u0027/UnidadFiscalizable/Ficha/12080\u0027 target=\u0027_blank\u0027\u003ePRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)\u003c/a\u003e\u003c/li\u003e\u003c/ul\u003e",

"\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003eRegión de los Lagos\u003c/li\u003e\u003c/ul\u003e",

"\u003cul class=\u0027sin-orden\u0027\u003e\u003cli\u003ePuerto Montt\u003c/li\u003e\u003c/ul\u003e",

"En SNIFA",

"\u003cspan\u003e\u003c/span\u003e\u003ca href=\u0027/Fiscalizacion/Ficha/1075953\u0027\u003e\u003ci class=\u0027fa fa-plus-circle\u0027\u003e\u003c/i\u003e Ver detalle\u003c/a\u003e"
],
```
Si por ejemplo extraemos de ahi los datos que nos interesan para la bd serian los siguientes:

expediente -> DFZ-2026-1585-X-NE
nombre_razon_social -> PRODUCTOS DEL SUR LTDA. (Al parecer es lo que va despues de fa-user)
unidad_fiscalizable -> PRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)
categoria -> Pesca y Acuicultura (Al parecer es despues de fa-angle-right)
region -> Región de los Lagos (Siempre tiene 'Región' antes al parecer)
estado -> En SNIFA
detalle_link -> https://snifa.sma.gob.cl + /Fiscalizacion/Ficha/1075953 
fecha_scraping -> Eso depende del scraping
ficha_id -> 1075953

Cada valor esta separado por comas, pero no nos interesa la comuna.

Esto ocurre tambien para los procedimientos sancionatorios con lo de `extract_ficha_id(url)`

Este es un ejemplo del json, te mapeo tambien lo que nos interesa:

```json
[
            "1",
            "D-078-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/24940' target='_blank'>Antros Rock Bar</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>EDUARDO CARTER GUIÑEZ</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Equipamiento</li></ul>",
            "<ul class='sin-orden'><li>Región de Los Lagos</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4501'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
        [
            "2",
            "F-016-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/16843' target='_blank'>ETFA 062-01 FISAM FISCALIZACIONES AMBIENTALES SPA</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>FISAM FISCALIZACIONES AMBIENTALES SPA</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>ETFA</li></ul>",
            "<ul class='sin-orden'><li>Región del Libertador General Bernardo O'Higgins</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4497'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
        [
            "3",
            "F-017-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/819' target='_blank'>TRANSPORTE DE RESIDUOS PELIGROSOS POR RUTAS DE LA REGION DE ANTOFAGASTA</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>LIMFOSEP S.A.</li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Transportes y almacenajes</li></ul>",
            "<ul class='sin-orden'><li>Región de Antofagasta</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4496'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
```

y aqui el mapeo para el siguiente ejemplo:
```json
[
            "5",
            "F-014-2026",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-building'></i><a href='/UnidadFiscalizable/Ficha/16839' target='_blank'>MOTEL MIRAGE</a></li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-user'></i>INVERSIONES MIRAGE SPA                                                          </li></ul>",
            "<ul class='fa-ul'><li><i class='fa-li fa fa-angle-right'></i>Equipamiento</li></ul>",
            "<ul class='sin-orden'><li>Región de la Araucanía</li></ul>",
            "En curso",
            "<span></span><a href='/Sancionatorio/Ficha/4492'><i class='fa fa-plus-circle'></i> Ver detalles</a>"
        ],
```
expediente -> F-014-2026
unidad_fiscalizable -> MOTEL MIRAGE
nombre_razon_social -> INVERSIONES MIRAGE SPA 
categoria -> Equipamiento
region -> Región de la Araucanía
estado -> En curso
detalle_link -> https://snifa.sma.gob.cl + /Sancionatorio/Ficha/4492
fecha_scraping -> Depende del scraping
ficha_id -> 4492

Ademas es importante notar que si por ejemplo la diferencia entre registros actuales y los registros totales es mayor que 10 (ej. 726 vs 743) es importante hacer la resta (743-726 = 17) y aproximarlo a la decena mas alta (17 -> 20) y ese valor se usara para el length en el POST (length=20)
Tambien puede hacerse que siempre se haga con 20 o 30 ya que casi nunca habra una diferencia mas alta que esa.
