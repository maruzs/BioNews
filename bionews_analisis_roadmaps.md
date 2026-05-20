# BioNews — Análisis Técnico y Roadmaps

---

## 1. 🔐 Análisis de Vulnerabilidades de Seguridad

### 🔴 CRÍTICO

#### 1.1 Secret Key hardcodeada en `server.py`
```python
# server.py:107
SECRET_KEY = "bionews_super_secret_key_change_in_prod"
```
**Riesgo:** Si el código fuente se filtra (GitHub, etc.), cualquiera puede generar JWTs válidos y autenticarse como admin.  
**Fix:** Moverlo a variable de entorno.
```python
SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("JWT_SECRET_KEY no configurado")
```

#### 1.2 Contraseña del admin por defecto hardcodeada
```python
# server.py:119-120
hashed_pw = hash_password("#81680085pls")
db.create_user("Administrador", "administrador@bionews.cl", hashed_pw, role="admin")
```
**Riesgo:** Credenciales de producción en código fuente.  
**Fix:** Leer desde variable de entorno `ADMIN_PASSWORD`.

#### 1.3 CORS completamente abierto
```python
# server.py:44
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
```
**Riesgo:** Cualquier origen puede hacer requests autenticados. Especialmente relevante si se usa algún día con cookies.  
**Fix:** Restringir a los dominios de la app (IP Tailscale + dominio producción).

#### 1.4 Puerto PostgreSQL expuesto en Docker
```yaml
# docker-compose.yml:15-16
ports:
  - "5432:5432"
```
**Riesgo:** La BD es accesible desde internet directamente, no solo desde los contenedores internos.  
**Fix:** Quitar el mapeo de puerto o restringirlo a `127.0.0.1:5432:5432`. La comunicación interna funciona igual por la red `bionews-net`.

#### 1.5 Puerto Redis expuesto sin autenticación
```yaml
# docker-compose.yml:39-40
ports:
  - "6379:6379"
```
**Riesgo:** Redis accesible desde internet sin contraseña → lectura/escritura de cache, potencial RCE.  
**Fix:** Quitar el mapeo de puerto. Agregar `requirepass` en Redis.

---

### 🟠 ALTO

#### 1.6 Sin rate limiting en `/api/auth/login`
```python
# server.py:157-168
@app.post("/api/auth/login")
def login(req: LoginRequest):
    user = db.get_user_by_email(req.email)
```
**Riesgo:** Fuerza bruta ilimitada sobre contraseñas.  
**Fix:** Agregar `slowapi` o `fastapi-limiter` con límite de ~10 intentos/minuto por IP.

#### 1.7 Sin rate limiting en `/api/auth/register`
**Riesgo:** Spam masivo de cuentas.  
**Fix:** Mismo mecanismo. Además, con email de confirmación (ver roadmap 4) se mitiga.

#### 1.8 Sin validación de tipo/extensión en upload de screenshots
```python
# server.py:270
file_ext = screenshot.filename.split(".")[-1] if "." in screenshot.filename else "png"
```
**Riesgo:** Un atacante puede subir `shell.php` renombrado como `bug.php`. No hay validación de MIME type real.  
**Fix:**
```python
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
ALLOWED_MIMES = {"image/png", "image/jpeg", "image/gif", "image/webp"}

import magic  # python-magic
mime = magic.from_buffer(contents[:1024], mime=True)
if mime not in ALLOWED_MIMES or file_ext.lower() not in ALLOWED_EXTENSIONS:
    raise HTTPException(400, "Tipo de archivo no permitido")
```

#### 1.9 Path traversal potencial en `screenshot_path`
```python
# server.py:271
filename = f"bug_{...}_{user['sub']}.{file_ext}"
filepath = os.path.join(UPLOAD_DIR, filename)
```
Si `file_ext` contuviese `../`, podría escapar el directorio. Aunque `os.path.join` mitiga esto parcialmente, combinar con validación explícita.

