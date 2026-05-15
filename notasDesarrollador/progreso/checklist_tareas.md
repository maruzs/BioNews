# Checklist de Implementación BioNews

Lista de tareas técnicas pendientes por categoría.

## 🗄️ Base de Datos y Backend

- [ ] Instalar PostgreSQL en Docker.
- [ ] Script de migración SQLite -> PostgreSQL.
- [ ] Implementar `SQLAlchemy` o `Tortoise ORM` para facilitar la gestión de microservicios.
- [ ] Crear servicio de correo (SMTP) con una cuenta de BioNews.

## 👤 Usuarios y Seguridad

- [ ] Endpoint de `/register` con envío de código de verificación.
- [ ] Sistema de Roles en JWT (`admin`, `pro`, `user`).
- [ ] Middleware para restringir acceso a ciertas tablas si el usuario no es `pro`.

## 🕷️ Scraping Avanzado

- [ ] Nuevo Scraper: Detalle de ficha de favoritos (extraer documentos adjuntos y texto completo).
- [ ] Comparador de cambios: Sistema que guarde "hashes" del contenido para detectar si una ficha favorita cambió.

## 💳 Negocio (SaaS)

- [ ] Diseño de tabla `subscriptions` (user_id, plan, status, expires_at).
- [ ] Integración de Checkout UI.
- [ ] Panel de administración para ver ingresos y usuarios activos.

## 🚀 Infraestructura (Cluster)

- [ ] Inicializar Docker Swarm en laptop Asus.
- [ ] Unir laptop HP como worker.
- [ ] Instalar `Portainer` para gestionar el cluster visualmente.
- [ ] Configurar `Healthchecks` avanzados en el docker-compose.

## 📱 Frontend y Mobile

- [ ] Rediseño de la Landing Page (Vender los beneficios del servicio).
- [ ] Implementar modo oscuro/claro persistente.
- [ ] Prototipo básico en Flutter para leer noticias.
