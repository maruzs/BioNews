Prompt 5: Fase 5 — Integración SSE con Redis y Despliegue en Docker Compose

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
