## Contexto general:
Ahora mismo estoy desde un PC con windows 11 donde desarrollo codigo, pero todo se despliega en una laptop con Ubuntu server que controlo mediante ssh:
```bash
ssh maru@192.168.1.35
Memr2026.
```
Dentro de esa laptop, en /opt/BioNews tengo los contenedores de Docker.
Afuera, en /opt/nginx-proxy/docker-compose.yml tengo lo siguiente:
```yml
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80'   # Tráfico HTTP
      - '81:81'   # Panel de Administración Web
      - '443:443' # Tráfico HTTPS
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - proxy_network

networks:
  proxy_network:
    external: true
```

Tienes prohibido hacer cualquier deploy o cambio directamente en el codigo de la laptop pero tienes permitido ejecutar comandos y ver los logs.
El readme esta un poco desactualizado, actualmente la bd es postgresql, no sqlite.