#### 1.10 `/api/scrape/all` sin autenticación
```python
# server.py:807-810
@app.post("/api/scrape/all")
def scrape_all(background_tasks: BackgroundTasks):
    # SIN Depends(get_current_admin)!
```
**Riesgo:** Cualquier persona puede triggear scrapings masivos, causando DoS en los servidores externos o carga excesiva.  
**Fix:** Agregar `admin = Depends(get_current_admin)`.

---

### 🟡 MEDIO

#### 1.11 Tokens JWT sin invalidación
Los tokens duran 30 días (`timedelta(days=30)`) y no existe mecanismo de revocación. Si un token se filtra, el atacante tiene acceso por 30 días.  
**Fix:** Implementar un `jti` (JWT ID) en la DB y verificarlo en `get_current_user` para poder revocar tokens individuales.

#### 1.12 `get_current_user` no verifica el usuario contra la BD en cada request
```python
# server.py:124-141
def get_current_user(...):
    payload = jwt.decode(token, SECRET_KEY, ...)
    return payload  # Solo verifica firma JWT, no si el usuario existe/está bloqueado
```
Un usuario bloqueado puede seguir usando su token 30 días. Solo `/api/auth/me` hace la verificación completa.  
**Fix:** Añadir verificación de `blocked` en `get_current_user` (con cache Redis para no sobrecargar la BD).

#### 1.13 Información sensible en logs de errores
```python
# server.py:770-771
log.error(f"Error en {nombre}:\n{traceback.format_exc()}")
```
Los stack traces completos pueden exponer rutas internas, variables, etc. si los logs se exponen.  
**Fix:** En producción, loguear stack trace solo a archivo interno, nunca en respuestas HTTP.

#### 1.14 Validación débil en `update_preferences`
```python
# server.py:193-197
@app.put("/api/auth/preferences")
def update_preferences(req: dict, user = Depends(get_current_user)):
    prefs_str = json.dumps(req)  # Sin validación de tamaño ni esquema
```
Un usuario podría enviar un JSON de 10MB. Usar un modelo Pydantic con schema definido.

---

### 🟢 BAJO / RECOMENDACIONES

- **HTTPS**: Verificar que Nginx Proxy Manager tiene HTTPS forzado (HSTS).
- **Headers de seguridad**: Agregar `SecurityHeadersMiddleware` (CSP, X-Frame-Options, etc.).
- **Variables de entorno**: El `.env` con contraseñas debe estar en `.gitignore` (verificar).
- **Contraseña mínima**: No hay validación de fortaleza de contraseña en registro.
- **Audit log**: No hay registro de quién hizo qué en el panel admin.

---

## 2. ⚡ Análisis de Optimizaciones de Queries

### 🔴 Alto Impacto

#### 2.1 `get_table_data` carga todas las columnas sin limit eficiente
```python
# manager.py:133
cur.execute(f'SELECT * FROM "{table_name}" {order_by} LIMIT %s', (limit,))
```
El `limit=1000` por defecto trae todos los datos al servidor Python y luego al frontend. Para tablas con 49k+ registros (fiscalizaciones), esto es pesado.  
**Fix:** 
- Implementar paginación real server-side con `OFFSET` + `LIMIT` variables.
- El frontend actualmente recibe todo de una vez. Con paginación server-side se podría reducir a 25-50 registros por request.

#### 2.2 `get_table_data` hace un `SELECT column_name FROM information_schema.columns` en **cada request**
```python
# manager.py:99-103
cur.execute("""
    SELECT column_name FROM information_schema.columns
    WHERE table_name = %s ...
""", (table_name,))
```
Este query a `information_schema` es lento y se ejecuta en **cada request**. Con caché Redis ya existente, cachear el resultado del schema por tabla.  
**Fix:**
```python
schema_key = f"schema:{table_name}"
cached = cache.get(schema_key)
if not cached:
    # ejecutar query
    cache.set(schema_key, columns, ttl=3600)  # 1 hora
```

