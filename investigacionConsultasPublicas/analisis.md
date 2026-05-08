# PAGINAS DE CONSULTAS PUBLICAS/CIUDADANASS

## Ministerio de Medio Ambiente (MMA)

- https://consultasciudadanas.mma.gob.cl/portal -> Consultas vigentes
  - consultasAbiertas.html
- https://consultasciudadanas.mma.gob.cl/portal/consultas_cerradas -> Consultas cerradas
  - consultasCerradas.html

### CONSULTAS ABIERTAS (Ej. consultasAbiertas.html)

Aqui tenemos el problema de que las consultas abiertas mostradas no contienen demasiada informacion inmediata, este es un ejemplo de una consulta abierta:

```html
<a href="https://consultasciudadanas.mma.gob.cl/portal/consulta/227">
    <p class="card-text">
        <div class="row">
            <div class="dayCounter p-4 flecha right col-lg-2 col-12 align-self-center">
                <h5 class="numberCounter text-center text-white mb-0 floatClose">35</h5>
                <h6 class="daysRemaining
                                                    text-center
                                                    floatClose
                                                    upCon
                                                    mt-lg-0
                                                    ml-lg-0
                                                    mt-3">
                    días para cierre
                </h6>
            </div>
            <div class="col-lg-9 col-10 align-self-center">
                <p class="card-text">
                <h6 class="m-3">ANTEPROYECTO DE LAS NORMAS SECUNDARIAS DE CALIDAD AMBIENTAL PARA LA PROTECCION DE LAS
                    AGUAS CONTINENTALES SUPERFICIALES DE LA CUENCA DEL RIO RAPEL</h6>
    </p>
    </div>
    <div class="chevron-hidden col-lg-1 col-2 align-self-center"><span class="chevron right"></span></div>
    </div>
    </p>
</a>
```

Como puedes ver no tiene mucha informacion, de hecho solo tenemos 4 consultas abiertas disponibles en este momento, lo cual facilita bastante lo que tenemos que hacer:

