import flet as ft
import os
import sys
import ssl
import certifi
from ui.main_window import create_main_window

# Configuracion de seguridad SSL para evitar errores de certificados en otros PCs
try:
    os.environ['SSL_CERT_FILE'] = certifi.where()
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
    ssl._create_default_https_context = ssl._create_unverified_context
except Exception:
    pass

# Configuracion global de rutas para Playwright
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.abspath(".")

# Indicamos a Playwright donde buscar sus controladores si los necesita de forma interna
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(base_path, "pw-browser")

def main(page: ft.Page):
    page.title = "BioNews - Inteligencia medioambiental"
    page.window.icon = "planet-earth.ico" 
    
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 900
    page.window.min_height = 600
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    layout = create_main_window(page)
    page.add(layout)

if __name__ == "__main__":
    # assets_dir permite que Flet encuentre el icono y las imagenes locales
    ft.run(main, assets_dir="assets")