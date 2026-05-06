Eres un experto en FastAPI (Python), SQLAlchemy, React con TypeScript y WebSockets. Debes corregir el sistema de notificaciones y etiquetas "Nuevo" del proyecto BioNews según las siguientes reglas exactas (basadas en notas.md y proyecto.md).

### Tecnologías reales del proyecto

- Backend: Python 3.12, FastAPI, SQLite con SQLAlchemy, WebSockets (starlette o fastapi-websockets).
- Frontend: React 18, TypeScript, Vite, Material UI, Context API (AuthContext).
- Scrapers: Playwright, BeautifulSoup, scheduler en scheduler.py.
- Archivos clave:
  - `server.py` (API principal)
  - `web/src/components/Sidebar.tsx`
  - `web/src/components/NewsPage.tsx` (y similares para normativas, etc.)
  - `web/src/context/AuthContext.tsx`
  - `src/database/manager.py` (CRUD)

### Estado actual (BUGS según notas.md)

1. Al entrar a una categoría, el punto rojo desaparece (bien), pero los distintivos "Nuevo" en las filas NO aparecen la primera vez, sí la segunda.
2. Los distintivos verdes no desaparecen después de ver la categoría completa (o al salir).
3. Al cerrar sesión y volver a entrar en el mismo dispositivo, el punto rojo ya no aparece (bien), pero el "Nuevo" sigue ahí (mal).
4. No es cross-device: lo visto en un dispositivo no se refleja en otro.
5. No hay actualización en tiempo real al agregar nuevo contenido (aunque hay WebSockets, no están implementados para esto).

### Reglas de negocio CORREGIDAS (según nota adicional)

- **Punto rojo** → indica que hay al menos un ítem nuevo NO VISTO en esa categoría. Desaparece **inmediatamente al entrar a la categoría** (sin importar si ves los ítems).
- **Distintivo "Nuevo" en cada fila**:
  - Un ítem es "nuevo" si su `fecha_creacion` es **posterior** a la última vez que el usuario **salió** de esa categoría (columna `last_exit_at` en `user_category_views`), **Y** el usuario no ha marcado ese ítem individualmente como visto.
  - **Al hacer clic en "Leer más" / "Acción"** → desaparece el distintivo solo de ese ítem (se registra en `user_item_views`).
  - **Al salir de la categoría** (navegar a Home u otra sección) → **todos** los distintivos "Nuevo" de esa categoría deben desaparecer para futuras visitas (se actualiza `last_exit_at = ahora`).
- **Cross-device**: todas las marcas (`last_exit_at` y `user_item_views`) se guardan por usuario en la DB. Al iniciar sesión desde cualquier dispositivo, se consulta la DB y se muestran los puntos rojos y etiquetas "Nuevo" coherentes.
- **Tiempo real**: cuando un scraper inserta un nuevo ítem en cualquier tabla (noticias, normativas, etc.), el backend debe:
  - Emitir un evento WebSocket a todos los clientes conectados con `{categoria, item_id, fecha_creacion}`.
  - El frontend (React) debe actualizar el punto rojo de esa categoría en la sidebar (sin recargar).
  - Si el usuario está actualmente viendo esa categoría, debe agregar la fila en la tabla con la etiqueta "Nuevo" (sin recargar).

### Estructuras de datos necesarias (agregar sin migrar tablas existentes)

Crear dos nuevas tablas en SQLite (usando SQLAlchemy en `manager.py`) :
(Esto solo si es necesario y crees que realmente los necesitamos para que funcione como quiero)
**Tabla `user_category_views`**:

- id (Integer, primary key)
- user_id (Integer, ForeignKey a users.id)
- category_slug (String, ejemplo: "noticias", "normativas", "sma-fiscalizaciones", etc.)
- last_exit_at (DateTime, nullable) -- momento en que el usuario salió por última vez de esa categoría (inicialmente NULL = nunca ha salido, entonces todos los ítems existentes son nuevos)

**Tabla `user_item_views`**:

- id (Integer, primary key)
- user_id (Integer, ForeignKey a users.id)
- item_id (Integer) -- ID del ítem en su tabla específica (noticias.id, normativas.id, etc.)
- category_slug (String)
- viewed_at (DateTime)