1. Vamos a entrar a cada consulta abierta y obtener la informacion necesaria
   Ejemplo del interior de una consulta (https://consultasciudadanas.mma.gob.cl/portal/consulta/227)
   Aqui dentro tenemos la siguiente card que nos interesa

```html
<div class="card text-letf border-light">
  <!---->
  <div class="card-header header-card bg-blue text-white">
    <div>Detalle consulta ciudadana</div>
  </div>
  <div class="card-body">
    <!----><!---->
    <div class="row">
      <div class="pb-4 pb-lg-0 col-lg-8 col-12">
        <p class="card-text font-weight-bold my-2">
          Nombre instrumento en consulta :
        </p>
        <p class="card-text">
          ANTEPROYECTO DE LAS NORMAS SECUNDARIAS DE CALIDAD AMBIENTAL PARA LA
          PROTECCION DE LAS AGUAS CONTINENTALES SUPERFICIALES DE LA CUENCA DEL
          RIO RAPEL
        </p>
      </div>
      <div class="col-lg-4 col-12">
        <div class="row">
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Estado consulta</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">Activo</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Fecha de inicio</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">3/16/2026</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Fecha de término</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">6/11/2026</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Días para el cierre</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">35 días corridos</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Tipo de Instrumento</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">Normas</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Tipo de Proceso</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">Revisión</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Ámbito Territorial</p>
          </div>
          <div class="col align-self-center">
            <p class="my-2">Regional</p>
          </div>
          <div class="w-100">
            <hr />
          </div>
          <div class="col align-self-center">
            <p class="font-weight-bold my-2">Expediente</p>
          </div>
          <div class="col align-self-center">
            <a
              href="https://planesynormas.mma.gob.cl/normas/expediente/index.php?tipo=busqueda&amp;id_expediente=943523"
              rel="noopener"
              target="_blank"
              class="doc"
            >
              Ir al expediente
            </a>
          </div>
        </div>
      </div>
      <div class="position p-0 w-autoResponive col-lg-8 col-12 align-self-end">
        <div class="row">
          <div class="p-0 col-lg-4 col-12">
            <a
              href="/storage/consultation/Z2JagRQfIgw6DnhtYTSqiWn0zXJ7UmeBZFH1ggC2.pdf"
              rel="noopener"
              target="_blank"
              class="doc"
            >
              Documento en consulta
            </a>
          </div>
          <div class="p-lg-0 col-lg-4 col-12"><span></span></div>
          <!---->
        </div>
      </div>
    </div>
  </div>
  <!----><!---->
</div>
```

De cada consulta abierta nos interesa obtener lo siguiente (usare los datos del ejemplo anterior):

1. Nombre instrumento en consulta -> ANTEPROYECTO DE LAS NORMAS SECUNDARIAS DE CALIDAD AMBIENTAL PARA LA PROTECCION DE LAS AGUAS CONTINENTALES SUPERFICIALES DE LA CUENCA DEL RIO RAPEL
2. Estado -> Activo
3. Fecha de inicio -> 3/16/2026
4. Fecha de termino -> 6/11/2026
5. Tipo de Instrumento -> Normas
6. Tipo de proceso -> Revisión
7. Ambito territorial -> Regional

La tabla para consultas abiertas tendra las siguientes columnas:
id (Text UNIQUE primary key) -> https://consultasciudadanas.mma.gob.cl/portal/consulta/227 -> 227 (Lo obtenemos del número al final del link de la consulta)
nombre_instrumento (Text)
fecha_inicio (Text) -> Formato mm/dd/yyyy
fecha_termino (Text) -> Formato mm/dd/yyyy
tipo_instrumento (Text)
tipo_proceso (Text)
ambito_territorial (Text)
link_detalle (Text)

### CONSULTAS CERRADAS

Aqui tenemos un problema y es que en las consultas cerradas hay 4 categorias pero no logro encontrar el metodo de paginacion.

```html
<ul
  role="tablist"
  id="closeConsultation__BV_tab_controls_"
  class="nav nav-tabs ahover nav-border"
>
  <!---->
  <li role="presentation" class="nav-item">
    <a
      role="tab"
      id="__BVID__17___BV_tab_button__"
      aria-selected="false"
      aria-setsize="4"
      aria-posinset="1"
      aria-controls="__BVID__17"
      href="#"
      target="_self"
      class="nav-link"
      tabindex="-1"
      >Planes</a
    >
  </li>
  <li role="presentation" class="nav-item">
    <a
      role="tab"
      aria-selected="true"
      aria-setsize="4"
      aria-posinset="2"
      href="#"
      target="_self"
      class="nav-link active font-weight-bold text-white bg-grey nav-border"
      id="__BVID__19___BV_tab_button__"
      aria-controls="__BVID__19"
      >Normas</a
    >
  </li>
  <li role="presentation" class="nav-item">
    <a
      role="tab"
      tabindex="-1"
      aria-selected="false"
      aria-setsize="4"
      aria-posinset="3"
      href="#"
      target="_self"
      class="nav-link"
      id="__BVID__21___BV_tab_button__"
      aria-controls="__BVID__21"
      >Otros Instrumentos</a
    >
  </li>
  <li role="presentation" class="nav-item">
    <a
      role="tab"
      tabindex="-1"
      aria-selected="false"
      aria-setsize="4"
      aria-posinset="4"
      href="#"
      target="_self"
      class="nav-link"
      id="__BVID__23___BV_tab_button__"
      aria-controls="__BVID__23"
      >Clasificación de Especies</a
    >
  </li>
  <!---->
</ul>
```

Dentro de cada uno de eso hay distintas Consultas cerradas, pero todas mantienen el mismo formato, este es el ejemplo de una consulta cerrada dentro de la categoria 'Planes':

```html
<a href="https://consultasciudadanas.mma.gob.cl/portal/consulta/216">
    <p class="card-text">
        <div class="row">
            <div class="lock p-3 text-center flecha right col-lg-2 col-12"><i
                    class="fas fa-lock fa-3x m-2 floatClose"></i>
                <h6 class="daysRemaining
                                            text-center
                                            mt-lg-0
                                            ml-lg-0
                                            ml-3
                                            mt-4
                                            floatClose">
                    Cerrada
                </h6>
            </div>
            <div class="col-lg-6 col-12 align-self-center">
                <p class="card-text">
                <h6 class="m-2">ANTEPROYECTO DE REGLAMENTO SOBRE DECLARACIÓN DE ZONAS LATENTES Y SATURADAS, PLANES DE
                    PREVENCIÓN Y DESCONTAMINACIÓN, Y MEDIDAS PROVISIONALES</h6>
    </p>
    </div>
    <div class="mid"></div>
    <div class="pr-1 col-lg-3 col-12 align-self-center">
        <p class="text-muted m-0"><strong>Ambito territorial:</strong>
            Nacional
        </p>
        <p class="text-muted m-0"><strong>Número de Observaciones:</strong>
            33
        </p>
        <p class="text-close m-0"><strong>Fecha inicio:</strong>
            2025-10-20 00:00:00
        </p>
        <p class="text-close m-0"><strong>Fecha término:</strong>
            2025-11-21 23:59:59
        </p>
    </div>
    <div class="lg-1 chevron-hidden col-lg-1 col-2 align-self-center"><span class="chevron right"></span></div>
    </div>
    </p>
</a>
```

Esta es una consulta de la categoria 'Normas':

```html
<a href="https://consultasciudadanas.mma.gob.cl/portal/consulta/212">
    <p class="card-text">
        <div class="row">
            <div class="lock p-3 text-center col-lg-2 col-12"><i class="fas fa-lock fa-3x m-2"></i>
                <h6 class="daysRemaining text-center">Cerrada</h6>
            </div>
            <div class="col-lg-6 col-12 align-self-center">
                <p class="card-text">
                <h6 class="m-2">ANTEPROYECTO DE LA NORMA SECUNDARIA DE CALIDAD DEL AIRE PARA DIÓXIDO DE AZUFRE (SO2),
                    ELABORADO A PARTIR DE LA REVISIÓN DEL DECRETO SUPREMO Nº22, DE 2009, DEL MINISTERIO SECRETARÍA
                    GENERAL DE LA PRESIDENCIA</h6>
    </p>
    </div>
    <div class="mid"></div>
    <div class="pr-1 col-lg-3 col-12 align-self-center">
        <p class="text-muted m-0"><strong>Ambito territorial:</strong>
            Nacional
        </p>
        <p class="text-muted m-0"><strong>Número de Observaciones:</strong>
            10
        </p>
        <p class="text-close m-0"><strong>Fecha inicio:</strong>
            2025-09-08 00:00:00
        </p>
        <p class="text-close m-0"><strong>Fecha término:</strong>
            2025-12-04 23:59:59
        </p>
    </div>
    <div class="lg-1 col-lg-1 col-2 align-self-center"><span class="chevron right"></span></div>
    </div>
    </p>
</a>
```

Esta es una consulta de la categoria 'Otros Instrumentos':

```html
<a href="https://consultasciudadanas.mma.gob.cl/portal/consulta/225">
    <p class="card-text">
        <div class="row">
            <div class="lock p-3 text-center col-lg-2 col-12"><i class="fas fa-lock fa-3x m-2"></i>
                <h6 class="daysRemaining text-center">Cerrada</h6>
            </div>
            <div class="col-lg-6 col-12 align-self-center">
                <p class="card-text">
                <h6 class="m-2">ANTEPROYECTO DE DECRETO SUPREMO QUE ESTABLECE METAS DE RECOLECCIÓN Y VALORIZACIÓN Y
                    OTRAS OBLIGACIONES ASOCIADAS DE BATERÍAS</h6>
    </p>
    </div>
    <div class="mid"></div>
    <div class="pr-1 col-lg-3 col-12 align-self-center">
        <p class="text-muted m-0"><strong>Ambito territorial:</strong>
            Nacional
        </p>
        <p class="text-muted m-0"><strong>Número de Observaciones:</strong>
            114
        </p>
        <p class="text-close m-0"><strong>Fecha inicio:</strong>
            2026-02-25 00:00:00
        </p>
        <p class="text-close m-0"><strong>Fecha término:</strong>
            2026-04-30 23:59:59
        </p>
    </div>
    <div class="lg-1 col-lg-1 col-2 align-self-center"><span class="chevron right"></span></div>
    </div>
    </p>
</a>
```

Esta es una consulta de la categoria 'Clasificación de Especies':

```html
<a href="https://consultasciudadanas.mma.gob.cl/portal/consulta/198"><p class="card-text"><div class="row"><div class="lock p-3 text-center col-lg-2 col-12"><i class="fas fa-lock fa-3x m-2"></i> <h6 class="daysRemaining text-center">Cerrada</h6></div> <div class="col-lg-6 col-12 align-self-center"><p class="card-text"><h6 class="m-2">ANTEPROYECTO DE REGLAMENTO PARA LA CLASIFICACIÓN DE ESPECIES SEGÚN SU ESTADO DE CONSERVACIÓN</h6></p></div> <div class="mid"></div> <div class="pr-1 col-lg-3 col-12 align-self-center"><p class="text-muted m-0"><strong>Ambito territorial:</strong>
                                            Nacional
                                        </p> <p class="text-muted m-0"><strong>Número de Observaciones:</strong>
                                            52
                                        </p> <p class="text-close m-0"><strong>Fecha inicio:</strong>
                                            2025-06-17 00:00:00
                                        </p> <p class="text-close m-0"><strong>Fecha término:</strong>
                                            2025-07-31 23:59:59
                                        </p></div> <div class="lg-1 col-lg-1 col-2 align-self-center"><span class="chevron right"></span></div></div></p></a>
```

En las consultas cerradas por suerte tenemos mas informacion expuesta directamente sin necesidad de entrar a cada consulta
De cada consulta cerrada nos interesa obtener lo siguiente (usare los datos del ejemplo 'Planes' anterior ):

1. Nombre instrumento en consulta -> ANTEPROYECTO DE REGLAMENTO SOBRE DECLARACIÓN DE ZONAS LATENTES Y SATURADAS, PLANES DE PREVENCIÓN Y DESCONTAMINACIÓN, Y MEDIDAS PROVISIONALES
2. Estado -> Cerrada
3. Fecha de inicio -> 2025-10-20 00:00:00
4. Fecha de termino -> 2025-11-21 23:59:59
5. Tipo de Instrumento -> Planes
6. Ambito territorial -> Regional
7. Link al detalle de la consulta ->

La tabla para consultas cerradas tendra las siguientes columnas:

id (Text UNIQUE primary key) -> https://consultasciudadanas.mma.gob.cl/portal/consulta/216 -> 216 (Lo obtenemos del número al final del link de la consulta)
nombre_instrumento (Text)
fecha_inicio (Text) -> Formato mm/dd/yyyy
fecha_termino (Text) -> Formato mm/dd/yyyy
tipo_instrumento (Text)
ambito_territorial (Text)
link_detalle (Text)

Para construir las tablas seguiremos estas respectivas logicas:

1. Consultas abiertas:
   Ingresamos al link de cada consulta abierta y obtenemos la informacion

2. Consultas cerradas:
   Basta con la informacion que se muestra en la card principal para obtener lo necesario, no es necesario ingresar al detalle de la consulta.
   Pero para obtenerlos todos necesitamos recorrer Planes, Normas, Otros Instrumentos y Clasificacion de Especies y aplicar la logica que describimos anteriormente.

Entonces seguiremos este flujo:

1. Vamos a la pagina -> https://consultasciudadanas.mma.gob.cl/portal/consultas_cerradas
2. Obtenemos todas las consultas cerradas de Planes:

```html
<li role="presentation" class="nav-item">
  <a
    role="tab"
    id="__BVID__17___BV_tab_button__"
    aria-selected="true"
    aria-setsize="4"
    aria-posinset="1"
    aria-controls="__BVID__17"
    href="#"
    target="_self"
    class="nav-link active font-weight-bold text-white bg-grey nav-border"
    >Planes</a
  >
</li>
```

3. Hacemos click en 'Normas' y obtenemos todas las consultas cerradas de Normas:

```html
<li role="presentation" class="nav-item">
  <a
    role="tab"
    aria-selected="false"
    aria-setsize="4"
    aria-posinset="2"
    href="#"
    target="_self"
    class="nav-link"
    id="__BVID__19___BV_tab_button__"
    aria-controls="__BVID__19"
    tabindex="-1"
    >Normas</a
  >
</li>
```

4. Hacemos click en 'Otros Instrumentos' y obtenemos todas las consultas cerradas de Otros Instrumentos:

```html
<li role="presentation" class="nav-item">
  <a
    role="tab"
    aria-selected="false"
    aria-setsize="4"
    aria-posinset="3"
    href="#"
    target="_self"
    class="nav-link"
    id="__BVID__21___BV_tab_button__"
    aria-controls="__BVID__21"
    tabindex="-1"
    >Otros Instrumentos</a
  >
</li>
```

5. Hacemos click en 'Clasificacion de Especies' y obtenemos todas las consultas cerradas de Clasificacion de Especies:

```html
<li role="presentation" class="nav-item">
  <a
    role="tab"
    aria-selected="false"
    aria-setsize="4"
    aria-posinset="4"
    href="#"
    target="_self"
    class="nav-link"
    id="__BVID__23___BV_tab_button__"
    aria-controls="__BVID__23"
    tabindex="-1"
    >Clasificación de Especies</a
  >
</li>
```

En resumen, una vez dentro de la pagina de consultas cerradas, necesitamos aplicar una logica para extraer toda la informacion de cada tipo de instrumento.

La primera vez que se ejecute el scraper deberan obtenerse TODAS las consultas abiertas y cerradas, despues cada vez que se ejecute el scraper solo debera obtener las consultas nuevas en Abiertas y Cerradas, y ademas debe verificar si alguna consulta que esta en Abiertas pasó a Cerradas y en ese caso actualizar el estado y la fecha de termino de esa consulta
