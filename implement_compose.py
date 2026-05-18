import re

with open('docker-compose.yml', 'r', encoding='utf-8') as f:
    compose = f.read()

# Replace monolithic 'api' and add the microservices
new_services = '''
  # ── API Gateway Interno ──────────────────────────────────────────
  api-gateway:
    image: nginx:alpine
    container_name: bionews-gateway
    restart: unless-stopped
    volumes:
      - ./gateway/gateway.conf:/etc/nginx/conf.d/default.conf:ro
    networks:
      - bionews-net
      - proxy_network  # <- Conectado a la red de tu Nginx Proxy Manager
    expose:
      - "8000"

  # ── Microservicios FastAPI ───────────────────────────────────────
  auth-service:
    build: .
    container_name: bionews-auth-service
    command: uvicorn src.services.auth.main:app --host 0.0.0.0 --port 8001
    restart: unless-stopped
    volumes:
      - ./src:/app/src
      - /opt/BioNews/data:/app/data
      - /opt/BioNews/logs:/app/logs
      - /opt/BioNews/uploads:/app/uploads
      - /etc/localtime:/etc/localtime:ro
    networks:
      - bionews-net
    depends_on:
      postgres_db:
        condition: service_healthy
    environment:
      - POSTGRES_HOST=postgres_db
      - REDIS_URL=redis://redis_broker:6379/0

  news-service:
    build: .
    container_name: bionews-news-service
    command: uvicorn src.services.news.main:app --host 0.0.0.0 --port 8002
    restart: unless-stopped
    volumes:
      - ./src:/app/src
      - /opt/BioNews/data:/app/data
      - /opt/BioNews/logs:/app/logs
      - /etc/localtime:/etc/localtime:ro
    networks:
      - bionews-net
    depends_on:
      postgres_db:
        condition: service_healthy
    environment:
      - POSTGRES_HOST=postgres_db
      - REDIS_URL=redis://redis_broker:6379/0

  legal-service:
    build: .
    container_name: bionews-legal-service
    command: uvicorn src.services.legal.main:app --host 0.0.0.0 --port 8003
    restart: unless-stopped
    volumes:
      - ./src:/app/src
      - /opt/BioNews/data:/app/data
      - /opt/BioNews/logs:/app/logs
      - /etc/localtime:/etc/localtime:ro
    networks:
      - bionews-net
    depends_on:
      postgres_db:
        condition: service_healthy
    environment:
      - POSTGRES_HOST=postgres_db
      - REDIS_URL=redis://redis_broker:6379/0

  consultations-service:
    build: .
    container_name: bionews-consultations-service
    command: uvicorn src.services.consultations.main:app --host 0.0.0.0 --port 8004
    restart: unless-stopped
    volumes:
      - ./src:/app/src
      - /opt/BioNews/data:/app/data
      - /opt/BioNews/logs:/app/logs
      - /etc/localtime:/etc/localtime:ro
    networks:
      - bionews-net
    depends_on:
      postgres_db:
        condition: service_healthy
    environment:
      - POSTGRES_HOST=postgres_db
      - REDIS_URL=redis://redis_broker:6379/0
'''

# Remove `api`
compose = re.sub(r'  # ── Backend FastAPI ──────────────────────────────────────────\n  api:.*?(?=  # ── Scheduler de Scrapers ───────────────────────────────────)', new_services, compose, flags=re.DOTALL)

# Update scheduler depends_on
compose = compose.replace('''    depends_on:
      api:
        condition: service_healthy''', '''    depends_on:
      postgres_db:
        condition: service_healthy''')

# Update web depends_on
compose = compose.replace('''    depends_on:
      api:
        condition: service_healthy''', '''    depends_on:
      postgres_db:
        condition: service_healthy''')

with open('docker-compose.yml', 'w', encoding='utf-8') as f:
    f.write(compose)
print("Updated docker-compose.yml")
