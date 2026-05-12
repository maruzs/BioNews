## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

### MEJORAS Y CAMBIOS

Boton para cambiar vista entre tabla y tarjeta (Para todas las Categorias menos 'Noticias')

Las barras del dashboard hay que corregirlas, deberia ser en base al total de registros pero se muestra una barra muy larga hasta el final, como si fuera un 100% o mas

Por ejemplo pero ocurre en general para categoria economica, por region, por tipo, etc.

En el dashboard de las normativas, en 'Normativas por tipo' y Normativas por 'Organismo' la barra se llena hasta el final, como si fuera 100%, cuando en realidad deberia mostrar el porcentaje real de registros que hay en cada categoria, region, tipo, etc. basado en el total. por ejemplo:

En normativas por tipo tenemos que hay un total de 432 normativas, las cuales 177 son Normas Generales, 132 son Normas particulares y 123 son del Boletin Oficial Mineria, sin embargo la barra de Normas Generales se muestra hasta el final, cuando en realidad deberia ser 41.0% del total de normativas, se entiende mas o menos la idea? Esto ocurre para las siguientes tarjetas de los dashboards:

Normativas: - Normativas por tipo - Normativas por Organismo - Distribucion por region

SEA - Pertinencias: - Pertinencias por Tipo - Categoria Economica

SEA - Proyectos Evaluados: - Razon de Ingreso - Categoria Economica - Proyectos por Region

SMA - Fiscalizaciones: - Categoria Economica - Registros por Region

SMA - Sancionatorios: - Categoria Economica - Registros por Region

SMA - Sanciones: - Categoria Economica - Registros por Region

SMA - Programas de cumplimiento (Programas): - Categoria Economica - Registros por Region

SMA - Medidas Provisionales (Medidas): - Categoria Economica - Registros por Region

SMA - Requerimientos de ingreso SEIA(Requerimientos): - Categoria Economica - Registros por Region

Tribunales Ambientles - Resoluciones: - Causas por Tribunal - Tipo de Procedimiento (Este grafico es distinto al resto, haz que sea el mismo tipo pero para los Tipos de Procedimientos)

Ademas otra cosa, aunque por paginacion solo permitamos que se muestren 5000 registros maximos por categoria, el dashboard debe estar basado en el total de registros, no en los registros que se muestran por paginacion, se entiende la diferencia?
De hecho esto se nota principalmente en lo que es SEA - Pertinencias, ya que son mas de 25000 registros en total y obviamente en el dashboard todo se esta haciendo bajo el maximo de 25k
