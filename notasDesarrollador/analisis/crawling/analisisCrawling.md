# Analisis crawling de SNIFA

Nosotros tenemos varios apartados de SNIFA, lo que quiero es que todo registro que haya sido agregado a favoritos se le pueda hacer seguimiento automatico mediante crawling a la pagina a la que lleva el hacer click el detalle.

El crawling se debera hacer una vez al dia para cada registro agregado a favoritos y deberan notificarse los cambios en la pestana de favoritos con un punto rojo como el resto de paginas.

Al entrar a favoritos debe mostrarse con una etiqueta lo que haya cambiado (ej. que diga 'cambios! o algo por el estilo') y al clickear sobre el registro (cualquier zona) debe abrirse un modal que muestre lo nuevo que aparecio (ej algun documento con su nombre y fecha) y que permita clickear el documento para poder verlo directamente o ir a la pagina de origen

Al mostrar los cambios, no se deben mostrar los documentos que ya existian, sino solo los nuevos que se agregaron.

## SMA - Fiscalizaciones (dfz-2026)

Dentro de una ficha de ejemplo para las fiscalizaciones tenemos lo siguiente
url de ejemplo -> https://snifa.sma.gob.cl/Fiscalizacion/Ficha/1075953

```html
<div class="container contenido">
  <script>
    $("#cargandoInformacion").modal({
      backdrop: "static",
      show: false,
    });
    var $modal = $("#cargandoInformacion");
    $modal.modal("show");
  </script>

  <!--CAMBIO LFI-->
  <div class="volver-busqueda tipo-fisc">
    <a href="/Fiscalizacion"
      ><img src="/images/f-fisc.png" /> Volver a la Búsqueda</a
    >
  </div>
  <!--FIN CAMBIO LFI-->

  <div class="categoria1">
    <div class="row">
      <div class="col-md-12">
        <!--CAMBIO LFI class titulo-->
        <div class="hidden-mobile panel titulo panel-default">
          <div class="panel-body">
            <div class="titulo-categoria">
              <img src="/images/ic1.png" /> Fiscalizaciones
            </div>
          </div>
        </div>
        <div class="item-mobile item1 titulo-interior hidden-desktop">
          <a href="#">
            <div>
              <img src="/images/ic1b.png" />
              <span>Fiscalizaciones</span>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <!--CAMBIO LFI-->
  <div class="tipo-fisc">
    <div class="row">
      <div class="col-md-4">
        <div class="panel panel-default panel-expediente panel-expediente1">
          <div class="panel-body sin-padding">
            <h3>Expediente: DFZ-2026-1585-X-NE</h3>
            <h4>
              <i class="fa fa-clipboard"></i> <b>Instrumento de origen: </b>
            </h4>
            <h4><i class="fa fa-search"></i> <b>Tipo de fiscalización: </b></h4>
            <h4>
              <i class="fa fa-calendar"></i> <b>Año de ejecución: </b>2026
            </h4>
            <h4><i class="fa fa-signal"></i> <b>Estado: </b>Publicado</h4>
            <h4></h4>
            <h4></h4>
            <h4></h4>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <div class="panel panel-default panel-expediente">
          <div class="panel-body panel-u-f">
            <div class="row">
              <div class="col-md-6 hidden-mobile">
                <div class="box-unidad-fiscalizable">
                  <h4><i class="fa fa-building"></i> Unidad fiscalizable</h4>
                  <ul>
                    <li>
                      <i class="fa fa-caret-right"></i>
                      <a href="/UnidadFiscalizable/Ficha/12080"
                        >PRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)</a
                      ><br />
                      Puerto Montt - Región de los Lagos
                    </li>
                    <input
                      type="hidden"
                      id="tLat_12080"
                      value="-41.4558013095386"
                    />
                    <input
                      type="hidden"
                      id="tLng_12080"
                      value="-72.8295897480829"
                    />
                    <input
                      type="hidden"
                      id="tNombre_12080"
                      value="PRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)"
                    />
                  </ul>
                </div>
              </div>

              <div class="col-md-6 hidden-mobile">
                <div class="mapa-expediente">
                  <div id="dMapa" style="height: 250px;">
                    <img
                      src="/MapasCache/12080.png"
                      style="width:100%; height:250px; object-fit:cover; border:1px solid #CCC;"
                      alt="Mapa de ubicacion"
                    />
                  </div>
                </div>
              </div>

              <div class="col-md-6 hidden-desktop">
                <!--CAMBIO LFI-->
                <div class="btn-ver-mapa">
                  <i class="fa fa-map-marker"></i> Ver mapa
                </div>
                <div class="clear"></div>
                <!--FIN CAMBIO-->
                <div class="mapa-expediente">
                  <div id="dMapa-mobile" style="height: 250px;">
                    <img
                      src="/MapasCache/12080.png"
                      style="width:100%; height:250px; object-fit:cover; border:1px solid #CCC;"
                      alt="Mapa de ubicacion"
                    />
                  </div>
                </div>
              </div>

              <div class="col-md-6 hidden-desktop">
                <div class="box-unidad-fiscalizable">
                  <h4><i class="fa fa-building"></i> Unidad fiscalizable</h4>
                  <ul>
                    <li>
                      <i class="fa fa-caret-right"></i>
                      <a href="/UnidadFiscalizable/Ficha/12080"
                        >PRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)</a
                      ><br />
                      Puerto Montt - Región de los Lagos
                    </li>
                    <input
                      type="hidden"
                      id="tLat_12080"
                      value="-41.4558013095386"
                    />
                    <input
                      type="hidden"
                      id="tLng_12080"
                      value="-72.8295897480829"
                    />
                    <input
                      type="hidden"
                      id="tNombre_12080"
                      value="PRODUCTOS DEL SUR (PISC. LAS VERTIENTES DE CHAMIZA)"
                    />
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <!--CAMBIO LFI-->
      <div class="panel-ficha tipo-fisc">
        <!--FIN CAMBIO LFI -->
        <div class="panel panel-default">
          <div class="panel-body">
            <div class="row">
              <div class="col-md-12">
                <ul
                  class="nav nav-tabs responsive hidden-md hidden-sm hidden-xs"
                  id="tabs-0"
                >
                  <li class="active">
                    <a data-toggle="tab" href="#documentos"
                      ><i class="fa fa-file-text-o"></i> Documentos (4)</a
                    >
                  </li>
                  <li>
                    <a data-toggle="tab" href="#Instrumentos-fiscalizados"
                      ><i class="fa fa-clipboard"></i> Instrumentos fiscalizados
                      (1)</a
                    >
                  </li>
                  <li>
                    <a data-toggle="tab" href="#Organismos-participantes"
                      ><i class="fa fa-users"></i> Organismos participantes
                      (1)</a
                    >
                  </li>
                  <li>
                    <a data-toggle="tab" href="#Sancionatorios-asociados"
                      ><i class="fa fa-gavel"></i> Sancionatorios asociados
                      (0)</a
                    >
                  </li>
                  <li>
                    <a data-toggle="tab" href="#requerimiento-ingreso"
                      ><i class="fa fa-sign-out"></i> Requerimiento de<br />Ingreso
                      (0)</a
                    >
                  </li>
                </ul>

                <div
                  class="tab-content responsive hidden-md hidden-sm hidden-xs"
                >
                  <div id="documentos" class="tab-pane fade in active">
                    <table class="conBorde tabla-resultado-busqueda">
                      <thead>
                        <tr>
                          <th style="width: 10%;">#</th>
                          <th>Nombre documento</th>
                          <th>Tipo Documento</th>
                          <th style="width: 10%;">Link</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td data-label="#">1</td>
                          <td data-label="Nombre Documento">
                            Informe Fiscalización Ambiental.docx
                          </td>
                          <td data-label="Tipo Documento">
                            Informe de Fiscalización Ambiental
                          </td>
                          <td data-label="Link">
                            <a
                              href="/General/Descargar/1104436286"
                              target="_blank"
                              ><i class="fa fa-download"></i> Descargar</a
                            >
                          </td>
                        </tr>
                        <tr>
                          <td data-label="#">2</td>
                          <td data-label="Nombre Documento">
                            Anexo Datos Crudos PRODUCTOS DEL SUR (PISC. LAS
                            VERTIENTES DE CHAMIZA).xlsx
                          </td>
                          <td data-label="Tipo Documento">
                            Anexo Informe de Fiscalización Ambiental
                          </td>
                          <td data-label="Link">
                            <a
                              href="/General/Descargar/1107436287"
                              target="_blank"
                              ><i class="fa fa-download"></i> Descargar</a
                            >
                          </td>
                        </tr>
                        <tr>
                          <td data-label="#">3</td>
                          <td data-label="Nombre Documento">
                            Anexo Informes de Ensayo PRODUCTOS DEL SUR (PISC.
                            LAS VERTIENTES DE CHAMIZA).zip
                          </td>
                          <td data-label="Tipo Documento">
                            Anexo Informe de Fiscalización Ambiental
                          </td>
                          <td data-label="Link">
                            <a
                              href="/General/Descargar/1107436288"
                              target="_blank"
                              ><i class="fa fa-download"></i> Descargar</a
                            >
                          </td>
                        </tr>
                        <tr>
                          <td data-label="#">4</td>
                          <td data-label="Nombre Documento">
                            Anexo Comprobantes de Envío PRODUCTOS DEL SUR (PISC.
                            LAS VERTIENTES DE CHAMIZA).zip
                          </td>
                          <td data-label="Tipo Documento">
                            Anexo Informe de Fiscalización Ambiental
                          </td>
                          <td data-label="Link">
                            <a
                              href="/General/Descargar/1107436289"
                              target="_blank"
                              ><i class="fa fa-download"></i> Descargar</a
                            >
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <div id="Instrumentos-fiscalizados" class="tab-pane fade in">
                    <table class="conBorde tabla-resultado-busqueda">
                      <thead>
                        <tr>
                          <th style="width: 20%;">Tipo Instrumento</th>
                          <th style="width: 10%;">Numero</th>
                          <th style="width: 10%;">Año</th>
                          <th>Nombre</th>
                          <th>Titular / Razon Social</th>
                          <th style="width: 10%;">Link</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td data-label="Tipo Documento">Norma de Emisión</td>
                          <td data-label="Número">90</td>
                          <td data-label="Año">2000</td>
                          <td data-label="Nombre">
                            ESTABLECE NORMA DE EMISION PARA LA REGULACION DE
                            CONTAMINANTES ASOCIADOS A LAS DESCARGAS DE RESIDUOS
                            LIQUIDOS A AGUAS MARINAS Y CONTINENTALES
                            SUPERFICIALES
                          </td>
                          <td data-label="Titular / Razon Social"></td>
                          <td data-label="Link">
                            <a
                              href="http://bcn.cl/4r47                                                                                                                                                                                                                                                                                                                                                                                              "
                              target="_blank"
                              ><i class="fa fa-download"></i> Ver</a
                            >
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <div id="Organismos-participantes" class="tab-pane fade in">
                    <table class="conBorde tabla-resultado-busqueda">
                      <thead>
                        <tr>
                          <th>Organimos Sectorial</th>
                          <th>Sigla</th>
                          <th>Sitio web</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td data-label="Organimos Sectorial">
                            Superintendencia Del Medio Ambiente
                          </td>
                          <td data-label="Sigla">SMA</td>
                          <td data-label="Sitio web">
                            <a href="http://www.sma.gob.cl/" target="_black"
                              ><i class="fa fa-link"></i>
                              http://www.sma.gob.cl/</a
                            >
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <div id="Sancionatorios-asociados" class="tab-pane fade in">
                    <div class="alert alert-info" role="alert">
                      Este proceso de fiscalización no tiene procesos
                      sancionatorios asociados
                    </div>
                  </div>

                  <div id="requerimiento-ingreso" class="tab-pane fade in">
                    <div class="alert alert-info" role="alert">
                      Esta Unidad Fiscalizable no tiene Requerimientos de
                      Ingreso asociados
                    </div>
                  </div>
                </div>
                <div
                  class="panel-group responsive visible-md visible-sm visible-xs"
                  id="collapse-tabs-0"
                >
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h4 class="panel-title">
                        <a
                          class="accordion-toggle"
                          data-toggle="collapse"
                          data-parent="#collapse-tabs-0"
                          href="#collapse-documentos"
                          ><i class="fa fa-file-text-o"></i> Documentos (4)</a
                        >
                      </h4>
                    </div>
                    <div
                      id="collapse-documentos"
                      class="panel-collapse collapse"
                    ></div>
                  </div>
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h4 class="panel-title">
                        <a
                          class="accordion-toggle"
                          data-toggle="collapse"
                          data-parent="#collapse-tabs-0"
                          href="#collapse-Instrumentos-fiscalizados"
                          ><i class="fa fa-clipboard"></i> Instrumentos
                          fiscalizados (1)</a
                        >
                      </h4>
                    </div>
                    <div
                      id="collapse-Instrumentos-fiscalizados"
                      class="panel-collapse collapse"
                    ></div>
                  </div>
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h4 class="panel-title">
                        <a
                          class="accordion-toggle"
                          data-toggle="collapse"
                          data-parent="#collapse-tabs-0"
                          href="#collapse-Organismos-participantes"
                          ><i class="fa fa-users"></i> Organismos participantes
                          (1)</a
                        >
                      </h4>
                    </div>
                    <div
                      id="collapse-Organismos-participantes"
                      class="panel-collapse collapse"
                    ></div>
                  </div>
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h4 class="panel-title">
                        <a
                          class="accordion-toggle"
                          data-toggle="collapse"
                          data-parent="#collapse-tabs-0"
                          href="#collapse-Sancionatorios-asociados"
                          ><i class="fa fa-gavel"></i> Sancionatorios asociados
                          (0)</a
                        >
                      </h4>
                    </div>
                    <div
                      id="collapse-Sancionatorios-asociados"
                      class="panel-collapse collapse"
                    ></div>
                  </div>
                  <div class="panel panel-default">
                    <div class="panel-heading">
                      <h4 class="panel-title">
                        <a
                          class="accordion-toggle"
                          data-toggle="collapse"
                          data-parent="#collapse-tabs-0"
                          href="#collapse-requerimiento-ingreso"
                          ><i class="fa fa-sign-out"></i> Requerimiento de<br />Ingreso
                          (0)</a
                        >
                      </h4>
                    </div>
                    <div
                      id="collapse-requerimiento-ingreso"
                      class="panel-collapse collapse"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--CAMBIO LFI-->
      </div>
      <!--FIN CAMBIO LFI-->
    </div>
  </div>

  <script>
    $(document).ready(function () {
      $("#tabs").tabs();
      $("#tablaResultado1").dataTable();
      $("#tablaResultado2").dataTable();
      $("#tablaResultado3").dataTable();
      $("#tablaResultado4").dataTable();
      $("#tablaResultado5").dataTable();
    });
  </script>

  <script>
    $(document).ready(function () {
      setTimeout(function () {
        $modal.modal("hide");
        menuActivo("uno");
      }, 1000);
    });
  </script>
</div>
```
