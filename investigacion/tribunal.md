# LINK
https://2ta.lexsoft.cl/2ta/search?proc=4
# ANALISIS
Dinamica
Informacion que nos interesa
Rol,link detalle, fecha Ingreso, Caratula, Etapa
Comparar con ultima tabla obtenida, si cambio algo (nuevo rol, cambio de etapa en rol previo, etc) se actualiza, si no se mantiene lo que habia
# PAGINA
## TABLE HEAD
```html
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
```
## TABLE BODY EXAMPLE
```html
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
```
## JSON FOR HREF
https://2ta.lexsoft.cl/2ta/rest/causa/searchPaginado/10/1
```json
"results": [
    {
      "id": 400705,
      "idOrdenTrabajo": 400705,
      "folio": 628,
      "anio": 2026,
      "era": 2026,
      "iniciales": "R",
      "customFormData": "{}",
      "descripcion": "Pastene Solís Juan Gilberto / Servicio de Evaluación Ambiental (Res. Ex. N° 202699101251, de fecha 6 de marzo de 2026)",
      "fechaIngreso": 1775846023013,
      "horaIngreso": "14:33:43",
      "cuadernos": [
        {
          "id": 400744,
          "descripcion": "Cuaderno principal",
          "idCausa": 400705,
          "fechaIngreso": 1775846023019,
          "etapa": {
            "id": 61,
            "name": "En espera del informe",
            "data": null
          },
          "tipoCuaderno": {
            "id": 20,
            "name": "Principal",
            "data": null
          },
          "habilitado": true,
          "tramites": [],
          "correlativo": null,
          "calidad": null,
          "estadoProcesal": {
            "id": 6,
            "name": "Admisibilidad",
            "data": null
          }
        }
      ],
      "escritos": [],
      "materias": [
        {
          "id": 19,
          "name": "Resoluciones De Calificación Ambiental (servicio De Evaluación Ambiental)",
          "data": null,
          "formulario": null,
          "tipoDocumento": null,
          "habilitada": true,
          "cobroMateria": null,
          "extendible": null,
          "finiquito": false,
          "cantCompareciente": 1,
          "distribucion": null
        }
      ],
      "notificacionesEmail": [
        {
          "id": 559664,
          "fromEmail": "notificaciones.2ta@kpitec.com",
          "toEmail": "mdaza@hdfo.cl",
          "ccEmail": "",
          "ccoEmail": "",
          "body": "",
          "title": "Notificación causa rol R-628-2026",
          "idCausa": 400705,
          "causa": {
            "id": 400705,
            "idOrdenTrabajo": 400705,
            "folio": 628,
            "anio": 2026,
            "era": 2026,
            "iniciales": "R",
            "customFormData": "{}",
            "descripcion": "Pastene Solís Juan Gilberto / Servicio de Evaluación Ambiental (Res. Ex. N° 202699101251, de fecha 6 de marzo de 2026)",
            "fechaIngreso": 1775846023013,
            "horaIngreso": "14:33:43",
            "cuadernos": [
              {
                "id": 400744,
                "descripcion": "Cuaderno principal",
                "idCausa": 400705,
                "fechaIngreso": 1775846023019,
                "etapa": {
                  "id": 61,
                  "name": "En espera del informe",
                  "data": null
                },
                "tipoCuaderno": {
                  "id": 20,
                  "name": "Principal",
                  "data": null
                },
                "habilitado": true,
                "tramites": [],
                "correlativo": null,
                "calidad": null,
                "estadoProcesal": {
                  "id": 6,
                  "name": "Admisibilidad",
                  "data": null
                }
              }
            ],
            "escritos": [],
            "materias": [
              {
                "id": 19,
                "name": "Resoluciones De Calificación Ambiental (servicio De Evaluación Ambiental)",
                "data": null,
                "formulario": null,
                "tipoDocumento": null,
                "habilitada": true,
                "cobroMateria": null,
                "extendible": null,
                "finiquito": false,
                "cantCompareciente": 1,
                "distribucion": null
              }
            ],
            "notificacionesEmail": [],
            "parte": null,
            "procedimiento": {
              "id": 4,
              "name": "Reclamación",
              "iniciales": "R",
              "habilitado": true,
              "materias": null
            },
            "formaInicio": {
              "id": 5,
              "name": "Reclamación",
              "data": null
            },
            "tramites": 0,
            "sectorEconomicos": null,
            "sectorEconomico": {
              "id": 1298,
              "habilitado": true,
              "name": "Otros"
            },
            "ministros": [],
            "relator": {
              "id": 400388,
              "name": "Alejandro Jara Straussmann",
              "data": null
            },
            "economista": null,
            "rol": "R-628-2026",
            "nombreFuncionario": "Mauricio Daza Carrasco",
            "urlExpediente": "",
            "resumen": "-",
            "multaValor": null,
            "tipoMoneda": null,
            "montoParte": null,
            "fechaArchivada": null,
            "fechaAcuerdo": null,
            "fechaSentencia": null,
            "fechaVista": null,
            "fechaVistaTemp": null,
            "complejidad": {
              "id": 0,
              "name": "Simple",
              "data": null
            },
            "habilitadoTramitacion": false,
            "caratula": {
              "id": 437906,
              "path": "/CARATULA/400705/4b7f49be-dc65-41c9-a8fd-0b0dd718d7fd/c9b9cd8f-45d7-4c4e-b5ab-76bc8764e8cb.doc",
              "nombre": "caratula_R-628-2026.doc",
              "contentType": "application/msword",
              "descripcion": "Carátula",
              "fojaInicio": null,
              "fojaTermino": null,
              "enviado": true,
              "validado": true,
              "reemplazable": true,
              "tipoArchivo": {
                "id": 1,
                "name": "Borrador",
                "data": null
              },
              "idOT": null,
              "idProtocolizado": null,
              "idEscrito": null,
              "idTramite": null,
              "idCuaderno": null,
              "paraFirmar": true,
              "firmado": true,
              "docPrincipalEscrito": null,
              "fojaTramite": null,
              "fojaEscrito": null,
              "size": null,
              "publico": null,
              "reservado": true,
              "pathFirmado": null,
              "estadoValidaDocumento": null,
              "esCuadernoDocs": null,
              "referenciaEscrito": null,
              "pronunciado": null,
              "rol": "628-2026"
            }
          },
          "idTramite": 416749,
          "tramite": {
            "id": null,
            "fechaIngreso": 1776178544221,
            "fechaBloqueo": 1776157200000,
            "referencia": null,
            "etapa": null,
            "estado": null,
            "tipoTramite": null,
            "idCuaderno": null,
            "idCausa": null,
            "ibFEA": null,
            "persona": null,
            "funcionario": null,
            "documento": null,
            "nombrePlantilla": null,
            "escritos": [],
            "hitos": [],
            "firmantes": [],
            "ministroRedacta": null,
            "detalleMinistroRedacta": null,
            "notificacionesEmail": [],
            "deParte": null,
            "reservada": null,
            "estadoDiario": null,
            "publico": null,
            "idEstadoD": null,
            "desbloqueable": null,
            "rol": null,
            "caratula": null,
            "estadoProcesal": null,
            "estadoAdministrativo": null,
            "urlDocumento": null,
            "foja": null,
            "historiaEscritos": [],
            "tieneDocumentos": null,
            "idPresidente": null,
            "ultimaBitacora": null,
            "esSesion": null,
            "rolConInicial": null,
            "idSolicitudCA": null,
            "idSolicitudCS": null,
            "checkReservada": null,
            "rolPlantilla": null
          },
          "idCompareciente": 406131,
          "compareciente": {
            "id": 406131,
            "persona": {
              "nombres": "Mauricio",
              "apellidoPaterno": "Daza",
              "apellidoMaterno": "Carrasco",
              "rut": 12263544,
              "dv": "9",
              "juridica": false,
              "direccion": "Miraflores",
              "direccionNumero": "178",
              "numeroDeptoOficina": "piso 22",
              "codigoPostal": "8320000",
              "telefono": "56994418194",
              "fax": "",
              "profesion": "",
              "email": "mdaza@hdfo.cl",
              "emailNotificacion": "mauriciodazac@gmail.com",
              "otrosDatos": "",
              "id": 401560,
              "comuna": "Santiago",
              "exentoImpuestoPagare": true,
              "habilitada": true,
              "pais": {
                "id": 45,
                "codigo": "CHI",
                "nombre": "Chile"
              },
              "paisOrigen": {
                "id": 45,
                "codigo": "CHI",
                "nombre": "Chile"
              },
              "estadoCivil": null,
              "clienteRegistrado": false,
              "cliente": null,
              "filialDe": null,
              "tipoEmpresa": null,
              "giro": null,
              "pasaporte": null,
              "ciudad": "Santiago",
              "razonSocial": null,
              "abogados": null,
              "representantes": null,
              "sexo": null
            },
            "fechaFirma": null,
            "puedeFirmar": true,
            "tienePieFirma": true,
            "numeroRepresentantes": 0,
            "idOT": 400705,
            "observacion": null,
            "denunciado": null,
            "firmas": 0,
            "empresa": null,
            "otrosComparecientes": false,
            "ordenIngreso": null,
            "principal": false,
            "abogadoPartes": null,
            "selComunica": true,
            "emailNotificacion": "mdaza@hdfo.cl",
            "tipoCompareciente": {
              "id": 29,
              "nombre": "Abogado Reclamante",
              "habilitado": true,
              "principal": null
            }
          },
          "fallido": false,
          "enviada": true,
          "fechaEnvio": 1776283455471,
          "tipoNotificacionCompareciente": {
            "id": 0,
            "name": "Email",
            "data": null
          },
          "estadoNotificacionEmail": {
            "id": 2,
            "name": "Enviada",
            "data": null
          },
          "notificar": true
        }
      ],
      "parte": null,
      "procedimiento": {
        "id": 4,
        "name": "Reclamación",
        "iniciales": "R",
        "habilitado": true,
        "materias": null
      },
      "formaInicio": {
        "id": 5,
        "name": "Reclamación",
        "data": null
      },
      "tramites": 0,
      "sectorEconomicos": null,
      "sectorEconomico": {
        "id": 1298,
        "habilitado": true,
        "name": "Otros"
      },
      "ministros": [],
      "relator": {
        "id": 400388,
        "name": "Alejandro Jara Straussmann",
        "data": null
      },
      "economista": null,
      "rol": "R-628-2026",
      "nombreFuncionario": "Mauricio Daza Carrasco",
      "urlExpediente": "",
      "resumen": "-",
      "multaValor": null,
      "tipoMoneda": null,
      "montoParte": null,
      "fechaArchivada": null,
      "fechaAcuerdo": null,
      "fechaSentencia": null,
      "fechaVista": null,
      "fechaVistaTemp": null,
      "complejidad": {
        "id": 0,
        "name": "Simple",
        "data": null
      },
      "habilitadoTramitacion": false,
      "caratula": {
        "id": 437906,
        "path": "/CARATULA/400705/4b7f49be-dc65-41c9-a8fd-0b0dd718d7fd/c9b9cd8f-45d7-4c4e-b5ab-76bc8764e8cb.doc",
        "nombre": "caratula_R-628-2026.doc",
        "contentType": "application/msword",
        "descripcion": "Carátula",
        "fojaInicio": null,
        "fojaTermino": null,
        "enviado": true,
        "validado": true,
        "reemplazable": true,
        "tipoArchivo": {
          "id": 1,
          "name": "Borrador",
          "data": null
        },
        "idOT": null,
        "idProtocolizado": null,
        "idEscrito": null,
        "idTramite": null,
        "idCuaderno": null,
        "paraFirmar": true,
        "firmado": true,
        "docPrincipalEscrito": null,
        "fojaTramite": null,
        "fojaEscrito": null,
        "size": null,
        "publico": null,
        "reservado": true,
        "pathFirmado": null,
        "estadoValidaDocumento": null,
        "esCuadernoDocs": null,
        "referenciaEscrito": null,
        "pronunciado": null,
        "rol": "628-2026"
      }
    },
```
# EJEMPLO LINK A DETALLE 
https://2ta.lexsoft.cl/2ta/search?proc=3&idCausa=400705