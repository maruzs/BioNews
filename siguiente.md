## Mejoras mas avanzadas

Implementar/mejorar dashboards con cartas (usar ecosinfoambiental como base)

Revisiones de seguridad -> Rate limiting

Autorizacion por correo electrónico

Revisar logs de horarios de ejecucion

## Correcciones y mejoras basicas

Los tribunales aparecen cosas que se extrajeron ayer como si hubiera sido hoy y las marca como nuevas. Por ejemplo ayer se descargaron R-159-2026, E-1-2026 y E-136-2026 y tienen fecha scraping 2026-05-07 17:57 y las vi ayer, pero hoy me aparecen como nuevas, creo que debe ser un problema del scraper, pero ahi revisa

## Mejoras SNIFA

## Tipo de documento

En fiscalizaciones quiero que haya un filtro (en desplegar filtro) para el tipo de documento. Eso lo puedes ver en el formato del expediente:
Formato expediente:
DFZ-ANO-NUMERO-REGION-TIPO (A veces despues de tipo hay TIPO FISCALIZACION y pueden ser -IA o -EI o no tener nada pero eso no lo tomamos en cuenta por ahora) y esto es lo que puede ser:

- DFZ -> Valor general, se repite para todas las fiscalizaciones
- ANO -> Ano en que se creo el expediente
  NUMERO -> Numero del expediente
  REGION -> Numero de la region (I a XIV)
  TIPO -> Tipo de documento:

* RCA (Resolucion de Clasificacion Ambiental)
* PC (Programa de Cumplimiento)
* PPDA (Plan de Prevención y Descontaminación Ambiental)
* NE (Norma de Emisión)
* LEY (Ley Ambiental)

* MP (Medidas Provisionales)
* NC (Norma de Calidad)
* SRCA (Sistema de Resoluciones de Clasificacion Ambiental)

Si hay algo despues de TIPO es el TIPO FISCALIZACION

- IA -> Inspeccion Ambiental
- EI -> Examen de Informacion

Reporte de bugs debe permitir pegar imagenes del clipboard para las capturas de pantalla, no solo mediante la seleccion de archivos

Ademas desde el panel de administrador no puedo ver las imagenes que se subieron
