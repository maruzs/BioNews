# LINK
https://snifa.sma.gob.cl/Sancionatorio/Resultado
# ANALISIS
Es necesario seleccionar categoria y click en buscar, eso para todas las categorias, y ese formulario carga con JS
Solo seleccionar categoria, no es necesario filtrar por region, comuna, etc.

## INFO A OBTENER
Expediente, Nombre, Categoria, Estado, Link detalle (o su numero de ficha)
# ESTRUCTURA PAGINA E INFORMACION

## Estructura formulario categorias
```html
<div class="col-sm-7">
<select class="form-control" id="categoria" name="categoria"><option value="">Seleccione Categoría</option>
<option selected="selected" value="6">Agroindustrias</option>
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
<button class="btn btn-default pull-right" type="button" onclick="buscar()">Buscar</button>
```

## SCRIPT BOTON BUSQUEDA
```js
<script type="text/javascript">
    
    function buscar() {
        var nombre = $("#nombre").val();
        var expediente = $("#expediente").val();
        var categoria = $("#categoria").val();
        var region = $("#ddlRegion").val();
        var comuna = $("#ddlComuna").val();

        if (nombre === "" && expediente === "" && categoria === "" && region === null && comuna === null) {
            $('#myModal').modal();
        } else {
            $('#formularioBuscarSancionatorio').submit();
        }
    }
    function limpiar() {
        $("#nombre").val("");
        $('#categoria option:first').attr('selected', 'selected');
        $('#ddlRegion').selectpicker('val', '');
        $('#ddlComuna').selectpicker('val', '');
        $("#expediente").val("");
        //getComunas();
        
    }
    $(document).ready(function () {
        $('#myTable').dataTable();
        $('#linkVerMapa').click(function () {
            $('#formularioBuscarSancionatorio').attr('action', '/Sancionatorio/Mapa');
            $('#formularioBuscarSancionatorio').submit();
        });
    });
</script>
```
## Estructura tabla
```html
<thead>
    <tr>
        <th class="th-contador sorting_asc">#</th>
        <th class="sorting">Expediente</th>
        <th class="sorting">Unidad Fiscalizable</th>
        <th class="sorting">Nombre razón social</th>
        <th class="sorting">Categoría</th>                              
        <th class="sorting">Región</th>
        <!-- <th>Comuna</th> -->                                
        <th class="sorting">Estado</th>
        <th style="width: 10%;" class="sorting">Detalle</th>
    </tr>
</thead>
<tbody><tr class="odd">
    <td data-label="#" class=" sorting_1">1</td>
    <td data-label="Expediente" nowrap="">D-058-2026</td>
    <td data-label="Unidad Fiscalizable">
            <ul class="fa-ul">
                    <li><i class="fa-li fa fa-building"></i><a href="/UnidadFiscalizable/Ficha/17749" target="_blank">FRUTOS RUCALHUE</a></li>
            </ul>
    </td>
    <td data-label="Nombre Razon Social">
            <ul class="fa-ul">
                <li><i class="fa-li fa fa-user"></i>FRUTOS RUCALHUE LTDA</li>
        </ul>
    </td>
    
    <td data-label="Categoría">
                <ul class="fa-ul">
                    <li><i class="fa-li fa fa-angle-right"></i>Agroindustrias</li>
                    </ul>
    </td>
    <td data-label="Región">
            <ul class="sin-orden">
                    <li>Región del Biobío</li>
            </ul>
    </td>
    <!--
    <td data-label="Comuna">
            <ul class="sin-orden">
                    <li>Quilaco</li>
            </ul>
    </td>
    -->
    
    <td data-label="Estado">En curso</td>
    <!--CAMBIO LFI data-label y span-->
    <td data-label="Detalle">
        <span></span>
        <a href="/Sancionatorio/Ficha/4475"><i class="fa fa-plus-circle"></i> Ver detalles</a>
    </td>
</tr><tr class="even">
    <td data-label="#" class=" sorting_1">2</td>
    <td data-label="Expediente" nowrap="">D-051-2026</td>
    <td data-label="Unidad Fiscalizable">
            <ul class="fa-ul">
                    <li><i class="fa-li fa fa-building"></i><a href="/UnidadFiscalizable/Ficha/15643" target="_blank">CENTRO DE MANEJO DE RESIDUOS ORGANICOS - COLHUE</a></li>
            </ul>
    </td>
    <td data-label="Nombre Razon Social">
            <ul class="fa-ul">
                <li><i class="fa-li fa fa-user"></i>CENTRO DE RESIDUOS ORGANICOS COLHUE S.A.                                                            </li>
        </ul>
    </td>
    
    <td data-label="Categoría">
                <ul class="fa-ul">
                    <li><i class="fa-li fa fa-angle-right"></i>Saneamiento Ambiental</li>
                    </ul>
    </td>
    <td data-label="Región">
            <ul class="sin-orden">
                    <li>Región del Libertador General Bernardo O'Higgins</li>
            </ul>
    </td>
    <!--
    <td data-label="Comuna">
            <ul class="sin-orden">
                    <li>Malloa</li>
            </ul>
    </td>
    -->
    
    <td data-label="Estado">En curso</td>
    <!--CAMBIO LFI data-label y span-->
    <td data-label="Detalle">
        <span></span>
        <a href="/Sancionatorio/Ficha/4473"><i class="fa fa-plus-circle"></i> Ver detalles</a>
    </td>
```

