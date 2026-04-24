import flet as ft
import threading
from ui.dashboard import DashboardView
from ui.legal import LegalView

# Importar scrapers (Asegurate de que los nombres coincidan con tus archivos)
# from scrapers.sma import SMAScraper
# from scrapers.snifa import SnifaScraper

def main(page: ft.Page):
    page.title = "BioNews - Inteligencia Ambiental"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800
    page.padding = 0

    # Vistas
    vista_dashboard = DashboardView()
    # Cargamos LegalView bajo demanda para ahorrar recursos
    contenedor_principal = ft.Container(content=vista_dashboard, expand=True, padding=20)

    # --- DIALOGO DE PROGRESO ---
    texto_progreso = ft.Text("Esperando inicio...", size=16)
    barra_progreso = ft.ProgressRing(width=30, height=30)
    
    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sincronizando Base de Datos"),
        content=ft.Row([barra_progreso, texto_progreso], spacing=20, tight=True),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda _: setattr(dialogo, "open", False) or page.update())
        ],
    )

    def ejecutar_scraping():
        try:
            # Deshabilitar boton cerrar
            dialogo.actions[0].disabled = True
            page.update()

            # Aqui ejecutas tus funciones de scraping
            texto_progreso.value = "Consultando fuentes SMA..."
            page.update()
            # SMAScraper().get_latest_news()
            
            # Repetir para los demas...
            
            texto_progreso.value = "Proceso finalizado con exito."
        except Exception as e:
            texto_progreso.value = f"Error: {str(e)}"
        finally:
            barra_progreso.value = 1
            dialogo.actions[0].disabled = False
            page.update()

    def iniciar_sincronizacion(e):
        page.dialog = dialogo
        dialogo.open = True
        barra_progreso.value = None
        page.update()
        threading.Thread(target=ejecutar_scraping, daemon=True).start()

    # --- MENU Y NAVEGACION ---
    def cambio_ruta(e):
        index = e.control.selected_index
        if index == 0:
            contenedor_principal.content = vista_dashboard
        else:
            contenedor_principal.content = LegalView()
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon="article", selected_icon="article", label="Noticias"),
            ft.NavigationRailDestination(icon="gavel", selected_icon="gavel", label="Legal"),
        ],
        on_change=cambio_ruta,
    )

    # Boton de actualizar usando Container para evitar errores de FloatingActionButton
    boton_sync = ft.Container(
        content=ft.Row([
            ft.Icon("sync", color="white"),
            ft.Text("Actualizar", color="white", weight="bold")
        ], alignment="center", spacing=10),
        bgcolor="blue700",
        padding=12,
        border_radius=8,
        ink=True,
        on_click=iniciar_sincronizacion
    )

    page.add(
        ft.Row([
            ft.Column([rail, ft.Container(boton_sync, padding=10)], alignment="spaceBetween"),
            ft.VerticalDivider(width=1),
            contenedor_principal
        ], expand=True)
    )

if __name__ == "__main__":
    # Si ft.app lanza warning, flet.app(main) suele ser el estandar
    ft.app(target=main)