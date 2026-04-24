import flet as ft
from database.manager import DatabaseManager

class LegalView(ft.Column):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.expand = True
        
        # Sub-pestanas para SNIFA
        self.snifa_tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            expand=True,
            tabs=[
                ft.Tab(text="Sancionatorios", content=self.construir_lista(["SNIFA"], "Sancionatorio")),
                ft.Tab(text="Requisitos Ingreso", content=self.construir_lista(["SNIFA"], "Ingreso SEIA")),
                ft.Tab(text="Fiscalizaciones", content=self.construir_lista(["SNIFA"], "Fiscalizacion"))
            ]
        )

        # Pestanas principales
        self.main_tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            expand=True,
            tabs=[
                ft.Tab(text="Tribunales", content=self.construir_lista(["1TA", "2TA", "3TA", "Corte Suprema"])),
                ft.Tab(text="SNIFA", content=ft.Container(content=self.snifa_tabs, padding=ft.padding.only(top=10))),
                ft.Tab(text="SEA (Pertinencias)", content=self.construir_lista(["SEA"]))
            ]
        )
        
        self.controls = [
            ft.Text("Legal y Transparencia", size=24, weight=ft.FontWeight.BOLD),
            self.main_tabs
        ]

    def construir_lista(self, fuentes_permitidas, filtro_tipo=None):
        lista = ft.ListView(expand=True, spacing=10, padding=10)
        
        # Obtenemos los datos legales de la base de datos
        datos = self.db.get_all_legal() 
        
        for item in datos:
            nombre = item[0]
            fecha = item[1]
            estado = item[2]
            tipo = item[3]
            fuente = item[4]
            link = item[5]
            
            # Aplicamos los filtros correspondientes a la pestana
            if fuente not in fuentes_permitidas:
                continue
                
            if filtro_tipo and filtro_tipo not in tipo:
                continue

            # Determinamos color del estado para hacerlo mas visual
            color_estado = ft.colors.GREEN_700 if "Terminado" in estado or "Resuelto" in estado else ft.colors.ORANGE_700

            lista.controls.append(
                ft.Card(
                    elevation=2,
                    content=ft.ListTile(
                        leading=ft.Icon(ft.icons.GAVEL if fuente != "SEA" else ft.icons.NATURE_PEOPLE),
                        title=ft.Text(nombre, weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"Tipo: {tipo} | Estado: {estado} | Fecha: {fecha}"),
                        trailing=ft.IconButton(
                            icon=ft.icons.OPEN_IN_NEW, 
                            tooltip="Ver detalle oficial",
                            url=link
                        )
                    )
                )
            )
            
        if not lista.controls:
            lista.controls.append(ft.Text("No hay registros disponibles para esta seccion.", padding=20))
            
        return lista