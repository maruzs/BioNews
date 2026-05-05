Ok, estan horribles pero los trabajaremos manana, ahora estoy muy cansado.
Me interesa desplegarlo a mi servidor propio (una laptop headless que esta en mi casa, con ubuntu server y que controlo mediante ssh)

Tengo tailscale para control del ssh desde otros dispositivos en otras redes (otra ciudad por ejemplo)

Tengo cloudfared tunnels gratis (los de testeo/try que cambian cada vez que se inicia el servicio) ya que no tengo un dominio propio registrado.

Actualmente en el servidor tengo el proyecto asi:

```bash
maruzs@maruzs-server:~/app/BioNews$ ls -l
total 112
-rw-rw-r-- 1 maruzs maruzs  1500 May  5 01:55 Dockerfile
drwxrwxr-x 2 maruzs maruzs  4096 May  5 01:55 assets
-rw-rw-r-- 1 maruzs maruzs  3473 May  5 03:26 cloudflared.log
drwxrwxr-x 2 maruzs maruzs  4096 May  5 18:48 data
-rw-rw-r-- 1 maruzs maruzs  2149 May  5 01:55 docker-compose.yml
-rw-rw-r-- 1 maruzs maruzs 13218 May  5 01:55 logo_sernageomin.png
drwxr-xr-x 2 root   root    4096 May  5 02:10 logs
-rw-rw-r-- 1 maruzs maruzs   668 May  5 01:55 prompt.md
-rw-rw-r-- 1 maruzs maruzs  5056 May  5 01:55 readme.md
-rw-rw-r-- 1 maruzs maruzs   735 May  5 01:55 requirements.docker.txt
-rw-rw-r-- 1 maruzs maruzs  1163 May  5 01:55 requirements.txt
-rw-rw-r-- 1 maruzs maruzs  7537 May  5 01:55 scheduler.py
-rw-rw-r-- 1 maruzs maruzs 16954 May  5 01:55 server.py
drwxrwxr-x 6 maruzs maruzs  4096 May  5 01:55 src
-rw-rw-r-- 1 maruzs maruzs  5614 May  5 02:04 startScraping.py
-rw-rw-r-- 1 maruzs maruzs  5580 May  5 01:55 tutorial.md
drwxrwxr-x 4 maruzs maruzs  4096 May  5 01:55 web
maruzs@maruzs-server:~/app/BioNews$ docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
bionews-api bionews-api "uvicorn server:app …" api 21 hours ago Up 11 hours (healthy) 8000/tcp
bionews-scheduler bionews-scheduler "python scheduler.py" scheduler 21 hours ago Up 11 hours 8000/tcp
bionews-web bionews-web "/docker-entrypoint.…" web 21 hours ago Up 11 hours 0.0.0.0:3080->80/tcp, [::]:3080->80/tcp
```

Me gustaria que estuviera directamente en ~/BioNews pero ya tengo una carpeta con ese nombre y no se como borrarla

No hay necesidad de un .env ya que las credenciales estan hardcodeadas en el codigo (solo es para las pertinencias SEA)

Subire el proyecto a github en https://github.com/maruzs/BioNews por lo que quiero clonarlo directamente en ~ pero no contiene la bd del proyecto por lo que tengo que copiarla de manera manual desde mi Desktop con windows (donde estoy trabajando ahora) al servidor con ubuntu usando scp y luego moverla a la carpeta del proyecto.

Quiero lo siguiente:

1. Que me des el comando para borrar todo el ~/BioNews y el ~/app/BioNews de mi servidor
2. Que configures los archivos de docker que tengo actualmente de manera que al clonarlo en mi servidor en la raiz (~) quede ~/BioNews y adentro el contenido
3. El comando para pasar la bd desde mi pc con windows al servidor y colocarla en la carpeta ~/BioNews/data/data.db
4. Darme el comando de cloudfared para desplegarlo usando los tunnels gratis que da cloudfare (proximamente le comprare un dominio para ponerle un tunnel permanente) sin que se cierre cuando cierro la sesion SSH (con nohup) y el comando para ver cual es la ip que me dio

el ssh es
ssh maruzs@192.168.1.26 y la clave yo la pongo

Antes de comenzar todo esto voy a detener los docker compose que estan ejecutandose
