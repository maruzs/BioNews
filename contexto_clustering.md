**CONTEXTO DE INFRAESTRUCTURA Y ARQUITECTURA DEL PROYECTO**

1. **Hardware y Sistema:** Estoy trabajando en un cluster de dos laptops headless con Ubuntu Server.

- **Manager (Asus):** i5-8250U, 8GB RAM, 128GB SSD. Nodo principal.
- **Worker (HP):** i3-7020U, 8GB RAM, 120GB HDD. Nodo de apoyo.

2. **Estado del Cluster:** Docker Swarm no está activo (No se como hacerlo) pero tengo las dos laptops conectadas al mismo switch fisico.
3. **Redes:** Existe una red global llamada `proxy_network` (bridge/overlay) que conecta el contenedor de **Nginx Proxy Manager (NPM)** con los proyectos individuales.
4. **Objetivo:** Configurar el proyecto **BioNews** para que sea servido a través de NPM (Reverse Proxy) y no directamente por puertos del host. Esto permitirá hostear múltiples sitios (Psicólogos, Descuéntrame) en el mismo servidor.
5. **Requerimientos para el archivo `docker-compose.yml` de BioNews:**

- Mantener los nombres de contenedores (`bionews-api`, `bionews-web`).
- Mantener los `healthcheck` actuales para asegurar la disponibilidad.
- **Networking:** El servicio `web` debe conectarse a dos redes: `bionews-net` (interna) y `proxy_network` (externa para el proxy).
- **Puertos:** Eliminar el mapeo de puertos del host (`3080:80`) del servicio `web`, ya que NPM se comunicará por la IP interna de la red.
- **Persistencia:** Asegurar que los volúmenes apunten a `/opt/BioNews/data`, `/opt/BioNews/logs` y `/opt/BioNews/uploads`.

6. **Tarea:** Por favor, reescribe el `docker-compose.yml` y todo lo que sea necesario para que funcione BioNews siguiendo estas directrices, asegurando que la sintaxis sea compatible con Docker Swarm/Stack.

---

### Comandos de red para auditar tu sistema

Para que estés seguro de qué está pasando antes y después de aplicar los cambios en Antigravity, usa estos comandos en tu terminal SSH:
