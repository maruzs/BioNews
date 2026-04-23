import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO, COLOR_SECUNDARIO

def view_dashboard():
    db = DatabaseManager()
    # Obtenemos los datos legales de la DB
    data_legal = db.get_all_legal(limit=50)
    
    tabla = ft.DataTable(
        # Ajustes para que no se vea apretado
        data_row_min_height=60,
        data_row_max_height=80,
        column_spacing=25,
        heading_row_color=ft.Colors.with_opacity(0.1, ft.Colors.GREY),
        divider_thickness=0.5,
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight="bold")),
            ft.DataColumn(ft.Text("Fecha", weight="bold")),
            ft.DataColumn(ft.Text("Estado", weight="bold")),
            ft.DataColumn(ft.Text("Tipo", weight="bold")),
            ft.DataColumn(ft.Text("Fuente", weight="bold")),
            ft.DataColumn(ft.IconButton(ft.Icons.SETTINGS, disabled=True)), # Columna de acciones
        ],
        rows=[]
    )

    for row in data_legal:
        link_url = row[0]
        
        async def handle_click(e, url=link_url):
            await e.page.launch_url(url)

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    # Cambio de ft.padding.vertical a ft.padding.symmetric
                    ft.DataCell(
                        ft.Container(
                            ft.Text(row[1], width=350, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            padding=ft.padding.symmetric(vertical=10)
                        )
                    ),
                    ft.DataCell(ft.Text(row[2])),
                    ft.DataCell(ft.Text(row[3])),
                    ft.DataCell(ft.Text(row[4])),
                    ft.DataCell(ft.Text(row[5])),
                    ft.DataCell(
                        ft.IconButton(
                            ft.Icons.OPEN_IN_NEW, 
                            on_click=handle_click,
                            icon_color=COLOR_PRIMARIO
                        )
                    ),
                ]
            )
        )

    return ft.Column([
        ft.Text("Dashboard de Seguimiento Legal", size=28, weight="bold", color=COLOR_PRIMARIO),
        ft.Divider(height=10, thickness=1),
        ft.ListView(expand=True, controls=[tabla], spacing=10)
    ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)