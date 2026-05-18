Fase 1 — Infraestructura de Datos (PostgreSQL + Docker) y Script ETL de Migración

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
