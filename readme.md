# Proyecto BioNews: Inteligencia y Vigilancia Medioambiental

## 1. Descripción del Proyecto

**BioNews** es una plataforma web avanzada de monitoreo, vigilancia e inteligencia medioambiental diseñada para centralizar, procesar y analizar información crítica proveniente de diversas fuentes gubernamentales y judiciales en Chile.

El sistema actúa como un centro de inteligencia que rastrea cambios normativos, procesos sancionatorios, fiscalizaciones, solicitudes de proyectos del SEIA y noticias judiciales en tiempo real. A través de perfiles de usuario, ofrece notificaciones inteligentes personalizadas ("puntos rojos") que informan de forma granular qué registros son nuevos para cada usuario específico.

---

## 2. Arquitectura y Funcionamiento

El sistema opera en un ciclo continuo compuesto por:

1.  **Extracción (Scraping):** Procesos automatizados en segundo plano que extraen datos de múltiples fuentes (SMA, SEA, Tribunales Ambientales, DGA, Diario Oficial, etc.) utilizando **BeautifulSoup4**, **Requests** y **Playwright**.
2.  **Procesamiento y Almacenamiento:** Los registros se normalizan y almacenan en una base de datos centralizada de **PostgreSQL 16**, dividida lógicamente en esquemas (`users` para la gestión interna de cuentas, y `scrapers` para la información recolectada).
3.  **Notificación en Tiempo Real (SSE):** Utiliza **Server-Sent Events (SSE)** para comunicar instantáneamente al frontend la llegada de nuevos registros. Los usuarios mantienen su estado de lectura sincronizado entre dispositivos (Cross-Device).
4.  **Caché Avanzada (Redis):** Se implementa una capa de caché en Redis para acelerar las consultas pesadas de tablas dinámicas (2m de TTL) y estáticas (5m de TTL), con invalidación automática basada en patrones cuando ingresa nuevo contenido.

---

## 3. Stack Tecnológico

### Backend
- **Lenguaje:** Python 3.11+
- **API Framework:** FastAPI (asíncrono, alto rendimiento)
- **Base de Datos:** PostgreSQL 16 (organizado por esquemas lógicos)
- **Caché y Mensajería:** Redis (cache de queries, invalidación por patrones, blacklist de JWTs)
- **Seguridad:** 
  - Autenticación JWT con identificadores únicos (`jti`) para soporte de revocación.
  - Cifrado de contraseñas con `bcrypt`.
  - Rate limiting en endpoints sensibles (ej. login) mediante `slowapi`.

### Frontend
- **Framework:** React 18+ (Vite)
- **Lenguaje:** TypeScript (código robusto y tipado)
- **Biblioteca UI:** Material UI (MUI) con diseño premium adaptado (Glassmorphism, Dark/Light modes)
- **Iconografía:** Lucide React

---

## 4. Estructura del Proyecto

```text
BioNews/
├── src/                        # Lógica Backend (FastAPI + Scrapers)
│   ├── database/               # Conectores y gestor de DB
│   │   ├── connection.py       # Pool de conexiones (PostgreSQL)
│   │   ├── manager.py          # Consultas, inserciones y lógica de lectura/vista
│   │   ├── schema_users.sql    # Inicialización del esquema de usuarios
│   │   └── schema_scrapers.sql # Inicialización del esquema de scrapers
│   ├── scrapers/               # Scripts individuales de scraping
│   │   ├── engine.py           # Clase base (ScrapingEngine) con soporte para Playwright
│   │   ├── sea_evaluados.py    # Proyectos evaluados del SEA (Paginación optimizada)
│   │   ├── scraper_dga.py      # Scraper DGA (Página de inicio y noticias recientes)
│   │   ├── tercerTribunal.py   # Scraper del Tercer Tribunal Ambiental
│   │   └── ...                 # Otros scrapers (SMA, MMA, Tribunales, etc.)
│   └── utils/                  # Utilidades comunes (date parser, normalizadores)
├── web/                        # Aplicación Frontend (React + TS)
│   ├── src/
│   │   ├── components/         # Vistas de la aplicación (Dashboard, Sidebar, etc.)
│   │   ├── context/            # AuthContext y notificaciones
│   │   ├── App.tsx             # Enrutamiento y estructura global
│   │   └── index.css           # Configuración del diseño visual
│   ├── public/                 # Archivos estáticos del cliente
│   └── Dockerfile              # Dockerfile para servir el build del frontend con Nginx
├── docker-compose.yml          # Orquestación de toda la infraestructura
├── Dockerfile                  # Dockerfile del Backend API
├── scheduler.py                # Servicio para la ejecución periódica de scrapers
├── server.py                   # Servidor de API (FastAPI)
├── requirements.txt            # Dependencias de Python locales
└── requirements.docker.txt     # Dependencias de Python optimizadas para el contenedor
```

