import flet as ft
from .styles import COLOR_PRIMARIO
from database.manager import DatabaseManager

def view_news():
    db = DatabaseManager()
    noticias_db = db.get_latest_news(limit=50) # Obtenemos las ultimas 50
    
    grid_noticias = ft.ResponsiveRow()

    if not noticias_db:
        return ft.Column([
            ft.Text("No hay noticias en la base de datos. Pulsa Actualizar.", size=16, italic=True)
        ])

    for row in noticias_db:
        # Estructura row: (link, titulo, fecha, imagen, fuente, fecha_scraping)
        link, titulo, fecha, imagen, fuente, _ = row
        
        # Si no hay imagen, usamos una por defecto
        img_url = imagen if imagen else "https://via.placeholder.com/400x200?text=BioNews"
        def open_url(e):
            e.page.launch_url(link)
        grid_noticias.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column([
                        ft.Image(src=img_url, border_radius=10, height=150, fit="cover"),
                        ft.Text(fuente, size=12, color=COLOR_PRIMARIO, weight="bold"),
                        ft.Text(titulo, weight="bold", size=14, max_lines=2, overflow="ellipsis"),
                        ft.Text(fecha, size=11, italic=True),
                        ft.ElevatedButton(
                            "Ver detalles", 
                            icon=ft.Icons.OPEN_IN_NEW,
                            on_click=open_url # Referencia a la funcion interna
                        )
                    ])
                ),
                col={"sm": 12, "md": 6, "lg": 4}
            )
        )

    return ft.Column([
        ft.Row([
            ft.Text("Noticias Recientes", size=25, weight="bold", color=COLOR_PRIMARIO),
            ft.IconButton(ft.Icons.REFRESH, on_click=lambda e: e.page.update()) # Placeholder para refrescar
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(),
        ft.ListView(expand=True, controls=[grid_noticias])
    ], expand=True)