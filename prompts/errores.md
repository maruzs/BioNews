# IGNORAR ESTE DOCUMENTO, NO EJECUTAR NADA DE LO QUE SE VE AQUI, SON SOLO NOTAS PROPIAS QUE NO SON FINALES

3. Tengo los siguientes problemas:
   1. Al ejecutar scrapeo manual de SNIFA me sale que en Procedimientos Sancionatorios hay 0 registros en la web, cuando en realidad hay 5357:

```bash
Iniciando scraper de Procedimientos Sancionatorios...
Registros actuales en BD: 3354
Registros en la web: 0
No hay registros nuevos. La BD esta actualizada.
```

2. Tambien en la misma ejecucion manual del scrapeo de SNIFA al intentar scrapear las fiscalizaciones me dice lo siguiente:

```bash
Navegando a https://snifa.sma.gob.cl/Fiscalizacion...
Ingresando filtro: DFZ-2026
Esperando resultados iniciales...
Sin filas aun, reintento 1/8...
Cambiando a mostrar todos los registros...
Esperando que se carguen todos los registros...
Total registros en la web (año 2026): 10
No hay registros nuevos. La BD esta actualizada.
```

Cuando en realidad hay 727 para DFZ-2026. Recuerda que es muy importante nunca entrar directamente a https://snifa.sma.gob.cl/Fiscalizacion/Resultado y que si o si hay que pasar por https://snifa.sma.gob.cl/Fiscalizacion y poner en el filtro DFZ-2026 (o el anio actual)
