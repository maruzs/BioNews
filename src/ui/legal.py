import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_legal():
    db = DatabaseManager()
    documentos_db = db.get_all_legal(limit=2000) 
    
    sea_docs = []
    snifa_docs = []
    tribunales_docs = []

    # Funcion para extraer el numero de ficha del final del link
    def extract_ficha_id(link):
        try:
            partes = [p for p in str(link).split('/') if p.strip()]
            if partes and partes[-1].isdigit():
                return int(partes[-1])
        except:
            pass
        return 0

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

    # AQUI: Ordenamos todos los registros de SNIFA por su ID de ficha (de mayor a menor)
    snifa_docs.sort(key=lambda r: extract_ficha_id(r[0]), reverse=True)

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
                meta_info = f"Estado: {row[3]} | Ficha: {extract_ficha_id(link)}" # Agregue el ID visible como extra
            else:
                subtitulo = row[5]
                meta_info = f"Fecha: {row[2]}"

            def create_open_url(url):
                async def open_url(e):
                    await e.page.launch_url(url)
                return open_url

            def toggle_favorite(e, f_id=link, f_src=row[5] if not es_snifa else row[4], f_name=titulo):
                is_fav = db.is_favorite(f_id)
                if is_fav:
                    db.remove_favorite(f_id)
                    e.control.icon = ft.Icons.FAVORITE_BORDER
                    e.control.icon_color = ft.Colors.GREY_400
                else:
                    db.add_favorite(f_id, f_src, f_name)
                    e.control.icon = ft.Icons.FAVORITE
                    e.control.icon_color = ft.Colors.RED_400
                e.control.update()

            is_currently_fav = db.is_favorite(link)
            fav_icon = ft.Icons.FAVORITE if is_currently_fav else ft.Icons.FAVORITE_BORDER
            fav_color = ft.Colors.RED_400 if is_currently_fav else ft.Colors.GREY_400

            tarjeta = ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column([
                        ft.Row([
                            ft.Text(subtitulo, size=12, color=COLOR_PRIMARIO, weight="bold", expand=True),
                            ft.IconButton(
                                icon=fav_icon,
                                icon_color=fav_color,
                                icon_size=20,
                                on_click=toggle_favorite,
                                tooltip="Agregar/Quitar de favoritos"
                            )
                        ]),
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
    
    # --- FILTROS SNIFA ---
    current_snifa_type = "todos"
    
    search_snifa = ft.TextField(
        label="Buscar por Expediente o Nombre...", 
        prefix_icon=ft.Icons.SEARCH,
        on_change=lambda e: apply_snifa_filters(),
        expand=True,
        height=45,
        text_size=13
    )
    
    # Extraer categorias y estados dinamicamente de snifa_docs
    categorias_snifa = set()
    estados_snifa = set()
    for r in snifa_docs:
        tipo_str = str(r[4])
        if "(" in tipo_str and ")" in tipo_str:
            cat = tipo_str.split("(")[1].split(")")[0]
            categorias_snifa.add(cat)
        
        estado_str = str(r[3])
        if estado_str:
            estados_snifa.add(estado_str)
            
    categorias_snifa = sorted(list(categorias_snifa))
    estados_snifa = sorted(list(estados_snifa))
    
    cat_checkboxes = [ft.Checkbox(label=c, value=False, on_change=lambda e: apply_snifa_filters()) for c in categorias_snifa]
    estado_checkboxes = [ft.Checkbox(label=est, value=False, on_change=lambda e: apply_snifa_filters()) for est in estados_snifa]
    
    btn_type_todos = ft.TextButton("Todos", on_click=lambda e: filter_snifa_type(e, "todos"), style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO))
    btn_type_sancionatorio = ft.TextButton("Sancionatorio", on_click=lambda e: filter_snifa_type(e, "sancionatorio"), style=ft.ButtonStyle(color=COLOR_PRIMARIO))
    btn_type_ingreso = ft.TextButton("Requisitos Ingreso", on_click=lambda e: filter_snifa_type(e, "Ingreso SEIA"), style=ft.ButtonStyle(color=COLOR_PRIMARIO))
    btn_type_fiscalizacion = ft.TextButton("Fiscalizaciones", on_click=lambda e: filter_snifa_type(e, "fiscalizacion"), style=ft.ButtonStyle(color=COLOR_PRIMARIO))
    
    snifa_type_buttons = [btn_type_todos, btn_type_sancionatorio, btn_type_ingreso, btn_type_fiscalizacion]
    
    def filter_snifa_type(e, keyword):
        nonlocal current_snifa_type
        current_snifa_type = keyword
        # Actualizar colores de los botones de tipo
        for btn in snifa_type_buttons:
            if btn == e.control:
                btn.style = ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO)
            else:
                btn.style = ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
        
        apply_snifa_filters()
        if e.control.page:
            e.control.page.update()

    def apply_snifa_filters():
        filtered_docs = snifa_docs
        
        # 1. Filtro de tipo (Sancionatorio, Fiscalizacion, etc)
        if current_snifa_type != "todos":
            filtered_docs = [r for r in filtered_docs if current_snifa_type.lower() in str(r[4]).lower()]
            
        # 2. Filtro de busqueda
        q = search_snifa.value.lower() if search_snifa.value else ""
        if q:
            filtered_docs = [r for r in filtered_docs if q in str(r[1]).lower()]
            
        # 3. Filtro de Categorias
        selected_cats = [cb.label for cb in cat_checkboxes if cb.value]
        if selected_cats:
            filtered_docs = [r for r in filtered_docs if any(f"({c})" in str(r[4]) for c in selected_cats)]
            
        # 4. Filtro de Estados
        selected_estados = [cb.label for cb in estado_checkboxes if cb.value]
        if selected_estados:
            filtered_docs = [r for r in filtered_docs if str(r[3]) in selected_estados]
            
        content_area.content = create_tab_list(filtered_docs, es_snifa=True)
        if content_area.page:
            content_area.update()

    filtros_snifa_container = ft.Column(
        visible=False,
        controls=[
            ft.Row(snifa_type_buttons),
            search_snifa,
            ft.ExpansionTile(
                title=ft.Text("Filtros Avanzados (Categoría y Estado)", size=14, weight="bold", color=COLOR_PRIMARIO),
                controls=[
                    ft.Text("Categorías", weight="bold", size=13),
                    ft.Row(cat_checkboxes, wrap=True),
                    ft.Divider(height=1),
                    ft.Text("Estado", weight="bold", size=13),
                    ft.Row(estado_checkboxes, wrap=True),
                ]
            )
        ]
    )


    def change_custom_tab(e, category, list_view):
        content_area.content = list_view
        filtros_snifa_container.visible = (category == "SNIFA")
        
        for btn, cat in [(btn_sea, "SEA"), (btn_snifa, "SNIFA"), (btn_tribunales, "Tribunales")]:
            if cat == category:
                btn.style = ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO)
            else:
                btn.style = ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
        
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
        filtros_snifa_container,
        ft.Divider(height=1, color=ft.Colors.GREY_300),
        content_area
    ], expand=True)