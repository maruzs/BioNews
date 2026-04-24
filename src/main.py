import flet as ft
import threading

# Importamos las vistas
from ui.dashboard import DashboardView
from ui.legal import LegalView

# Importar tus scrapers (Ajusta los nombres segun tu test_all.py)
from scrapers.sma import SMAScraper
from scrapers.snifa import SnifaScraper
from scrapers.reqSEIA import SnifaIngresoScraper
from scrapers.fiscalizaciones import SnifaFiscalizacionScraper
# etc...

def main(page: ft.Page):
    page.title = "BioNews - Inteligencia Ambiental"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = 1200
    page.window_height = 800

    # Instancias de las vistas
    vista_dashboard = DashboardView()
    vista_legal = LegalView()

    # Contenedor principal donde cambiaremos el contenido
    contenedor_principal = ft.Container(
        content=vista_dashboard,
        expand=True,
        padding=20
    )

    # --- LOGICA DE SCRAPING CON INTERFAZ ---
    texto_progreso = ft.Text("Iniciando sincronizacion...", size=16)
    barra_progreso = ft.ProgressRing()
    
    dialogo_sincronizacion = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sincronizando Base de Datos"),
        content=ft.Column([
            barra_progreso,
            texto_progreso
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, height=150),
        actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo())],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def cerrar_dialogo():
        dialogo_sincronizacion.open = False
        page.update()
        # Recargamos las vistas para que muestren los datos nuevos
        vista_dashboard.cargar_noticias()
        # Al recargar legal, se tendra que re-instanciar o crear un metodo cargar_legal()

    def ejecutar_scrapers():
        # Deshabilitamos el boton cerrar mientras carga
        dialogo_sincronizacion.actions[0].disabled = True
        page.update()

        try:
            # --- RUTINA DE SCRAPERS ---
            texto_progreso.value = "Consultando noticias SMA..."
            page.update()
            SMAScraper().get_latest_news()

            texto_progreso.value = "Consultando SNIFA Sancionatorios..."
            page.update()
            SnifaScraper().get_legal_data()

            texto_progreso.value = "Consultando SNIFA Requisitos Ingreso..."
            page.update()
            SnifaIngresoScraper().get_legal_data()

            texto_progreso.value = "Consultando SNIFA Fiscalizaciones..."
            page.update()
            SnifaFiscalizacionScraper().get_legal_data()
            
            # (Anade aqui el resto de tus scrapers)

            texto_progreso.value = "Sincronizacion completada con exito."
        except Exception as e:
            texto_progreso.value = f"Error en sincronizacion: {e}"
        finally:
            # Habilitar boton de cerrar y detener anillo
            dialogo_sincronizacion.actions[0].disabled = False
            barra_progreso.value = 1 
            page.update()

    def iniciar_sincronizacion(e):
        page.dialog = dialogo_sincronizacion
        dialogo_sincronizacion.open = True
        barra_progreso.value = None # Que gire indefinidamente
        page.update()
        
        # Usamos un hilo para no congelar la aplicacion mientras hace web scraping
        hilo = threading.Thread(target=ejecutar_scrapers)
        hilo.start()


    # --- NAVEGACION LATERAL ---
    def cambiar_pestana(e):
        if e.control.selected_index == 0:
            contenedor_principal.content = vista_dashboard
        elif e.control.selected_index == 1:
            # Es recomendable re-instanciar la vista legal al entrar para asegurar datos frescos
            contenedor_principal.content = LegalView() 
            
        page.update()

    menu_lateral = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.ARTICLE_OUTLINED, selected_icon=ft.icons.ARTICLE, label="Noticias"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ACCOUNT_BALANCE_OUTLINED, selected_icon=ft.icons.ACCOUNT_BALANCE, label="Legal"
            ),
        ],
        on_change=cambiar_pestana,
    )

    # Boton de sincronizacion en la barra de navegacion
    boton_sincronizar = ft.FloatingActionButton(
        icon=ft.icons.SYNC,
        text="Actualizar BD",
        on_click=iniciar_sincronizacion,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE
    )

    # Layout final
    layout = ft.Row(
        [
            ft.Column([menu_lateral, ft.Container(boton_sincronizar, padding=20)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.VerticalDivider(width=1),
            contenedor_principal
        ],
        expand=True,
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)