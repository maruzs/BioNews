import flet as ft
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

def view_favorites():
    db = DatabaseManager()
    
    # Contenedor principal de la lista
    list_container = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
    
    # Campo de busqueda
    search_input = ft.TextField(
        label="Buscar en favoritos...",
        prefix_icon=ft.Icons.SEARCH,
        expand=True,
        border_radius=20,
        height=40,
        content_padding=10
    )
    
    # Controles para añadir manual
    add_source_dropdown = ft.Dropdown(
        label="Fuente",
        options=[
            ft.dropdown.Option("SEA"),
            ft.dropdown.Option("SNIFA"),
            ft.dropdown.Option("Tribunales")
        ],
        width=150,
        height=50
    )
    
    add_id_input = ft.TextField(
        label="ID o Link (ej: PERTI-1234)",
        expand=True,
        height=50
    )
    
    def refresh_list(filter_source=None, search_term=""):
        list_container.controls.clear()
        favorites = db.get_favorites(fuente=filter_source)
        
        if search_term:
            favorites = [f for f in favorites if search_term.lower() in f[2].lower() or search_term.lower() in f[0].lower()]
            
        if not favorites:
            list_container.controls.append(ft.Text("No hay favoritos guardados.", italic=True))
        else:
            for fav in favorites:
                id_link, fuente, nombre, fecha = fav
                
                def remove_fav(e, target_id=id_link):
                    db.remove_favorite(target_id)
                    # Trigger a refresh. We need to know the current active tab.
                    current_tab = active_tab[0]
                    source_filter = None
                    if current_tab == 1: source_filter = "SEA"
                    elif current_tab == 2: source_filter = "SNIFA"
                    elif current_tab == 3: source_filter = "Tribunales"
                    refresh_list(source_filter, search_input.value)
                    list_container.update()

                card = ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Row([
                            ft.Column([
                                ft.Text(fuente, size=12, color=COLOR_PRIMARIO, weight="bold"),
                                ft.Text(nombre if nombre else id_link, weight="bold", size=14),
                                ft.Text(f"Agregado: {fecha.split()[0]}", size=11, italic=True),
                                ft.Text(f"ID/Link: {id_link}", size=11, color=ft.Colors.GREY_700),
                            ], expand=True),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=ft.Colors.RED_400,
                                tooltip="Eliminar de favoritos",
                                on_click=remove_fav
                            )
                        ])
                    )
                )
                list_container.controls.append(card)
                
    active_tab = [0] # List to act as a mutable reference
    
    def on_search_change(e):
        current_tab = active_tab[0]
        source_filter = None
        if current_tab == 1: source_filter = "SEA"
        elif current_tab == 2: source_filter = "SNIFA"
        elif current_tab == 3: source_filter = "Tribunales"
        refresh_list(source_filter, search_input.value)
        list_container.update()

    search_input.on_change = on_search_change

    def change_custom_tab(e, index, category):
        active_tab[0] = index
        source_filter = category if category != "Todos" else None
        
        # Update button styles
        for idx, btn in enumerate(tab_buttons):
            if idx == index:
                btn.style = ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO)
            else:
                btn.style = ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT)
                
        refresh_list(source_filter, search_input.value)
        list_container.update()
        if e and e.control and e.control.page:
            e.control.page.update()

    btn_todos = ft.TextButton("Todos", on_click=lambda e: change_custom_tab(e, 0, "Todos"), style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_PRIMARIO))
    btn_sea = ft.TextButton("SEA", on_click=lambda e: change_custom_tab(e, 1, "SEA"), style=ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT))
    btn_snifa = ft.TextButton("SNIFA", on_click=lambda e: change_custom_tab(e, 2, "SNIFA"), style=ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT))
    btn_trib = ft.TextButton("Tribunales", on_click=lambda e: change_custom_tab(e, 3, "Tribunales"), style=ft.ButtonStyle(color=COLOR_PRIMARIO, bgcolor=ft.Colors.TRANSPARENT))
    
    tab_buttons = [btn_todos, btn_sea, btn_snifa, btn_trib]
    tabs = ft.Row(tab_buttons, alignment="start")
    
    def add_manual_favorite(e):
        fuente = add_source_dropdown.value
        id_val = add_id_input.value.strip()
        
        if not fuente or not id_val:
            # Simple validation
            return
            
        nombre = f"Seguimiento manual ({fuente})"
        success = db.add_favorite(id_val, fuente, nombre)
        
        if success:
            add_id_input.value = ""
            add_source_dropdown.value = None
            add_id_input.update()
            add_source_dropdown.update()
            
            # Use current active tab to refresh
            source_filter = None
            if active_tab[0] == 1: source_filter = "SEA"
            elif active_tab[0] == 2: source_filter = "SNIFA"
            elif active_tab[0] == 3: source_filter = "Tribunales"
            refresh_list(source_filter, search_input.value)
            list_container.update()
            
    btn_add = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD,
        bgcolor=COLOR_PRIMARIO,
        color=ft.Colors.WHITE,
        on_click=add_manual_favorite
    )
    
    add_panel = ft.Container(
        padding=10,
        bgcolor=ft.Colors.GREY_100,
        border_radius=10,
        content=ft.Column([
            ft.Text("Agregar Seguimiento Manual", weight="bold"),
            ft.Row([add_source_dropdown, add_id_input, btn_add])
        ])
    )

    # Initial load
    refresh_list()

    return ft.Column([
        ft.Row([ft.Text("Mis Favoritos y Seguimientos", size=25, weight="bold", color=COLOR_PRIMARIO)]),
        ft.Divider(),
        add_panel,
        ft.Container(height=10),
        ft.Row([search_input]),
        tabs,
        ft.Container(content=list_container, expand=True)
    ], expand=True)
