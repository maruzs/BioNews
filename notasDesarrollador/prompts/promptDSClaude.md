Aquí tienes una versión mejorada y estructurada del prompt para Claude Opus, conservando toda la información original y organizándola para maximizar la claridad y la acción:

---

## Contexto general

Eres un asistente experto en desarrollo de software, especializado en Python, scraping, bases de datos SQL, APIs REST (FastAPI) y frontend (JavaScript/React o similar). Trabajarás sobre un sistema existente que gestiona scrapers de noticias, normativas, fiscalizaciones, etc., con un panel de administración, autenticación de usuarios, notificaciones en tiempo real y lógica de “visto/marcado como leído” cross-device.

A continuación se detallan tareas pendientes, errores identificados y requerimientos específicos. Debes implementar soluciones completas, eficientes y documentadas.

---

## 1. Nueva fuente de noticias: scraper DGA

**Requerimiento:**
Implementar `src/scrapers/scraper_dga.py` para que funcione igual que los demás scrapers de noticias:

- Debe insertar datos en la tabla `Noticias`.
- Debe ejecutarse junto con los otros scrapers de noticias (mismo scheduler).
- Debe aparecer en el panel de administración con su propio checkbox.
- Mismo formato de salida (título, fecha, imagen, fuente, link, fecha_scraping).

**Acción esperada:**
Escribir el scraper siguiendo la estructura y patrones de los scrapers existentes.

---

## 2. Problema de exceso de notificaciones y consultas a la API

**Observaciones:**

- Tanto en servidor (Docker logs) como en terminal local, se ven solicitudes repetitivas a:
  - `/api/config/notifications`
  - `/api/notifications/status`
- Ocurren cada pocos segundos, incluso sin actividad del usuario.
- El punto rojo de notificaciones y la etiqueta “Nuevo” reaparecen poco después de marcarlos como leídos o visitados.

**Comportamiento deseado:**

- El sistema **no debe** consultar estas APIs continuamente.
- Las notificaciones y etiquetas “Nuevo” deben actualizarse **solo cuando**:
  - Un scraper agrega contenido nuevo (entonces se marca como no leído para los usuarios).
  - El usuario interactúa con la interfaz (entra a una categoría, ve un elemento con “Ver más”, hace clic en “Marcar todo como leído”, cambia de categoría, recarga la página, etc.).
- La actualización debe reflejarse **cross-device** (misma sesión en diferentes dispositivos) de forma coherente, aunque no necesariamente en tiempo real.

**Nuevo diseño lógico sugerido:**

- Al agregar un nuevo registro (noticia, normativa, etc.) con fecha_scraping, se inserta también un registro en una tabla `usuario_contenido_visto` (o similar) que por defecto está como “no visto” para cada usuario.
- El frontend consulta el estado **solo al cargar la página o al cambiar de sección**, no en intervalos fijos.
- Al marcar como leído, se actualiza esa tabla y se re-renderiza la UI sin nuevas solicitudes automáticas.

**Acción esperada:**

1. Revisar el código actual que provoca las consultas repetitivas.
2. Eliminar o modificar los intervalos automáticos.
3. Implementar la lógica cross-device con actualizaciones bajo demanda.
4. Asegurar que el punto rojo y las etiquetas “Nuevo” desaparezcan correctamente después de la interacción del usuario.

---

## 3. Descarga repetida de normativas

**Problema:**

- En la BD hay registros duplicados de normativas (ej. 846 registros en lugar de ~70 únicos).
- Al ejecutar el scraper múltiples veces, se duplican todos los registros, no solo los nuevos.

**Causa probable:**
Falta de clave primaria única. La URL (`Accion`) es el único campo que diferencia normativas, incluso cuando el mismo contenido se publica en diferentes fechas.

**Formato de URL:**

```
https://www.diariooficial.interior.gob.cl/publicaciones/{año}/{mes}/{dia}/{numero_edicion}/{tipo_documento}/{numero_documento}.pdf
```

- `tipo_documento`: `01` (Normas Generales), `02` (Normas Particulares), `07` (Boletín Oficial Minería).
- `numero_documento` es único por normativa, incluso si el contenido es similar a otra fecha.

**Acciones esperadas:**

