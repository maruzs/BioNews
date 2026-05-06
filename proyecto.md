# Proyecto BioNews: Inteligencia y Vigilancia Medioambiental

## 1. Descripción del Proyecto

**BioNews** es una plataforma avanzada de monitoreo y vigilancia medioambiental diseñada para centralizar, procesar y analizar información crítica proveniente de diversas fuentes gubernamentales y judiciales en Chile.

El objetivo principal es transformar el flujo constante de datos públicos en información accionable para la toma de decisiones estratégicas. A diferencia de un sistema de noticias convencional, BioNews actúa como un centro de inteligencia que rastrea cambios normativos, procesos sancionatorios y noticias judiciales en tiempo real, ofreciendo una experiencia personalizada para cada usuario.

## 2. Cómo Funciona

El sistema opera en un ciclo continuo de cuatro etapas:

1.  **Extracción (Scraping):** Un motor automatizado utiliza **Playwright** y **BeautifulSoup** para navegar y extraer datos de fuentes como la SMA (Superintendencia del Medio Ambiente), el SEA (Servicio de Evaluación Ambiental), Tribunales Ambientales y el Diario Oficial.
2.  **Procesamiento:** Los datos extraídos son normalizados (estandarización de fechas, limpieza de texto y categorización) y se almacenan en una base de datos centralizada.
3.  **Notificación Inteligente:** El sistema detecta nuevos registros y marca "puntos rojos" en la interfaz del usuario. Gracias a un sistema de seguimiento por usuario, la plataforma sabe qué ítems han sido vistos por quién, manteniendo la sincronización entre diferentes dispositivos (Cross-Device).
4.  **Visualización:** Los usuarios acceden a un portal web moderno donde pueden filtrar, buscar y analizar la información mediante tablas interactivas (DataGrids) y paneles de control.

## 3. Tecnologías Utilizadas

### Backend

- **Lenguaje:** Python 3.12+
- **Framework API:** FastAPI (Asíncrono y de alto rendimiento).
- **Base de Datos:** SQLite con SQLAlchemy (ORM) para la persistencia.
- **Seguridad:** Autenticación basada en JWT (JSON Web Tokens) y cifrado de contraseñas con Passlib.
- **Comunicación:** WebSockets para actualizaciones en tiempo real de notificaciones.

### Frontend

- **Framework:** React 18+ con Vite.
- **Lenguaje:** TypeScript para un desarrollo robusto y tipado.
- **Interfaz de Usuario:** Material UI (MUI) para componentes premium y responsivos.
- **Iconografía:** Lucide React.
- **Estado:** Context API para la gestión de autenticación y notificaciones.

### Scrapers y Automatización

- **Playwright:** Para interactuar con sitios web modernos que requieren ejecución de JavaScript.
- **BeautifulSoup4 / Requests:** Para scraping eficiente de sitios estáticos.
- **Scheduler:** Script dedicado para la programación de tareas de extracción periódicas.

### Despliegue e Infraestructura

- **Contenedores:** Docker y Docker Compose para orquestar los servicios de backend, frontend y base de datos.
- **Servidor Web:** Nginx como proxy inverso y servidor de archivos estáticos.

## 4. Estructura Completa del Proyecto

A continuación se detalla la jerarquía completa de archivos y directorios:

```text
BioNews/
├── data/                       # Almacenamiento persistente
│   └── data.db                 # Base de datos SQLite principal
├── src/                        # Lógica de Backend y Scrapers
│   ├── database/               # Gestión de base de datos
│   │   ├── __init__.py
│   │   └── manager.py          # Lógica CRUD y conexión
│   ├── scrapers/               # Motores de extracción de datos
│   │   ├── __init__.py
│   │   ├── corteSuprema.py
│   │   ├── diario_oficial.py
│   │   ├── engine.py           # Clase base para scrapers
│   │   ├── fiscalizaciones.py
│   │   ├── medidas.py
│   │   ├── mma.py
│   │   ├── pdc.py
│   │   ├── primerTribunal.py
│   │   ├── reqSEIA.py
│   │   ├── sanciones.py
│   │   ├── sbap.py
│   │   ├── sea.py
│   │   ├── sea_legal.py
│   │   ├── segundoTribunal.py
│   │   ├── sernageomin.py
│   │   ├── sma.py
│   │   ├── snifa.py
│   │   ├── tercerTribunal.py
│   │   ├── tribunal2.py
│   │   └── tribunal3.py
│   ├── utils/                  # Herramientas de apoyo
│       └── date_parser.py      # Normalización de formatos de fecha
├── web/                        # Aplicación Frontend (React)
│   ├── src/
│   │   ├── components/         # Componentes y Páginas de la App
│   │   │   ├── AdminPanel.tsx
│   │   │   ├── DashboardView.tsx
│   │   │   ├── Home.tsx
│   │   │   ├── Landing.tsx
│   │   │   ├── Login.tsx
│   │   │   ├── NewsPage.tsx
│   │   │   ├── Profile.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── ReportLayout.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── context/
│   │   │   └── AuthContext.tsx # Manejo de sesión y JWT
│   │   ├── assets/             # Recursos estáticos del frontend
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── index.css           # Estilos globales
│   │   └── main.tsx            # Punto de entrada de React
│   ├── Dockerfile              # Docker para el frontend
│   ├── nginx.conf              # Configuración de Nginx
│   ├── package.json            # Dependencias de Node.js
│   ├── tsconfig.json           # Configuración de TypeScript
│   └── vite.config.ts          # Configuración de Vite
├── .dockerignore
├── .env                        # Variables de entorno (claves, puertos)
├── .gitignore
├── docker-compose.yml          # Orquestación de contenedores
├── Dockerfile                  # Docker para el backend
├── logo_sernageomin.png
├── requirements.txt            # Dependencias de Python
├── scheduler.py                # Servicio de tareas programadas
├── server.py                   # API principal (FastAPI)
├── startScraping.py            # Ejecución manual de scrapers
└── proyecto.md                 # Este documento
```

---

**BioNews** - _Transformando el cumplimiento ambiental en una ventaja competitiva._
