import flet as ft
from database.manager import DatabaseManager

class DashboardView(ft.Column):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.expand = True
        self.spacing = 20
        
        # Fuentes de noticias conocidas
        self.fuentes_disponibles = ["SMA", "SEA", "Corte Suprema", "Tercer Tribunal", "MMA"]
        self.fuentes_seleccionadas = self.fuentes_disponibles.copy()

        # Contenedor de las tarjetas de noticias
        self.news_list = ft.ListView(expand=True, spacing=15, padding=10)
        
        # Generar controles de filtro
        checkboxes = []
        for fuente in self.fuentes_disponibles:
            cb = ft.Checkbox(
                label=fuente, 
                value=True, 
                on_change=self.filtrar_noticias,
                data=fuente
            )
            checkboxes.append(cb)

        self.filtros_row = ft.Row(controls=checkboxes, wrap=True)

        self.controls = [
            ft.Text("Noticias Ambientales", size=24, weight=ft.FontWeight.BOLD),
            self.filtros_row,
            ft.Divider(),
            self.news_list
        ]
        
        self.cargar_noticias()

    def filtrar_noticias(self, e):
        # Actualizar la lista de fuentes seleccionadas
        fuente = e.control.data
        if e.control.value:
            if fuente not in self.fuentes_seleccionadas:
                self.fuentes_seleccionadas.append(fuente)
        else:
            if fuente in self.fuentes_seleccionadas:
                self.fuentes_seleccionadas.remove(fuente)
                
        self.cargar_noticias()

    def cargar_noticias(self):
        self.news_list.controls.clear()
        
        # Asumiendo que get_all_news devuelve todas las noticias de la BD
        # Ajusta este llamado segun la estructura exacta de tu DatabaseManager
        todas_las_noticias = self.db.get_all_news() 
        
        noticias_filtradas = [n for n in todas_las_noticias if n[4] in self.fuentes_seleccionadas]

        if not noticias_filtradas:
            self.news_list.controls.append(ft.Text("No hay noticias para las fuentes seleccionadas."))
        else:
            for noticia in noticias_filtradas:
                titulo = noticia[0]
                fecha = noticia[1]
                link = noticia[2]
                fuente = noticia[4]
                
                card = ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Column([
                            ft.Row([
                                ft.Text(fuente, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
                                ft.Text(fecha, color=ft.colors.GREY_500)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Text(titulo, size=16, weight=ft.FontWeight.W_500),
                            ft.TextButton("Leer noticia", url=link, icon=ft.icons.OPEN_IN_NEW)
                        ])
                    )
                )
                self.news_list.controls.append(card)
        
        self.update()