#### 2.3 `/api/options` carga 5000 filas para extraer distintos valores
```python
# server.py:503-507
normativas = db.get_table_data("normativas", limit=5000)
sma = db.get_table_data("fiscalizaciones", limit=5000)
orgs = list(set(n.get("organismo") for n in normativas if n.get("organismo")))
```
**Fix:** Usar `SELECT DISTINCT` directamente en PostgreSQL:
```sql
SELECT DISTINCT organismo FROM normativas WHERE organismo IS NOT NULL ORDER BY organismo
```

#### 2.4 `get_notification_status` hace hasta 14 queries independientes por usuario
```python
# manager.py:431-438
def get_notification_status(self, user_id):
    categories = ["noticias", "normativas", ...]  # 14 categorías
    return {cat: self._check_if_category_has_new(user_id, cat) for cat in categories}
```
Cada `_check_if_category_has_new` hace 2 queries (get_user_category_last_exit + SELECT 1 FROM tabla). Total: hasta **28 queries por poll**.  
**Fix:** Consolidar en una query con `UNION ALL` o cachear el resultado 60 segundos en Redis.

#### 2.5 `get_items_with_new_flag` hace comparación de fechas como strings en Python
```python
# manager.py:513-515
item_date_str = str(item_date)[:19]
item['is_new'] = item_date_str > last_exit_str
```
Esto funciona solo porque el formato ISO lo permite lexicográficamente. Es frágil y fuerza al servidor a cargar todos los items para comparar en Python.  
**Fix:** Delegar la comparación a PostgreSQL con `WHERE fecha_scraping > %s` directamente.

---

### 🟠 Medio Impacto

#### 2.6 Falta de índices probables en tablas de alta consulta

Las queries de ordenamiento en SNIFA usan `CAST(SUBSTRING(detalle_link FROM '/([0-9]+)$') AS INTEGER)` — un index funcional puede acelerar esto significativamente:
```sql
CREATE INDEX idx_fiscalizaciones_detalle_link 
ON fiscalizaciones ((CAST(SUBSTRING(detalle_link FROM '/([0-9]+)$') AS INTEGER)));

CREATE INDEX idx_fecha_scraping_fiscalizaciones ON fiscalizaciones (fecha_scraping DESC);
CREATE INDEX idx_fecha_scraping_normativas ON normativas (fecha_scraping DESC);
CREATE INDEX idx_user_category_views ON user_category_views (user_id, category_slug);
CREATE INDEX idx_user_item_views ON user_item_views (user_id, category_slug);
```

#### 2.7 Búsqueda global con `LOWER(campo) LIKE '%query%'` en 11 tablas secuencialmente
```python
# server.py:546-549
where_clauses = " OR ".join([f'LOWER("{f}") LIKE %s' for f in fields])
cursor.execute(f'SELECT * FROM "{table}" WHERE {where_clauses} LIMIT {LIMIT_PER_TABLE}', params)
```
`LIKE '%...%'` con wildcard inicial **no usa índices**. Para 11 tablas grandes, esto puede tardar segundos.  
**Fix a corto plazo:** `pg_trgm` con índices GIN:
```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX idx_fiscalizaciones_trgm ON fiscalizaciones 
USING GIN (unidad_fiscalizable gin_trgm_ops, nombre_razon_social gin_trgm_ops);
```
**Fix a largo plazo:** PostgreSQL full-text search o Elasticsearch.

#### 2.8 `get_table_data` ordena por `to_date()` sin índice funcional
```sql
ORDER BY to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC
```
Esta función se aplica fila por fila en toda la tabla en cada request. Si `sea_proyectos_evaluados` tiene 49k+ filas, esto es un full table scan con ordenamiento en memoria.  
**Fix:** Agregar columna `fecha_presentacion_date DATE GENERATED ALWAYS AS (to_date(nullif(fecha_presentacion,''),'DD/MM/YYYY')) STORED` y crear índice sobre ella.

---

## 3. 📱 Roadmap: App Android (y posterior iOS)

### Estrategia Recomendada: React Native

> Dado que el frontend ya es React (TypeScript), la opción más eficiente es **React Native** — permite reutilizar lógica de negocio, tipos, y conocimiento de React.

