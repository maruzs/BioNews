# BioNews - Guía de Despliegue en Servidor Local

Esta guía detalla los pasos para desplegar **BioNews** en tu servidor local (Intel i3 7ma gen, 4GB RAM), asegurando que el proceso se ejecute de forma robusta con Docker, y permitiendo acceso remoto de forma segura.

---

## 1. Preparación del Entorno

### Requisitos Previos en el Servidor

1. **Instalar Docker y Docker Compose:**
   - Descarga e instala [Docker Desktop](https://www.docker.com/products/docker-desktop/) si tu servidor usa Windows, o Docker Engine si usa Linux (Ubuntu/Debian).
2. **Instalar Git:**
   - Necesario para clonar y actualizar el repositorio.
3. **Instalar Tailscale (Recomendado para acceso privado):**
   - Descarga e instala [Tailscale](https://tailscale.com/download) en el servidor, tu notebook y tu celular. Inicia sesión con la misma cuenta en todos los dispositivos.

### Pasar el código al Servidor (Vía Git)

En tu servidor, abre una terminal y clona el repositorio (si es privado, te pedirá tus credenciales de GitHub):

```bash
git clone https://github.com/maruzs/BioNews.git
cd BioNews
```

> **Nota sobre la base de datos (`data.db`):**
> Hemos configurado el archivo `.gitignore` para ignorar `data.db` y evitar problemas al sincronizar. Para pasar tu base de datos actual al servidor, simplemente copia el archivo `data/bionews.db` desde tu computador actual y pégalo en la misma carpeta `data/` dentro de tu servidor mediante un pendrive o transferencia de red directa.

---

## 2. Levantar la Aplicación con Docker

El proyecto está configurado para ejecutarse completamente aislado en contenedores de Docker (Backend, Frontend+Nginx y el Scheduler de Scrapers automático).

Ejecuta el siguiente comando en la raíz del proyecto para construir y levantar todo en segundo plano (`-d` significa _detached_, por lo que si cierras la terminal, el proceso no muere):

```bash
docker compose up -d --build
```

**Comandos útiles de Docker:**

- Para ver si están corriendo: `docker compose ps`
- Para ver los logs en tiempo real (útil para ver si los scrapers se activaron): `docker compose logs -f`
- Para detener el sistema: `docker compose down`

> El sistema está configurado con `restart: unless-stopped`, lo que significa que **si apagas tu servidor y lo vuelves a encender, Docker levantará automáticamente BioNews sin que tengas que hacer nada.**

---

## 3. Acceso Remoto al Servidor

Tienes dos opciones para acceder desde afuera. Como mencionaste ambas (Cloudflare y Tailscale), te explico cómo funcionan. **Te recomiendo encarecidamente la Opción A (Tailscale)**, ya que es más segura, privada y la URL no cambiará.

### Opción A: Usando Tailscale (Recomendada, Privada y Fija)

Dado que quieres acceder solo tú, desde tu notebook y celular, Tailscale es perfecto.

1. Abre Tailscale en tu Servidor y anota la dirección IP que te asigna (suele empezar con `100.x.x.x`).
2. En tu celular o notebook personal (que deben tener Tailscale instalado y conectado a la misma cuenta), abre el navegador.
3. Ingresa la URL: `http://100.x.x.x:3080` (reemplazando las 'x' por la IP de tu servidor).
4. ¡Listo! Accederás de forma segura y nadie más en internet podrá ver tu página. Además, esa IP nunca cambia aunque reinicies el servidor.

### Opción B: Túneles Rápidos de Cloudflare (Público pero Temporal)

Si necesitas acceder desde un dispositivo en el que _no puedes_ instalar Tailscale, puedes usar un túnel gratuito de Cloudflare. Como no tienes dominio, Cloudflare te dará un link aleatorio del tipo `https://palabras-al-azar.trycloudflare.com`.

1. Descarga el ejecutable `cloudflared` en tu servidor.
2. Abre la terminal y ejecuta:
   ```bash
   cloudflared tunnel --url http://localhost:3080
   ```
3. En la consola te arrojará un link público. Podrás usar ese link desde cualquier parte del mundo.
   > **Importante:** Este link cambia cada vez que cierras el comando o reinicias el servidor. Además, cualquier persona con el link podría ver tu página de inicio (aunque tendrían que saber tu clave para entrar al sistema).

---

## 4. Archivos Innecesarios a Eliminar

Para mantener el proyecto limpio antes de que lo pases todo al servidor, te recomiendo **eliminar** los siguientes archivos y carpetas que ya no están siendo utilizados por la nueva arquitectura (ya configuramos todo en Docker y la API):

1. **Carpetas:**
   - `nuevo/` (Parece ser código de prueba antiguo)
   - `developer/` (Documentación antigua de versiones anteriores)
2. **Archivos sueltos:**
   - `startScraping.py` (Reemplazado por el nuevo `scheduler.py`)
   - `scrape_news.py` (Reemplazado e integrado en el backend)
   - `inspect_db.py` (Script antiguo de depuración)
   - `deployment_guide.md` (Reemplazado por este mismo `README.md`)
   - `bionews.nginx.conf` (Reemplazado por `web/nginx.conf` que ahora se usa dentro de Docker)

Para eliminarlos en Git, simplemente bórralos de tu computador, luego haz `git add .`, `git commit -m "Limpieza de archivos muertos"` y `git push`.

---

## 5. Actualizaciones de Código (Ciclo de Desarrollo)

Cuando hagas mejoras en tu computador principal y quieras pasarlas al servidor:

1. En tu computador personal:
   ```bash
   git add .
   git commit -m "Nueva actualización"
   git push origin master
   ```
2. En tu servidor (abres una terminal dentro de la carpeta `BioNews`):
   ```bash
   git pull origin master
   docker compose up -d --build
   ```
   Al agregar `--build`, Docker detectará los cambios en tu código y reconstruirá la aplicación en pocos segundos aplicando tus últimas mejoras.

Iniciar servidor
nohup cloudflared tunnel --url http://localhost:3080 > cloudflared.log 2>1 &
ver IP
cat cloudflared.log | grep trycloudflare.com

nohup cloudflared tunnel --url http://localhost:3080 > cloudflare.log 2>&1 &
cat cloudflare.log | grep -o 'https://[a-zA-Z0-9-]\+\.trycloudflare\.com'
