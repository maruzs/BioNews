# LINK
https://2ta.lexsoft.cl/2ta/search?proc=4
# ANALISIS
Es dinamica
Recibe un json con paginacion, pero si intenta cambiar la url da el siguiente error

JBWEB000065: HTTP Status 405 - Request method 'GET' not supported
JBWEB000309: type JBWEB000067: Status report
JBWEB000068: message Request method 'GET' not supported
JBWEB000069: description JBWEB000125: The specified HTTP method is not allowed for the requested resource.
JBoss Web/7.4.8.Final-redhat-4

Ese json esta bien ordenado pero la verdad no tiene tanta utilidad, es muy largo y solo muestra los ultimos 10 de su paginacion, pero no entrega si quiera la id correcta para ir a ver la causa directamente. 
Debido a esto sera mejor solo leer la tabla presentada

## INFO A OBTENER
rol, fecha ingreso, caratula, procedimiento, etapa, link a detalle (href del rol)
# ESTRUCTURA PAGINA E INFORMACION
ejemplo tabla entera para la paginacion 1, que muestra los ultimos 10
```html
<table id="selectable" class="table table-condensed table-hover">
    <thead>
    <tr>
        <th width="10%"><span>Rol</span></th>
        <th width="10%"><span>Fecha Ingreso</span></th>
        <th width="50%"><span>Carátula</span></th>
        <th width="10%"><span>Procedimiento</span></th>
        <th width="10%"><span>Etapa</span></th>
        <th width="10%" style="text-align:center"><span>Entrar</span></th>
    </tr>
    </thead>
    <tbody data-bind="foreach: causas()">
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400705">R-628-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">10-04-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Pastene Solís Juan Gilberto / Servicio de Evaluación Ambiental (Res. Ex. N° 202699101251, de fecha 6 de marzo de 2026)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400704">R-627-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">09-04-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Suárez Vallejos Héctor Rodrigo / Superintendencia del Medio Ambiente (Res. Ex. N° N°2 / Rol D-302-2025 de fecha 16 de marzo de 2026) </td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400703">R-626-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">03-04-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Universidad Las Américas/ Superintendencia del Medio Ambiente (Res. Ex. N°  819 de fecha 25 de marzo de 2026) </td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400701">R-625-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">27-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Cancino Cardoza Liliana Andrea / Servicio de Evaluación Ambiental (Res. Ex. N° 202699101152, de 12 de febrero de 2025)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400700">R-624-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">23-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Salmones Islas del Sur Limitada/ Ministerio del Medio Ambiente ( Oficio Ordinario Nº 234053, de 22 de septiembre de 2023)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400699">R-623-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">13-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Pérez Vera Miguel Angel / Servicio de Evaluación Ambiental (Res. Ex. 202699101102 de 29 de enero de 2026)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400698">R-622-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">13-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Ilustre Municipalidad de la Ligua / Servicio de Evaluación Ambiental (Res. Ex. 202699101102 de 29 de enero de 2026)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400696">R-621-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">05-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Inmobiliaria e Inversiones Las Olas SpA. y otros / Ministerio de Medio Ambiente (Res. Ex. N° 373/2026  22 de enero de 2026)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400695">R-620-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">04-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Sánchez Sandoval Gonzalo Andrés Rafael / Servicio de Evaluación Ambiental (Res. Ex. N°20269910191 de 28 de enero de 2026)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    
    <tr>
        <td width="10%" style="font-weight: bold;"><u>
            <a data-bind="text: rol, click: function(){$parent.openCausa($data)},
                    attr: {href: 'search?proc=3&amp;idCausa='+$data.id()}" style="cursor: pointer;" href="search?proc=3&amp;idCausa=400693">R-619-2026</a></u></td>
        <td width="10%" nowrap="" data-bind="text: fecha">04-03-2026</td>
        <td width="50%" style="white-space: normal;" nowrap="" data-bind="text: descripcion">Echeverría Izquierdo Edificaciones S.A. / Superintendencia del Medio Ambiente (Res. Ex. N° 3013 de 31 de diciembre de 2025)</td>
        <td width="10%" nowrap="" data-bind="text: procedimiento().name">Reclamación</td>
        <td width="10%" nowrap="" data-bind="text: 'Ingreso'">Ingreso</td>
        <td width="10%" align="center" nowrap=""><span data-bind="click: function(){$parent.openCausa($data)}" style="cursor: pointer;" class="glyphicon glyphicon-new-window"></span></td>
    </tr>
    </tbody>
</table>
``` 
elemento de paginacion
```html
<ul class="box-pagination-causa pagination"><li class="active"><span class="current prev">Anterior</span></li><li class="active"><span class="current">1</span></li><li><a class="page-link">2</a></li><li><a class="page-link">3</a></li><li><a class="page-link">4</a></li><li><a class="page-link">5</a></li><li><a class="page-link next">Siguiente</a></li></ul>
```