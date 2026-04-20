import flet as ft
from .styles import COLOR_PRIMARIO
from database.manager import DatabaseManager

def view_dashboard():
    db = DatabaseManager()
    data_legal = db.get_all_legal()
    
    tabla = ft.DataTable(
        heading_row_color=ft.Colors.BLACK12,
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight="bold")),
            ft.DataColumn(ft.Text("Fecha", weight="bold")),
            ft.DataColumn(ft.Text("Estado", weight="bold")),
            ft.DataColumn(ft.Text("Tipo", weight="bold")),
            ft.DataColumn(ft.Text("Fuente", weight="bold")),
            ft.DataColumn(ft.Text("Detalle", weight="bold")),
        ],
        rows=[]
    )

    for row in data_legal:
        # row: (link, nombre, fecha, estado, tipo, fuente, fecha_scraping)
        link, nombre, fecha, estado, tipo, fuente, _ = row
        
        async def open_link(e, url=link):
            await e.page.launch_url(url)

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(nombre, max_lines=1)),
                    ft.DataCell(ft.Text(fecha)),
                    ft.DataCell(ft.Text(estado)),
                    ft.DataCell(ft.Text(tipo)),
                    ft.DataCell(ft.Text(fuente)),
                    ft.DataCell(
                        ft.IconButton(
                            ft.Icons.OPEN_IN_NEW, 
                            icon_color=COLOR_PRIMARIO,
                            on_click=open_link
                        )
                    ),
                ]
            )
        )

    return ft.Column([
        ft.Text("Dashboard de Seguimiento Legal", size=25, weight="bold", color=COLOR_PRIMARIO),
        ft.Divider(),
        ft.ListView(expand=True, controls=[tabla])
    ], expand=True)