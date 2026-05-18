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