1. **Eliminar duplicados existentes en la tabla de normativas**, dejando solo un registro por URL única (la más reciente o la primera según fecha de publicación).
2. **Modificar el scraper** para que antes de insertar verifique si la URL ya existe en la BD. Si ya existe, no insertar.
3. (Opcional) Establecer la columna `Accion` como clave primaria o al menos como unique.

---

## 4. Barra de búsqueda por palabra clave

**Problema actual:**
La barra de búsqueda solo funciona al hacer clic en “Aplicar filtro” dentro del desplegable de filtros.

**Opciones planteadas:**

1. Búsqueda en tiempo real mientras se escribe (mayor consumo de recursos).
2. Búsqueda con botón “Aplicar búsqueda” al lado de la barra, o al presionar Enter.

**Criterios:** rendimiento, experiencia de usuario, consumo de recursos.

**Acción esperada:**
Elegir e implementar la opción 2 (botón o Enter) por ser más eficiente sin sacrificar UX. Asegurar que el comportamiento esté documentado y sea claro para el usuario.

---

## 5. Normalización del campo `fecha_scraping`

**Requerimientos:**

- Todo registro sin `fecha_scraping` debe recibir `2026-05-04 23:59:59`.
- Cualquier `fecha_scraping` con microsegundos (`yyyy-mm-dd hh:mm:ss.ssssss`) debe convertirse a `dd-mm-yyyy hh:mm:ss` (sin microsegundos).
- Toda nueva inserción debe guardar `fecha_scraping` con precisión de segundos (sin microsegundos).

**Acción esperada:**
Escribir un script de migración que:

- Actualice todos los registros existentes según estas reglas.
- Modifique la lógica de los scrapers y modelos para que futuras inserciones respeten el formato.

---

## 6. Corrección de `fecha_scraping` en scrapers de noticias

**Problema detectado:**
Ejemplo: una noticia real del 2026-05-04 tiene `fecha_scraping = 2026-05-07 13:16:24.557715`, aunque se extrajo el 4 de mayo.

**Causa:**
Los scrapers actualizan `fecha_scraping` cada vez que se ejecutan, incluso si la noticia ya existía.

**Solución esperada:**

- `fecha_scraping` debe ser la **primera fecha en que el scraper encontró y guardó esa noticia**.
- Al re-ejecutar un scraper, si la noticia ya existe (por ejemplo, por link único), **no se debe actualizar `fecha_scraping`**.
- Implementar esta lógica en todos los scrapers de noticias y normativas.

**Acción:**
Modificar el flujo de inserción/actualización para respetar la fecha de primera detección.

---

## 7. Problemas con SMA / SNIFA (fiscalizaciones, sancionatorios, etc.)

**Síntomas:**

- No se muestran los registros más nuevos en la interfaz, aunque existen en la base de datos.
- Ejemplo con fiscalizaciones: los expedientes `DFZ-2026-614-XIV-PC`, `DFZ-2026-758-IX-PC`, `DFZ-2026-795-XIII-PC` no aparecen al buscar, incluso sin filtros.

**Causas hipotéticas:**

- Límite de 5000 registros mal aplicado (los más nuevos deberían aparecer primero).
- Falta de ordenamiento por fecha descendente.
- Problemas de paginación o filtros no actualizados.

**Mejora adicional solicitada:**
Permitir filtrar fiscalizaciones por año (extraído del expediente: `DFZ-{año}-...`).

**Formato de expediente:**

```
DFZ-{año}-{número}-{región}-{tipo}
```

Donde `región` = I a XIV, `tipo` puede ser:

- RCA, PC, PPDA, NE, LEY, MP, NC, SRCA

Si hay algo después del tipo (ej. `-IA`, `-EI`), corresponde a tipo de fiscalización (Inspección Ambiental o Examen de Información), ignorable para el filtro base.

**Acciones esperadas:**

1. Revisar la consulta SQL o el endpoint que devuelve fiscalizaciones: asegurar orden descendente por año o por fecha de creación.
2. Implementar filtro por año (desde el frontend y backend).
3. Verificar que los límites y paginación no oculten los registros más recientes.
4. Si es necesario, corregir el orden por defecto de la tabla.

---

## Formato de entrega esperado

Para cada punto, entrega:

- Explicación clara del problema y tu diagnóstico.
- Código modificado o nuevo (con rutas relativas al proyecto).
- Instrucciones de migración si aplica (ej. scripts SQL).
- Breve justificación de decisiones técnicas.