### Fase 1 — Preparación (2-4 semanas)
- [ ] Crear repositorio `BioNews-Mobile` (monorepo o separado)
- [ ] Configurar **React Native** con Expo (más fácil) o CLI (más control)
- [ ] Definir y documentar la API como contrato estable (OpenAPI/Swagger desde FastAPI: `/docs`)
- [ ] Asegurarse de que la API devuelve `CORS` apropiado para apps móviles
- [ ] Revisar que todos los endpoints críticos tienen autenticación adecuada (ver vulnerabilidades)

### Fase 2 — Autenticación y Estructura Base (2-3 semanas)
- [ ] Pantalla de Login / Registro con token JWT almacenado en `SecureStore` (Expo)
- [ ] Contexto de autenticación global (similar al `AuthContext` web)
- [ ] Navegación con `React Navigation` (Tab Navigator + Stack Navigator)
- [ ] Splash screen y app icon
- [ ] Interceptor HTTP con manejo de token expirado (refresh o re-login)

### Fase 3 — Pantallas Principales (4-6 semanas)
- [ ] **Noticias**: Feed con cards, imagen, fecha, fuente
- [ ] **Fiscalizaciones / Sancionatorios**: Lista con filtros, modal detalle
- [ ] **Proyectos SEA**: Tarjetas con estado coloreado
- [ ] **Normativas**: Lista con búsqueda
- [ ] **Tribunales**: Lista + detalle
- [ ] **Consultas Públicas** (MMA/MINSAL/DGA): Vista simplificada

### Fase 4 — Funcionalidades Nativas (3-4 semanas)
- [ ] **Push Notifications** con Firebase Cloud Messaging (FCM)
  - Registrar `FCM token` en el backend por usuario
  - El scheduler envía push cuando hay nuevos registros (reemplaza/complementa SSE)
- [ ] **Favoritos**: Sincronizados con la misma API
- [ ] **Búsqueda global**: Pantalla dedicada
- [ ] **Dashboard**: Gráficos con `react-native-chart-kit` o `Victory Native`
- [ ] **Biometría**: Login con Face ID / Fingerprint para reautenticación

### Fase 5 — Publicación Android (2-3 semanas)
- [ ] Configurar `android/` para release
- [ ] Generar keystore y firmar APK/AAB
- [ ] Crear cuenta Google Play Developer ($25 USD, único pago)
- [ ] Preparar screenshots, descripción, política de privacidad
- [ ] Subir a Google Play (Internal Testing → Closed Testing → Production)
- [ ] Configurar CI/CD con GitHub Actions para builds automáticos

### Fase 6 — iOS (posterior, 3-4 semanas adicionales)
- [ ] Cuenta Apple Developer ($99 USD/año)
- [ ] Configurar `ios/` con Xcode
- [ ] Ajustes de UI para iOS (SafeAreaView, etc.)
- [ ] TestFlight para beta testing
- [ ] Publicar en App Store

### Consideraciones técnicas importantes
- La API ya está lista (FastAPI REST + JWT) — no necesita cambios mayores
- Agregar endpoint `POST /api/devices/register` para guardar FCM tokens
- Considerar WebSockets o FCM en lugar de SSE (SSE no funciona bien en mobile background)

---

## 4. 📧 Roadmap: Login/Signup con Confirmación por Mail y Cambio de Contraseña

### Stack recomendado
- **SMTP**: SendGrid (gratuito hasta 100 emails/día) o AWS SES (más barato a escala)
- **Templates**: Jinja2 (ya en el stack Python) o HTML templates simples
- **Librería**: `fastapi-mail` o `smtplib` directo

### Fase 1 — Infraestructura de Email (1 semana)
- [ ] Configurar cuenta SendGrid/SES y obtener API key
- [ ] Agregar variables de entorno: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `FROM_EMAIL`
- [ ] Crear módulo `src/email/sender.py` con función `send_email(to, subject, html_body)`
- [ ] Crear tabla `email_tokens`:
```sql
CREATE TABLE email_tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    token VARCHAR(64) UNIQUE NOT NULL,
    type VARCHAR(20) NOT NULL,  -- 'verify', 'reset_password'
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);
```
- [ ] Diseñar templates HTML de email (confirmación, reset)

