## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.
Siempre revisa bien el codigo antes de confirmar, muchas veces hay problemas de identacion/sintaxis (corchetes, <div> no cerrado, puntoycoma, etc) Sobretodo en lo que son los archivos .tsx

## INSTRUCCION

Quiero convertir este proyecto de monolito a microservicios, pero eso lo vere despues, de momento lo que me interesa primero que nada es migrar la base de datos y todo lo que eso conlleve.

Actualment estoy con SQLite en data/data.db pero quiero pasar a PostgreSQL en un servidor local usando docker.

Me gustaria dividir la actual en las siguientes db:

1. DB Usuarios:
   - favoritos
   - users
   - user_item_views
   - user_category_views
   - bug_reports
     basicamente todo lo relacionado a usuarios, sus perfiles, visitas, vistos (para las notificaciones), preferencias para el filtrado, etc.

2. DB Scrapers:
   - Noticias
   - pertinencias
   - sea_proyectos_evaluados
   - normativas
   - fiscalizaciones
   - medidas_provisionales
   - programasDeCumplimiento
   - registroSanciones
   - requerimientos
   - sancionatorios
   - Tribunales
   - dga_consultas
   - documentos
   - minsal_resultados
   - minsal_vigentes
   - mma_abiertas
   - mma_cerradas
   - scraper_logs

Hay varias de esas cosas que estan relacionadas entre si, ve como solucionarlo.
Sobre el ORM usa el que prefieras, pero que funcione. Cuidado con muchas cosas ya que src/database/manager.py es medio extrano, sobretodo por los formatos de las cosas (fechas por ejemplo)

Ademas debes decirme como implementar los cambios en mi servidor (Es una laptop con Ubuntu Server con docker y docker-compose)

Actualmente uso un nginx proxy manager para la salida a la web, este es su docker compose:

```yaml
services:
  app:
    image: "jc21/nginx-proxy-manager:latest"
    restart: unless-stopped
    ports:
      - "80:80" # Tráfico HTTP
      - "81:81" # Panel de Administración Web
      - "443:443" # Tráfico HTTPS
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - proxy_network

networks:
  proxy_network:
    external: true
```
