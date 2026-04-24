import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_legal():
    db = DatabaseManager()
    documentos_db = db.get_all_legal() 
    
    lista_legal = ft.ListView(expand=True, spacing=10)

    if not documentos_db:
        return ft.Column([ft.Text("Sin registros legales en la base de datos", size=16, italic=True)])

    for row in documentos_db:
        link = row[0]
        titulo = row[1]
        fecha = row[2]
        institucion = row[4] if len(row) > 4 else "Institucion Legal"

        def create_open_url(url):
            def open_url(e):
                e.page.launch_url(url)
            return open_url

        tarjeta = ft.Card(
            content=ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text(institucion, size=12, color=COLOR_PRIMARIO, weight="bold"),
                    ft.Text(titulo, weight="bold", size=14),
                    ft.Text(fecha, size=11, italic=True),
                    ft.ElevatedButton(
                        "Abrir documento",
                        icon=ft.Icons.GAVEL,
                        on_click=create_open_url(link)
                    )
                ])
            )
        )
        lista_legal.controls.append(tarjeta)

    return ft.Column([
        ft.Row([ft.Text("Actualizaciones Legales", size=25, weight="bold", color=COLOR_PRIMARIO)]),
        ft.Divider(),
        lista_legal
    ], expand=True)