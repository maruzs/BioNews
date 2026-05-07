# Plan de Implementación - BioNews Fixes

## Tareas identificadas del prompt.md

### 1. ✅ Integrar `scraper_dga.py` como scraper de noticias

- Agregar DGA al listado de scrapers de noticias en `server.py` y `startScraping.py`
- Agregar checkbox DGA en el panel de admin (ya usa el mismo flujo)

### 2. ✅ Exceso de notificaciones en terminal (Polling)

- **Causa raíz**: `NotificationsContext.tsx` hace polling cada 15 segundos a `/api/config/notifications` + `/api/notifications/status`
- **Solución**: Eliminar el polling periódico. Usar solo `refreshStatus()` bajo demanda:
  - Al cargar la app (login/refresh)
  - Después de un `markExit` o `markItemViewed` (ya actualiza estado local)
  - Cuando un WebSocket notifique nuevo contenido

### 3. ✅ Notificaciones "vuelven" después de marcar como leído

- **Causa raíz**: `save_news` usa `ON CONFLICT DO UPDATE SET fecha_scraping=datetime.now()`. Esto actualiza `fecha_scraping` para noticias que YA existían, lo que hace que parezcan "nuevas" comparado con `last_exit_at`.
- **Solución**: Cambiar `save_news` para que solo inserte noticias nuevas (INSERT OR IGNORE) y NO actualice `fecha_scraping` de las existentes.

### 4. ✅ Descarga repetida de normativas

- **Causa raíz**: `diario_oficial.py` usa `INSERT INTO` sin verificar duplicados (no tiene PK en la tabla).
- **Solución**:
  - Usar `accion` (URL) como identificador único: agregar `UNIQUE(accion)` y usar `INSERT OR IGNORE`
  - Limpiar duplicados existentes en la BD

### 5. ✅ Barra de búsqueda por palabra clave

- **Solución**: Búsqueda al presionar Enter + botón de buscar (opción 2, más óptima)

### 6. ✅ Fecha scraping sin microsegundos

- Asignar `2026-05-04 23:59:59` a registros sin `fecha_scraping`
- Eliminar microsegundos de fechas existentes
- Usar `strftime` para nuevas fechas

### 7. ✅ Corrección scrapers de noticias (fecha_scraping se actualiza para registros existentes)

- Misma causa raíz que #3, se resuelve junto

### 8. ✅ SMA/SNIFA - Ordenar por más nuevos primero

- Ordenar fiscalizaciones por `detalle_link` DESC (número de ficha más alto = más nuevo)
- Asegurar que el límite de 5000 trae las más nuevas primero

### 9. ✅ Filtro por año en fiscalizaciones

- Agregar filtro por año basado en el campo expediente
