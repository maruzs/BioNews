# Plan de Implementación – SNIFA/SMA (Solo Pendientes)

## 1. Estado Actual (Ya Resuelto – No requiere acción)

- [x] Extraer y guardar `ficha_id` en todas las tablas.
- [x] Corrección de filtro por año en Sancionatorios, RegistroSanciones, Programas de Cumplimiento, Medidas Provisionales y Requerimientos.
- [x] Reparación del scraper de `pago_multa` en RegistroSanciones.
- [x] Filtro de `pago_multa` convertido a dropdown (Pagada / Pendiente / No Aplica).

---

## 2. Acciones Pendientes por Ejecutar

### 2.1 Ordenamiento de Normativas

**Problema:** Actualmente ordenado por `ficha_id`.  
**Requerido:** Ordenar por `fecha_publicacion DESC` (más nueva → más vieja).  
**Acción:** Modificar la consulta de la tabla Normativas. No usar `ficha_id` para orden.

---

### 2.2 Borrar y Recargar Tabla de Sanciones

**Motivo:** El scraper ya extrae `pago_multa` correctamente, pero los registros existentes no tienen ese campo poblado.  
**Acción:**

1. Truncar / borrar toda la tabla `RegistroSanciones`. (necesario, solo por esta vez)
2. Ejecutar nuevamente el scraper completo para esa tabla. (no necesario)
3. Verificar que todos los registros tengan `pago_multa` con valores `Pagada`, `Pendiente` o `No Aplica`. (No necesario)

---

### 2.3 Notificaciones de Ítems Nuevos (No tiempo real)

**Comportamiento actual:**  
Solo aparece punto rojo al hacer F5. No hay etiqueta “Nuevo”.  
Al cambiar de categoría o cerrar sesión, no desaparecen.

**Comportamiento deseado:**

| Evento                                                                 | Acción esperada                                                                                        |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Scraper (programado o manual) detecta nuevos ítems en BD               | Marcar esos ítems como `nuevo = true` en BD para ese usuario (o global + tabla de lectura por usuario) |
| Usuario está en la plataforma (sin F5) y hay nuevos ítems              | Aparece punto rojo al lado de la categoria correspondiente al nuevo item                               |
| Usuario hace clic en “Ver más” (noticia) o en columna “Acción” (tabla) | Marcar ese ítem específico como `leído` → desaparece etiqueta “Nuevo”                                  |
| Usuario hace clic en “Marcar todo como leído”                          | Marcar **todos** los ítems de esa categoría como leídos                                                |
| Usuario cambia de categoría (ej. de Fiscalización a Sanciones)         | Al volver a la categoría anterior, los ítems ya vistos NO muestran “Nuevo”                             |
| Usuario cierra sesión o cierra navegador                               | Al reingresar, los ítems ya marcados como leídos siguen sin etiqueta (persistencia entre dispositivos) |

**Requisitos técnicos:**

- **NO** usar WebSockets ni polling cada N segundos.
- **Sí** usar:
  - Tabla `usuario_item_visto` (`usuario_id`, `item_tipo`, `item_id`, `visto_en`).
  - O campo global `nuevo_desde` + última visita por usuario por categoría.
- Si hubo nuevos items debe aparecer un punto rojo al lado del nombre de la categoria correspondiente al nuevo item
- Al cargar una categoría, los items nuevos deberan estar marcados como nuevos y los leidos no
- Etiqueta visual “Nuevo” en cada fila nueva.
- **Noticias:** Misma lógica + **borde verde** adicional.

---

### 2.4 Paginación en Servidor

**Problema actual:**  
Frontend carga todos los registros (hasta 1000). Ineficiente en tablas grandes.

**Acción:**  
Implementar paginación real desde la API para **todas las tablas principales**:

- Fiscalizaciones
- Sancionatorios
- RegistroSanciones
- Programas de Cumplimiento
- Medidas Provisionales
- Requerimientos
- Normativas
- Noticias

**Formato de la API:**
GET /api/tabla?page=2&limit=50
Response:
{
"data": [...],
"total": 1240,
"page": 2,
"limit": 50,
"totalPages": 25
}

**Frontend:**

- Mostrar controles de paginación.
- Límite configurable (20, 50, 100).

---

### 2.5 Búsqueda Global

**Ubicación:** Barra en el Home.  
**Acción:**

- Consultar todas las tablas simultáneamente.
- Buscar en: expediente, título, contenido relevante.
- Mostrar resultados agrupados por tipo de tabla.
- Límite: 50 resultados por tipo o 200 totales.

---

### 2.6 Eliminación de Polling en NotificationsContext.tsx

**Problema actual:**  
Llamadas constantes a la API para notificaciones.

**Acción:**

- Eliminar polling automático.
- Reemplazar por:
  - Carga bajo demanda al cambiar de categoría.
  - Botón manual “Buscar novedades”.
  - (Opcional) Evento desde backend cuando el scraper termina (webhook / SSE).

---

### 2.7 Persistencia de “Visto” entre dispositivos

**Problema:**  
Actualmente la etiqueta “Nuevo” reaparece en otro dispositivo o tras cerrar sesión.

**Acción:**

- Guardar estado de “leído” en **backend**, no en localStorage/sesión.
- Usar tabla `usuario_item_visto` con `usuario_id` + `item_id`.
- Al marcar como leído desde cualquier dispositivo, se sincroniza por BD.

---

## 3. Resumen de Tareas por Orden de Ejecución

| #   | Tarea                                                              | Tabla(s) afectada(s)    |
| --- | ------------------------------------------------------------------ | ----------------------- |
| 1   | Cambiar ordenamiento de Normativas a `fecha_publicacion DESC`      | Normativas              |
| 2   | Borrar tabla de Sanciones con `pago_multa`                         | RegistroSanciones       |
| 3   | Implementar backend de “ítems nuevos” (tabla `usuario_item_visto`) | Todas                   |
| 4   | Agregar etiqueta “Nuevo” + borde verde en noticias                 | Todas + Noticias        |
| 5   | Implementar “Marcar todo como leído” por categoría                 | Todas                   |
| 6   | Eliminar polling en NotificationsContext                           | Frontend                |
| 7   | Persistencia de “visto” entre dispositivos                         | Backend + Frontend      |
| 8   | Paginación en servidor                                             | Todas                   |
| 9   | Búsqueda global                                                    | Home + todas las tablas |

---

## 4. Criterios de Aceptación

- [ ] Normativas ordenadas por fecha descendente.
- [ ] Los nuevos ítems muestran etiqueta “Nuevo” sin necesidad de F5.
- [ ] Al hacer clic en “Ver más” o “Acción”, desaparece la etiqueta.
- [ ] “Marcar todo como leído” funciona por categoría.
- [ ] Cambiar de categoría no muestra ítems ya vistos como nuevos.
- [ ] Al cerrar sesión y volver a entrar (mismo u otro dispositivo), los ítems vistos siguen sin etiqueta.
- [ ] No hay polling constante a la API.
- [ ] Paginación funciona en todas las tablas.
- [ ] Búsqueda global retorna resultados agrupados desde el Home.
