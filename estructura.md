# Estructura del Proyecto: BioNews

Este documento describe la arquitectura técnica y funcional del proyecto BioNews para que sea interpretado por agentes de IA.

## 1. Resumen del Proyecto

BioNews es una plataforma de monitoreo y agregación de noticias y datos legales/ambientales de Chile. Automatiza la recolección de información desde múltiples fuentes gubernamentales y judiciales, centralizándolas en un dashboard interactivo.

## 2. Tecnologías Principales (Tech Stack)

### Backend (Directorio Raíz)

- **Lenguaje**: Python 3.10+
- **Framework API**: FastAPI (Uvicorn como servidor ASGI)
- **Base de Datos**: SQLite (almacenada en `data/data.db`)
- **Web Scraping**: Playwright, BeautifulSoup4, Requests
- **Autenticación**: JWT (JSON Web Tokens) con contraseñas hasheadas (Bcrypt)
- **Notificaciones**: Server-Sent Events (SSE) para actualizaciones en tiempo real
- **Tareas Programadas**: Paquete `schedule` (ejecutado vía `scheduler.py`)

### Frontend (Directorio `/web`)

- **Framework**: React 19 + TypeScript
- **Tooling**: Vite
- **UI Components**: Material UI (MUI) v9+
- **Visualización**: Recharts (Dashboards y gráficos)
- **Iconografía**: Lucide React
- **Navegación**: React Router v7+

### Infraestructura y DevOps

- **Contenedores**: Docker y Docker Compose
- **Servidor Web**: Nginx (para servir el frontend en producción)

## 3. Estructura de Directorios

```text
BioNews/
├── server.py              # Punto de entrada de la API FastAPI. Define endpoints y lógica de SSE.
├── scheduler.py           # Gestor de tareas programadas (scraping periódico).
├── startScraping.py       # Script para ejecución manual de todos los scrapers.
├── requirements.txt       # Dependencias de Python.
├── Dockerfile             # Configuración Docker para el Backend.
├── docker-compose.yml     # Orquestación de servicios (backend, frontend, db).
├── data/                  # Almacenamiento persistente (SQLite DB y configs JSON).
├── uploads/               # Archivos subidos (ej: capturas de reportes de errores).
├── src/                   # Lógica central del Backend.
│   ├── database/          # Gestión de persistencia.
│   │   └── manager.py     # Clase DatabaseManager (Singleton). Gestiona esquemas y queries.
│   ├── scrapers/          # Módulos individuales de scraping por fuente.
│   │   ├── engine.py      # Lógica base/utilidades para scrapers.
│   │   ├── sea.py, sma.py, etc. # Implementaciones específicas.
│   └── utils/             # Helpers genéricos.
└── web/                   # Proyecto Frontend (React).
    ├── src/
    │   ├── components/    # Componentes reutilizables (Sidebar, Charts, Modals).
    │   ├── pages/         # Vistas principales (Dashboard, News, Admin).
    │   ├── hooks/         # Custom hooks (ej: useSSE para notificaciones).
    │   ├── services/      # Cliente API (fetch/axios).
    │   └── theme/         # Configuración de Material UI.
    └── vite.config.ts     # Configuración de Vite.
```

## 4. Arquitectura de Datos y Lógica

### Sistema de Scraping

Existen dos tipos de recolección de datos:

1. **Noticias (Genéricas)**: Scrapers que devuelven título, link, fecha y fuente. Se almacenan en la tabla `noticias`.
2. **Datos Estructurados**: Scrapers para fuentes específicas (SEA, SMA/SNIFA, Tribunales). Cada uno tiene su propia tabla (ej: `sea_proyectos_evaluados`, `fiscalizaciones`, `Tribunales`) con campos detallados.

### Sistema de Notificaciones ("Nuevos")

La plataforma rastrea qué ha visto cada usuario:

- **`user_category_views`**: Almacena cuándo fue la última vez que un usuario salió de una categoría.
- **`user_item_views`**: Almacena IDs de ítems específicos que el usuario ya abrió.
- **Lógica**: Un ítem se marca como `is_new: true` si su `fecha_scraping` es mayor a `last_exit_at` Y el ID no está en `user_item_views`.

### API (FastAPI)

- **Auth**: Endpoints en `/api/auth/*`.
- **Data**: Endpoints genéricos en `/api/data/{table_name}` y específicos para búsquedas globales en `/api/search`.
- **SSE**: Endpoint `/api/notifications/stream` que mantiene una conexión persistente para notificar cuando un scraper termina con éxito y hay datos nuevos.

## 5. Esquema de Base de Datos (SQLite)

