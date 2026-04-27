` GUIA MAESTRA - VIRTUAL ENVIRONMENTS, GIT, GITHUB Y DOCKER `
Usando un Desktop con Windows 11 y una laptop con Kali linux (Ambos con VSCode)

# NUNCA OLVIDAR (CHECKLIST INICIAL)
1. Crear .gitignore -> Evitamos subir basura, archivos pesados o informacion importante al servidor
    - Contenido basico: 
        .env
        __pycache__/
        .venv/
        node_modules/
        .DS_Store
2. Crear .env -> Aqui van las API keys y credenciales, jamas deben subirse a github
    - Formato basico:
        API_KEY=claveapi
        RUT=xx.xxx.xxx-x
3. Crear README.md -> La cara del proyecto (Explicacion en su propio apartado)
4. Crear requirements.txt -> Lista de ingredientes del proyecto
5. Crear un .dockerignore -> Evitamos subir cosas que hagan pesada la imagen del contenedor
    - Contenido basico:
        .git
        .venv
# SINCRONIZACION ENTRE DISPOSITIVOS
* Primera vez 
```bash
# Para evitar carpetas duplicadas es mejor ir a la carpeta padre (donde estan todos los proyectos) y ejecutar el clone ahi
# O tambien se puede usar el . para clonar el contenido directamente en la carpeta en la que estoy
# CLONAR REPOSITORIO
git clone url_del_repositorio . # El punto clona directamente donde estoy
# CREAR Y ACTIVAR VENV 
python -m venv .venv 
.venv\Scripts\Activate.ps1 # WINDOWS 11 (Powershell)
source .venv/bin/activate # KALI LINUX
# INSTALAR LIBRERIAS
pip install -r requirements.txt
```
* No primera vez pero si hice cambios desde otro dispositivo
```bash
# Original (Envia cambios):
git add .
git commit -m "WIP: Trabajando en x funcion, linea: "
git push origin main # o la branch en la que se este trabajando INVESTIGAR TAGS (origin)!!!

# Nuevo (Recibe cambios) 
git pull origin master # No es necesario hacer pull de main si solo se trabaja en una rama
git pull origin rama 
```

# VIRTUAL ENVIRONMENTS (Venv)
Sirve para que las librerias de un proyecto no interfieran con las de otros, debe hacerse en una consola dentro de la carpeta del proyecto ('ctrl + `' o 'cd' hasta el directorio del proyecto)

## Configuracion
Siempre dentro del directorio del proyecto
1. Crear el entorno 
```bash
python -m venv .venv # .venv es el nombre de la carpeta, puede ser cualquiera
```
2. Activacion (Varia segun OS)
- Windows 11 (Powershell)
```bash
.venv\Scripts\Activate.ps1 # Scripts es la carpeta dentro del entorno virtual donde residen los ejecutables y el archivo de activacion
```
- Kali Linux
```bash
source .venv/bin/activate # Bin es la carpeta dentro del entorno virtual donde residen los ejecutables y el archivo de activacion
```
3. Instalar librerias
```bash
pip install nombre_libreria
```
4. Guardar cambios en la lista
```bash
pip freeze > requirements.txt
```
5. Instalar desde la lista en otro PC
pip install -r requirements.txt


# GIT Y GITHBUB (CONTROL DE VERSIONES)
Git gestiona los cambios localmente, GitHub es la copia en la nube

