# 📱 Tutorial: Convertir BioNews en App Móvil con CapacitorJS

Este tutorial te guiará paso a paso para empaquetar la aplicación frontend React de **BioNews** en una aplicación móvil nativa para Android usando **CapacitorJS**. Este enfoque híbrido aprovecha el 100% de la interfaz existente sin necesidad de reescribir código.

---

## Prerrequisitos en tu Computador (Local)
1.  **Node.js** (versión 18 o superior).
2.  **Android Studio** instalado (necesario para compilar el archivo `.apk` final).
3.  **SDK de Android** configurado en tu sistema.

---

## Paso 1: Generar el build de producción de React

Antes de empaquetar, debes generar la versión optimizada de producción del frontend:

1.  Abre una consola y dirígete al directorio de la aplicación web:
    ```bash
    cd web
    ```
2.  Instala las dependencias si no lo has hecho:
    ```bash
    npm install
    ```
3.  Ejecuta el script de compilación:
    ```bash
    npm run build
    ```
    *Nota: Esto creará una carpeta llamada `dist` dentro del directorio `web`, la cual contiene todos los archivos HTML, CSS y JS optimizados.*

---

## Paso 2: Instalar e Inicializar CapacitorJS

Instalaremos Capacitor directamente en tu proyecto frontend:

1.  Instala el núcleo y la interfaz de comandos (CLI) de Capacitor en la carpeta `web`:
    ```bash
    npm install @capacitor/core @capacitor/cli
    ```
2.  Inicializa la configuración de la App:
    ```bash
    npx cap init BioNews com.bionews.app --web-dir=dist
    ```
    *   **App name:** `BioNews`
    *   **App Package ID:** `com.bionews.app` (identificador único para Google Play)
    *   **Web asset directory:** `dist`

---

## Paso 3: Agregar la plataforma Android

1.  Instala el paquete de Android para Capacitor:
    ```bash
    npm install @capacitor/android
    ```
2.  Agrega la carpeta de la plataforma nativa de Android a tu proyecto:
    ```bash
    npx cap add android
    ```
    *Esto creará un subdirectorio llamado `android/` en tu carpeta `web` que contiene un proyecto nativo completo de Android Studio.*

---

## Paso 4: Sincronizar el Frontend con Android

Cada vez que hagas un cambio en tus archivos React o quieras actualizar la app, debes sincronizar la carpeta `dist` con el código nativo:

1.  Vuelve a compilar el frontend (si hiciste cambios):
    ```bash
    npm run build
    ```
2.  Sincroniza los archivos compilados con Capacitor:
    ```bash
    npx cap sync
    ```

---

## Paso 5: Compilar el APK en Android Studio

1.  Abre el proyecto de Android Studio directamente desde la consola:
    ```bash
    npx cap open android
    ```
2.  Espera a que Android Studio cargue el proyecto y descargue los archivos de Gradle (puede tardar unos minutos la primera vez).
3.  Para probar en un emulador o en tu propio teléfono:
    *   Conecta tu teléfono por USB con la **Depuración USB** activada.
    *   Presiona el botón **Run** (ícono de play verde 🟢) en Android Studio.
4.  Para generar el archivo de instalación final (`.apk`):
    *   En el menú superior de Android Studio ve a: **Build** > **Build Bundle(s) / APK(s)** > **Build APK(s)**.
    *   Una vez finalice, aparecerá un aviso en la esquina inferior derecha. Haz clic en **Locate** para encontrar tu archivo `app-debug.apk` listo para instalar en cualquier teléfono.

---

## ⚡ Recomendación para llamadas a la API (CORS y URLs)

Dado que la app móvil no corre sobre `http://localhost:5173` sino bajo el protocolo interno `capacitor://localhost`, asegúrate de:

1.  **Configurar la URL Base:** En el frontend, la URL de Axios o Fetch para apuntar al backend no debe ser relativa. Debe apuntar a la IP pública de tu servidor o dominio de producción (ej: `https://api.bionews.cl`).
2.  **CORS:** Asegúrate de agregar el origen `"http://localhost"` a tu variable `CORS_ALLOWED_ORIGINS` en el archivo `.env` de tu backend (Capacitor usa `http://localhost` internamente para simular la web en dispositivos Android).
