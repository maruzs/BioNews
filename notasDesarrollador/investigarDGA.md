# LINK 
https://dga.mop.gob.cl/

# NOTICIAS
https://dga.mop.gob.cl/noticias/

Aqui tenemos un problema y es que las 3 noticias mas nuevas se presentan en un slider y no muestra la fecha de publicacion.

Slider:
```html
<div
    class="et_pb_module et_pb_post_slider et_pb_post_slider_0 et_pb_slider et_pb_post_slider_image_background et_pb_slider_fullwidth_off et_pb_slider_with_overlay et_pb_bg_layout_dark">




    <div class="et_pb_slides">
        <div class="et_pb_slide et_pb_bg_layout_dark et_pb_post_slide-987612035 et-pb-active-slide"
            style="background-image: url(https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1.jpg);">
            <div class="et_pb_slide_overlay_container"></div>
            <div class="et_pb_container clearfix" style="height: 547.033px;">
                <div class="et_pb_slider_container_inner">
                    <div class="et_pb_slide_description">
                        <h2 class="et_pb_slide_title"><a
                                href="https://dga.mop.gob.cl/asumen-funciones-nuevos-directores-regionales-de-la-dga/">Asumen
                                funciones nuevos directores regionales de la DGA</a></h2>
                        <div class="et_pb_slide_content
																">
                            <div>
                                <p>Durante los días 13, 14 y 15 de mayo, los nuevos directores regionales sostendrán un
                                    encuentro de trabajo con los equipos y jefaturas del Nivel Central.</p>
                            </div>
                        </div>
                        <div class="et_pb_button_wrapper"><a class="et_pb_button et_pb_more_button"
                                href="https://dga.mop.gob.cl/asumen-funciones-nuevos-directores-regionales-de-la-dga/">Leer
                                más</a></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="et_pb_slide et_pb_bg_layout_dark et_pb_post_slide-987612029"
            style="background-image: url(https://dga.mop.gob.cl/uploads/sites/13/2026/05/Estudio-Sta-Maria-y-Mocha-Lebu-DR-Biobio.jpg);">
            <div class="et_pb_slide_overlay_container"></div>
            <div class="et_pb_container clearfix" style="height: 547.033px;">
                <div class="et_pb_slider_container_inner">
                    <div class="et_pb_slide_description">
                        <h2 class="et_pb_slide_title"><a
                                href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/">DGA
                                Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha</a></h2>
                        <div class="et_pb_slide_content
																">
                            <div>
                                <p>El análisis, que se inició el 23 de abril y durará 12 meses, apunta a fortalecer la
                                    gestión eficiente del recurso hídrico a nivel local, promoviendo además el trabajo
                                    coordinado entre instituciones.</p>
                            </div>
                        </div>
                        <div class="et_pb_button_wrapper"><a class="et_pb_button et_pb_more_button"
                                href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/">Leer
                                más</a></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="et_pb_slide et_pb_bg_layout_dark et_pb_post_slide-987611960"
            style="background-image: url(https://dga.mop.gob.cl/uploads/sites/13/2026/04/Foto-FIIE-Coquimbo.jpeg);">
            <div class="et_pb_slide_overlay_container"></div>
            <div class="et_pb_container clearfix" style="height: 547.033px;">
                <div class="et_pb_slider_container_inner">
                    <div class="et_pb_slide_description">
                        <h2 class="et_pb_slide_title"><a
                                href="https://dga.mop.gob.cl/presentan-resultados-de-proyecto-que-investigo-balance-hidrico-del-rio-limari-gracias-al-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos-fiie/">Presentan
                                resultados de proyecto que investigó balance hídrico del río Limarí gracias al Fondo
                                para la Investigación, Innovación y Educación en Recursos Hídricos (FIIE)</a></h2>
                        <div class="et_pb_slide_content
																">
                            <div>
                                <p>Actualmente está en desarrollo la tercera versión del concurso FIIE, y el plazo de
                                    cierre de las postulaciones es el domingo 26 de abril.</p>
                            </div>
                        </div>
                        <div class="et_pb_button_wrapper"><a class="et_pb_button et_pb_more_button"
                                href="https://dga.mop.gob.cl/presentan-resultados-de-proyecto-que-investigo-balance-hidrico-del-rio-limari-gracias-al-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos-fiie/">Leer
                                más</a></div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <div class="et-pb-slider-arrows"><a class="et-pb-arrow-prev" href="#"><span>Anterior</span></a><a
            class="et-pb-arrow-next" href="#"><span>Siguiente</span></a></div>
    <div class="et-pb-controllers"><a href="#" class="et-pb-active-control">1</a><a href="#">2</a><a href="#">3</a>
    </div>
</div>
```

