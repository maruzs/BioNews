import flet as ft
from database.manager import DatabaseManager

class DashboardView(ft.Column):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.expand = True
        self.spacing = 20
        
        self.fuentes = ["SMA", "SEA", "Corte Suprema", "Tercer Tribunal", "MMA"]
        self.seleccionadas = self.fuentes.copy()

        self.lista_noticias = ft.ListView(expand=True, spacing=10)
        
        # Filtros
        opciones_filtros = ft.Row(wrap=True, controls=[
            ft.Checkbox(label=f, value=True, data=f, on_change=self.toggle_filtro) 
            for f in self.fuentes
        ])

        self.controls = [
            ft.Text("Noticias Ambientales", size=24, weight="bold"),
            opciones_filtros,
            ft.Divider(),
            self.lista_noticias
        ]

    def did_mount(self):
        # Se ejecuta cuando el control se agrega a la pagina
        self.cargar_datos()

    def toggle_filtro(self, e):
        fuente = e.control.data
        if e.control.value:
            if fuente not in self.seleccionadas: self.seleccionadas.append(fuente)
        else:
            if fuente in self.seleccionadas: self.seleccionadas.remove(fuente)
        self.cargar_datos()

    def cargar_datos(self):
        self.lista_noticias.controls.clear()
        # Asegurate de que el metodo en manager.py sea get_news()
        data = self.db.get_latest_news()
        
        filtradas = [n for n in data if n[4] in self.seleccionadas]
        
        for item in filtradas:
            self.lista_noticias.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Column([
                            ft.Text(item[4], color="blue700", size=12, weight="bold"),
                            ft.Text(item[0], size=16, weight="w500"),
                            ft.Row([
                                ft.Text(item[1], color="grey"),
                                ft.TextButton("Abrir", icon="open_in_new", url=item[2])
                            ], alignment="spaceBetween")
                        ])
                    )
                )
            )
        self.update()