### Fase 2 — Confirmación de Email en Registro (1 semana)
- [ ] Modificar `POST /api/auth/register`:
  - Crear usuario con `email_verified = FALSE`
  - Generar token UUID aleatorio, guardarlo en `email_tokens` con TTL 24h
  - Enviar email con link `https://bionews.cl/verify-email?token=xxx`
  - Retornar mensaje "Revisa tu correo para confirmar tu cuenta"
- [ ] Agregar `GET /api/auth/verify-email?token=xxx`:
  - Validar token, marcar `email_verified = TRUE`, invalidar token
- [ ] Bloquear login si `email_verified = FALSE` (con mensaje claro)
- [ ] Agregar `POST /api/auth/resend-verification` (con rate limit: 1 cada 5 min)
- [ ] Frontend: Página de verificación pendiente + pantalla de éxito

### Fase 3 — Cambio de Contraseña (1 semana)
#### "Olvidé mi contraseña"
- [ ] `POST /api/auth/forgot-password` (con email): genera token reset, envía email
- [ ] `POST /api/auth/reset-password` (con token + nueva contraseña):
  - Validar token no expirado y no usado
  - Hashear nueva contraseña, actualizar en BD
  - Invalidar token
  - Opcionalmente invalidar todas las sesiones del usuario
- [ ] Frontend: Formulario de solicitud → Pantalla "revisa tu correo" → Formulario nueva contraseña

#### "Cambiar contraseña" (usuario autenticado)
- [ ] `PUT /api/auth/change-password` (con contraseña actual + nueva):
  - Verificar contraseña actual
  - Validar que la nueva es diferente y cumple requisitos mínimos
- [ ] Frontend: Sección en perfil de usuario

### Validaciones de Contraseña a Implementar
- [ ] Mínimo 8 caracteres
- [ ] Al menos 1 número
- [ ] Al menos 1 mayúscula (recomendado)
- [ ] Implementar en Pydantic validator para reusar en registro y reset

---

## 5. 📨 Roadmap: Newsletters Diarios por Email

### Concepto
Email diario (o configurable) enviado a cada usuario con los nuevos registros del día, organizado por categoría, con diseño profesional similar a un reporte PDF.

### Fase 1 — Diseño del Template (1 semana)
- [ ] Diseñar template HTML responsive para email (compatible con Gmail/Outlook)
  - Header con logo BioNews
  - Sección por categoría (solo las que tienen novedades)
  - Card por item nuevo: título, estado, fecha, link a ficha oficial
  - Footer con botón "Ver en BioNews" + link para desuscribirse