Nota: No es necesario modificar las tablas existentes de contenido (noticias, normativas, etc.). Solo estas dos tablas de seguimiento.

### Cambios específicos en el código (backend)

1. **En `src/database/manager.py`**:
   - Agregar modelos `UserCategoryView` y `UserItemView`.
   - Función `get_or_create_category_view(user_id, category_slug)`.
   - Función `update_category_exit(user_id, category_slug)` (actualiza `last_exit_at` a now).
   - Función `mark_item_viewed(user_id, item_id, category_slug)`.
   - Función `get_items_with_new_flag(user_id, category_slug, items_list)` (recibe lista de ítems de la tabla correspondiente y agrega campo `is_new` según regla: `item.created_at > last_exit_at` (si last_exit_at no es NULL, si es NULL entonces es nuevo) y no existe en user_item_views).

2. **En `server.py` (endpoints FastAPI)**:
   - `POST /categoria/entrada` (recibe category_slug): NO actualiza last_exit_at (solo sirve para que frontend sepa que ya no mostrará punto rojo). En realidad, el punto rojo se calcula consultando los ítems nuevos según la última salida. Para quitar el punto rojo al entrar, basta con que el frontend lo oculte localmente; pero para cross-device, se debe recalcular al volver a entrar. Simplificamos: el punto rojo se calcula en base a `last_exit_at` y los items existentes. Al entrar a la categoría no se modifica la DB. En su lugar, el frontend esconde el punto rojo visualmente. La DB se actualiza **solo al salir** (`POST /categoria/salida`).
   - `POST /categoria/salida` → llama a `update_category_exit(user_id, category_slug)`.
   - `POST /item/visto` → llama a `mark_item_viewed`.
   - `GET /items/{categoria}` → devuelve los ítems de esa categoría con el flag `is_new` calculado.
   - `GET /estado-notificaciones` (para sidebar) → devuelve para cada categoría un booleano `has_new`: existe al menos un ítem con `created_at > last_exit_at` y no marcado individualmente.
   - WebSocket: ruta `/ws/notificaciones` que envía eventos cuando se inserta un nuevo ítem (desde los scrapers). Usar `manager.broadcast` o similar.

3. **Integración con scrapers**: En `startScraping.py` o en el scheduler, después de insertar un nuevo ítem en la DB, llamar a una función que emita el evento WebSocket (p.ej. `notify_new_item(category_slug, item_id)`).

### Cambios específicos en el frontend (React + TypeScript)

1. **Contexto de notificaciones** (nuevo o dentro de AuthContext):
   - Estado: `categoryNewStatus: Record<CategorySlug, boolean>` (puntos rojos).
   - WebSocket connection: se abre al login, se cierra al logout.
   - Listener: al recibir `nuevo_contenido`, actualiza `categoryNewStatus` y, si la página actual es esa categoría, dispara una recarga de datos o agrega la fila directamente.

2. **Sidebar.tsx**:
   - Lee `categoryNewStatus` del contexto y muestra punto rojo (badge) en cada elemento del menú.
   - Al hacer clic en una categoría, localmente oculta el punto rojo (pero no afecta a la DB hasta que se salga). Navega a la ruta correspondiente.

3. **NewsPage.tsx (y páginas similares)**:
   - Al cargar la página, obtiene los ítems con `is_new` desde API `/items/{categoria}`.
   - Renderiza cada fila; si `is_new === true`, muestra el distintivo verde (ej. Chip con texto "Nuevo").
   - Botón "Leer más" (o "Acción"): al hacer clic, además de abrir el detalle, llama a `POST /item/visto`. Luego actualiza el estado local para eliminar el distintivo solo de ese ítem.
   - Al salir de la página (unmount o navegación a otra ruta), debe llamar a `POST /categoria/salida` **una sola vez** (evitar múltiples llamadas). Usar `useEffect` con cleanup o un listener del router.

