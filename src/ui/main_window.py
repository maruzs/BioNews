import flet as ft
from ui.dashboard import view_dashboard
from ui.legal import view_legal
from ui.sync import view_sync  # Nueva importacion
from ui.styles import COLOR_PRIMARIO, COLOR_FONDO

def create_main_window(page: ft.Page):
    content_area = ft.Container(
        expand=True,
        content=view_dashboard() 
    )

    chk_mma = ft.Checkbox(label="MMA", value=True, active_color=COLOR_PRIMARIO)
    chk_sea = ft.Checkbox(label="SEA", value=True, active_color=COLOR_PRIMARIO)
    chk_sma = ft.Checkbox(label="SMA / SNIFA", value=True, active_color=COLOR_PRIMARIO)
    chk_corte = ft.Checkbox(label="Corte Suprema", value=True, active_color=COLOR_PRIMARIO)
    chk_tribunales = ft.Checkbox(label="Tribunales Amb.", value=True, active_color=COLOR_PRIMARIO)
    chk_diario = ft.Checkbox(label="Diario Oficial", value=True, active_color=COLOR_PRIMARIO)
    chk_sbap = ft.Checkbox(label="SBAP", value=True, active_color=COLOR_PRIMARIO)


    def apply_filters(e):
        fuentes_activas = []
        if chk_mma.value: fuentes_activas.append("MMA")
        if chk_sea.value: fuentes_activas.append("SEA")
        if chk_sma.value: 
            fuentes_activas.append("SMA")
            fuentes_activas.append("SNIFA")
        if chk_corte.value: fuentes_activas.append("Corte Suprema")
        if chk_tribunales.value: fuentes_activas.append("Tribunal") 
        if chk_diario.value: fuentes_activas.append("Diario Oficial")
        if chk_sbap.value: fuentes_activas.append("SBAP")

        content_area.content = view_dashboard(fuentes_activas)
        content_area.update()

    def change_view(e):
        index = e.control.selected_index
        if index == 0:
            content_area.content = view_dashboard()
            filtros_panel.visible = True
        elif index == 1:
            content_area.content = view_legal()
            filtros_panel.visible = False 
        elif index == 2:
            # Nueva logica para la pestana de Sincronizacion
            content_area.content = view_sync()
            filtros_panel.visible = False
        
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.DASHBOARD,
                label="Noticias",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.GAVEL_OUTLINED,
                selected_icon=ft.Icons.GAVEL,
                label="Legal",
            ),
            # Nueva opcion de Sincronizacion
            ft.NavigationRailDestination(
                icon=ft.Icons.SYNC_OUTLINED,
                selected_icon=ft.Icons.SYNC,
                label="Sincronizar",
            ),
            # Nueva opcion de favoritos
        ],
        on_change=change_view,
    )

    filtros_panel = ft.Container(
        width=200,
        padding=10,
        visible=True, 
        content=ft.Column([
            ft.Text("Filtros de Noticias", weight="bold", size=16),
            chk_mma,
            chk_sea,
            chk_sma,
            chk_corte,
            chk_tribunales,
            chk_diario,
            chk_sbap,
            ft.Container(height=20),
            ft.ElevatedButton(
                "Aplicar Filtros", 
                bgcolor=COLOR_PRIMARIO, 
                color=ft.Colors.WHITE,
                on_click=apply_filters
            )
        ])
    )

    layout = ft.Row([
        rail,
        ft.VerticalDivider(width=1),
        filtros_panel,
        ft.VerticalDivider(width=1),
        content_area
    ], expand=True)

    return layout