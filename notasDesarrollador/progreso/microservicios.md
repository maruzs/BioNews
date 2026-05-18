# Propuesta de Arquitectura: BioNews SaaS (Microservicios)

Este documento resume la estrategia para transformar BioNews de una arquitectura monolítica a una arquitectura de microservicios escalable, ideal para un cluster de laptops y un modelo de negocio SaaS.

## 1. Descomposición de Microservicios

Para un SaaS, lo ideal es separar las responsabilidades para que si un scraper falla, la web siga funcionando, y si el sistema de pagos se cae, las noticias se sigan recolectando.

| Microservicio            | Responsabilidad                                                                             | Tecnología sugerida               |
| :----------------------- | :------------------------------------------------------------------------------------------ | :-------------------------------- |
| **Auth Service**         | Gestión de usuarios, Login (JWT), Registro, Roles y Permisos.                               | FastAPI / Node.js                 |
| **Scraper Engine**       | Orquestación de crawlers. Puede subdividirse en "workers" que corren en diferentes laptops. | Python (Playwright/BeautifulSoup) |
| **Notification Service** | Envío de Emails (SendGrid/Mailgun), Newsletters, Alertas Push y SSE.                        | Go o Node.js                      |
| **Billing Service**      | Gestión de suscripciones, integración con pasarelas de pago (Stripe/Webpay).                | Node.js / Python                  |
| **Search/Data API**      | Servicio optimizado para consultas rápidas y filtrado de grandes volúmenes de datos.        | FastAPI + PostgreSQL              |

## 2. Estrategia de Base de Datos

### ¿Por qué migrar de SQLite?

SQLite es excelente para proyectos locales, pero tiene limitaciones críticas para un SaaS:

- **Bloqueos de Escritura**: Solo un proceso puede escribir a la vez.
- **Distribución**: No puedes acceder al mismo archivo `.db` fácilmente desde dos laptops distintas en un cluster (sin usar sistemas de archivos complejos).

### Propuesta: PostgreSQL

- **Multi-tenant**: Puedes manejar esquemas separados para usuarios Pro y gratuitos.
- **JSONB**: Ideal para guardar datos de scraping que cambian de estructura frecuentemente sin migrar tablas.
- **Escalabilidad**: Soporta miles de conexiones concurrentes.

## 3. Mejoras Arquitectónicas Sugeridas

1. **Message Broker (Redis/RabbitMQ)**:
   - En lugar de que el Scraper llame a la DB directamente, envía un mensaje: _"Encontré nueva normativa"_.
   - El **Notification Service** escucha ese mensaje y envía el correo automáticamente.
   - Esto hace que el sistema sea "Event-Driven" (basado en eventos).

2. **Object Storage (MinIO)**:
   - En lugar de guardar los screenshots de bugs o documentos en una carpeta `/uploads`, usa **MinIO** (un S3 local que puedes instalar en tu cluster). Así los archivos están disponibles para todos los nodos.

3. **CI/CD Pipeline**:
   - **GitHub Actions**: Al hacer `push`, que se construyan las imágenes de Docker.
   - **Watchtower** o un script de despliegue: Que actualice los contenedores en tu cluster automáticamente.

4. **API Gateway Dedicado**:
   - Seguir usando NPM es bueno para el tráfico HTTP, pero considera **Traefik** si decides profundizar en Swarm, ya que se autoconfigura al detectar nuevos contenedores.

## 4. Próximos Pasos (SaaS Roadmap)

1. **Dominio Propio**: Configurar Cloudflare (Tunnels con nombre) para apuntar a `api.bionews.cl` y `app.bionews.cl`.
2. **Sistema de Pagos**: Implementar Webhooks para que cuando un usuario pague, se le active el flag `is_pro` en el Auth Service.
3. **App Móvil**: Crear una API REST limpia (la actual está bien encaminada) para que Flutter o React Native consuman los mismos datos.

---
