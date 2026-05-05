# Guía de Despliegue BioNews en Ubuntu Server

Este documento detalla los pasos para realizar una instalación limpia del sistema BioNews en tu servidor Ubuntu Server, utilizando Docker para el backend, frontend y el programador de tareas.

## 1. Limpieza del Servidor

Para evitar conflictos con instalaciones previas, ejecuta los siguientes comandos en tu terminal SSH (`maruzs@192.168.1.26`):

```bash
# Detener contenedores si están corriendo (dentro de la carpeta actual)
cd ~/app/BioNews && docker compose down
cd ~/BioNews && docker compose down

# Borrar carpetas antiguas y obsoletas
rm -rf ~/app/BioNews
rm -rf ~/BioNews
```

## 2. Preparación del Proyecto

### Clonar el Repositorio
Ubícate en tu carpeta personal (`~`) y clona el proyecto:

```bash
cd ~
git clone https://github.com/maruzs/BioNews.git
cd BioNews
```

### Crear Directorios de Persistencia
Crea las carpetas necesarias para que la base de datos y los logs persistan fuera de Docker:

```bash
mkdir -p ~/BioNews/data
mkdir -p ~/BioNews/logs
```

## 3. Transferencia de la Base de Datos

Desde **tu computadora con Windows** (donde tienes el archivo `data.db`), abre una terminal (PowerShell o CMD) y ejecuta:

```powershell
# Comando para enviar la base de datos al servidor desde Windows
scp "C:\Users\maria\Desktop\BioNews\data\data.db" maruzs@192.168.1.26:~/BioNews/data/data.db
```
*Te pedirá la contraseña del usuario `maruzs`.*

## 4. Despliegue con Docker

En el servidor, dentro de `~/BioNews`, levanta todos los servicios:

```bash
docker compose up -d --build
```

Esto levantará 3 servicios:
1.  **bionews-api**: El backend en FastAPI (puerto 8000 interno).
2.  **bionews-scheduler**: El robot que ejecuta los scrapers cada hora.
3.  **bionews-web**: El frontend en React servido por Nginx (puerto 3080).

## 5. Acceso Público con Cloudflared (TryCloudflare)

Para exponer tu servidor local a internet sin necesidad de un dominio propio, utilizaremos los túneles temporales de Cloudflare.

### Iniciar el Túnel en Segundo Plano
Ejecuta el siguiente comando para iniciar el túnel de forma persistente (incluso si cierras la sesión SSH):

```bash
nohup cloudflared tunnel --url http://localhost:3080 > ~/BioNews/cloudflared.log 2>&1 &
```

### Obtener la URL Generada
Para saber cuál es la dirección web que Cloudflare te asignó, ejecuta:

```bash
grep -o 'https://[a-zA-Z0-9-]\+\.trycloudflare\.com' ~/BioNews/cloudflared.log | head -n 1
```

## 6. Comandos de Mantenimiento Útiles

- **Ver logs de la aplicación**: `docker compose logs -f`
- **Reiniciar el sistema**: `docker compose restart`
- **Actualizar código (si haces cambios en GitHub)**:
  ```bash
  git pull
  docker compose up -d --build
  ```
- **Ver logs del túnel**: `tail -f ~/BioNews/cloudflared.log`
