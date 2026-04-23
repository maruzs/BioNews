# LINK
https://snifa.sma.gob.cl/RequerimientoIngreso
# ANALISIS 1 (Pagina seleccion categoria)
A veces basta con presionar buscar, pero muchas veces falla y es mejor hacerlo por categoria (ademas de que es mas ordenado). Estas son las categorias que nos interesan:
Agroindustrias
Energía 
Infraestructura Portuaria 
Instalación fabril
Minería 
Saneamiento Ambiental 
Transportes y almacenajes

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
El problema aqui recae en que no esta ordenado, por lo que es necesario que se guarde en la bbdd ordenado y estuve analizando y el link tiene el siguiente formato https://snifa.sma.gob.cl/RequerimientoIngreso/Ficha/10
y el numero despues de Ficha es el orden, los mas nuevos tienen un numero mas alto por lo que habria que ordenarlos basado en eso. El primero es el Ficha/8 

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




# A FUTURO, NO IMPLEMENTAR AHORA
A futuro me gustaria que pudiera marcarse como 'favoritos' aquellos que quiera mantener vigilados y hacerles seguimiento, de manera que me informe si hubo actualizaciones DENTRO del expediente (nuevos documentos por ejemplo)