---

## 5. Esquema de Base de Datos Principal (PostgreSQL 16)

La base de datos se estructura en dos esquemas principales para garantizar el aislamiento y la organización del almacenamiento:

### Esquema `users`
- **`users`**: Almacena información de cuentas, contraseña cifrada, rol (admin/user), estado de bloqueo (`blocked`) y preferencias en JSON.
- **`favoritos`**: Guarda los ítems guardados por los usuarios para rápido acceso.
- **`user_item_views`**: Registra qué ítems individuales han sido vistos por cada usuario.
- **`user_category_views`**: Registra la marca de tiempo de la última vez que un usuario visitó una sección para calcular la presencia de "puntos rojos" (notificaciones).
- **`bug_reports`**: Almacena reportes de fallos enviados por los usuarios y la ruta física a su captura de pantalla.

### Esquema `scrapers`
- **`noticias`**: Noticias generales de fuentes del sector.
- **`pertinencias`**: Consultas de pertinencia al SEA.
- **`sea_proyectos_evaluados`**: Proyectos evaluados ingresados al SEIA.
- **`normativas`**: Leyes, decretos y normativas publicadas en el Diario Oficial.
- **`fiscalizaciones`**: Registros de fiscalizaciones ambientales del SNIFA.
- **`medidas_provisionales`**: Medidas de corrección provisionales del SNIFA.
- **`Tribunales`**: Causas presentadas en los distintos tribunales ambientales.
- **`scraper_logs`**: Tiempos de ejecución, registros obtenidos y errores ocurridos en las ejecuciones de scrapers.

---

## 6. Despliegue y Configuración

El proyecto está completamente preparado para desplegarse mediante Docker Compose en cualquier servidor Linux (compatible con proxies inversos como Nginx Proxy Manager).

### Paso 1: Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto basado en las siguientes variables obligatorias:
```env
# Configuración Base de Datos
DB_NAME=bionews
DB_USER=bionews
DB_PASS=tu_password_segura

# Configuración Redis
REDIS_PASSWORD=RedisPasswordSegura

# Backend API
JWT_SECRET_KEY=ClaveSecretaSuperSeguraJWT
```

### Paso 2: Levantar la Infraestructura
Ejecuta el siguiente comando para compilar las imágenes e iniciar todos los contenedores en segundo plano:
```bash
docker compose up -d --build
```

Esto desplegará los siguientes servicios:
1.  `postgres-db` (`bionews-db`): Servidor PostgreSQL (Puerto 5432 expuesto únicamente a localhost).
2.  `redis` (`bionews-redis`): Caché de datos y blacklist de JWTs.
3.  `api` (`bionews-api`): API FastAPI corriendo en el puerto interno 8000.
4.  `scheduler` (`bionews-scheduler`): Servicio ejecutor de scrapings programados.
5.  `web` (`bionews-web`): Frontend React compilado y servido a través de Nginx.

### Paso 3: Aplicar Cambios en Caliente
Si realizas modificaciones en los archivos de la API o del Scheduler, puedes reiniciar los servicios correspondientes para que tomen los cambios:
```bash
docker compose restart api scheduler
```

---

**BioNews** - _Inteligencia y cumplimiento ambiental consolidado._
