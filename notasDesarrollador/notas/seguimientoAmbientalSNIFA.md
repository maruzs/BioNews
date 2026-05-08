### Nuevo apartado SNIFA:

Seguimiento ambiental:

Deberemos implementar un nuevo apartado de SNIFA llamado Seguimiento Ambiental

https://snifa.sma.gob.cl/SeguimientoAmbiental/RCA

Es importante no entrar directamente a https://snifa.sma.gob.cl/SeguimientoAmbiental/RCA/Resultado ya que nunca va a cargar por la enorme cantidad de registros

Hay que entrar a https://snifa.sma.gob.cl/SeguimientoAmbiental/RCA y usar el formulario y filtrar por anio.

Me gustaria que en el codigo de este scraper haya una lista de los anios que hay que revisar, asi puedo llenar la base de datos cambiando los anios que se agreguen y luego simplemente dejar el anio actual para que solo empiece a buscar los mas nuevos.
Es decir algo asi:

anios_revisar = [2024, 2025, 2026] para que se descarguen los registros de los ultimos 3 anios la primera vez que se ejecute el scraper y luego simplemente dejar el anio actual para que solo empiece a buscar los mas nuevos.

Utiliza el resto de scrapers de SNIFA/SMA como base para la estructura del codigo de scrapeo de RCA, sobretodo el de fiscalizaciones que tiene un funcionamiento similar ya que tampoco se puede ingresar directamente a la pagina de resultados y hay que pasar por el formulario. Tambien ten en consideracion que existe paginacion dentro de las tablas (Similar en todos los scrapers de snifa/sma)

- Scrapers SNIFA/SMA:

* fiscalizaciones.py
* medidas.py
* reqSEIA.py
* sanciones.py
* pdc.py
* snifa.py (son los sancionatorios)

Este es el html del formulario de la pagina https://snifa.sma.gob.cl/SeguimientoAmbiental/RCA:

```html
<form action="/SeguimientoAmbiental/Resultado" class="form-horizontal" id="formularioBuscarSeguimientoAmbiental"
    method="post">
    <div class="form-group">
        <label class="col-sm-5 control-label" for="nombre">Nombre Unidad Fiscalizable</label>
        <div class="col-sm-7">
            <input class="form-control" id="nombre" name="nombre" placeholder="Ingrese Nombre de Unidad Fiscalizable"
                type="text" value="">
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-5 control-label" for="categoria">Categoría Unidad Fiscalizable</label>
        <div class="col-sm-7">
            <select class="form-control" id="categoria" name="categoria">
                <option value="">Seleccione Categoría</option>
                <option value="6">Agroindustrias</option>
                <option value="20">Alumbrado</option>
                <option value="10">Energía</option>
                <option value="11">Equipamiento </option>
                <option value="19">ETCA</option>
                <option value="14">ETFA</option>
                <option value="7">Forestal </option>
                <option value="4">Infraestructura de Transporte </option>
                <option value="2">Infraestructura Hidráulica</option>
                <option value="5">Infraestructura Portuaria </option>
                <option value="1">Instalación fabril</option>
                <option value="9">Minería </option>
                <option value="18">Monitoreo de calidad Ambiental</option>
                <option value="15">Otras categorías</option>
                <option value="8">Pesca y Acuicultura </option>
                <option value="3">Saneamiento Ambiental </option>
                <option value="13">Transportes y almacenajes</option>
                <option value="12">Vivienda e Inmobiliarios</option>
            </select>
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-5 control-label" for="ddlRegion">Región</label>
        <div class="col-sm-7">
            <div class="btn-group bootstrap-select show-tick" style="width: 100%;"><button type="button"
                    class="btn dropdown-toggle bs-placeholder btn-multiselect" data-toggle="dropdown" role="button"
                    data-id="ddlRegion" title="Seleccione Región"><span class="filter-option pull-left">Seleccione
                        Región</span>&nbsp;<span class="bs-caret"><span class="caret"></span></span></button>
                <div class="dropdown-menu open" role="combobox">
                    <div class="bs-searchbox"><input type="text" class="form-control" autocomplete="off" role="textbox"
                            aria-label="Search"></div>
                    <div class="bs-actionsbox">
                        <div class="btn-group btn-group-sm btn-block"><button type="button"
                                class="actions-btn bs-select-all btn btn-multiselect">Todos</button><button
                                type="button" class="actions-btn bs-deselect-all btn btn-multiselect">Ninguno</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-5 control-label" for="ddlComuna">Comuna</label>
        <div class="col-sm-7">
            <div class="btn-group bootstrap-select show-tick" style="width: 100%;"><button type="button"
                    class="btn dropdown-toggle bs-placeholder btn-multiselect" data-toggle="dropdown" role="button"
                    data-id="ddlComuna" title="Seleccione Comuna"><span class="filter-option pull-left">Seleccione
                        Comuna</span>&nbsp;<span class="bs-caret"><span class="caret"></span></span></button>
                <div class="dropdown-menu open" role="combobox">
                    <div class="bs-searchbox"><input type="text" class="form-control" autocomplete="off" role="textbox"
                            aria-label="Search"></div>
                    <div class="bs-actionsbox">
                        <div class="btn-group btn-group-sm btn-block"><button type="button"
                                class="actions-btn bs-select-all btn btn-multiselect">Todos</button><button
                                type="button" class="actions-btn bs-deselect-all btn btn-multiselect">Ninguno</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-group">
            <label class="col-sm-5 control-label" for="numero">Número RCA</label>
            <div class="col-sm-7">
                <input class="form-control" id="numero" name="numero" placeholder="Ingrese Número RCA" type="text"
                    value="">
            </div>
        </div>
        <div class="form-group">
            <label class="col-sm-5 control-label" for="anno">Año RCA</label>
            <div class="col-sm-7">
                <input class="form-control" id="anno" name="anno" placeholder="Ingrese Año RCA" type="text" value="">
            </div>
        </div>
        <div class="form-group">
            <label class="col-sm-5 control-label" for="idsea">Id Seia</label>
            <div class="col-sm-7">
                <input class="form-control" id="idsea" name="idsea" placeholder="Ingrese Id Seia" type="text" value="">
            </div>
        </div>
        <!--CAMBIO LFI class botones -->
        <button class="btn btn-default pull-right btn-reiniciar" type="button" onclick="limpiar()">Reiniciar
            Búsqueda</button>
        <button class="btn btn-default pull-right hidden-mobile" onclick="buscar()" type="button">Buscar</button>
        <button class="btn btn-default pull-right hidden-desktop btn-buscar" onclick="cambiar()"
            type="button">Buscar</button>
        <div class="clearfix"></div>
</form>
```

