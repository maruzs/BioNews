## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

Ok, tenemos 1 problema nuevo y otros 2 antiguos:

1. El problema nuevo es que cuando hay un registro nuevo (borre la ultima pertinencia y luego la scrapee y todo bien) y entro a la categoria me aparece como nueva, pero solo durante unos segundos, esos segundos son durante el rato que se muestran 100 registros y no los 25k (Esto ocurre para todas las categorias pero en pertinencias logre notarlo mejor ya que el lapso fue mayor), una vez que cargan los 25k registros desaparece la etiqueta de 'Nueva'. Deberia seguir ahi hasta que yo cierre la categoria.

2. Uno de los problemas antiguos tiene que ver con SNIFA/SMA, como puedes ver en los logs :

```bash
INFO:     172.18.0.6:60970 - "POST /api/scrape/snifa HTTP/1.1" 200 OK
bionews-api        | 2026-05-19 13:20:02,278 [INFO] MANUAL
bionews-api        | Iniciando scraper de Procedimientos Sancionatorios...
bionews-web        | 172.20.0.4 - - [19/May/2026:17:20:02 +0000] "POST /api/scrape/snifa HTTP/1.1" 200 55 "https://moscow-office-browsers-close.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:a17b:95f3:4ef4:7b0, 172.20.0.1"
bionews-api        | Registros actuales en BD: 3354
bionews-api        | Registros en la web: 0
bionews-api        | No hay registros nuevos. La BD esta actualizada.
```

Me sale que hay 0 registros en la web cuando en realidad hay 3,358 registros en https://snifa.sma.gob.cl/Sancionatorio/Resultado. El funcionamiento de este scraper es igual al de todos los demas de SMA/SNIFA con la excepcion de fiscalizaciones que requeria pasar por el filtro primero y no directamente a 'Resultados'

3. El otro problema antiguo que estuve viendo es que en las consultas publicas del minsal no se estan extrayendo las nuevas consultas publicas vigentes. Por ejemplo el 18 de mayo hubo una pero la ultima que se ve es del 5 de mayo, y al ejecutar el scraper me sale lo siguiente:

```bash
bionews-api        | INFO:     172.18.0.6:57334 - "POST /api/scrape/consultas HTTP/1.1" 200 OK
bionews-api        | 2026-05-19 13:33:35,863 [INFO] Procesando MINSAL Consultas...
bionews-web        | 172.20.0.4 - - [19/May/2026:17:33:35 +0000] "POST /api/scrape/consultas HTTP/1.1" 200 69 "https://moscow-office-browsers-close.trycloudflare.com/admin" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0" "2803:c600:7115:a6b9:a17b:95f3:4ef4:7b0, 172.20.0.1"
bionews-api        |   MINSAL: 37 consultas analizadas, 0 nuevas.
```

Si bien es verdad que si hay 37 consultas en total en la pagina, no aparece la nueva del 18 de mayo en la tabla. Eso si me di cuenta que la ultima que aparece en las vigentes en la tabla de bionews ya no existe en la pagina de consultas vigentes del minsal, puede que tenga que ver con eso, sobretodo porque puede haber ocurrido que se haya borrado la del 5 de mayo en la pagina del minsal (No esta tampoco en los resultados de consultas) y que la del 5 de mayo haya tenido la misma ID que la del 18 de mayo, solo que al borrarse la del 5 de mayo no se descarga la nueva ya que se compara con una ID que ya existia. El problema ahora recae en que no existe ninguna otra manera de caracterizarlas ya que en el propio HTML no hay ningun otro valor que sea unico aparte del "e-n-accordion-item-8720"
La otra opcion que se me ocurre es que todas las veces que se ejecute el scraper de consultas vigentes del minsal se borren todas las que habian y se descarguen todas nuevamente, de esa manera siempre se tendra constancia de lo nuevo que aparecio, ademas no importa TANTO el llevar un historial de las consultas publicas previas en el minsal especificamente.
