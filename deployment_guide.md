# 🚀 BioNews — Pasos de Despliegue en el Servidor

> [!IMPORTANT]
> Ejecuta estos comandos desde tu PC Windows **conectado por SSH al servidor Ubuntu**.

---

## Paso 0: Conectarte al servidor

```bash
ssh <usuario>@<ip-del-servidor>
```

---

## Paso 1: Copiar el código al servidor

Desde **PowerShell en tu PC Windows** (no en SSH):

```powershell
# Opción A: SCP (copia directa)
scp -r C:\Users\maria\Desktop\BioNews <usuario>@<ip-servidor>:~/BioNews

# Opción B: Si usas Git (más limpio)
# En tu PC: git add, commit, push
# En el servidor: git clone <repo-url> ~/BioNews
```

---

## Paso 2: Configurar el .env en el servidor

```bash
cd ~/BioNews
# Verificar que .env existe con las credenciales
cat .env
# Debería mostrar SEA_USER y SEA_PASSWORD
```

---

## Paso 3: Instalar Tailscale (si no está instalado)

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

# Anotar la IP Tailscale:
tailscale ip -4
# Ejemplo de output: 100.99.88.77
```

---

## Paso 4: Levantar con Docker Compose

```bash
cd ~/BioNews

# Construir y levantar (primera vez tarda ~5-10 min)
docker compose up -d --build

# Verificar que todo está corriendo
docker compose ps

# Ver logs en tiempo real
docker compose logs -f
```

> [!NOTE]
> Deberías ver 3 contenedores:
> - `bionews-api` → **healthy**
> - `bionews-scheduler` → **running**
> - `bionews-web` → **running**

---

## Paso 5: Configurar Nginx del host

```bash
# Eliminar el default de nginx si existe
sudo rm -f /etc/nginx/sites-enabled/default

# Copiar la configuración de BioNews
sudo cp ~/BioNews/bionews.nginx.conf /etc/nginx/sites-available/bionews

# Habilitar el sitio
sudo ln -sf /etc/nginx/sites-available/bionews /etc/nginx/sites-enabled/bionews

# Verificar que la configuración es válida
sudo nginx -t

# Recargar nginx
sudo systemctl reload nginx
```

---

## Paso 6: ¡Acceder desde cualquier dispositivo!

Instala **Tailscale** en cada dispositivo desde el que quieras acceder y abre en el navegador:

```
http://<IP-Tailscale-del-servidor>
```

Ejemplo: `http://100.99.88.77`

> [!TIP]
> También puedes configurar un **nombre DNS** en la consola de Tailscale ([login.tailscale.com](https://login.tailscale.com)) para acceder con algo como `http://bionews` en vez de la IP.

---

## Comandos útiles para después

| Acción | Comando |
|---|---|
| Ver estado | `docker compose ps` |
| Ver logs | `docker compose logs -f` |
| Reiniciar todo | `docker compose restart` |
| Actualizar código | `cd ~/BioNews && git pull && docker compose up -d --build` |
| Ver logs scheduler | `docker compose logs -f scheduler` |
| Lanzar scraping manual | `curl -X POST http://localhost/api/scrape/all` |
| Parar todo | `docker compose down` |
| Backup de BD | `docker cp bionews-api:/app/data/bionews.db ~/backup.db` |

---

## Estructura de archivos creados

```
BioNews/
├── Dockerfile                  ← Imagen Python (backend + scheduler)
├── docker-compose.yml          ← Orquestación de los 3 servicios
├── requirements.docker.txt     ← Dependencias Python (sin flet/pyinstaller)
├── scheduler.py                ← Scheduler automático (7am-7pm)
├── bionews.nginx.conf          ← Config nginx para el host Ubuntu
├── .dockerignore               ← Exclusiones del build Docker
├── server.py                   ← Backend FastAPI (actualizado)
├── src/scrapers/engine.py      ← Motor scraping (actualizado para Linux)
├── web/
│   ├── Dockerfile              ← Build multi-stage (Node → Nginx)
│   ├── nginx.conf              ← Config nginx dentro del contenedor
│   ├── .dockerignore           ← Exclusiones del build frontend
│   └── vite.config.ts          ← Proxy /api para desarrollo local
└── DEPLOY.md                   ← Guía completa de despliegue
```