## CONFIGURACION INICIAL Y FLUJO DIARIO
Inicializacion de git, conexion con el servidor, y uso diario (dentro de main/master)
1. INICIALIZACION Y VINCULO
```bash
git init
git remote add origin url_del_repositorio 
# DEFINICION: Origin es simplemente un alias para la url del servidor (github), es el estandar, pueden ser otros
git branch -M main # o master 
```
2. FLUJO DIARIO (Guardar cambios)
```bash
git add .
# DEFINICION: add prepara los cambios, al usar . es para todo lo que no este en el .gitignore
git commit -m "Mensaje: Explicacion lo mas completa de lo que se hizo"
git push origin main # Se sube al repositorio desde la main/master branch
```
3. COMENZAR A TRABAJAR DESDE OTRO COMPUTADOR (Nunca trabajado este proyecto)
```bash
# Para evitar carpetas duplicadas es mejor ir a la carpeta padre (donde estan todos los proyectos) y ejecutar el clone ahi
# O tambien se puede usar el . para clonar el contenido directamente en la carpeta en la que estoy
# CLONAR REPOSITORIO
git clone url_del_repositorio . # El punto clona directamente donde estoy
```
4. OBTENER TRABAJO (Subido al server desde otro dispositivo)
```bash
git fetch 
# DEFINICION: fetch ve si el servidor se actualizo pero no pide nada
git pull origin master # No es necesario hacer pull de main si solo se trabaja en una rama
# DEFINICION: pull pide los cambios
git pull origin rama 
```
5. VOLVER ATRAS (Ultimo commit)
```bash
# Ya sea dentro de una rama o en el main/master
git restore nombre_archivo.py # o cualquier extension que haya tenido el archivo
# O para restaurar todo 
git restore .
```
6. CAMBIO DE RAMA  
```bash
git branch # Ver rama actual
git checkout rama # Para cambiar de rama
```
## LABORATORIO (BRANCHES)
Para probar ideas sin romper lo que ya funciona
1. CREAR Y TRABAJAR EN UNA RAMA
```bash
git checkout -b experimental # Crea y cambia inmediatamente a la nueva rama llamada 'experimental', puede hacerse en dos pasos
```
2. FLUJO DIARIO (Guardar cambios dentro de la rama de forma local)
```bash
git add .
git commit -m "Mensaje: Explicacion de la rama y cambios hechos dentro de ella, lo mas completo posible"
```
3. SINCRONIZACION DE RAMA
```bash
git fetch # Actualiza lo que hay en el servidor
git checkout rama # Vamos a la rama de trabajo
git pull origin rama # Traemos solo lo especifico de esa rama
```

### CASOS POSIBLES CON BRANCHES
Casos que pueden ocurrir al trabajar con mas de un dispositivo
1. FUNCIONA Y QUIERO UNIRLO A LA PRINCIPAL (MAIN/MASTER)
Desde el PC inicial, sin haber hecho cambios en otros dispositivos
```bash
git checkout main # Volvemos a la rama principal
git merge experimental # Traemos los cambios de 'experimental' a 'main'
git branch -d experimental # Borrado seguro de la rama experimental (Es opcional, d minuscula indica seguro, D indica forzado)
# En caso que se hayan hecho cambios en main y a la vez en branch no sabra con cual quedarse
# Habra que decidir linea por linea respecto a los cambios, VSCode las marca verde y rojo
```
2. NO FUNCIONA Y QUIERO ANULAR TODO
Desde el PC inicial o laptop no funcionaron los cambios, por lo que decido volver al main y borrar la rama
```bash
git checkout main
git branch -D experimental # Borra la rama con todo lo malo, -D es borrado forzado, -d es borrado seguro
```
3. Trabajo en progreso (PC <--> LAPTOP)
No alcance a terminar el trabajo en el PC y quiero continuar en la laptop
- Desde el PC
```bash
git add .
git commit -m "WIP PC: Avance de funcion x" # Work In Progress
git push origin experimental # Sube la rama al servidor
```
- Desde la laptop
```bash
git fetch # Actualizacion de la informacion del servidor
git checkout experimental
git pull origin experimental 
# Al terminar en la laptop
git add .
git commit -m "WIP LAPTOP: Avance/Fin de funcion x"
git push origin experimental 
# Desde el PC se haria solo el git pull, ya que la rama ya existe
```


# DOCKER (EMPAQUETADOR)
Hace que funcione el codigo en cualquier dispositivo que tenga instalado docker. Crea un contenedor que lleva su propio sistema operativo, codigo y librerias exactas

## CONCEPTOS CLAVE
1. Docker hub -> Es como el **'github de las imagenes'**, de aqui se descargan imagenes oficiales (y no oficiales)
2. Imagen -> Un archivo inerte que contiene el **codigo** + **librerias** + **OS ligero**
3. Contenedor -> La imagen en ejecucion. Puedes borrar el contenedor y la imagen sigue ahi intacta
4. Docker Desktop -> En windows siempre asegurarse que el icono de la ballena este en verde antes de ejecutar
Siempre debe ejecutarse en la raiz del proyecto (Donde este el Dockerfile)

## IMAGENES EXTERNAS
Si quieres usar imagenes externas sin instalar nada (Se hara el ejemplo con nginx)
```bash
# 1. Descargar imagen oficial
docker pull nginx
# 2. Correr el servidor
docker run --name mi-servidor -p 8080:80 -d nginx # -p redirige el puerto, -d (Detached) para que corra en segundo plano y no bloquee consola
```

