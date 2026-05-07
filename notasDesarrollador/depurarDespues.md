He corregido los errores técnicos que mencionaste y he añadido herramientas de diagnóstico para resolver el problema de la etiqueta "Nuevo":

1. Solución al RuntimeWarning y 404
   AwaitFor asyncio.to_thread: He añadido el await faltante en el monitor del scheduler. Ahora la terminal no mostrará el error de "coroutine was never awaited" y el proceso de SNIFA se ejecutará correctamente en segundo plano.
   Eliminación del 404: He eliminado la llamada a /api/test/status desde el frontend (NotificationsContext.tsx). Como tú mismo comentaste ese endpoint en el backend, el frontend seguía intentando llamarlo cada pocos segundos. Ya no verás más errores 404 por esto.
   Limpieza de server.py: He restaurado el archivo server.py eliminando bloques de código duplicados o comentados para que sea más legible y estable.
2. Diagnóstico de la etiqueta "Nuevo"
   Aunque el "puntito rojo" funciona (lo que indica que la base de datos detecta novedades), la etiqueta dentro de la tabla no aparece. Para entender por qué, he añadido logs de depuración profundos en manager.py.

Por favor, haz lo siguiente para ayudarnos a encontrar el fallo:

Entra en una categoría donde sepas que hay algo nuevo (ej. Pertinencias).
Mira la terminal donde corre el servidor (uvicorn). Verás líneas que dicen: DEBUG pertinencias: Item XXX, Date YYY > Exit ZZZ = True/False
Pégame aquí lo que dicen esas líneas. Eso nos dirá exactamente qué fechas está comparando el servidor y por qué decide poner False (o si pone True y el problema es del frontend). 3. Notas sobre los errores de Vite (ECONNREFUSED)
Esos errores en la consola de npm run dev ocurren simplemente porque el servidor de Python se estaba reiniciando (debido a mis cambios o a los tuyos). Una vez que el backend está arriba, esos mensajes deberían cesar.

He actualizado los archivos:

- server.py: Corrección de await, limpieza y logs de salida.
- NotificationsContext.tsx: Eliminación de la llamada al endpoint inexistente.
- manager.py: Logs de depuración para las etiquetas "Nuevo".
  ¿Qué dicen los logs de DEBUG en la terminal ahora?
