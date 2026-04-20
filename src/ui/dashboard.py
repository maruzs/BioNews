import flet as ft
from .styles import COLOR_PRIMARIO

def view_dashboard():
    # Tabla con la estructura: Nombre|Fecha|Estado|Tipo|Fuente|Detalle
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

    tabla.rows.append(
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("Proyecto Minero")),
                ft.DataCell(ft.Text("2026-04-20")),
                ft.DataCell(ft.Text("En Calificacion")),
                ft.DataCell(ft.Text("Pertinencia")),
                ft.DataCell(ft.Text("SEA")),
                ft.DataCell(ft.IconButton(ft.Icons.OPEN_IN_BROWSER, icon_color=COLOR_PRIMARIO))
            ]
        )
    )

    return ft.Column([
        ft.Text("Dashboard de Seguimiento Legal", size=25, weight="bold", color=COLOR_PRIMARIO),
        ft.Divider(),
        ft.ListView(expand=True, controls=[tabla])
    ], expand=True)