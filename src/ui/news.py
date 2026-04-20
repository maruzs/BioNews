import flet as ft
from .styles import COLOR_PRIMARIO
from database.manager import DatabaseManager

def view_news():
    db = DatabaseManager()
    noticias_db = db.get_latest_news(limit=50) 
    grid_noticias = ft.ResponsiveRow()

    # Imagen ecologica por defecto
    IMG_DEFAULT = "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop"

    if not noticias_db:
        return ft.Column([ft.Text("Sin datos en DB", size=16, italic=True)])

    for row in noticias_db:
        link, titulo, fecha, imagen, fuente, _ = row
        img_url = imagen if (imagen and len(imagen) > 10) else IMG_DEFAULT

        # El click SI debe ser awaitable
        async def open_url(e, url_to_open=link):
            await e.page.launch_url(url_to_open)

        grid_noticias.controls.append(
            ft.Card(
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
                        ft.Text(titulo, weight="bold", size=14, max_lines=2, overflow="ellipsis"),
                        ft.Text(fecha, size=11, italic=True),
                        ft.ElevatedButton(
                            "Ver detalles", 
                            icon=ft.Icons.OPEN_IN_NEW,
                            on_click=open_url
                        )
                    ])
                ),
                col={"sm": 12, "md": 6, "lg": 4}
            )
        )

    return ft.Column([
        ft.Row([ft.Text("Noticias Recientes", size=25, weight="bold", color=COLOR_PRIMARIO)]),
        ft.Divider(),
        ft.ListView(expand=True, controls=[grid_noticias])
    ], expand=True)