4. **Tiempo real**:
   - Si el usuario está en una categoría y llega un evento `nuevo_contenido` de esa misma categoría:
     - Agregar el nuevo ítem a la tabla (puede ser pidiendo solo ese ítem a la API o insertando localmente con flag `is_new: true`).
     - Asegurar que el punto rojo en sidebar ya no se muestre (porque ya está en la categoría, pero el punto rojo debería reaparecer si el usuario sale sin haber visto ese ítem? Según regla: el punto rojo se quita al entrar a la categoría, pero al recibir un nuevo ítem mientras estás dentro, el punto rojo no debe aparecer porque ya estás viendo la categoría. Sin embargo, si el usuario sale y vuelve a entrar sin haber visto ese nuevo ítem, entonces el punto rojo debería estar. Esto se maneja porque la última salida aún no ha ocurrido. Al salir, se actualizará `last_exit_at` y entonces el punto rojo ya no aparecerá. Para que el punto rojo aparezca solo si no se ha visto, necesitamos que el punto rojo se calcule dinámicamente. Simplificamos: **el punto rojo se recalcula cada vez que se carga la sidebar** (al login y después de cada evento de nuevo contenido). La regla: un punto rojo está activo si existe al menos un ítem con `created_at > last_exit_at` y no marcado individualmente. Al recibir un nuevo ítem mientras estás dentro, el punto rojo debería activarse en la sidebar solo después de que salgas y vuelvas a entrar. Para evitar confusión, puedes decidir no mostrar punto rojo si el usuario ya está en esa categoría (es una mejora de UX). Pero según requisito original, "cada vez que haya una nueva noticia debería aparecer un punto rojo sin necesidad de reiniciar página". Eso implica que aunque estés dentro, el punto rojo debería aparecer en la sidebar (aunque ya estés viendo la tabla). Lo dejo a tu criterio; yo recomiendo que sí aparezca, pero no interfiera. Se puede implementar.

### Corrección de los bugs específicos

- Bug 1 (primera vez no aparece "Nuevo"): causado por no calcular `is_new` correctamente al entrar. Se arregla usando `last_exit_at` (no `last_visit_at`). Asegurar que `last_exit_at` se actualiza solo al salir, no al entrar.
- Bug 2 (distintivo no desaparece al ver categoría completa): se arregla con la regla "al salir se borran todos" (actualizando `last_exit_at`).
- Bug 3 (después de cerrar sesión sigue "Nuevo"): porque se usaba estado local en lugar de DB. Ahora todo se basa en DB.
- Bug 4 (no cross-device): usar las tablas nuevas.
- Bug 5 (sin tiempo real): implementar WebSocket.

### Entregables que debe producir la IA (para que integres en tu código)

1. **Código de los modelos SQLAlchemy** (para `manager.py`).
2. **Funciones de gestión** (marcar salida, marcar ítem visto, consultar con flag `is_new`).
3. **Endpoints FastAPI** modificados/nuevos.
4. **Integración WebSocket**: lógica de broadcast desde scrapers y cliente React.
5. **Frontend**: contexto de notificaciones, `Sidebar` modificada, `NewsPage` con manejo de `is_new` y llamadas a salida de categoría.
6. **Pruebas a realizar** (lista de pasos para verificar cada escenario descrito en notas.md).

### Escenario final de validación

- Usuario A ve punto rojo en Noticias y Normativas.
- Entra a Noticias → punto rojo desaparece (localmente). Ve etiquetas "Nuevo" en las noticias nuevas.
- Hace clic en "Leer más" de una noticia → esa noticia pierde su etiqueta "Nuevo" (las demás siguen).
- Vuelve a Home → se ejecuta `POST /categoria/salida` para Noticias. Ahora todas las noticias pierden la etiqueta "Nuevo" (en futura visita).
- Entra a Normativas (sin haber salido de sesión) → ve etiquetas "Nuevo" en normativas nuevas.
- Cierra sesión y abre en otro navegador → No hay puntos rojos ni etiquetas "Nuevo" para Noticias (porque ya salió), pero sí para Normativas (porque aún no ha salido de Normativas).
- Admin (scraper) agrega una nueva normativa → ambos navegadores (con sesión activa) ven punto rojo en Normativas, y si están dentro de Normativas, ven la nueva fila con etiqueta "Nuevo".
