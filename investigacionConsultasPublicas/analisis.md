# Consulta publica DGA

Este es mas facil de analizar
Funciona sin JS pero la imagen carga con JS

De la pagina
https://dga.mop.gob.cl/consulta-publica/

Debemos obtener lo que esta en pantalla, me dijeron que si cambia pero yo veo/creo que no.

Actualmente en la pantalla hay 3 formularios

```html
<div class="et_builder_inner_content et_pb_gutters3">
  <div
    class="et_pb_section et_pb_section_0 et_pb_fullwidth_section et_section_regular"
  >
    <section
      class="et_pb_module et_pb_fullwidth_header et_pb_fullwidth_header_0 et_pb_text_align_left et_pb_bg_layout_dark"
    >
      <span class="et_pb_background_mask"></span>
      <div class="et_pb_fullwidth_header_container left">
        <div class="header-content-container center">
          <div class="header-content">
            <h1 class="et_pb_module_header">Consulta Pública</h1>

            <div class="et_pb_header_content_wrapper"></div>
          </div>
        </div>
      </div>
      <div class="et_pb_fullwidth_header_overlay"></div>
      <div class="et_pb_fullwidth_header_scroll"></div>
    </section>
  </div>
  <div class="et_pb_section et_pb_section_1 et_section_regular">
    <div class="et_pb_row et_pb_row_0">
      <div
        class="et_pb_column et_pb_column_1_3 et_pb_column_0  et_pb_css_mix_blend_mode_passthrough"
      >
        <div
          class="et_pb_module et_pb_blurb et_pb_blurb_0 et_clickable  et_pb_text_align_left  et_pb_blurb_position_top et_pb_bg_layout_light"
        >
          <div class="et_pb_blurb_content">
            <div class="et_pb_main_blurb_image">
              <a href="http://forms.gle/7frq6iWfj41MDeuy6" target="_blank"
                ><span class="et_pb_image_wrap"
                  ><span
                    class="et-waypoint et_pb_animation_top et_pb_animation_top_tablet et_pb_animation_top_phone et-pb-icon agsdi-loaded et-animated"
                    >l</span
                  ></span
                ></a
              >
            </div>
            <div class="et_pb_blurb_container">
              <h4 class="et_pb_module_header">
                <a href="http://forms.gle/7frq6iWfj41MDeuy6" target="_blank"
                  >Reglamento declaración jurada para obras de construcción,
                  modificación, cambio y unificación de bocatomas</a
                >
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div
        class="et_pb_column et_pb_column_1_3 et_pb_column_1  et_pb_css_mix_blend_mode_passthrough"
      >
        <div
          class="et_pb_module et_pb_blurb et_pb_blurb_3 et_clickable  et_pb_text_align_left  et_pb_blurb_position_top et_pb_bg_layout_light"
        >
          <div class="et_pb_blurb_content">
            <div class="et_pb_main_blurb_image">
              <a href="https://forms.gle/CaVkytDpk9nn88kv7" target="_blank"
                ><span class="et_pb_image_wrap"
                  ><span
                    class="et-waypoint et_pb_animation_top et_pb_animation_top_tablet et_pb_animation_top_phone et-pb-icon agsdi-loaded et-animated"
                    >l</span
                  ></span
                ></a
              >
            </div>
            <div class="et_pb_blurb_container">
              <h4 class="et_pb_module_header">
                <a href="https://forms.gle/CaVkytDpk9nn88kv7" target="_blank"
                  >Reglamento declaración jurada de obras de modificación de
                  cauces naturales o artificiales</a
                >
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div
        class="et_pb_column et_pb_column_1_3 et_pb_column_2  et_pb_css_mix_blend_mode_passthrough et-last-child"
      >
        <div
          class="et_pb_module et_pb_blurb et_pb_blurb_4 et_clickable  et_pb_text_align_left  et_pb_blurb_position_top et_pb_bg_layout_light"
        >
          <div class="et_pb_blurb_content">
            <div class="et_pb_main_blurb_image">
              <a href="http://forms.gle/jxKf4aBFefHFeEum7" target="_blank"
                ><span class="et_pb_image_wrap"
                  ><span
                    class="et-waypoint et_pb_animation_top et_pb_animation_top_tablet et_pb_animation_top_phone et-pb-icon agsdi-loaded et-animated"
                    >i</span
                  ></span
                ></a
              >
            </div>
            <div class="et_pb_blurb_container">
              <h4 class="et_pb_module_header">
                <a href="http://forms.gle/jxKf4aBFefHFeEum7" target="_blank"
                  >Reglamento establece las condiciones técnicas que deberán
                  cumplirse en el proyecto, construcción y operación de obras
                  hidráulicas (DS N°50)</a
                >
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

Nos interesa obtener lo siguiente:

Nombre formulario:

```html
<a href="http://forms.gle/7frq6iWfj41MDeuy6" target="_blank"
  >Reglamento declaración jurada para obras de construcción, modificación,
  cambio y unificación de bocatomas</a
>
```

URL formulario ->
<a href="http://forms.gle/7frq6iWfj41MDeuy6"s
Imagen formulario ->

```html
<div class="et_pb_main_blurb_image">
  <a href="http://forms.gle/7frq6iWfj41MDeuy6" target="_blank"
    ><span class="et_pb_image_wrap"
      ><span
        class="et-waypoint et_pb_animation_top et_pb_animation_top_tablet et_pb_animation_top_phone et-pb-icon agsdi-loaded et-animated"
        >l</span
      ></span
    ></a
  >
</div>
```

y debera ir a la tabla:
id -> lo que esta despues de .gl/ del url (ej. 7frq6iWfj41MDeuy6)
nombre -> el nombre del formulario
imagen -> la url de la imagen
url -> la url del formulario

debera revisarse si hay algo nuevo al mismo tiempo que las otras consultas (click consultas en panel admin)

en la pestana de DGA debera simplemente mostrarse tarjetas asi:

imagen
nombre formulario
y que al clickearlas diga en un modal 'Esto te llevara a un formulario de Google' y un boton que diga 'ir al formulario' con la url correspondiente
el modal debe aparecer al hacer click en la tarjeta.
así con los 3 formularios

Si en un futuro desaparece uno de esos formularios y/o hay uno nuevo debera actualizarse borrando los formularios viejos y agregando el nuevo (en caso de haber).
Si despues hay cosas que no son formularios igual debera ser la misma idea de las tarjetas pero mas general y que diga tipo "Esto no es un formulario" y un boton para ir al link asociado

Necesito que se implemente un scheduler para las consultas publicas en general y que sea a ciertas horas, no cada cierto tiempo.
El boton de Consultas para scrapear manualmente debe seguir existiendo. Y el scheduler y el boton deben hacer lo mismo (scrapear consultas y agregarlas a la BD basado en los scrapers especificos).
