import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_legal():
    db = DatabaseManager()
    # Se aumenta el limite para capturar todos los registros de las fuentes
    documentos_db = db.get_all_legal(limit=2000) 
    
    sea_docs = []
    snifa_docs = []
    tribunales_docs = []

    for row in documentos_db:
        # Estructura: (link[0], nombre[1], fecha[2], estado[3], tipo[4], fuente[5])
        fuente_str = str(row[5]).lower() if len(row) > 5 else ""
        
        if "sea" in fuente_str:
            sea_docs.append(row)
        elif "snifa" in fuente_str or "sma" in fuente_str:
            snifa_docs.append(row)
        elif any(x in fuente_str for x in ["ta", "tribunal", "corte"]):
            tribunales_docs.append(row)
        else:
            tribunales_docs.append(row)

    def create_tab_list(docs, es_snifa=False):
        lista = ft.ListView(expand=True, spacing=10)
        if not docs:
            lista.controls.append(ft.Text("Sin registros en esta subcategoria", italic=True))
            return lista

        for row in docs:
            link = row[0]
            titulo = row[1]
            
            if es_snifa:
                subtitulo = row[4] 
                meta_info = f"Estado: {row[3]}"
            else:
                subtitulo = row[5]
                meta_info = f"Fecha: {row[2]}"

            def create_open_url(url):
                async def open_url(e):
                    await e.page.launch_url(url)
                return open_url

            tarjeta = ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column([
                        ft.Text(subtitulo, size=12, color=COLOR_PRIMARIO, weight="bold"),
                        ft.Text(titulo, weight="bold", size=14),
                        ft.Text(meta_info, size=11, italic=True),
                        ft.ElevatedButton(
                            "Abrir documento",
                            icon=ft.Icons.GAVEL,
                            on_click=create_open_url(link)
                        )
                    ])
                )
            )
            lista.controls.append(tarjeta)
        return lista

    # Listas base
    list_sea = create_tab_list(sea_docs)
    list_snifa_full = create_tab_list(snifa_docs, es_snifa=True)
    list_tribunales = create_tab_list(tribunales_docs)

    content_area = ft.Container(content=list_sea, expand=True, padding=10)
    
    # Area de sub-filtros para SNIFA
    def filter_snifa(e, keyword):
        if keyword == "todos":
            content_area.content = list_snifa_full
        else:
            filtered_docs = [r for r in snifa_docs if keyword.lower() in str(r[4]).lower()]
            content_area.content = create_tab_list(filtered_docs, es_snifa=True)
        content_area.update()

    sub_filtros_snifa = ft.Row(
        visible=False,
        controls=[
            ft.TextButton("Todos", on_click=lambda e: filter_snifa(e, "todos")),
            ft.TextButton("Sancionatorio", on_click=lambda e: filter_snifa(e, "sancionatorio")),
            ft.TextButton("Requerimiento Ingreso", on_click=lambda e: filter_snifa(e, "Ingreso SEIA")),
            ft.TextButton("Fiscalizaciones", on_click=lambda e: filter_snifa(e, "fiscalizacion")),
        ]
    )

    def change_custom_tab(e, category, list_view):
        content_area.content = list_view
        # Mostrar sub-filtros solo si es SNIFA
        sub_filtros_snifa.visible = (category == "SNIFA")
        
        for btn, cat in [(btn_sea, "SEA"), (btn_snifa, "SNIFA"), (btn_tribunales, "Tribunales")]:
            if cat == category:
                btn.style = ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO)
            else:
                btn.style = ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
        
        # Usamos e.control.page para asegurar que el control este montado
        if e.control.page:
            e.control.page.update()

    btn_sea = ft.TextButton(
        "SEA", 
        on_click=lambda e: change_custom_tab(e, "SEA", list_sea),
        style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO)
    )
    btn_snifa = ft.TextButton(
        "SNIFA", 
        on_click=lambda e: change_custom_tab(e, "SNIFA", list_snifa_full),
        style=ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
    )
    btn_tribunales = ft.TextButton(
        "Tribunales", 
        on_click=lambda e: change_custom_tab(e, "Tribunales", list_tribunales),
        style=ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
    )

    tab_row = ft.Row([btn_sea, btn_snifa, btn_tribunales], alignment="start")

    return ft.Column([
        ft.Row([ft.Text("Actualizaciones Legales", size=25, weight="bold", color=COLOR_PRIMARIO)]),
        ft.Divider(),
        tab_row,
        sub_filtros_snifa,
        ft.Divider(height=1, color=ft.Colors.GREY_300),
        content_area
    ], expand=True)