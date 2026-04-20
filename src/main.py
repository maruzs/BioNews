import flet as ft
from ui.dashboard import view_dashboard
from ui.news import view_news

async def main(page: ft.Page):
    page.title = "BioNews - Monitoreo Ambiental"
    page.padding = 0
    page.spacing = 0
    
    container_principal = ft.Container(expand=True, padding=20)

    async def cambiar_pestana(e):
        index = e.control.selected_index
        if index == 0:
            container_principal.content = view_dashboard()
        elif index == 1:
            container_principal.content = view_news()
        elif index == 2:
            container_principal.content = ft.Text("Seccion por Pagina - Pendiente")
        page.update() # Quitamos await: es sincrono en 0.84.0

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME_OUTLINED, label="Inicio"),
            ft.NavigationRailDestination(icon=ft.Icons.ARTICLE_OUTLINED, label="Noticias"),
            ft.NavigationRailDestination(icon=ft.Icons.WEB_OUTLINED, label="Fuentes"),
        ],
        on_change=cambiar_pestana
    )

    # Quitamos await de add: devuelve None
    
    page.add(
        ft.Row([
            rail,
            ft.VerticalDivider(width=1),
            container_principal
        ], expand=True)
    )
    
    container_principal.content = view_dashboard()
    page.update()

if __name__ == "__main__":
    ft.run(main)