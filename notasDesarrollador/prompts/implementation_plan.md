# Plan de Implementación – SNIFA/SMA

## 1. Objetivo General

Unificar el criterio de ordenamiento en todas las tablas del sistema (Fiscalizaciones, Sancionatorios, RegistroSanciones, Programas de Cumplimiento, Requerimientos, Medidas Provisionales), reemplazando el actual orden lexicográfico del campo `detalle_link` por un orden numérico basado en el ID de ficha extraído de la URL.

Además, corregir los filtros por año en múltiples tablas y reparar la extracción del campo `pago_multa` en RegistroSanciones.

---

## 2. Nueva Columna Obligatoria en Cada Tabla

Agregar en **cada registro de todas las tablas** una columna llamada:

| nombre_columna | tipo    | origen                         |
| -------------- | ------- | ------------------------------ |
| `ficha_id`     | integer | Extraído de la URL del detalle |

### Regla de extracción

Tomar el número entero al final de la URL:

- `https://snifa.sma.gob.cl/RegistroPublico/Ficha/3979` → `3979`
- `https://snifa.sma.gob.cl/Sancionatorio/Ficha/4490` → `4490`
- `https://snifa.sma.gob.cl/RequerimientoIngreso/Ficha/254` → `254`

### Ordenamiento definitivo

Toda tabla se ordenará por `ficha_id DESC` (más alto = más nuevo).

---

## 3. Corrección de Filtros por Año en las Tablas

### Tablas afectadas actualmente

- Sancionatorios
- RegistroSanciones
- Programas de Cumplimiento
- Medidas Provisionales
- Requerimientos

### Problema detectado

El dropdown de “Filtrar por Año (Expediente)” está tomando el **segundo** valor del expediente (`NÚMERO`) en lugar del **tercero** (`AÑO`).

### Formato correcto del expediente

`LETRA - NÚMERO - AÑO`
Ejemplo: `D-063-2026` → año = `2026`

### Acción requerida

- Modificar la lógica de extracción del año en el scraper/filtro.
- El dropdown de años debe mostrar años reales (2026, 2025, 2024, …) orden descendente.
- Aplicar el mismo cambio en todas las tablas mencionadas.

---

## 4. Corrección Específica para RegistroSanciones

### Campo `pago_multa`

Actualmente no se extrae ningún valor.

### Posibles valores reales según el HTML

| HTML contiene                                 | Valor a guardar |
| --------------------------------------------- | --------------- |
| `<span class="pagada">...Pagada</span>`       | `Pagada`        |
| `<span class="pendiente">...Pendiente</span>` | `Pendiente`     |
| `<i>No Aplica</i>`                            | `No Aplica`     |

### Cambio solicitado en el filtro

- Actual: filtro de texto libre.
- Nuevo: **dropdown con 3 opciones**:
  - Pagada
  - Pendiente
  - No Aplica

---

## 5. Tablas Sin Primary Key (Normativas)

La tabla **Normativas** no tiene primary key actualmente.

- La URL del detalle es única por día.
- Usar `url` o `ficha_id` como identificador único (según disponibilidad).
- Aplicar también el orden por `ficha_id` si existe, o conservar el orden por fecha si `ficha_id` no está disponible.

---

## 6. Notificaciones de Ítems Nuevos

### Estado actual

- Solo se muestran al refrescar con F5.
- Las tablas no tienen etiqueta visual de “nuevo”.

### No se requiere acción inmediata

El documento solo solicita **registro del comportamiento actual**, no cambios específicos.

---

## 7. Resumen de Acciones por Tabla

| Tabla                     | Orden por `ficha_id` | Filtro año corregido | Campo `pago_multa` | Dropdown pago multa |
| ------------------------- | -------------------- | -------------------- | ------------------ | ------------------- |
| Fiscalizaciones           | Sí                   | No indica error      | N/A                | N/A                 |
| Sancionatorios            | Sí                   | Sí                   | N/A                | N/A                 |
| RegistroSanciones         | Sí                   | Sí                   | Sí                 | Sí                  |
| Programas de Cumplimiento | Sí                   | Sí                   | N/A                | N/A                 |
| Medidas Provisionales     | Sí                   | Sí                   | N/A                | N/A                 |
| Requerimientos            | Sí                   | Sí                   | N/A                | N/A                 |
| Normativas                | Sí (si aplica)       | No aplica            | N/A                | N/A                 |

---

## 8. Orden de Ejecución Recomendado

1. **Extraer y guardar `ficha_id`** en todas las tablas.
2. **Migrar ordenamiento** a `ficha_id DESC`.
3. **Corregir filtro de año** (expediente) en las 5 tablas afectadas.
4. **Reparar scraper de `pago_multa`** en RegistroSanciones.
5. **Cambiar filtro de pago multa** a dropdown.
6. **Validar** que el orden por ficha refleje correctamente “nuevo más arriba”.
