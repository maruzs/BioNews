# Sancionatorio

https://snifa.sma.gob.cl/Sancionatorio/Resultado

## ANALISIS

Dentro de la pagina hay que seleccionar categoria y luego buscar, hay que hacerlo para todas
Al buscar una categoria se mostrara una tabla, la cual debera compararse con la ultima tabla obtenida, si ha cambiado se debe actualizar, si no ha cambiado se mantiene todo igual.
Las columnas que nos interesan de cada tabla son las siguientes
Expediente
Unidad fiscalizable
Categoria
Estado
Detalle (Link al detalle)
En caso de que alguna columna o dato haya cambiado se debera actualizar toda esa informacion

### Seleccion categoria

```html
<div
  class="panel panel-default panel-busqueda-realizada"
  style="display: block;"
>
  <select class="form-control" id="categoria" name="categoria">
    <option value="">Seleccione Categoría</option>
    <option selected="selected" value="6">Agroindustrias</option>
    <option value="20">Alumbrado</option>
    <option value="10">Energía</option>
    <option value="11">Equipamiento</option>
    <option value="19">ETCA</option>
    <option value="14">ETFA</option>
    <option value="7">Forestal</option>
    <option value="4">Infraestructura de Transporte</option>
    <option value="2">Infraestructura Hidráulica</option>
    <option value="5">Infraestructura Portuaria</option>
    <option value="1">Instalación fabril</option>
    <option value="9">Minería</option>
    <option value="18">Monitoreo de calidad Ambiental</option>
    <option value="15">Otras categorías</option>
    <option value="8">Pesca y Acuicultura</option>
    <option value="3">Saneamiento Ambiental</option>
    <option value="13">Transportes y almacenajes</option>
    <option value="12">Vivienda e Inmobiliarios</option>
  </select>
  <button class="btn btn-default pull-right" type="button" onclick="buscar()">
    Buscar
  </button>
</div>
```
### TABLE HEAD AND BODY EXAMPLE
```html
<thead>
    <tr>
    <th class="th-contador sorting">#</th>
    <th class="sorting">Expediente</th>
    <th class="sorting">Unidad Fiscalizable</th>
    <th class="sorting">Nombre razón social</th>
    <th class="sorting_asc">Categoría</th>                              
    <th class="sorting">Región</th>
    <!-- <th>Comuna</th> -->                                
    <th class="sorting">Estado</th>
    <th style="width: 10%;" class="sorting">Detalle</th>
    </tr>
</thead>
<tr class="odd">
    <td data-label="#" class="">1</td>
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
    
<td data-label="Categoría" class=" sorting_1">
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
</tr>
```
En resumen

Por cada categoria -> buscar
Ver tabla
Comparar con ultima informacion tabla (nuevo expediente, cambio de estado de expediente previo)
Si hubo cambios descargar, si no se mantiene todo igual