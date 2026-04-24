import flet as ft
from ui.main_window import create_main_window

def main(page: ft.Page):
    # Configuracion basica de la ventana
    page.title = "BioNews - Inteligencia medioambiental"
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 900
    page.window.min_height = 600
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # Generar la estructura principal (navegacion, filtros y area de contenido)
    layout = create_main_window(page)

    # Anadir el layout a la pagina
    page.add(layout)

if __name__ == "__main__":
    # Iniciar la aplicacion de escritorio usando run() en lugar de app()
    ft.run(main)