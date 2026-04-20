# LINK
https://www.sea.gob.cl/noticias
# ANALISIS
Pagina estatica con una tabla con noticias en 'wrappers'
Es con paginacion en el siguiente formato
https://www.sea.gob.cl/noticias?page=1
De todas formas como nos interesa siempre lo mas nuevo usaremos la pagina 0
## INFO A OBTENER
Imagen, fecha, hora, nombre noticia, link detalle
# ESTRUCTURA PAGINA E INFORMACION
Son varios de estos
```html
<div class="views-row">
    <div class="wrapper"><div class="views-field views-field-field-shared-imagen-portada"><div class="field-content">  <a href="/noticias/director-regional-de-sea-araucania-sostuvo-jornada-de-trabajo-con-nueva-seremi-del-medio" hreflang="es"><img loading="lazy" src="/sites/default/files/styles/imagen_noticia/public/imagenes/noticias/portada/DR-ARAUCANIA-Y-SEREMI-MEDIO-AMBIENTE.jpg?itok=K5xn3YWZ" width="555" height="310" alt="Dirección de la Araucania y Seremi Medio Ambiente" title="Dirección de la Araucania y Seremi Medio Ambiente" typeof="foaf:Image" class="image-style-imagen-noticia">

</a>
</div></div><div class="views-field views-field-field-shared-created"><div class="field-content"><time datetime="2026-04-17T21:34:18Z" class="datetime">Vie, 17/04/2026 - 17:34</time>
</div></div><div class="views-field views-field-title"><span class="field-content"><a href="/noticias/director-regional-de-sea-araucania-sostuvo-jornada-de-trabajo-con-nueva-seremi-del-medio" hreflang="es">Director regional de SEA Araucanía sostuvo jornada de trabajo con nueva seremi del Medio Ambiente de la región</a></span></div></div>
  </div>
```