# BioNews - Inteligencia Medioambiental

**BioNews** es una plataforma avanzada de monitoreo y vigilancia medioambiental diseñada para centralizar, procesar y analizar información crítica proveniente de diversas fuentes gubernamentales y judiciales en Chile. 

A diferencia de los newsletters estáticos tradicionales, BioNews ofrece una interfaz interactiva y en tiempo real para la toma de decisiones estratégicas.

## Características Principales

### 1. Monitoreo Multi-Fuente (Scraping Inteligente)
El sistema utiliza un motor basado en **Playwright** y **BeautifulSoup** para extraer datos de:
* **SEA (Servicio de Evaluación Ambiental):** Seguimiento de Pertinencias y expedientes legales.
* **Tribunales Ambientales:** Extracción de causas y noticias del Primer, Segundo y Tercer Tribunal.
* **Instituciones Clave:** SMA (Superintendencia), MMA (Ministerio), SBAP, Sernageomin y Diario Oficial.

### 2. Gestión de Datos y Persistencia
* **Base de Datos Local:** Almacenamiento eficiente en SQLite para acceso rápido e histórico de noticias y procesos.
* **Normalización de Fechas:** Algoritmos de parsing para estandarizar formatos de fecha heterogéneos de diferentes sitios web.

### 3. Interfaz de Usuario (UI)
* Desarrollado con **Flet (Flutter for Python)**, proporcionando una experiencia fluida, moderna y con soporte para modo claro/oscuro.
* Sistema de filtros dinámicos por fuente y palabras clave.

### 4. Seguridad y Portabilidad
* **Certificación SSL:** Implementación de `certifi` para asegurar conexiones HTTPS confiables en cualquier entorno corporativo.
* **Arquitectura Portable:** Empaquetado optimizado que incluye su propio motor de navegación (Chromium) sin requerir instalaciones previas en el sistema del cliente.

## Requisitos Técnicos

* **Lenguaje:** Python 3.12+
* **Librerías Core:** `flet`, `playwright`, `beautifulsoup4`, `certifi`, `python-dotenv`.
* **Infraestructura:** Navegador Chromium integrado en la carpeta `pw-browser`.
## Estructura

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

## Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/maruzs/BioNews.git](https://github.com/maruzs/BioNews.git)
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configurar Navegadores:**
    ```bash
    playwright install chromium
    ```
4.  **Ejecutar la aplicación:**
    ```bash
    python src/main.py
    ```

## Información de Copyright

**Desarrollador:** Maruzs
**Versión:** 1.2.1  
**Estado:** Estable / En desarrollo activo de funciones de seguimiento e IA.

---
*BioNews - Transformando el cumplimiento ambiental en una ventaja competitiva.*