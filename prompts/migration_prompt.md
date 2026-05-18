# Prompts Maestros para la Migración de BioNews a Microservicios

Este documento contiene un conjunto de **Prompts de Ingeniería** listos para ser copiados y pasados a un asistente de IA de codificación. Están organizados de manera estrictamente incremental para ejecutar la migración del monolito de BioNews a microservicios y PostgreSQL sin romper el sistema actual.

---

# Prompt 1: Fase 1 — Infraestructura de Datos (PostgreSQL + Docker) y Script ETL de Migración

## Contexto de la Tarea:

Estamos migrando la plataforma **BioNews** de una base de datos monolítica SQLite (`data/data.db`) a un clúster PostgreSQL en contenedores Docker. Siguiendo el plan de arquitectura, levantaremos un único contenedor PostgreSQL (`postgres:15-alpine`) que albergará 4 bases de datos lógicas independientes (`bionews_users_db`, `bionews_news_db`, `bionews_legal_db` y `bionews_consultations_db`).

## Archivos Involucrados:

- [docker-compose.yml](file:///c:/Users/maria/Desktop/BioNews/docker-compose.yml)
- `init-multiple-databases.sh` (Nuevo script de inicialización)
- `migrate_data.py` (Nuevo script de migración ETL)

## Instrucciones para el Desarrollador de IA:

### 1. Crear el Script de Inicialización de Bases de Datos

Crea el archivo `init-multiple-databases.sh` en el directorio raíz. Este script de shell debe:

- Leer la variable de entorno `POSTGRES_MULTIPLE_DATABASES` (que contendrá la string `"bionews_users_db,bionews_news_db,bionews_legal_db,bionews_consultations_db"`).
- Dividir el string por comas y ejecutar comandos `psql` para crear cada base de datos lógica y otorgar todos los privilegios al usuario administrador `POSTGRES_USER`.

### 2. Actualizar el `docker-compose.yml`

Modifica el archivo `docker-compose.yml` actual para añadir los siguientes servicios manteniendo la estructura de red y volumen existente:

- **`postgres_db`**: Imagen `postgres:15-alpine`. Container name `bionews-postgres`. Monta el volumen de datos `postgres_data` en `/var/lib/postgresql/data`. Monta el script `./init-multiple-databases.sh` en `/docker-entrypoint-initdb.d/init-multiple-databases.sh:ro`. Expone el puerto `5432:5432`. Define las variables de entorno para el usuario (`bionews_admin`), contraseña (`secret_master_password`), base de datos principal (`bionews_master`) y la lista de base de datos a crear.
- **`redis_broker`**: Imagen `redis:7-alpine`. Container name `bionews-redis`. Expone el puerto `6379:6379`.
- Asegúrate de agregar `postgres_data` a la sección de `volumes` global y que todos los contenedores pertenezcan a la red `bionews-net`.

### 3. Desarrollar el Script de Migración ETL (`migrate_data.py`)

Escribe un script estructurado en Python en la raíz llamado `migrate_data.py` que realice la migración de datos histórica.
El script debe:

1.  **Conectarse a la base de datos origen SQLite** (`data/data.db`).
2.  **Conectarse a las 4 bases de datos destino de PostgreSQL** usando el driver `psycopg2` (añade `psycopg2-binary` si es necesario).
3.  **Mapear y Crear Tablas en PostgreSQL:** El script debe ejecutar sentencias `CREATE TABLE IF NOT EXISTS` en cada base de datos lógica según el siguiente mapeo:
    - **`bionews_news_db`**: Tabla `noticias`.
    - **`bionews_users_db`**: Tablas `users` (reemplaza `id INTEGER PRIMARY KEY AUTOINCREMENT` por `id SERIAL PRIMARY KEY`), `favoritos`, `user_category_views`, `user_item_views`, `bug_reports` (agregar serial id primary key).
    - **`bionews_legal_db`**: Tablas `fiscalizaciones`, `medidas_provisionales`, `normativas`, `pertinencias`, `programasDeCumplimiento`, `registroSanciones`, `requerimientos`, `sancionatorios`, `Tribunales` (reemplazar rowid implícitos por un campo serial explicit: `id SERIAL PRIMARY KEY`).
    - **`bionews_consultations_db`**: Tablas `minsal_vigentes`, `minsal_resultados`, `mma_abiertas`, `mma_cerradas`, `dga_consultas`.
4.  **Extraer y Cargar por Lotes (Batch Insertion):**
    - Leer los registros de SQLite.
    - Realizar transformaciones de tipos de datos: parsear strings de fechas a objetos `datetime` de Python para que PostgreSQL los guarde correctamente como `TIMESTAMP` o `DATE` en lugar de strings de texto.
    - Insertar los registros en PostgreSQL utilizando inserciones masivas eficientes (`cursor.executemany`) en bloques de 500 a 1000 registros para evitar el desbordamiento de memoria RAM.
5.  **Validación de Totales:** Imprimir en consola la comparación del conteo de filas de cada tabla entre SQLite y PostgreSQL para confirmar la integridad del proceso.

Por favor, genera el código del script de shell `init-multiple-databases.sh`, la modificación exacta de `docker-compose.yml` y el script de migración completo `migrate_data.py`. No realices cambios destructivos en el código del servidor web ni en los scrapers en esta fase.

# Prompt 2: Fase 2 — Refactorización de la Capa de Guardado y Conexión de Scrapers

## Contexto de la Tarea:

Hemos configurado la infraestructura de Docker con PostgreSQL multi-base de datos en la Fase 1. Ahora, adaptaremos los scrapers de BioNews ubicados en `src/scrapers/` para que escriban nativamente en PostgreSQL.

**Lineamiento Crítico:** La lógica de extracción, crawling y parsing de datos (Playwright, BeautifulSoup, obtención de JSON y selectores) debe quedar **100% intacta**. Solamente se modificará la capa de conexión y las consultas SQL de guardado.

## Archivos Involucrados:

- [src/database/manager.py](file:///c:/Users/maria/Desktop/BioNews/src/database/manager.py) (Conexión)
- Todos los archivos en [src/scrapers/](file:///c:/Users/maria/Desktop/BioNews/src/scrapers/) (Guardado y sentencias SQL)

## Instrucciones para el Desarrollador de IA:

### 1. Refactorizar `DatabaseManager` en `src/database/manager.py`

Actualiza el `DatabaseManager` para conectarse a PostgreSQL mediante `psycopg2` en lugar de `sqlite3`:

- Asegúrate de que lea los datos de acceso (host, user, password, port) desde variables de entorno con valores por defecto locales (`localhost`, `bionews_admin`, `secret_master_password`, `5432`).
- Modifica o sobrecarga la función `get_connection(self, database_name)` para que reciba el nombre de la base de datos lógica destino a la cual conectarse, retornando una conexión nativa de `psycopg2`.

### 2. Modificar las Consultas SQL en los Scrapers (`src/scrapers/*`)

Revisa secuencialmente cada uno de los scrapers y adapta sus métodos de persistencia:

- **Cambio de Placeholders:** Reemplaza el marcador de parámetros de SQLite `?` por el marcador nativo de PostgreSQL `%s` en todas las ejecuciones `cursor.execute(...)` y `cursor.executemany(...)`.
- **Actualización de Cláusulas de Conflicto:**
  - Donde veas `INSERT OR IGNORE INTO tabla`, modifícalo a la sintaxis estándar de PostgreSQL usando cláusulas `ON CONFLICT (columna_pk) DO NOTHING`.
  - Donde veas `INSERT OR REPLACE INTO tabla`, modifícalo a la sintaxis `ON CONFLICT (columna_pk) DO UPDATE SET campo1 = EXCLUDED.campo1, ...`.
- **Asignación de Conexiones por Servicio:** Modifica las inicializaciones de base de datos en los scrapers para que soliciten la base de datos correcta. Por ejemplo:
  - Scrapers de SMA, SEA y Tribunales (`sea_legal.py`, `primerTribunal.py`, `segundoTribunal.py`, `tercerTribunal.py`, `snifa.py`, `sanciones.py`, `reqSEIA.py`, `pdc.py`, `medidas.py`, `fiscalizaciones.py`, `diario_oficial.py`): Deben conectarse a la base de datos `bionews_legal_db`.
  - Scrapers de Consultas Públicas (`minsal.py`, `mma_consultas.py`, `dga_consultas.py`): Deben conectarse a `bionews_consultations_db`.
  - Scrapers de Noticias (`mma.py`, `sbap.py`, `sea.py`, `sernageomin.py`, `tribunal2.py`, `sma.py`, `corteSuprema.py`, `tribunal3.py`, `scraper_dga.py`): Deben guardar las noticias consumiendo el método de guardado en la base de datos `bionews_news_db`.

Aplica estos cambios de forma incremental y segura, garantizando que el resto de los métodos (de extracción y parsing) no sean modificados.

# Prompt 3: Fase 3 — Refactorización de DatabaseManager y Servidor Monolítico

## Contexto de la Tarea:

Ahora que la base de datos y los scrapers se ejecutan en PostgreSQL, adaptaremos los endpoints del monolito principal `server.py` y completaremos la lógica de persistencia y helpers de `DatabaseManager`. Esto preparará al sistema para ser dividido de forma segura.

## Archivos Involucrados:

- [src/database/manager.py](file:///c:/Users/maria/Desktop/BioNews/src/database/manager.py)
- [server.py](file:///c:/Users/maria/Desktop/BioNews/server.py)

## Instrucciones para el Desarrollador de IA:

### 1. Completar CRUDs en `DatabaseManager` para PostgreSQL

Modifica los métodos restantes de `src/database/manager.py`:

- **`save_news`**: Adaptar placeholders a `%s` y la cláusula de inserción o conflicto a PostgreSQL sobre `bionews_news_db`.
- **`add_favorite`**, **`remove_favorite`**, **`get_favorites`**: Mapear a la base de datos `bionews_users_db` con parámetros `%s` e instrucciones `ON CONFLICT` correspondientes.
- **`create_user`**, **`get_user_by_email`**, **`get_all_users`**, **`update_user_preferences`**: Mapear a `bionews_users_db`.
- **`get_table_data`**: Configurar la función genérica para que enrute dinámicamente la conexión a la base de datos que corresponda según la tabla solicitada (por ejemplo, si pide `fiscalizaciones` conecta a `bionews_legal_db`, si pide `mma_abiertas` conecta a `bionews_consultations_db`).
- Reemplazar cualquier consulta de paginación o depuración basada en `rowid` de SQLite por ordenación explícita mediante claves seriales (`id` o `ficha_id`).

### 2. Adaptar `server.py` a las Múltiples Bases de Datos

Revisa los endpoints del backend en `server.py` y asegúrate de que consuman las conexiones correctas del `DatabaseManager` refactorizado.

- Presta especial atención al endpoint de depuración de registros `/api/admin/debug/delete-latest/{category}`: modifica la lógica de borrado que usaba `rowid` en SQLite para usar la ordenación por campo serial `id` o `ficha_id` en PostgreSQL según la tabla.
- Actualiza el endpoint de estadísticas `/api/stats/{table_name}` para realizar las agregaciones (`COUNT`, `GROUP BY`) usando SQL nativo de PostgreSQL.
- Actualiza el endpoint global de búsqueda `/api/search`: Dado que en esta fase el servidor aún es monolítico pero tiene acceso a las 4 bases de datos, implementa la búsqueda ejecutando consultas concurrentes con hilos (`ThreadPoolExecutor` o `asyncio`) a cada una de las bases de datos lógicas usando el `DatabaseManager` y consolida el JSON de salida unificado.

Por favor, genera la refactorización completa de `src/database/manager.py` y los fragmentos de actualización necesarios para `server.py` asegurando la estabilidad y compatibilidad de todos los endpoints.

# Prompt 4: Fase 4 — Desacoplamiento en Microservicios y API Gateway

## Contexto de la Tarea:

Tenemos el monolito adaptado a PostgreSQL. Procederemos a dividir físicamente `server.py` en 4 microservicios FastAPI independientes y a configurar el API Gateway para enrutar las peticiones de forma transparente.

## Archivos Involucrados:

- [server.py](file:///c:/Users/maria/Desktop/BioNews/server.py) (Monolito original)
- `gateway.conf` (NUEVA configuración para Nginx API Gateway)
- Creación de subdirectorios/servicios: `/src/services/auth`, `/src/services/news`, `/src/services/legal`, `/src/services/consultations`

## Instrucciones para el Desarrollador de IA:

### 1. Crear los 4 Microservicios FastAPI

Extrae la lógica de `server.py` y crea cuatro aplicaciones FastAPI independientes en sus respectivos archivos:

1.  **Auth & Users Service (`/src/services/auth/main.py`)**:
    - Maneja endpoints: `/api/auth/login`, `/api/auth/register`, `/api/auth/me`, `/api/auth/preferences`, `/api/favorites/*`, `/api/bugs/*`, `/api/admin/users/*` y `/api/admin/bugs/*`.
    - Se conecta exclusivamente a la base de datos `bionews_users_db`.
    - Puerto asignado: `8001`.
2.  **News Service (`/src/services/news/main.py`)**:
    - Maneja endpoints: `/api/news` (listado y flags de noticias).
    - Se conecta exclusivamente a `bionews_news_db`.
    - Puerto asignado: `8002`.
3.  **Legal & Regulatory Service (`/src/services/legal/main.py`)**:
    - Maneja endpoints: `/api/data/{table_name}`, `/api/data/{table_name}/count`, `/api/options` y el endpoint `/api/admin/debug/delete-latest/*`.
    - Se conecta exclusivamente a `bionews_legal_db`.
    - Puerto asignado: `8003`.
4.  **Public Consultations Service (`/src/services/consultations/main.py`)**:
    - Maneja endpoints: `/api/consultas/documentos/{consulta_id}` y `/api/minsal/documents/{consulta_id}`.
    - Se conecta exclusivamente a `bionews_consultations_db`.
    - Puerto asignado: `8004`.

_Nota:_ Asegura que cada microservicio maneje correctamente los esquemas Pydantic requeridos para sus endpoints y que hereden el middleware CORS.

### 2. Configurar el API Gateway (Nginx)

Crea una carpeta `gateway` en la raíz del proyecto y escribe el archivo `gateway.conf` (configuración de Nginx). Este gateway debe escuchar en el puerto `8000` (el puerto original del backend) y actuar como proxy reverso:

- Redireccionar `/api/auth/`, `/api/users/`, `/api/favorites/`, `/api/bugs/`, `/api/admin/users/` y `/api/admin/bugs/` a `http://auth-service:8001`.
- Redireccionar `/api/news/` a `http://news-service:8002`.
- Redireccionar `/api/data/`, `/api/options` y `/api/admin/debug/delete-latest/` a `http://legal-service:8003`.
- Redireccionar `/api/consultas/` y `/api/minsal/` a `http://consultations-service:8004`.

### 3. Implementar Búsqueda Global y "is_new" Desacoplados

- **Búsqueda Global (`/api/search`)**: Configúrala en el servicio de gateway o crea un endpoint agregador en el **Legal Service** que realice llamadas HTTP asíncronas concurrentes (utilizando `httpx` de forma asíncrona) a `/api/news/search`, `/api/legal/search` y `/api/consultations/search`, consolidando los resultados en un único JSON unificado.
- **Flag "is_new"**: Modifica la firma de `/api/data/{table_name}` en el Legal/News Service para que el frontend envíe el timestamp `last_exit_at` y el array `viewed_ids` como query params o headers. Con esto, los servicios calcularán de forma estática e hiperveloz el flag `is_new` sin realizar consultas de red cruzadas.

Genera la estructura de directorios y los archivos de inicialización y main de cada microservicio, junto con el archivo de configuración del API Gateway.

# Prompt 5: Fase 5 — Integración SSE con Redis y Despliegue en Docker Compose

## Contexto de la Tarea:

Hemos dividido el backend en 4 microservicios y configurado el API Gateway. Ahora implementaremos la arquitectura asíncrona de notificaciones en tiempo real basada en Redis Pub/Sub, y actualizaremos los contenedores en `docker-compose.yml` para el despliegue final.

## Archivos Involucrados:

- Microservicios FastAPI (`auth/main.py`, `legal/main.py`, etc.)
- [docker-compose.yml](file:///c:/Users/maria/Desktop/BioNews/docker-compose.yml)
- [scheduler.py](file:///c:/Users/maria/Desktop/BioNews/scheduler.py) / Workers de Scraping

## Instrucciones para el Desarrollador de IA:

### 1. Implementar la Arquitectura SSE y Redis Pub/Sub

Alinea la lógica de notificaciones en tiempo real del sistema:

1.  **Publicador (Scrapers / Ingestion Engine):** Cuando el scheduler de scraping complete una ingesta exitosa, debe publicar un mensaje en Redis utilizando `redis-py` (ej. canal `bionews_events`):
    ```json
    {
      "type": "new_ingestion",
      "category": "fiscalizaciones",
      "timestamp": "2026-05-18T13:15:00Z"
    }
    ```
2.  **Subscriptor (Auth & Users Service):** En el microservicio de autenticación, suscríbete de forma asíncrona al canal de Redis.
    - Al recibir un evento, actualiza de inmediato la tabla local `category_last_updates (category_slug, last_updated_at)` en `bionews_users_db`.
    - Transmite el mensaje mediante el flujo SSE activo a los clientes conectados a través del endpoint `/api/notifications/stream` (que ahora reside en este microservicio).
3.  **Endpoint Sidebar:** El endpoint `/api/notifications/status` (en el Auth Service) responderá comparando simplemente los registros de `user_category_views.last_exit_at` con `category_last_updates.last_updated_at` para iluminar eficientemente los puntos rojos en el Sidebar de la interfaz React sin llamadas de red cruzadas.

### 2. Reestructurar el `docker-compose.yml` de Producción

Modifica el `docker-compose.yml` para levantar toda la infraestructura de microservicios:

- **`postgres_db`** y **`redis_broker`** (Fase 1).
- **`gateway`**: Contenedor Nginx API Gateway que mapea el puerto `8000:8000` y depende de los microservicios.
- **`auth-service`**, **`news-service`**, **`legal-service`**, **`consultations-service`**: Microservicios independientes expuestos únicamente en la red privada de Docker, configurados para depender de `postgres_db` y `redis_broker`.
- **`scheduler`**: Motor de scraping configurado para correr `scheduler.py` en segundo plano con las variables correspondientes de acceso a la base de datos PostgreSQL y Redis.
- **`web`**: El contenedor del frontend React que se mantiene apuntando a `gateway:8000` de forma transparente.

Por favor, genera la implementación exacta del Listener Pub/Sub en el microservicio de autenticación y la reestructuración completa del archivo `docker-compose.yml` final, garantizando que el clúster inicie de forma secuencial y coordinada mediante políticas de salud (`healthchecks`).

```

```
