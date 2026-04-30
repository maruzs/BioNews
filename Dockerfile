# ============================================================
# BioNews Backend + Scheduler
# Imagen Python con Playwright + Chromium
# ============================================================

FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Dependencias del sistema para Playwright/Chromium
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.docker.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Chromium para Playwright
RUN playwright install chromium && playwright install-deps chromium

# Copiar código fuente
COPY server.py .
COPY scheduler.py .
COPY startScraping.py .
COPY src/ ./src/
COPY .env .env

# Crear directorio para datos
RUN mkdir -p /app/data /app/logs

# Exponer puerto del backend
EXPOSE 8000

# Por defecto arranca el backend FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