Pero resulta que si vamos a la pagina principal (https://dga.mop.gob.cl/) podemos ver que hay un apartado de noticias donde estan las 3 mas nuevas que se muestran en el slider pero con sus fechas. Por lo que nos conviene primero scrapear las noticias de la pagina principal y luego del apartado de noticias.

## NOTICIAS EN PAGINA PRINCIPAL
```html
<div class="et_pb_section et_pb_section_2 et_pb_section_parallax et_pb_with_background et_section_regular">

    <span class="et_parallax_bg_wrap"><span class="et_parallax_bg"
            style="background-image: url(&quot;https://dga.mop.gob.cl/uploads/sites/13/2023/11/DGA-fondowebgris.jpg&quot;); height: 753.967px; transform: translate(0px, 72.35px);"></span></span>




    <div class="et_pb_row et_pb_row_1">
        <div class="et_pb_column et_pb_column_4_4 et_pb_column_4  et_pb_css_mix_blend_mode_passthrough et-last-child">




            <div
                class="et_pb_with_border et_pb_module et_pb_text et_pb_text_0  et_pb_text_align_left et_pb_bg_layout_light">




                <div class="et_pb_text_inner">
                    <h2 style="text-align: left"><span style="color: #ffffff"><span
                                style="color: #00498e">Noticias</span></span></h2>
                </div>
            </div>
        </div>




    </div>
    <div class="et_pb_row et_pb_row_2 et_pb_gutters2">
        <div class="et_pb_column et_pb_column_4_4 et_pb_column_5  et_pb_css_mix_blend_mode_passthrough et-last-child">




            <div class="et_pb_with_border et_pb_module et_pb_blog_0 et_pb_blog_grid_wrapper et_pb_bg_layout_light">
                <div class="et_pb_blog_grid clearfix ">




                    <div class="et_pb_ajax_pagination_container">
                        <div class="et_pb_salvattore_content" data-columns="3">
                            <div class="column size-1of3">
                                <article id="post-987612035"
                                    class="et_pb_post clearfix et_pb_blog_item_0_0 post-987612035 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias">

                                    <div class="et_pb_image_container"><a
                                            href="https://dga.mop.gob.cl/asumen-funciones-nuevos-directores-regionales-de-la-dga/"
                                            class="entry-featured-image-url"><img fetchpriority="high" decoding="async"
                                                src="https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1-400x250.jpg"
                                                alt="Asumen funciones nuevos directores regionales de la DGA" class=""
                                                srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1-400x250.jpg 480w "
                                                sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a>
                                    </div>
                                    <h2 class="entry-title">
                                        <a
                                            href="https://dga.mop.gob.cl/asumen-funciones-nuevos-directores-regionales-de-la-dga/">Asumen
                                            funciones nuevos directores regionales de la DGA</a>
                                    </h2>

                                    <p class="post-meta"><span class="published">05/05/2026</span></p>
                                    <div class="post-content">
                                        <div class="post-content-inner et_multi_view_hidden">
                                            <p>Desde ayer lunes 4 de mayo ya está en funciones la totalidad de los
                                                nuevos directores regionales de la Dirección General de Aguas, quienes
                                                encabezarán el organismo a nivel local en cada una de las 16 regiones
                                                del país. La DGA les da la bienvenida a sus nuevas...</p>
                                        </div>
                                    </div>
                                </article>
                            </div>
                            <div class="column size-1of3">
                                <article id="post-987612029"
                                    class="et_pb_post clearfix et_pb_blog_item_0_1 post-987612029 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias">

                                    <div class="et_pb_image_container"><a
                                            href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/"
                                            class="entry-featured-image-url"><img loading="lazy" decoding="async"
                                                src="https://dga.mop.gob.cl/uploads/sites/13/2026/05/Estudio-Sta-Maria-y-Mocha-Lebu-DR-Biobio-400x250.jpg"
                                                alt="DGA Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha"
                                                class=""
                                                srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/05/Estudio-Sta-Maria-y-Mocha-Lebu-DR-Biobio.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/05/Estudio-Sta-Maria-y-Mocha-Lebu-DR-Biobio-400x250.jpg 480w "
                                                sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a>
                                    </div>
                                    <h2 class="entry-title">
                                        <a
                                            href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/">DGA
                                            Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha</a>
                                    </h2>

                                    <p class="post-meta"><span class="published">05/05/2026</span></p>
                                    <div class="post-content">
                                        <div class="post-content-inner et_multi_view_hidden">
                                            <p>El director regional de Aguas del Biobío, Matías Mendoza Lama, presentó
                                                ayer en dependencias de la Municipalidad de Lebu los alcances que tendrá
                                                el estudio denominado “Diagnóstico hidrológico e hidrogeológico Isla
                                                Santa María y Mocha”, que analizará los sistemas...</p>
                                        </div>
                                    </div>
                                </article>
                            </div>
                            <div class="column size-1of3">
                                <article id="post-987611960"
                                    class="et_pb_post clearfix et_pb_blog_item_0_2 post-987611960 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias">

                                    <div class="et_pb_image_container"><a
                                            href="https://dga.mop.gob.cl/presentan-resultados-de-proyecto-que-investigo-balance-hidrico-del-rio-limari-gracias-al-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos-fiie/"
                                            class="entry-featured-image-url"><img loading="lazy" decoding="async"
                                                src="https://dga.mop.gob.cl/uploads/sites/13/2026/04/Foto-FIIE-Coquimbo-400x250.jpeg"
                                                alt="Presentan resultados de proyecto que investigó balance hídrico del río Limarí gracias al Fondo para la Investigación, Innovación y Educación en Recursos Hídricos (FIIE)"
                                                class=""
                                                srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/04/Foto-FIIE-Coquimbo.jpeg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/04/Foto-FIIE-Coquimbo-400x250.jpeg 480w "
                                                sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a>
                                    </div>
                                    <h2 class="entry-title">
                                        <a
                                            href="https://dga.mop.gob.cl/presentan-resultados-de-proyecto-que-investigo-balance-hidrico-del-rio-limari-gracias-al-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos-fiie/">Presentan
                                            resultados de proyecto que investigó balance hídrico del río Limarí gracias
                                            al Fondo para la Investigación, Innovación y Educación en Recursos Hídricos
                                            (FIIE)</a>
                                    </h2>

                                    <p class="post-meta"><span class="published">13/04/2026</span></p>
                                    <div class="post-content">
                                        <div class="post-content-inner et_multi_view_hidden">
                                            <p>El pasado miércoles 8 de abril, y con la asistencia del Seremi MOP de
                                                Coquimbo, Cristian Smitmans y otras autoridades locales, se presentaron
                                                en Ovalle los resultados de la “Investigación de Recarga Actualizada del
                                                SHAC Limarí”, proyecto ejecutado por la Corporación...</p>
                                        </div>
                                    </div>
                                </article>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="et_pb_button_module_wrapper et_pb_button_0_wrapper et_pb_button_alignment_center et_pb_module ">
                <a class="et_pb_button et_pb_button_0 et_pb_bg_layout_dark" href="https://dga.mop.gob.cl/noticias/">MÁS
                    NOTICIAS</a>
            </div>
        </div>




    </div>


</div>
```

De ahi nos interesa rellenar la siguiente tabla que estara en la base de datos data/data.db
Table: noticias
link (TEXT) PK
titulo (TEXT)
fecha (TEXT)
imagen (TEXT)
fuente (TEXT)
fecha_scraping (TIMESTAMP)

Se debe llenar con lo siguiente

- link:
Hay que identificar pero generalmente esta dentro de un h2 y un enlace como ves en el ejemplo:
```html
<h2 class="entry-title">
    <a
        href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/">DGA
        Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha</a>
</h2>
```
Aqui seria -> https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/
- titulo:
Hay que identificar pero generalmente esta dentro de un h2 y el titulo como ves en el ejemplo:
```html
<h2 class="entry-title">
    <a
        href="https://dga.mop.gob.cl/dga-biobio-presenta-alcances-de-estudio-hidrico-en-islas-santa-maria-y-mocha/">DGA
        Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha</a>
</h2>
```
De aqui seria -> DGA Biobío presenta alcances de estudio hídrico en islas Santa María y Mocha
- fecha
Se puede encontrar en el siguiente apartado y formato:
```html
<p class="post-meta"><span class="published">05/05/2026</span></p>
```
De aqui seria -> 05/05/2026`
imagen:
Se puede encontrar en el siguiente apartado:
```html
<img fetchpriority="high" decoding="async"
src="https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1-400x250.jpg">
```
De aqui seria -> https://dga.mop.gob.cl/uploads/sites/13/2026/05/Directores-Regionales-DGA-2026-1-400x250.jpg
fuente -> DGA
fecha_scraping -> Fecha en que el scraping se haya ejecutado

## NOTICIAS EN SECCION DE NOTICIAS

De aqui ignoramos la informacion dentro del slider y pasamos directamente a las noticias que estan como una tabla:

```html
<div class="et_pb_salvattore_content" data-columns="3">
    <div class="column size-1of3">
        <article id="post-40493"
            class="et_pb_post clearfix et_pb_blog_item_0_0 post-40493 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/mop-constituye-primera-reserva-de-aguas-subterraneas-para-subsistencia-en-san-pedro-de-atacama/"
                    class="entry-featured-image-url"><img fetchpriority="high" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Salar-de-Atacama-1-400x250.jpg"
                        alt="MOP constituye primera reserva de aguas subterráneas para subsistencia en San Pedro de Atacama"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Salar-de-Atacama-1.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/03/Salar-de-Atacama-1-400x250.jpg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/mop-constituye-primera-reserva-de-aguas-subterraneas-para-subsistencia-en-san-pedro-de-atacama/">MOP
                    constituye primera reserva de aguas subterráneas para subsistencia en San Pedro de Atacama</a>
            </h2>

            <p class="post-meta"><span class="published">10 marzo, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>Contraloría General de la República tomó razón de la primera reserva declarada por la Dirección
                        General de Aguas en el país bajo facultad excepcional del Código de Aguas de abril de 2022.</p>
                </div>
            </div>
        </article>
        <article id="post-40466"
            class="et_pb_post clearfix et_pb_blog_item_0_3 post-40466 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/el-catastro-de-las-aguas-en-chile-datos-historicos-en-la-gestion-de-permisos/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Director-General-de-Aguas-Rodrigo-Sanhueza_en-Alta-Res-2-400x250.jpg"
                        alt="El catastro de las aguas en Chile, datos históricos en la gestión de permisos" class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Director-General-de-Aguas-Rodrigo-Sanhueza_en-Alta-Res-2.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/03/Director-General-de-Aguas-Rodrigo-Sanhueza_en-Alta-Res-2-400x250.jpg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/el-catastro-de-las-aguas-en-chile-datos-historicos-en-la-gestion-de-permisos/">El
                    catastro de las aguas en Chile, datos históricos en la gestión de permisos</a>
            </h2>

            <p class="post-meta"><span class="published">5 marzo, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>Columna de opinión del director general de Aguas del MOP, Rodrigo Bravo Sanhueza.</p>
                </div>
            </div>
        </article>
        <article id="post-40316"
            class="et_pb_post clearfix et_pb_blog_item_0_6 post-40316 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/ocho-colegios-son-finalistas-en-el-concurso-junior-del-agua-que-organiza-la-dga-del-mop/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/02/MOP-JUNIOR-DEL-AGUA-GANADORES-CONVOCATORIA-2024-400x250.jpg"
                        alt="Ocho colegios son finalistas en el concurso Junior del Agua que organiza la DGA del MOP"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/02/MOP-JUNIOR-DEL-AGUA-GANADORES-CONVOCATORIA-2024.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/02/MOP-JUNIOR-DEL-AGUA-GANADORES-CONVOCATORIA-2024-400x250.jpg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/ocho-colegios-son-finalistas-en-el-concurso-junior-del-agua-que-organiza-la-dga-del-mop/">Ocho
                    colegios son finalistas en el concurso Junior del Agua que organiza la DGA del MOP</a>
            </h2>

            <p class="post-meta"><span class="published">4 febrero, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>Los tres mejores proyectos deberán ser presentados al jurado en marzo para definir el equipo
                        ganador para representar a Chile en la versión internacional del certamen en Suecia en agosto
                        próximo.</p>
                </div>
            </div>
        </article>
    </div>
    <div class="column size-1of3">
        <article id="post-40487"
            class="et_pb_post clearfix et_pb_blog_item_0_1 post-40487 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/estudiantes-del-liceo-blanco-encalada-de-caldera-representaran-a-chile-en-el-concurso-junior-del-agua-en-suecia/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Premiacion-primer-lugar-1-400x250.jpeg"
                        alt="Estudiantes del Liceo Blanco Encalada de Caldera representarán a Chile en el concurso Junior del Agua en Suecia"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Premiacion-primer-lugar-1.jpeg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/03/Premiacion-primer-lugar-1-400x250.jpeg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/estudiantes-del-liceo-blanco-encalada-de-caldera-representaran-a-chile-en-el-concurso-junior-del-agua-en-suecia/">Estudiantes
                    del Liceo Blanco Encalada de Caldera representarán a Chile en el concurso Junior del Agua en
                    Suecia</a>
            </h2>

            <p class="post-meta"><span class="published">10 marzo, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>El segundo lugar lo obtuvo el Liceo Bicentenario Polivalente Nuestra Señora de la Merced de San
                        Carlos, Región de Ñuble y el tercer lugar el Instituto Federico Errázuriz de Santa Cruz, Región
                        de O’Higgins.</p>
                </div>
            </div>
        </article>
        <article id="post-40406"
            class="et_pb_post clearfix et_pb_blog_item_0_4 post-40406 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/mop-invita-a-participar-en-la-tercera-version-del-concurso-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/02/Proyecto-CEAZA-2025-400x250.jpg"
                        alt="MOP invita a participar en la tercera versión del concurso Fondo para la Investigación, Innovación y Educación en Recursos Hídricos"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/02/Proyecto-CEAZA-2025.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/02/Proyecto-CEAZA-2025-400x250.jpg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/mop-invita-a-participar-en-la-tercera-version-del-concurso-fondo-para-la-investigacion-innovacion-y-educacion-en-recursos-hidricos/">MOP
                    invita a participar en la tercera versión del concurso Fondo para la Investigación, Innovación y
                    Educación en Recursos Hídricos</a>
            </h2>

            <p class="post-meta"><span class="published">25 febrero, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>El presupuesto total es de $166.776.000 y el plazo para ingresar postulaciones al concurso de la
                        Dirección General de Aguas cierra el 26 de abril.</p>
                </div>
            </div>
        </article>
        <article id="post-40275"
            class="et_pb_post clearfix et_pb_blog_item_0_7 post-40275 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/mesa-estrategica-de-recursos-hidricos-de-la-cuenca-costera-entre-seno-andrew-y-punta-desengano-avanza-con-analisis-de-indicadores-de-seguridad-hidrica/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/02/MERH-extraordinaria-enero-2026-400x250.jpeg"
                        alt="Mesa Estratégica de Recursos Hídricos de la cuenca costera entre seno Andrew y Punta Desengaño avanza con análisis de indicadores de seguridad hídrica"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/02/MERH-extraordinaria-enero-2026.jpeg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/02/MERH-extraordinaria-enero-2026-400x250.jpeg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/mesa-estrategica-de-recursos-hidricos-de-la-cuenca-costera-entre-seno-andrew-y-punta-desengano-avanza-con-analisis-de-indicadores-de-seguridad-hidrica/">Mesa
                    Estratégica de Recursos Hídricos de la cuenca costera entre seno Andrew y Punta Desengaño avanza con
                    análisis de indicadores de seguridad hídrica</a>
            </h2>

            <p class="post-meta"><span class="published">2 febrero, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>En la primera sesión extraordinaria del año, los integrantes de la Mesa abordaron en un taller
                        los indicadores que servirán para medir la efectividad y eficiencia de las medidas del Plan
                        Estratégico de Recursos Hídricos en la cuenca. </p>
                </div>
            </div>
        </article>
    </div>
    <div class="column size-1of3">
        <article id="post-40470"
            class="et_pb_post clearfix et_pb_blog_item_0_2 post-40470 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/plan-de-adaptacion-al-cambio-climatico-en-recursos-hidricos-10-medidas-y-35-acciones-para-la-seguridad-hidrica/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Difusion-PACC-RH-03_03_2026x-400x250.jpeg"
                        alt="Plan de Adaptación al Cambio Climático en Recursos Hídricos: 10 medidas y 35 acciones para la seguridad hídrica"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/03/Difusion-PACC-RH-03_03_2026x.jpeg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/03/Difusion-PACC-RH-03_03_2026x-400x250.jpeg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/plan-de-adaptacion-al-cambio-climatico-en-recursos-hidricos-10-medidas-y-35-acciones-para-la-seguridad-hidrica/">Plan
                    de Adaptación al Cambio Climático en Recursos Hídricos: 10 medidas y 35 acciones para la seguridad
                    hídrica</a>
            </h2>

            <p class="post-meta"><span class="published">6 marzo, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>Los alcances de la iniciativa que lidera la Dirección General de Aguas del MOP con apoyo de FAO y
                        el financiamiento del Fondo Verde del Clima fueron socializados con la sociedad civil, sector
                        público y privado en una jornada presencial y vía streaming. </p>
                </div>
            </div>
        </article>
        <article id="post-40322"
            class="et_pb_post clearfix et_pb_blog_item_0_5 post-40322 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/dga-ohiggins-inaugura-nuevas-estaciones-de-la-red-hidrometrica-regional-en-sectores-precordilleranos-del-alto-cachapoal/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/02/Nuevas-estaciones-DGA-OHiggins-1-400x250.jpeg"
                        alt="DGA O’Higgins inaugura nuevas estaciones de la red hidrométrica regional en sectores precordilleranos del alto Cachapoal"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/02/Nuevas-estaciones-DGA-OHiggins-1.jpeg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/02/Nuevas-estaciones-DGA-OHiggins-1-400x250.jpeg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/dga-ohiggins-inaugura-nuevas-estaciones-de-la-red-hidrometrica-regional-en-sectores-precordilleranos-del-alto-cachapoal/">DGA
                    O’Higgins inaugura nuevas estaciones de la red hidrométrica regional en sectores precordilleranos
                    del alto Cachapoal</a>
            </h2>

            <p class="post-meta"><span class="published">4 febrero, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>La red consta de 197 estaciones del tipo fluviométricas, meteorológicas, embalses, glaciológicas,
                        nivométricas y de pozos para monitorear las aguas subterráneas.</p>
                </div>
            </div>
        </article>
        <article id="post-40256"
            class="et_pb_post clearfix et_pb_blog_item_0_8 post-40256 post type-post status-publish format-standard has-post-thumbnail hentry category-noticias has-box-shadow-overlay">
            <div class="box-shadow-overlay"></div>

            <div class="et_pb_image_container"><a
                    href="https://dga.mop.gob.cl/a-mas-de-397-mil-millones-de-pesos-asciende-el-monto-identificado-a-pagar-en-patentes-por-no-uso-de-aguas/"
                    class="entry-featured-image-url"><img loading="lazy" decoding="async"
                        src="https://dga.mop.gob.cl/uploads/sites/13/2026/01/DGAer-400x250.jpg"
                        alt="A más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de aguas"
                        class=""
                        srcset="https://dga.mop.gob.cl/uploads/sites/13/2026/01/DGAer-scaled.jpg 479w, https://dga.mop.gob.cl/uploads/sites/13/2026/01/DGAer-400x250.jpg 480w "
                        sizes="(max-width:479px) 479px, 100vw " width="400" height="250"></a></div>
            <h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/a-mas-de-397-mil-millones-de-pesos-asciende-el-monto-identificado-a-pagar-en-patentes-por-no-uso-de-aguas/">A
                    más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de
                    aguas</a>
            </h2>

            <p class="post-meta"><span class="published">30 enero, 2026</span></p>
            <div class="post-content">
                <div class="post-content-inner et_multi_view_hidden">
                    <p>• El proceso de cobro de patentes 2026 comenzó oficialmente el jueves 15 de enero con la
                        publicación en el Diario Oficial del listado de titulares de derechos de aprovechamiento de
                        aguas que elabora la Dirección General de Aguas del MOP y cuyo pago se debe realizar en la
                        Tesorería General de la República el 31 de marzo próximo.</p>
                </div>
            </div>
        </article>
    </div>
</div>
```

De ahi tambien debemos llenar la tabla y es basicamente lo mismo de la parte de arriba

De ahi nos interesa rellenar la siguiente tabla que estara en la base de datos data/data.db
Table: noticias
link (TEXT) PK
titulo (TEXT)
fecha (TEXT)
imagen (TEXT)
fuente (TEXT)
fecha_scraping (TIMESTAMP)

Se debe llenar con lo siguiente

- link:
Hay que identificar pero generalmente esta dentro de un h2 y un enlace como ves en el ejemplo:
```html
<h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/a-mas-de-397-mil-millones-de-pesos-asciende-el-monto-identificado-a-pagar-en-patentes-por-no-uso-de-aguas/">A
                    más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de
                    aguas</a>
            </h2>
```
Aqui seria -> https://dga.mop.gob.cl/a-mas-de-397-mil-millones-de-pesos-asciende-el-monto-identificado-a-pagar-en-patentes-por-no-uso-de-aguas/

- titulo:
Hay que identificar pero generalmente esta dentro de un h2 y el titulo como ves en el ejemplo:
```html
<h2 class="entry-title">
                <a
                    href="https://dga.mop.gob.cl/a-mas-de-397-mil-millones-de-pesos-asciende-el-monto-identificado-a-pagar-en-patentes-por-no-uso-de-aguas/">A
                    más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de
                    aguas</a>
            </h2>
```
De aqui seria -> A más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de aguas

- fecha
Se puede encontrar en el siguiente apartado y formato:
```html
<p class="post-meta"><span class="published">30 enero, 2026</span></p>
```
De aqui seria -> 30 enero, 2026 

- imagen:
Se puede encontrar en el siguiente apartado:
```html
class="entry-featured-image-url"><img loading="lazy" decoding="async"
src="https://dga.mop.gob.cl/uploads/sites/13/2026/01/DGAer-400x250.jpg"
alt="A más de 397 mil millones de pesos asciende el monto identificado a pagar en patentes por no uso de aguas"
class=""
```
De aqui seria -> https://dga.mop.gob.cl/uploads/sites/13/2026/01/DGAer-400x250.jpg
fuente -> DGA
fecha_scraping -> Fecha en que el scraping se haya ejecutado


