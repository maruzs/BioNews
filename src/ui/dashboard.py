import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_dashboard():
    db = DatabaseManager()
    data_legal = db.get_all_legal(limit=50)
    
    tabla = ft.DataTable(
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
        # link, nombre, fecha, estado, tipo, fuente, fecha_scraping
        link_url = row[0]
        
        async def handle_click(e, url=link_url):
            await e.page.launch_url(url)

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row[1], width=300)),
                    ft.DataCell(ft.Text(row[2])),
                    ft.DataCell(ft.Text(row[3])),
                    ft.DataCell(ft.Text(row[4])),
                    ft.DataCell(ft.Text(row[5])),
                    ft.DataCell(ft.IconButton(ft.Icons.OPEN_IN_NEW, on_click=handle_click)),
                ]
            )
        )

    return ft.Column([
        ft.Text("Dashboard de Seguimiento Legal", size=25, weight="bold", color=COLOR_PRIMARIO),
        ft.Divider(),
        ft.ListView(expand=True, controls=[tabla])
    ], scroll=ft.ScrollMode.ADAPTIVE)