La base de datos se encuentra en `data/data.db`. A continuación se detallan los esquemas de las tablas principales:

### Tablas de Usuario y Sistema

- **`users`**: Usuarios de la plataforma.
  ```sql
  CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      email TEXT UNIQUE,
      password_hash TEXT,
      role TEXT,
      blocked INTEGER DEFAULT 0,
      preferences TEXT,
      last_login TIMESTAMP
  )
  ```
- **`favoritos`**: Ítems guardados por los usuarios.
  ```sql
  CREATE TABLE favoritos (
      user_id INTEGER,
      id_o_link TEXT,
      fuente TEXT,
      nombre TEXT,
      fecha_agregado TIMESTAMP,
      accion TEXT,
      PRIMARY KEY (user_id, id_o_link)
  )
  ```
- **`noticias`**: Noticias generales de diversas fuentes.
  ```sql
  CREATE TABLE noticias (
      link TEXT PRIMARY KEY,
      titulo TEXT,
      fecha TEXT,
      imagen TEXT,
      fuente TEXT,
      fecha_scraping TIMESTAMP
  )
  ```

### Tablas de Monitoreo de Vistas (Notificaciones)

- **`user_category_views`**: Tracking de salida de categorías.
- **`user_item_views`**: Tracking de ítems individuales vistos.

### Tablas de Fuentes Específicas

#### SNIFA (Superintendencia del Medio Ambiente)

Tablas: `fiscalizaciones`, `sancionatorios`, `registroSanciones`, `programasDeCumplimiento`, `medidas_provisionales`, `requerimientos`.

```sql
-- Ejemplo representativo (fiscalizaciones)
CREATE TABLE fiscalizaciones (
    expediente TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria TEXT,
    region TEXT,
    estado TEXT,
    detalle_link TEXT,
    fecha_scraping TIMESTAMP,
    ficha_id INTEGER
)
```

#### Tribunales y Legal

- **`Tribunales`**:
  ```sql
  CREATE TABLE Tribunales (
      Rol TEXT PRIMARY KEY,
      Fecha TEXT,
      Caratula TEXT,
      Tribunal TEXT,
      Tipo_de_Procedimiento TEXT,
      Estado_Procesal TEXT,
      Accion TEXT,
      fecha_scraping TIMESTAMP
  )
  ```
- **`normativas`**:
  ```sql
  CREATE TABLE normativas (
      fecha TEXT,
      normativa TEXT,
      tipo_normativa TEXT,
      organismo TEXT,
      suborganismo TEXT,
      accion TEXT PRIMARY KEY,
      fecha_scraping TEXT,
      ficha_id INTEGER
  )
  ```

#### SEA (Servicio de Evaluación Ambiental)

- **`pertinencias`**:
  ```sql
  CREATE TABLE pertinencias (
      Expediente TEXT PRIMARY KEY,
      Nombre_de_Proyecto TEXT,
      Proponente TEXT,
      Fecha TEXT,
      Estado TEXT,
      Accion TEXT,
      fecha_scraping TIMESTAMP,
      tipo_proyecto TEXT,
      categoria_economica TEXT
  )
  ```
- **`sea_proyectos_evaluados`**:
  ```sql
  CREATE TABLE sea_proyectos_evaluados (
      id TEXT PRIMARY KEY,
      nombre TEXT,
      titular TEXT,
      via_ingreso TEXT,
      estado_proyecto TEXT,
      razon_ingreso TEXT,
      fecha_presentacion TEXT,
      subestado_proyecto TEXT,
      categoria_economica TEXT,
      url TEXT,
      fecha_scraping TIMESTAMP,
      region TEXT,
      tipo_proyecto TEXT
  )
  ```

#### Otros Organismos

- **`minsal_vigentes`**: Consultas públicas de Salud.
- **`mma_abiertas` / `mma_cerradas`**: Consultas del Ministerio del Medio Ambiente.
- **`dga_consultas`**: Consultas de la Dirección General de Aguas.

### Soporte Técnico

- **`scraper_logs`**: Registro histórico de ejecuciones de cada scraper.
- **`bug_reports`**: Reportes de errores enviados por los usuarios.

## 6. Flujo de Trabajo Típico

1. `scheduler.py` dispara un scraper en `src/scrapers/`.
2. El scraper usa `Playwright` para obtener datos y los guarda vía `DatabaseManager`.
3. Al finalizar, el backend emite un evento SSE.
4. El frontend recibe el evento y actualiza los indicadores visuales (puntos rojos en Sidebar).
5. El usuario accede a la categoría, ve los ítems marcados como "Nuevos" y al salir se actualiza su timestamp de vista.
