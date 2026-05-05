# BUGS Y ERRORES IDENTIFICADOS (v2)

## Corregido

Casi todo lo que hiciste previamente esta bien:

- Pertinencias ahora si muestra las mas nuevas primero.
- Preferencias de normativas esta funcionando bien
- Preferencias de SMA (Categorias) esta funcionando bien

## Errores nuevos y cosas a corregir

### Noticias

Ahora todas las noticias del SBAP son del 2026-05-05

Del MMA solo aparece una noticia, que si bien es de hoy, no aparecen las de dias anteriores que igual deberian aparecer.
Ademas en la tabla noticias en la BD ahora todas las 189 noticias son del 2026-05-05 cuando en realidad no lo son, son de dias anteriores!

Probablemente tenga que limpiar la tabla de noticias y ejecutar los scrapers de noticias, pero deberia ser de manera que las fechas sean correctas (como estaba antes)