- [ ] Crear en `src/email/templates/newsletter.html` (Jinja2)
- [ ] Probar en [Maizzle](https://maizzle.com/) o usar framework email CSS-inlined

### Fase 2 — Preferencias de Usuario (1 semana)
- [ ] Agregar en tabla `users` o tabla separada `user_newsletter_prefs`:
  ```sql
  CREATE TABLE user_newsletter_prefs (
      user_id INTEGER REFERENCES users(id) PRIMARY KEY,
      enabled BOOLEAN DEFAULT TRUE,
      send_time TIME DEFAULT '08:00',
      categories JSONB DEFAULT '["all"]',  -- o lista específica
      unsubscribe_token VARCHAR(64) UNIQUE  -- para link de baja sin login
  );
  ```
- [ ] `GET/PUT /api/auth/newsletter-preferences` — configurar desde el perfil
- [ ] Frontend: Panel de configuración de newsletter en perfil

### Fase 3 — Generación y Envío (2 semanas)
- [ ] Crear `src/newsletter/generator.py`:
  - Función `get_new_items_since(since_datetime, categories)` — consulta todas las tablas
  - Función `build_newsletter_html(user, items_by_category)` — renderiza Jinja2 template
- [ ] Agregar tarea en el scheduler:
  ```python
  # Cada día a las 08:00 (configurable por usuario en el futuro)
  if current_time == "08:00":
      asyncio.create_task(send_daily_newsletters())
  ```
- [ ] `send_daily_newsletters()`:
  - Obtener todos los usuarios con newsletter habilitado
  - Para cada usuario, obtener nuevos ítems desde `last_newsletter_sent_at`
  - Si hay ítems nuevos, generar y enviar email
  - Actualizar `last_newsletter_sent_at`
- [ ] Link de desuscripción que funcione sin login (con `unsubscribe_token`)

### Fase 4 — Mejoras (1-2 semanas)
- [ ] Versión PDF adjunta (con `weasyprint` o `reportlab`): genera el mismo contenido como PDF
- [ ] Preview en la app web antes de enviar (admin puede ver cómo se ve)
- [ ] Estadísticas de apertura (tracking pixel) — opcional/GDPR
- [ ] Frecuencia configurable: diaria / semanal / inmediata (push on new item)

---

## 6. 💡 Recomendaciones Generales Extra

### 6.1 Migrar a paginación server-side completa
Actualmente el frontend recibe hasta 50.000 registros de una vez. Esto es el mayor problema de performance. Con paginación real (25 items/página, total count separado), la app sería mucho más rápida.

### 6.2 Implementar caché agresiva en Redis para datos que no cambian frecuentemente
```python
# Fiscalizaciones no cambia más que 2 veces al día
cache.set(f"table_data:fiscalizaciones:0:1000", data, ttl=1800)  # 30 min
```
Con el sistema de `cache.invalidate_pattern("table_data:*")` ya existente, solo falta configurar los TTLs apropiados.

### 6.3 Monitoreo y alertas
- Configurar **Sentry** (plan gratuito) para capturar errores en producción automáticamente
- Agregar **Uptime monitoring** (UptimeRobot gratuito) para alertas si el servidor cae
- El `/api/health` existente es perfecto para este propósito

### 6.4 Backup automatizado de PostgreSQL
```bash
# Cron diario en el servidor
0 2 * * * docker exec bionews-db pg_dump -U bionews bionews | gzip > /backups/bionews_$(date +\%Y\%m\%d).sql.gz
```
Rotar backups (mantener últimos 30 días). Considerar backup en S3/R2 de Cloudflare (barato).

### 6.5 Separar el scheduler del proceso de API
Actualmente hay dos mecanismos de scheduling que podrían colisionar: el `scheduler_monitor` dentro de `server.py` y el proceso `scheduler.py` separado. Consolidar en uno solo para evitar ejecuciones duplicadas.

### 6.6 Agregar `Alembic` para migraciones de base de datos
Actualmente el schema se define en `.sql` que solo se ejecuta en `docker-entrypoint-initdb.d` (solo en DB vacía). Para actualizaciones de schema en producción, se necesita `Alembic`:
```bash
pip install alembic
alembic init alembic
# define env.py para conectarse a PostgreSQL
```

### 6.7 Tests automatizados
No existe ningún test. Agregar al menos:
- Tests de endpoints críticos (login, register, get_table_data) con `pytest` + `httpx`
- Tests unitarios de `DatabaseManager`
- Esto previene regresiones al agregar nuevas funcionalidades

### 6.8 Variables de entorno centralizadas
Crear un archivo `src/config.py` que centralice toda la configuración:
```python
# src/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str
    admin_email: str = "administrador@bionews.cl"
    admin_password: str
    smtp_host: str = ""
    db_host: str = "localhost"
    # ...
    class Config:
        env_file = ".env"

settings = Settings()
```

### 6.9 Documentación de API con Swagger UI
FastAPI ya genera `/docs` automáticamente. Asegurarse de que esté accesible para el equipo y documentar los modelos de respuesta con tipos Pydantic para auto-documentación.

### 6.10 Considerar WebSockets en lugar de SSE para notificaciones
El SSE actual tiene problemas en mobile y con proxies. WebSockets (ya hay código legacy en `server.py`) son más robustos y bidireccionales.
