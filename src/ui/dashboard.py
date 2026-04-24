import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_dashboard(fuentes_activas=None):
    db = DatabaseManager()
    # Traemos mas noticias de la DB para asegurarnos de tener suficientes al filtrar
    noticias_db = db.get_latest_news(limit=150)
    grid_noticias = ft.ResponsiveRow()

    IMG_DEFAULT = "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop"

    if not noticias_db:
        return ft.Column([ft.Text("Sin datos en la base de datos", size=16, italic=True)])

    noticias_filtradas = []
    for row in noticias_db:
        # row[4] es la fuente en la tabla de noticias
        fuente_db = str(row[4]).lower() 
        
        # Logica de filtrado
        if fuentes_activas is None:
            noticias_filtradas.append(row)
        else:
            # Revisa si alguna de las fuentes seleccionadas esta en el texto de la fuente de la DB
            if any(f.lower() in fuente_db for f in fuentes_activas):
                noticias_filtradas.append(row)

    if not noticias_filtradas:
        return ft.Column([ft.Text("No hay noticias para las fuentes seleccionadas.", size=16, italic=True)])

    for row in noticias_filtradas:
        link = row[0]
        titulo = row[1]
        fecha = row[2]
        imagen = row[3]
        fuente = row[4]
        
        img_url = imagen if (imagen and len(imagen) > 10) else IMG_DEFAULT

        # SOLUCION AL ERROR 1: async/await
        def create_open_url(url):
            async def open_url(e):
                await e.page.launch_url(url)
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