import flet as ft
import ssl
import os
import sys
import certifi

# Añadimos la raíz del proyecto al path para que las importaciones funcionen correctamente
# tanto en desarrollo como al compilar con PyInstaller.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.main_window import create_main_window

# --- SOLUCION PARA OTROS COMPUTADORES ---
# Este comando ignora la verificacion de certificados SSL. 
# Es vital porque en muchos PCs los certificados de Python estan desactualizados
# y eso impide que Flet descargue su motor de ejecucion.
# ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

def main(page: ft.Page):
    page.title = "BioNews - Inteligencia medioambiental"
    
    # Configuracion del Icono
    # Al usar assets_dir="assets" en ft.run, Flet busca aqui directamente.
    page.window.icon = "planet-earth.ico" 
    
    # Dimensiones de la ventana
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 900
    page.window.min_height = 600
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # Cargar la interfaz
    layout = create_main_window(page)
    page.add(layout)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    
    # assets_dir le dice a Flet que busque imagenes e iconos en esa carpeta absoluta
    ft.run(main, assets_dir=ASSETS_DIR)