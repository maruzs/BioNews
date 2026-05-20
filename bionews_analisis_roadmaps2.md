# BioNews — Análisis Técnico y Roadmaps

> [!NOTE]
> Este documento contiene el análisis de seguridad, la evaluación de optimización de bases de datos y las recomendaciones arquitectónicas para la plataforma BioNews.
> 
> *Estado actual:* **Última actualización: 20 de Mayo de 2026.**
> *Nota del usuario:* Los roadmaps de Aplicación Móvil, Sistema de Confirmación por Mail / Cambio de Contraseña y Newsletters se encuentran **postergados e ignorados temporalmente** para priorizar la estabilidad del núcleo de scraping, notificaciones y base de datos.

---

## 1. 🔐 Estado de Vulnerabilidades de Seguridad

Se evalúa la infraestructura actual y los endpoints expuestos en el backend FastAPI y Docker Compose. A continuación se detalla su estado actual (Corregido / Pendiente):

### 🔴 CRÍTICO

#### 1.1 Secret Key hardcodeada en `server.py`
* **Estado:** **CORREGIDO**
* **Detalle:** Se eliminó la clave quemada. Ahora `SECRET_KEY` se carga mediante variables de entorno en la inicialización: `os.getenv("JWT_SECRET_KEY")`.
* **Recomendación futura:** Asegurar que las variables de entorno de producción usen una clave fuerte autogenerada.

#### 1.2 Contraseña del admin por defecto hardcodeada
* **Estado:** ⚠️ **PENDIENTE (VIGENTE)**
* **Código:** `server.py:140`
  ```python
  hashed_pw = hash_password("#81680085pls")
  db.create_user("Administrador", "administrador@bionews.cl", hashed_pw, role="admin")
  ```
* **Riesgo:** Si un atacante tiene acceso al repositorio, conocerá las credenciales de administración por defecto.
* **Solución propuesta:** Leer la contraseña por defecto desde la variable de entorno `ADMIN_PASSWORD` o utilizar un script de inicialización seguro de base de datos (`setup.py`).

#### 1.3 CORS completamente abierto
* **Estado:** ⚠️ **PENDIENTE (VIGENTE)**
* **Código:** `server.py:59`
  ```python
  allow_origins=["*"]
  ```
* **Riesgo:** Permite que scripts maliciosos cargados en navegadores de terceros hagan solicitudes en nombre de usuarios autenticados.
* **Solución propuesta:** Reemplazar el comodín `"*"` con los orígenes autorizados específicos (ej. dominio de la plataforma e IPs del entorno Tailscale).

#### 1.4 Puerto PostgreSQL expuesto en Docker
* **Estado:** **CORREGIDO**
* **Detalle:** En `docker-compose.yml`, el mapeo del puerto de Postgres se restringió a la interfaz de loopback local (`127.0.0.1:5432:5432`).
* **Impacto:** Evita que el puerto de base de datos sea escaneado o accedido directamente desde internet pública.

#### 1.5 Puerto Redis expuesto sin autenticación
* **Estado:** **CORREGIDO**
* **Detalle:** Se eliminó el mapeo de puertos del host para Redis (ahora solo se comunica a través de la red aislada `bionews-net`) y se añadió autenticación con contraseña mediante `--requirepass ${REDIS_PASSWORD}`.

---

### 🟠 ALTO

#### 1.6 Sin rate limiting en `/api/auth/login`
* **Estado:** **CORREGIDO**
* **Detalle:** Se configuró el middleware de `slowapi` restringiendo el login a un máximo de 10 intentos por minuto por dirección IP (`@limiter.limit("10/minute")`).

#### 1.7 Sin rate limiting en `/api/auth/register`
* **Estado:** ⚠️ **PENDIENTE (VIGENTE)**
* **Riesgo:** Expone la plataforma a la creación masiva automatizada de cuentas de usuario falso (Spam accounts), saturando la base de datos de usuarios.
* **Solución propuesta:** Agregar el decorador `@limiter.limit("5/minute")` al endpoint `/api/auth/register`.

#### 1.8 Sin validación de tipo/extensión en upload de screenshots
* **Estado:** **CORREGIDO**
* **Detalle:** El validador `_validate_image_upload` ahora verifica que la extensión sea permitida (png, jpg, jpeg, gif, webp) y analiza la firma mágica del archivo para garantizar que es una imagen legítima y no un script malicioso renombrado.

