# Roadmap BioNews SaaS: De Monolito a Plataforma Global

Este plan divide la evolución del proyecto en fases incrementales para asegurar la estabilidad mientras se añaden funciones de negocio.

## Fase 1: Cimientos y Confiabilidad (Corto Plazo)

El objetivo es profesionalizar el backend y asegurar los datos antes de crecer.

- [ ] **Migración a PostgreSQL**: Configurar contenedor de Postgres y migrar tablas de SQLite.
- [ ] **Refactorización de Auth**:
  - Implementar flujo de confirmación de email (SMTP).
  - Recuperación de contraseña mediante tokens temporales.
- [ ] **Mejora del Home**: Dashboard con métricas clave (Total de nuevas normativas hoy, alertas críticas, etc.).

## Fase 2: Monetización y SaaS Core (Medio Plazo)

Preparar la plataforma para recibir pagos y tener una identidad propia.

- [ ] **Dominio y SSL**: Comprar dominio `.cl` o `.com` y configurar Cloudflare Tunnel permanente.
- [ ] **Integración de Pagos**:
  - Implementar Stripe o Webpay (vía Flow).
  - Creación de planes (Free vs Pro).
  - Webhooks para activar suscripciones automáticamente.
- [ ] **Sistema de Favoritos Inteligente**: Crawling automático de fichas técnicas solo para los documentos marcados como favoritos.

## Fase 3: Comunicación y Engagement

Mantener a los usuarios informados fuera de la plataforma.

- [ ] **Servicio de Newsletters**: Envío semanal/diario automatizado de las noticias más relevantes según preferencias del usuario.
- [ ] **Notificaciones en Tiempo Real**: Mejorar el sistema SSE para alertas críticas en el navegador.

## Fase 4: Escalabilidad y DevOps

Aprovechar tu cluster de laptops y automatizar el trabajo aburrido.

- [ ] **Microservicios**: Separar el motor de Scraping del servidor de la API.
- [ ] **CI/CD Pipeline**: Configurar GitHub Actions para que al hacer `git push`, tu cluster descargue la nueva versión automáticamente.
- [ ] **Docker Swarm**: Activar el cluster para que BioNews corra en ambas laptops simultáneamente (Alta disponibilidad).

## Fase 5: Expansión Multiplataforma

Llevar BioNews al bolsillo de los usuarios.

- [ ] **API Mobile Ready**: Asegurar que todos los endpoints devuelven JSON estandarizado.
- [ ] **App Móvil (iOS/Android)**: Desarrollo con Flutter o React Native para notificaciones push nativas.
