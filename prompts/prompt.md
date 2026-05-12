## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

### MEJORAS Y CAMBIOS

Lo mismo que hiciste para el SEA hazlo ahora para las normativas del diario oficial, pero la verdad me interesa solo el nuevo boton con filtro por fecha en el panel de administrador.

Boton para cambiar vista entre tabla y tarjeta (Para todas las Categorias menos 'Noticias')

## CORRECCION DE ERRORES:

### SEA - PROYECTOS EVALUADOS

Al intentar scrapear los proyectos evaluados del sea ya sea con el rango por fecha, el general o el de scheduler me da este error (La parte de las pertinencias esta bien):

```bash
Iniciando scraping SEA Proyectos Evaluados. Modo diario.
Error parseando JSON en offset 0: Expecting value: line 1 column 1 (char 0)
Contenido: En este momento no es posible realizar la operación solicitada. Regrese a la página anterior e intente nuevamente.
Scraping SEA Proyectos finalizado. Nuevos: 0
```