#### 1.9 Path traversal potencial en `screenshot_path`
* **Estado:** **CORREGIDO**
* **Detalle:** Se sanitiza el nombre de archivo y se valida que el path absoluto resuelto comience con la ruta del directorio de subidas:
  ```python
  if not abs_filepath.startswith(abs_upload + os.sep):
      raise HTTPException(400, "Nombre de archivo inválido")
  ```

#### 1.10 `/api/scrape/all` sin autenticación
* **Estado:** **CORREGIDO**
* **Detalle:** El endpoint se protegió requiriendo privilegios de administrador mediante FastAPI dependencies: `admin = Depends(get_current_admin)`.

---

### 🟡 MEDIO

#### 1.11 Tokens JWT sin invalidación
* **Estado:** **CORREGIDO**
* **Detalle:** Se introdujo la validación del identificador único del JWT (`jti`) en `get_current_user`. Al cerrar sesión, el `jti` se agrega a una lista negra persistida en Redis, invalidando el token inmediatamente.

#### 1.12 `get_current_user` no verifica el usuario contra la BD en cada request
* **Estado:** **CORREGIDO**
* **Detalle:** Ahora se consulta si el usuario existe y si su estado es `blocked` en cada request. Para evitar saturar PostgreSQL, se lee desde la caché de Redis con un TTL de 60 segundos.

#### 1.13 Información sensible en logs de errores
* **Estado:** ⚠️ **PENDIENTE (VIGENTE)**
* **Riesgo:** En caso de fallos críticos, los traceback detallados del backend se escriben a la salida estándar visible en contenedores Docker de producción.
* **Solución propuesta:** Redirigir el traceback detallado únicamente a un archivo de log local con permisos restringidos, y mostrar mensajes genéricos sanitizados en los logs generales del sistema.

#### 1.14 Validación débil en `update_preferences`
* **Estado:** ⚠️ **PENDIENTE (VIGENTE)**
* **Riesgo:** El backend acepta cualquier JSON dict arbitrario y lo guarda directamente en la BD sin validar esquema o tamaño, abriendo paso a ataques de denegación de servicio (guardado de archivos de texto masivos en la fila de preferencias).
* **Solución propuesta:** Definir un modelo de datos Pydantic para el esquema de preferencias de usuario y restringir el payload entrante.

---

## 2. ⚡ Análisis de Optimizaciones de Queries

Evaluación técnica detallada de las optimizaciones implementadas y del roadmap de rendimiento:

### 2.1 Caching y optimización en `get_table_data` (Completado)
* **Acción:** Se implementó una capa de caché inteligente en Redis. Las tablas estáticas se almacenan por 5 minutos, y las dinámicas por 2 minutos. Además, se cacheó el schema de las columnas de `information_schema.columns` reduciendo queries internas innecesarias.
* **Invalidación:** Se añadió invalidación automática en el post-scraping de nuevos registros (`cache.invalidate_pattern("table_data:*")`).

### 2.2 Optimización de opciones en `/api/options` (Completado)
* **Acción:** Se reemplazó la carga de 5,000 registros en memoria Python por consultas directas a base de datos usando `SELECT DISTINCT` ordenados y filtrados. Se cachea por 10 minutos.

### 2.3 Batching de estatus de notificaciones (Completado)
* **Acción:** Se eliminó el problema N+1 en la barra lateral reduciendo 28 consultas individuales por usuario a una sola consulta batch inicial combinada contra el estado guardado.

---

### 🔍 Análisis de Queries Pendientes (2.6 - 2.8)

#### 2.6 Creación de Índices Críticos
La falta de índices en columnas de ordenamiento y filtrado provoca que PostgreSQL realice búsquedas secuenciales completas (*Sequential Scans*). 

**Índices recomendados:**
1.  **Índice de Notificaciones por Fecha de Scraping:**
    ```sql
    CREATE INDEX IF NOT EXISTS idx_sea_scraping ON scrapers.sea_proyectos_evaluados (fecha_scraping DESC);
    CREATE INDEX IF NOT EXISTS idx_normativas_scraping ON scrapers.normativas (fecha_scraping DESC);
    CREATE INDEX IF NOT EXISTS idx_tribunales_scraping ON scrapers.Tribunales (fecha_scraping DESC);
    ```
    *Impacto:* Acelera exponencialmente la query de notificaciones de nuevos registros (`fecha_scraping::text > %s`) para todas las categorías que carecían de él.
2.  **Índice de Vistas del Usuario (Tracking):**
    ```sql
    CREATE INDEX IF NOT EXISTS idx_user_category_views ON users.user_category_views (user_id, category_slug);
    ```
    *Impacto:* Evita escaneos de la tabla completa de vistas de usuarios al cargar el sidebar.

