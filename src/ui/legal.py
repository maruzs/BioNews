import flet as ft
from database.manager import DatabaseManager

class LegalView(ft.Column):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.expand = True

        # Sub-pestanas SNIFA
        self.tabs_snifa = ft.Tabs(
            selected_index=0,
            expand=True,
            tabs=[
                ft.Tab(text="Sancionatorios", content=self.generar_lista("SNIFA", "Sancionatorio")),
                ft.Tab(text="Ingreso SEIA", content=self.generar_lista("SNIFA", "Ingreso SEIA")),
                ft.Tab(text="Fiscalizaciones", content=self.generar_lista("SNIFA", "Fiscalizacion")),
            ]
        )

        # Pestanas Principales
        self.tabs_main = ft.Tabs(
            selected_index=0,
            expand=True,
            tabs=[
                ft.Tab(text="Tribunales", content=self.generar_lista("Tribunales")),
                ft.Tab(text="SNIFA", content=self.tabs_snifa),
                ft.Tab(text="SEA", content=self.generar_lista("SEA")),
            ]
        )

        self.controls = [
            ft.Text("Legal y Transparencia", size=24, weight="bold"),
            self.tabs_main
        ]

    def generar_lista(self, fuente_grupo, tipo_especifico=None):
        lista = ft.ListView(expand=True, spacing=10, padding=10)
        
        # Obtenemos datos (Asegurate de que el metodo sea get_all_legal)
        data = self.db.get_all_legal()
        
        fuentes_tribunales = ["1TA", "2TA", "3TA", "Corte Suprema"]
        
        for item in data:
            # Filtro por grupo
            if fuente_grupo == "Tribunales" and item[4] not in fuentes_tribunales:
                continue
            if fuente_grupo != "Tribunales" and item[4] != fuente_grupo:
                continue
                
            # Filtro por tipo (para SNIFA)
            if tipo_especifico and tipo_especifico not in item[3]:
                continue

            lista.controls.append(
                ft.ListTile(
                    title=ft.Text(item[0], weight="bold"),
                    subtitle=ft.Text(f"{item[3]} | {item[2]} | {item[1]}"),
                    trailing=ft.IconButton("open_in_new", url=item[5]),
                )
            )
        
        return lista