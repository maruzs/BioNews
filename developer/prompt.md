# Prompt de Contexto para IA: Proyecto BioNews

**Contexto del Proyecto:**
BioNews es una aplicación de escritorio desarrollada en **Python 3.12** diseñada para el monitoreo de inteligencia medioambiental en Chile. El software centraliza noticias y procesos legales de múltiples fuentes gubernamentales.

**Arquitectura Técnica:**
1.  **Interfaz (UI):** Desarrollada con **Flet 0.84.0**, operando bajo el modelo de `ft.run(main, assets_dir="assets")`.
2.  **Motor de Extracción (Scraping):** * Utiliza **Playwright 1.58.0** para la navegación y **BeautifulSoup4** para el parsing de HTML.
    * Posee un `ScrapingEngine` que gestiona las rutas de los binarios de Chromium de forma dinámica.
    * Los scrapers legales (como `sea_legal.py`) manejan flujos complejos: login, intercepción de respuestas API JSON y navegación interactiva.
3.  **Persistencia:** Base de datos **SQLite** (`data/bionews.db`) gestionada por un `DatabaseManager`.
4.  **Despliegue y Portabilidad:** * Empaquetado con **PyInstaller** usando un archivo `.spec` personalizado.
    * Incluye un bundle de navegadores en la carpeta `pw-browser`.
    * **Configuración Crítica:** El software redirige globalmente a Playwright para buscar navegadores en `_internal/playwright/driver/package/.local-browsers` mediante la inyección en el `.spec` y variables de entorno en `main.py`.
    * **Seguridad:** Implementa `certifi` para la validación de certificados SSL en entornos corporativos.

**Lógica de los Scrapers:**
* **SBAP:** Extrae fechas de noticias directamente desde la estructura de la URL (`/detalle/YYYY/MM/DD/`) para evitar errores de formato en el HTML.
* **Tercer Tribunal:** Prioriza la extracción del atributo `datetime` de la etiqueta `<time>` para obtener fechas precisas de publicación.
* **SEA Legal:** Realiza un login automatizado y consume datos de la API interna del portal de pertinencias.

**Instrucción para la IA:**
Analiza el repositorio `https://github.com/maruzs/BioNews.git` considerando esta arquitectura. Tu objetivo es ayudar en el desarrollo de nuevas funciones (como el sistema de seguimiento de favoritos para pertinencias) y optimizaciones de rendimiento, respetando siempre las reglas de estilo de no utilizar tildes ni emojis en comentarios o prints de consola.

## ESTRUCTURA PROYECTO
# Estructura
BioNews/
├── analisis/               # Documentacion y reportes de investigacion (ya existente)
├── assets/                 # Iconos, logos e imagenes de la app
├── data/                   # Almacenamiento de la base de datos SQLite
├── pw-browser/             # Buscadores de playwright
├── src/                    # Codigo fuente principal
│   ├── main.py             # Punto de entrada (inicializa la app Flet)
│   ├── database/           # Gestion de persistencia
│   │   ├── __init__.py
│   │   └── manager.py      # Operaciones CRUD para noticias y casos legales
│   ├── scrapers/           # Motores de extraccion (Playwright + BS4)
│   │   ├── __init__.py
│   │   ├── corteSuprema.py # Noticias
│   │   ├── diario_oficial.py # Noticias
│   │   ├── fiscalizaciones.py # Legal (SNIFA)
│   │   ├── mma.py          # Noticias
│   │   ├── primerTribunal.py  # Causas
│   │   ├── reqSEIA.py      # Legal SNIFA
│   │   ├── sbap.py         # Noticias
│   │   ├── sea_legal.py    # Legal (Pertinencias)
│   │   ├── segundoTribunal.py # Legal (Causas)
│   │   ├── sernageomin.py  # Noticias
│   │   ├── sma.py          # Noticias
│   │   ├── snifa.py        # Legal (Sancionatorios SNIFA)
│   │   ├── tercerTribunal.py # Legal (Causas)
│   │   ├── tribunal2.py    # Noticias
│   │   ├── tribunal3.py    # Noticias
│   │   ├── engine.py       # Logica base y manejo de navegadores headless
│   │   ├── sea.py          # Scraper especifico para SEA
│   │   └── snifa.py        # Scraper especifico para SNIFA
│   ├── ui/                 # Componentes de la interfaz de usuario
│   │   ├── __init__.py
│   │   ├── dashboard.py    # Vista de la tabla principal
│   │   ├── legal.py        # Vista de apartado legal (Categorizado por fuente)
│   │   ├── main_window.py  # Vista principal (IMPORTANTE)
│   │   ├── sync.py         # Sincronizacion de scrapeo y muestra 
│   │   ├── news.py         # Vista de tarjetas de noticias
│   │   ├── settings.py     # Vista de configuracion por pagina
│   │   └── styles.py       # Definicion de colores "ecologicos" y temas
│   └── utils/              # Funciones auxiliares (formateo de fechas, logs)
├── .env 
├── startScraping.py        # Funcion principal que inicia el scrapeo
├── .gitignore              # Archivos a ignorar (venv, __pycache__, .db)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Instrucciones de instalacion y uso