## LINK DETALLES EJEMPLO

## ANALISIS
De cada procedimiento sancionatorio de cada categoria se deberan guardar
Expediente, Nombre, Categoria, Estado, numero de ficha (al final del link de detalles)
Se debera guardar el numero de ficha de todos los procedimientos sancionatorios que esten "en curso"
Cada vez que se actualice se debera revisar por categoria si hay algun nuevo procedimiento (expediente), siempre se anaden al inicio de la tabla.
Ademas se debera revisar el detalle de cada procedimiento sancionatorio que haya estado en curso.
Es decir, usando el numero de ficha guardado se debera buscar https://snifa.sma.gob.cl/Sancionatorio/Ficha/{numero_ficha} y revisar lo siguiente:
Estado
Fecha de termino
En la tabla de documentos revisar si hay nuevos documentos, no me interesa nada mas que el nombre y la fecha

Resumen del funcionamiento

1. Se debera ingresar a la pagina, seleccionar la primera categoria de un listado de categorias predefinido
2. Una vez seleccionada la categoria se debera dar click a 'Buscar'
3. Una vez la tabla haya cargado se debera descargar la siguiente informacion de cada una de las filas
    * Expediente
    * Nombre proyecto
    * Categoria
    * Numero de ficha que esta al final de la url de los detalles
4. Ademas debera ingresar a los detalles (snifa.sma.gob.cl/Sancionatorio/Ficha/{numero_ficha}) de cada una de las filas y revisar lo siguiente:
    * Fecha inicio
    * Fecha Termino
    * Estado
    y abajo hay una tabla con documentos, la cual tiene fechas. La ultima fila siempre es el ultimo cambio con la ultima fecha. Deberas guardar esa ultima fecha
    ```html
    <div id="documentos" class="tab-pane fade in active">
        <table class="conBorde tabla-resultado-busqueda"> 
            <thead>
                <tr>
                    <th style="width: 10%;">#</th>
                    <th>Nombre Documento</th>
                    <th style="width: 30%;">Tipo Documento</th>
                    <th style="width: 10%;">Fecha</th>
                    <th style="width: 10%;">Link</th>
                </tr>
            </thead>
            <tbody>
                    <tr>
                        <td data-label="#">1</td>
                        <td data-label="Nombre Documento">Formulación de Cargos</td>
                        <td data-label="Tipo Documento">Formulación de Cargos</td>
                        <td data-label="Fecha">31-03-2026</td>
                        <td data-label="Link">
                            <a href="/General/Descargar/20601092864" target="_blank"><i class="fa fa-download"></i> Descargar</a>
                        </td>
                    </tr>
                    <tr>
                        <td data-label="#">2</td>
                        <td data-label="Nombre Documento">Memorándum DSC 131/2026</td>
                        <td data-label="Tipo Documento">Otros</td>
                        <td data-label="Fecha">31-03-2026</td>
                        <td data-label="Link">
                            <a href="/General/Descargar/20612092865" target="_blank"><i class="fa fa-download"></i> Descargar</a>
                        </td>
                    </tr>
                    <tr>
                        <td data-label="#">3</td>
                        <td data-label="Nombre Documento">Carpeta de antecedentes</td>
                        <td data-label="Tipo Documento">Otros</td>
                        <td data-label="Fecha">31-03-2026</td>
                        <td data-label="Link">
                            <a href="/General/Descargar/20612093218" target="_blank"><i class="fa fa-download"></i> Descargar</a>
                        </td>
                    </tr>
                    <tr>
                        <td data-label="#">4</td>
                        <td data-label="Nombre Documento">Notificación Titular Res. Ex. N°1</td>
                        <td data-label="Tipo Documento">Notificación Formulación de Cargos</td>
                        <td data-label="Fecha">09-04-2026</td>
                        <td data-label="Link">
                            <a href="/General/Descargar/20634093217" target="_blank"><i class="fa fa-download"></i> Descargar</a>
                        </td>
                    </tr>
            </tbody>
        </table>
    </div>
    ```

    Es decir, para los ultimos 50 procedimientos sancionatorios debera obtener lo siguiente
    Expediente, nombre, categoria, estado, fecha inicio, fecha ultima actualizacion, numero_ficha
    Y cada vez que se pida actualizar la informacion debera revisar si hay procedimientos nuevos y guardar la informacion, pero para los procedimientos antiguos que sigan teniendo el estado "en curso" se debera actualizar el estado (si cambio) y la fecha de ultima actualizacion (si hubo nuevos documentos)



1. Click en actualizar info (pagina principal)
2. Revisar tabla de procedimientos por categoria
3. Revisar estado y actualizaciones de procedimientos en curso
4. Agregar si hay nuevos procedimientos, actualizar estado si ya no esta en curso, actualizar fecha ultima actualizacion si hay nuevos documentos