## CONFIGURACION INICIAL Y REQUERIMIENTOS
Debe estar docker engine instalado en todos los computadores
1. DOCKERFILE
```bash
# En realidad el archivo se debe llamar Dockerfile sin extension, son las instrucciones para armar la imagen
# 1. La base: Python versión slim (ligera)
FROM python:3.10-slim
# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app
# 3. Copiar lista de librerías e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 4. Copiar el resto del código
COPY . .
# 5. Comando para ejecutar tu app
CMD ["python", "main.py"]
```
2. DOCKERIGNORE
```bash
# En realidad el archivo se debe llamar .dockerignore, evita subir archivos para no hacer pesada la imagen
.venv
__pycache__
.git
.env
```
## COMANDOS BASICOS
1. Construir imagen
```bash
docker build -t nombre-app .
```
2. Correr el contenedor
```bash
# Ejecutarlo pasando tus llaves de API desde el .env
docker run --env-file .env nombre-app
```
3. Obtener de repositorio (hub.docker.com)
```bash
docker pull nombre_imagen
```
4. Comandos de mantenimiento
```bash
docker ps # Que contenedores estan corriendo
docker stop ID # Detener el contenedor con la ID 
docker rm ID # Borrar un contenedor
docker images # Ver imagenes
docker rmi # Borrar una imagen
docker system prune # ¡¡¡CUIDADO!!! -> Borra todo lo que no se esta usando (Liberar GB)
```
5. Tags de imagenes
    * latest -> Ultima version, no recomendada para proyectos serios porque puede cambiar y romper el codigo
    * slimp -> Minimalista, pesa muy poco
    * alpine -> La mas liviana de todas, basada en distro ultraligera
    * En el dockerfile se usa -> `FROM python:3.10-slim`
6. Flags de comandos
    * -it (Interactive terminal) -> Para entrar a la consola dentro del contenedor
    * -v o --volume -> Para conectar la carpeta de tu PC con una del contenedor (Cambios en el PC se reflejan sin reconstruir)
    * --rm -> Borra el contenedor directamente cuando lo detienes (Limpieza en el PC)
    * -e -> Para pasar directamente variables de entorno `-e API_KEY=12345`
## DOCKER COMPOSE
Si el proyecto necesita una base de datos y Python al mismo tiempo, se usa un archivo llamado **docker-compose.yml** que permite levantar 5 contenedores distintos con un solo comando **docker-compose up**.
Sirve para coordinar varios contenedores (App + BBDD + Redis) con un solo comando (docker-compose up/down)
Los contenedores se ven entre si por nombre de servicio (app habla con db sin saber la ip)
Es persistente, gestiona volumenes facilmente, en caso de borrar el contenedor los datos no mueren

Ejemplo de un docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .             # Usa el Dockerfile de la carpeta actual
    ports:
      - "8000:8000"      # Mapeo de puertos
    env_file:
      - .env             # Carga automáticamente tus llaves del .env
    volumes:
      - .:/app           # Sincroniza tu código en tiempo real
  db:
    image: postgres:15   # Descarga una imagen oficial de base de datos
    environment:
      POSTGRES_PASSWORD: example
```


# README.MD
Manual de instrucciones, un buen readme.md debe tener lo siguiente
1. Titulo y descripcion corta -> Que hace el proyecto?
2. Requisitos -> Que necesita el otro para empezar? (Python, Docker, etc.)
3. Instalacion -> Paso a paso de los comandos (git clone, pip install, etc)
4. Uso -> Como se ejecuta el programa
5. Variables de entorno -> Lista de llaves que necesita el .env y su formato (sin poner los valores reales)

# BUENAS PRACTICAS FINALES

* Commits pequenos -> Mejor hacer 10 commits pequenos que uno gigante, permite identificar donde empezo a fallar todo
* Mensajes claros -> Evitar mensajes ambiguos o poco explicativos, ahondar bien en la explicacion de los cambios
* Sincronizacion -> Siempre hacer **git pull origin master** antes de empezar a trabajar para tener certeza de que se trabaja con los ultimos cambios hechos
* Seguridad -> Si por error se sube el **.env**, hacer cambio de las API keys inmediatamente (y de las respectivas credenciales)
* Comentarios -> Codigo bien comentado 