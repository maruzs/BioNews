# Explicación del Funcionamiento del Proyecto BioNews

Este documento detalla la arquitectura técnica, el flujo de datos y la interacción entre los distintos componentes del proyecto.

## 1. Arquitectura General

El proyecto se basa en una arquitectura de **Cliente-Servidor** con procesos de automatización en segundo plano:

- **Frontend**: Aplicación web desarrollada en React (ubicada en `/web`).
- **Backend (API)**: Servidor FastAPI en Python (`server.py`) que gestiona la lógica de negocio, autenticación y acceso a datos.
- **Base de Datos**: SQLite (`data/data.db`), centralizando toda la información recolectada y de usuarios.
- **Automatización (Scheduler)**: Proceso independiente (`scheduler.py`) encargado de ejecutar los scrapers de forma programada.

---

## 2. Flujo de Datos y Scrapeo

El corazón del proyecto es la recolección automática de datos desde diversas fuentes institucionales.

### Recolección (Scrapers)

Ubicados en `src/scrapers/`, existen dos tipos de scrapers:

1.  **Scrapers de Noticias**: Recolectan artículos de prensa de sitios como MMA, SEA, SMA, Sernageomin y Tribunales Ambientales.
2.  **Scrapers de Datos Estructurales**: Extraen registros detallados de:
    - **SNIFA**: Fiscalizaciones, Sancionatorios, Medidas Provisionales, Programas de Cumplimiento, etc.
    - **SEA**: Pertinencias de ingreso al SEIA.
    - **Tribunales Ambientales**: Causas legales de los tres tribunales del país.
    - **Diario Oficial**: Nuevas normativas y reglamentos.

### Almacenamiento

Cada scraper procesa la información y la envía al `DatabaseManager` (`src/database/manager.py`), el cual:

- Realiza una **deduplicación** basada en claves únicas (como el número de expediente o el link de la noticia).
- Guarda los registros en sus respectivas tablas.
- Registra el resultado de la ejecución en la tabla `scraper_logs` (éxito, errores, cantidad de nuevos registros).

---

## 3. Automatización (El Scheduler)

El archivo `scheduler.py` funciona como un demonio (proceso continuo):

1.  **Configuración Dinámica**: Lee `data/scheduler.json` para conocer las horas y frecuencias de ejecución.
2.  **Ejecución Programada**: Utiliza la librería `schedule` para disparar los scrapers en los intervalos definidos.
3.  **Control de Horario**: Muchos scrapers solo corren en horario hábil (ej. 07:00 a 19:00) para optimizar recursos.
4.  **Recarga en Caliente**: Si un administrador cambia la configuración desde la web, el scheduler detecta el cambio en el JSON y se reconfigura automáticamente sin reiniciarse.

---

## 4. Comunicación en Tiempo Real (WebSockets)

Para que el usuario vea notificaciones sin refrescar la página:

- Cuando un scraper (vía `server.py` o disparado manualmente) detecta nuevos registros, el servidor emite un mensaje a través de un **WebSocket**.
- El frontend escucha estos mensajes y actualiza los indicadores visuales (puntos rojos) en la barra lateral.

---

## 5. Sistema de Notificaciones y "Vistos"

El sistema rastrea qué ha visto cada usuario de forma individual:

- **Salida de Categoría**: Cuando un usuario sale de una sección (ej. "Fiscalizaciones"), el sistema guarda el timestamp actual en `user_category_views`.
- **Identificación de "Nuevo"**: Un ítem se considera nuevo si su fecha de recolección es posterior a la última vez que el usuario visitó esa categoría.
- **Marcado Individual**: Los usuarios pueden hacer clic en un ítem para marcarlo como "visto", lo que lo elimina del estado "nuevo" incluso si la fecha es reciente.
- **Indicadores**: La API calcula dinámicamente el flag `is_new` para cada registro basándose en esta lógica.

---

## 6. Autenticación y Seguridad

- **JWT (JSON Web Tokens)**: El sistema utiliza tokens para validar las sesiones. Los tokens expiran y deben ser incluidos en cada petición al backend.
- **Roles**: Existen roles de `user` y `admin`.
  - Los **Admins** pueden gestionar usuarios, bloquear cuentas y configurar el scheduler.
- **Criptografía**: Las contraseñas se almacenan cifradas usando `bcrypt`.

---

## 7. Despliegue y Entorno

El proyecto está diseñado para ejecutarse en contenedores **Docker**:

- `docker-compose.yml` orquestra el contenedor del backend y asegura que la base de datos persista en un volumen.
- El entorno utiliza variables definidas en `.env` para configuraciones sensibles.
