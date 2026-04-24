import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_dashboard():
    db = DatabaseManager()
    noticias_db = db.get_latest_news(limit=50)
    grid_noticias = ft.ResponsiveRow()

    IMG_DEFAULT = "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop"

    if not noticias_db:
        return ft.Column([ft.Text("Sin datos en la base de datos", size=16, italic=True)])

    for row in noticias_db:
        link = row[0]
        titulo = row[1]
        fecha = row[2]
        imagen = row[3]
        fuente = row[4]
        
        img_url = imagen if (imagen and len(imagen) > 10) else IMG_DEFAULT

        def create_open_url(url):
            def open_url(e):
                e.page.launch_url(url)
            return open_url

        tarjeta = ft.Card(
            content=ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Image(
                        src=img_url,
                        border_radius=10,
                        height=150,
                        fit="cover",
                        error_content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED)
                    ),
                    ft.Text(fuente, size=12, color=COLOR_PRIMARIO, weight="bold"),
                    ft.Text(
                        titulo, 
                        weight="bold", 
                        size=14, 
                        max_lines=2, 
                        overflow="ellipsis"
                    ),
                    ft.Text(fecha, size=11, italic=True),
                    ft.ElevatedButton(
                        "Ver en navegador",
                        icon=ft.Icons.OPEN_IN_NEW,
                        on_click=create_open_url(link)
                    )
                ])
            ),
            col={"sm": 12, "md": 6, "lg": 4}
        )
        grid_noticias.controls.append(tarjeta)

    return ft.Column([
        ft.Row([ft.Text("Dashboard - Noticias Recientes", size=25, weight="bold", color=COLOR_PRIMARIO)]),
        ft.Divider(),
        ft.ListView(expand=True, controls=[grid_noticias])
    ], expand=True)