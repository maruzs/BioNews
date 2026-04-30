# BioNews — Guía de Despliegue con Docker en Ubuntu Server

## Arquitectura

```
[Cualquier dispositivo con Tailscale]
        ↕  Tailscale VPN (100.x.x.x)
[Ubuntu Server (laptop headless)]
    └─ Docker Compose
        ├─ web       (Nginx + React build)  → puerto 80
        ├─ api       (FastAPI + Playwright) → puerto 8000 (interno)
        └─ scheduler (scrapers cada hora)
        └─ Volumes: bionews-data, bionews-logs
```

---

## Paso 1: Instalar Tailscale en el servidor

```bash
# Si no está instalado aún:
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

# Verificar la IP Tailscale:
tailscale ip -4
# Ejemplo: 100.99.88.77
```

También instala Tailscale en cada dispositivo desde el que quieras acceder:
- https://tailscale.com/download

---

## Paso 2: Copiar el código al servidor

Desde tu PC Windows (PowerShell), copia todo el proyecto al servidor vía SCP:

```powershell
# Ajusta <usuario> y <ip-servidor> a tus datos
scp -r C:\Users\maria\Desktop\BioNews <usuario>@<ip-servidor>:~/BioNews
```

Si el proyecto ya está en Git:

```bash
# En el servidor:
cd ~
git clone <tu-repo-url> BioNews
```

---

## Paso 3: Configurar el archivo .env

```bash
cd ~/BioNews

# Crear/verificar el archivo .env
nano .env
```

Contenido:
```
SEA_USER=<tu-usuario>
SEA_PASSWORD=<tu-contraseña>
```

---

## Paso 4: Levantar con Docker Compose

```bash
cd ~/BioNews

# Construir y levantar todos los servicios
docker compose up -d --build

# Ver los logs en tiempo real
docker compose logs -f

# Ver el estado de los contenedores
docker compose ps
```

La primera vez tardará unos minutos porque:
- Descarga la imagen de Python y Node
- Instala Playwright + Chromium
- Compila el frontend React

---

## Paso 5: Acceder a la aplicación

| Desde | URL |
|---|---|
| **El mismo servidor** | `http://localhost` |
| **Otro PC con Tailscale** | `http://<IP-Tailscale>` |

Ejemplo: `http://100.99.88.77`

> **Nota:** No necesitas especificar puerto. Todo va por el puerto 80 (HTTP estándar).

---

## Gestión de contenedores

```bash
# Detener todo
docker compose down

# Reiniciar todo
docker compose restart

# Reconstruir después de cambios en el código
docker compose up -d --build

# Ver logs del scheduler
docker compose logs -f scheduler

# Ver logs del backend
docker compose logs -f api

# Ver logs del frontend
docker compose logs -f web
```

---

## Scheduler automático

El scheduler corre dentro del contenedor `bionews-scheduler`:

- **Horario:** Cada hora en punto, entre **07:00 y 19:00** (hora del servidor)
- **Primera ejecución:** Al arrancar el contenedor
- **Logs:**
  ```bash
  docker compose logs -f scheduler
  # O dentro del volumen:
  docker compose exec scheduler cat /app/logs/scheduler.log
  ```

---

## Datos persistentes

Los datos de la base de datos SQLite y los logs se guardan en **Docker volumes**:

```bash
# Ver los volúmenes
docker volume ls | grep bionews

# Backup de la base de datos
docker compose exec api cp /app/data/bionews.db /app/data/bionews_backup.db
docker cp bionews-api:/app/data/bionews_backup.db ./backup_bionews.db
```

---

## Si ya tienes Nginx en el host

Si quieres usar el Nginx del host como proxy reverso (por ejemplo, para agregar HTTPS o múltiples apps):

```nginx
# /etc/nginx/sites-available/bionews
server {
    listen 80;
    server_name bionews.tu-dominio.com;  # o la IP Tailscale

    location / {
        proxy_pass http://127.0.0.1:3080;  # Cambiar el puerto en docker-compose
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

En ese caso, cambia el puerto en `docker-compose.yml`:
```yaml
web:
  ports:
    - "3080:80"   # En vez de "80:80"
```

---

## Troubleshooting

| Problema | Solución |
|---|---|
| Puerto 80 ya en uso | Cambia `"80:80"` a `"3080:80"` en docker-compose.yml y configura nginx del host |
| Scrapers fallan | `docker compose logs scheduler` para ver errores |
| Base de datos vacía | Los scrapers aún no han corrido. Espera a la primera hora en punto o lanza manualmente: `curl -X POST http://localhost/api/scrape/all` |
| Contenedores no inician | `docker compose logs` para ver errores de build |