#### 2.7 Búsqueda global con `LIKE` en múltiples tablas
Actualmente, las búsquedas globales de texto usan:
```sql
LOWER(campo) LIKE '%consulta%'
```
Esto fuerza a la base de datos a hacer escaneos de todas las filas porque PostgreSQL no puede usar índices B-Tree estándar cuando la cadena de búsqueda comienza con un comodín (`%`).

*   **Propuesta a corto plazo (Índices GIN Trigram):**
    Habilitar la extensión de trigramas y crear índices GIN (*Generalized Inverted Index*) sobre los campos principales de búsqueda:
    ```sql
    CREATE EXTENSION IF NOT EXISTS pg_trgm;
    
    CREATE INDEX IF NOT EXISTS idx_fisc_trgm ON scrapers.fiscalizaciones 
    USING GIN (unidad_fiscalizable gin_trgm_ops, nombre_razon_social gin_trgm_ops);
    
    CREATE INDEX IF NOT EXISTS idx_sea_trgm ON scrapers.sea_proyectos_evaluados 
    USING GIN (nombre gin_trgm_ops, titular gin_trgm_ops);
    ```
    *Mecanismo:* Los índices de trigramas dividen las palabras en fragmentos de 3 letras. Permiten que queries del tipo `LIKE '%texto%'` realicen búsquedas indexadas ultra rápidas en milisegundos en lugar de escaneos completos.

#### 2.8 `get_table_data` ordena por función en caliente (`to_date()`)
En `sea_proyectos_evaluados` se ordena la tabla mediante:
```sql
ORDER BY to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC
```
*Problema:* Al ordenar utilizando una función sobre una columna de tipo `TEXT`, PostgreSQL tiene que parsear cada fila de la tabla a formato `DATE` antes de ordenar, lo cual destruye la velocidad del query en tablas grandes.
*   **Propuesta de Columna Generada:**
    Convertir `fecha_presentacion` a un tipo nativo `DATE` mediante una columna generada guardada en disco (*Generated Always As ... Stored*) y crear un índice sobre ella:
    1. Modificar tabla agregando columna fecha nativa:
       ```sql
       -- Es necesario migrar la columna a un formato real DATE
       ALTER TABLE scrapers.sea_proyectos_evaluados 
       ADD COLUMN IF NOT EXISTS fecha_presentacion_date DATE;
       ```
    2. Modificar el scraper para insertar la fecha formateada en `fecha_presentacion_date`.
    3. Crear índice:
       ```sql
       CREATE INDEX IF NOT EXISTS idx_sea_fecha_date ON scrapers.sea_proyectos_evaluados (fecha_presentacion_date DESC);
       ```
    4. Cambiar el ordenamiento en el backend para usar la nueva columna indexada de fecha nativa.

---

## 3. 💡 Recomendaciones Generales (Punto 6)

Análisis general del estado de viabilidad de las recomendaciones de infraestructura:

### 3.1 Paginación Server-Side (Alta Prioridad)
* **Viabilidad:** Excelente y necesario. Actualmente el frontend pide todos los registros de una vez (ej: `-1` o `1000` límites) cargándolos en el navegador del cliente. 
* **Impacto:** Reduce la transferencia de red de megabytes a kilobytes y acelera el renderizado del navegador al pintar solo 25-50 filas por página con scroll infinito o paginador clásico.

### 3.2 Monitoreo de Errores con Sentry (Media Prioridad)
* **Viabilidad:** Muy simple. FastAPI tiene integración oficial con el SDK de Sentry que requiere menos de 5 líneas de código.
* **Impacto:** Captura excepciones de producción y errores silenciosos en scrapers en tiempo real enviando alertas al correo del equipo administrador.

### 3.3 Consolidación del Scheduler de Scrapers (Alta Prioridad)
* **Viabilidad:** Indispensable. Actualmente corre de dos formas: `scheduler_monitor` en la API y `scheduler.py` como servicio de Docker separado. 
* **Impacto:** Se debe apagar el monitor interno de la API y dejar únicamente el servicio `bionews-scheduler` para evitar duplicidad de solicitudes que pueden derivar en bloqueos de IPs desde los sitios web de origen (SEA, SMA, etc.).

### 3.4 Migraciones de Esquema con Alembic (Media Prioridad)
* **Viabilidad:** Útil para desarrollos futuros. SQLite no sufría tanto por cambios en caliente, pero al pasar a PostgreSQL en producción, cambiar tipos de columnas, nombres o tablas requiere migraciones declarativas y versionadas. Alembic nos dará control absoluto sin pérdida de datos.