De ahi el apartado que nos interesa es el siguiente:

```html
<div class="form-group">
  <label class="col-sm-5 control-label" for="anno">Año RCA</label>
  <div class="col-sm-7">
    <input
      class="form-control"
      id="anno"
      name="anno"
      placeholder="Ingrese Año RCA"
      type="text"
      value=""
    />
  </div>
</div>
```

y el boton

```html
<button class="btn btn-default pull-right hidden-mobile" onclick="buscar()" type="button">Buscar</button>
<button class="btn btn-default pull-right hidden-desktop btn-buscar"
```

Una vez dentro tendremos la siguiente tabla:

```html
<thead>
  <tr>
    <th style="width: 5%" class="sorting_asc">#</th>

    <th style="width: 10%" class="sorting">Fecha Informe</th>
    <th style="width: 10%" class="sorting">RCA Asociada</th>
    <th style="width: 10%" class="sorting">SubComponente Ambiental</th>
    <th style="width: 10%" class="sorting">Unidad Fiscalizable</th>
    <th style="width: 10%" class="sorting">Nombre razón social</th>
    <th style="width: 10%" class="sorting">Categoría</th>
    <th style="width: 10%" class="sorting">Región</th>

    <th style="width: 5%;" class="sorting">Detalle</th>
  </tr>
</thead>
```

y al final de la pagina lo que te decia de la paginacion:

```html
<div id="myTable_length" class="dataTables_length">
  Mostrar
  <select size="1" name="myTable_length">
    <option value="50" selected="selected">50</option>
    <option value="100">100</option>
    <option value="200">200</option>
    <option value="300">300</option>
    <option value="500">500</option>
    <option value="1000">1000</option>
    <option value="-1">Todos</option>
  </select>
  registros
</div>
```

De la tabla las columnas que nos interesan para cada registro son:

1. Fecha Informe (Esta en dd-mm-yyyy y debera guardarse como yyyy-mm-dd)
2. RCA Asociada (numero)
3. Enlace RCA Asociada (Enlace a la RCA)
4. SubComponente ambiental
5. Unidad Fiscalizable
6. Nombre razón social
7. Categoría
8. Región
9. Link detalle -> https://snifa.sma.gob.cl/SeguimientoAmbiental/Ficha/1092186

Y deberemos construir una nueva tabla en data/data.db con las siguientes columnas (debe tambien tener favoritos, las primeras dos columnas deben ser igual que como se ven las otras de SNIFA en la pagina)

tabla -> seguimiento_ambiental
RCA Asociada (PK - Text) -> 2026100012-2026
Fecha (Debe guardarse como yyyy-mm-dd)
SubComponente ambiental (Lista con los indices de los subcomponentes ambientales de otra tabla llamada indices_seguimiento_ambiental)
Nombre razon social (Text)
Categoria (Text)
Region (Text)
rca_asociada (text) -> Enlace a la RCA Asociada (ej. https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?id_expediente=2154523601)
Accion (Text - es el enlace a ver detalles en la pagina original)

Tabla -> indices_seguimiento_ambiental

1. id_seguimiento (INT)
2. nombre_seguimiento (Text)

En la interfaz debera verse lo siguiente:

Nº | Corazon | RCA Asociada | SubComponente ambiental | Unidad Fiscalizable | Nombre razon social | Categoria | Region | Ver RCA | Accion

La pagina debe ser igual a las otras del SMA y estar dentro de la categoria de SMA bajo el nombre seguimiento ambiental.
