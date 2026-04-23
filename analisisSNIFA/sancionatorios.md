# LINK
https://snifa.sma.gob.cl/Sancionatorio
# ANALISIS 1 (Pagina seleccion categoria)
A veces basta con presionar buscar, pero muchas veces falla y es mejor hacerlo por categoria (ademas de que es mas ordenado). Estas son las categorias que nos interesan:
Agroindustrias
Energía 
Infraestructura Portuaria 
Instalación fabril
Minería 
Saneamiento Ambiental 
Transportes y almacenajes

## INFO A OBTENER
# ESTRUCTURA PAGINA E INFORMACION
## PAGINA SELECCION CATEGORIA
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
<button class="btn btn-default pull-right btn-reiniciar" type="button" onclick="limpiar()">Reiniciar Búsqueda</button>
```

# ANALISIS 2 (Extraccion datos tabla)
Al haber seleccionado una categoria y clickeado 'buscar' nos llevara a una pagina que cuando es estatica muestra todos los resultados de la busqueda por categoria, cuando funciona de forma dinamica muestra los primeros 50 y para que muestre mas hay que cambiar la cantidad abajo. 
La pagina se genera de HTML, por lo que se demora un poco en cargar, no obtiene nada de json.
El problema con los datos de la tabla (de cualquier categoria) es que no incluyen la fecha, pero el de mas arriba siempre es el mas nuevo.
La informacion que nos interesa de cada fila es el expediente, el nombre razon social, categoria, estado y el link del detalle.

Esto se debe repetir para cada categoria deseada, volviendo atras, presionando reiniciar busqueda, pasando a la siguiente categoria, dandole a buscar y luego descargar x numero de pertinencias (la primera vez deberan ser todas, de ahi en adelante deberan ser solo las ultimas, revisando si la que antes tenia el indice 1 ahora ya no lo sigue teniendo, se entiende?)

# ESTRUCTURA PAGINA TABLAS
## Nombres columnas
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
```
## Ejemplo de filas
```html
<tr class="odd">
                                        <td data-label="#" class=" sorting_1">1</td>
                                        <td data-label="Expediente" nowrap="">F-006-2026</td>
                                        <td data-label="Unidad Fiscalizable">
                                                <ul class="fa-ul">
                                                        <li><i class="fa-li fa fa-building"></i><a href="/UnidadFiscalizable/Ficha/24436" target="_blank">TRANSFORMADORES TUSAN S.A. - ESTACIÓN CENTRAL</a></li>
                                                </ul>
                                        </td>
                                        <td data-label="Nombre Razon Social">
                                                <ul class="fa-ul">
                                                    <li><i class="fa-li fa fa-user"></i>TRANSFORMADORES TUSAN S.A.                                                                          </li>
                                            </ul>
                                        </td>
                                        
                                        <td data-label="Categoría">
                                                 <ul class="fa-ul">
                                                        <li><i class="fa-li fa fa-angle-right"></i>Energía</li>
                                                     </ul>
                                        </td>
                                        <td data-label="Región">
                                                <ul class="sin-orden">
                                                        <li>Región Metropolitana</li>
                                                </ul>
                                        </td>
                                        <!--
                                        <td data-label="Comuna">
                                                <ul class="sin-orden">
                                                        <li>Estaci&#243;n Central</li>
                                                </ul>
                                        </td>
                                        -->
                                        
                                        <td data-label="Estado">En curso</td>
                                        <!--CAMBIO LFI data-label y span-->
                                        <td data-label="Detalle">
                                            <span></span>
                                            <a href="/Sancionatorio/Ficha/4462"><i class="fa fa-plus-circle"></i> Ver detalles</a>
                                        </td>
                                    </tr>
<tr class="even">
                                        <td data-label="#" class=" sorting_1">2</td>
                                        <td data-label="Expediente" nowrap="">D-041-2026</td>
                                        <td data-label="Unidad Fiscalizable">
                                                <ul class="fa-ul">
                                                        <li><i class="fa-li fa fa-building"></i><a href="/UnidadFiscalizable/Ficha/3897" target="_blank">COMPLEJO INDUSTRIAL FORESTAL LEÓN</a></li>
                                                </ul>
                                        </td>
                                        <td data-label="Nombre Razon Social">
                                                <ul class="fa-ul">
                                                    <li><i class="fa-li fa fa-user"></i>FORESTAL LEON LIMITADA</li>
                                            </ul>
                                        </td>
                                        
                                        <td data-label="Categoría">
                                                 <ul class="fa-ul">
                                                        <li><i class="fa-li fa fa-angle-right"></i>Energía</li>
                                                     </ul>
                                        </td>
                                        <td data-label="Región">
                                                <ul class="sin-orden">
                                                        <li>Región de Ñuble</li>
                                                </ul>
                                        </td>
                                        <!--
                                        <td data-label="Comuna">
                                                <ul class="sin-orden">
                                                        <li>Coelemu</li>
                                                </ul>
                                        </td>
                                        -->
                                        
                                        <td data-label="Estado">En curso</td>
                                        <!--CAMBIO LFI data-label y span-->
                                        <td data-label="Detalle">
                                            <span></span>
                                            <a href="/Sancionatorio/Ficha/4451"><i class="fa fa-plus-circle"></i> Ver detalles</a>
                                        </td>
                                    </tr>
```



# A FUTURO, NO IMPLEMENTAR AHORA
A futuro me gustaria que pudiera marcarse como 'favoritos' aquellos que quiera mantener vigilados y hacerles seguimiento, de manera que me informe si hubo actualizaciones DENTRO del expediente (nuevos documentos por ejemplo)