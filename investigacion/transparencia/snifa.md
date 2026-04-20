# LINK
https://snifa.sma.gob.cl/Sancionatorio
# ANALISIS
En la pagina principal hay que llenar el formulario, el cual es dinamico y darle a buscar.
Eso se debe hacer para todas las categorias
Llevara a una pagina donde se muestran los ultimos 50 procedimientos de la categoria.
La mas nueva siempre ira primero   
Cada fila de la tabla es un procedimiento y la ultima columna es un link a los detalles del procedimiento con el siguiente formato https://snifa.sma.gob.cl/Sancionatorio/Ficha/{numero_ficha}.
Dentro de cada ficha podemos encontrar la siguiente informacion importante
Fecha de incio
Fecha de termino
Estado
y una tabla con documentos que tiene fecha, siempre el mas nuevo ira al final y de esa tabla nos interesa la fecha
# PROCEDIMIENTO E INFO A OBTENER
Por cada categoria hay que buscar y ver la tabla
Por cada fila de la tabla hay que obtener indice(#), expediente, nombre, estado, numero_ficha (final de la url) y su categoria, la cual se puede obtener al llenar el formulario
Luego se debe ingresar a la ficha de cada procedimiento que siga en curso y se debe obtener fecha de inicio, fecha de termino, estado, y de la tabla de documentos se debe obtener la fecha del documento mas nuevo.
Al final por procedimiento debemos tener la siguiente informacion
Nombre, Categoria, Estado, Fecha Inicio, Fecha Termino, Ultima Actualizacion, Link ficha
Para saber si cambio la tabla hay que ver si el indice (#) sigue con el expediente que tenia antes
ejemplo 
 # | Expediente
 1 D-058-2026

# PAGINA CON EJEMPLOS
## FORMULARIO CATEGORIA
https://snifa.sma.gob.cl/Sancionatorio
```html
<select class="form-control" id="categoria" name="categoria"><option value="">Seleccione Categoría</option>
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
<button class="btn btn-default pull-right hidden-mobile" onclick="buscar()" type="button">Buscar</button>
```
## ESTRUCTURA TABLA ULTIMOS 50 PROCEDIMIENTOS POR CATEGORIA
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

## ESTRUCTURA PAGINA FICHA
https://snifa.sma.gob.cl/Sancionatorio/Ficha/4475
Fecha inicio, Fecha Termino, Estado: 
```html
<div class="panel panel-default panel-expediente panel-expediente1">
                <div class="panel-body sin-padding">
                    <h3>Expediente: D-058-2026</h3>
                    <h4><i class="fa fa-calendar"></i> <b>Fecha Inicio :</b> <i>31-03-2026</i></h4>
                    <h4><i class="fa fa-calendar-check-o"></i> <b>Fecha Término: </b> <i></i></h4>
                    <h4><i class="fa fa-signal"></i> <b>Estado: </b> <i>En curso</i></h4>
                    <h4></h4>
                    <h4></h4>
                    <h4> </h4>
                    <h4></h4>
                </div>
            </div>
```

Tabla documentos
```html
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
```

