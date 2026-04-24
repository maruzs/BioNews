import flet as ft
import threading
import os
from datetime import datetime
import startScraping 
from .styles import COLOR_PRIMARIO

LOGS_MEMORIA = []
PROCESO_ACTIVO = False

def view_sync():
    global PROCESO_ACTIVO
    
    btn_start = ft.ElevatedButton(
        "Iniciar Extraccion", 
        icon=ft.Icons.SYNC, 
        bgcolor=COLOR_PRIMARIO, 
        color=ft.Colors.WHITE,
        disabled=PROCESO_ACTIVO
    )
    
    def save_logs_action(e):
        if not LOGS_MEMORIA:
            return
        try:
            if not os.path.exists("logs"):
                os.makedirs("logs")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"logs/registro_{timestamp}.txt"
            with open(path, "w", encoding="utf-8") as f:
                for line in LOGS_MEMORIA:
                    f.write(line + "\n")
            
            # Notificacion en consola de depuracion
            print(f"Registro guardado exitosamente en {path}")
        except Exception as ex:
            print(f"Error al intentar guardar el registro: {ex}")

    btn_save = ft.ElevatedButton(
        "Guardar Registro",
        icon=ft.Icons.SAVE,
        on_click=save_logs_action
    )
    
    progress_bar = ft.ProgressBar(width=400, value=0, visible=PROCESO_ACTIVO, color=COLOR_PRIMARIO)
    status_text = ft.Text(
        "Listo para iniciar." if not PROCESO_ACTIVO else "Extraccion en curso...", 
        italic=True
    )
    
    warning_banner = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.ORANGE_700),
            ft.Text(
                "ADVERTENCIA: No cambie de pestana mientras la extraccion este activa.",
                color=ft.Colors.ORANGE_900,
                weight="bold",
                size=12
            )
        ]),
        bgcolor=ft.Colors.ORANGE_50,
        padding=10,
        border_radius=5,
        visible=PROCESO_ACTIVO
    )
    
    log_list = ft.ListView(expand=True, spacing=5, auto_scroll=True)
    
    # Recuperar logs de la sesion actual
    for m in LOGS_MEMORIA:
        log_list.controls.append(ft.Text(m, size=12, selectable=True))

    def run_scrapers(page):
        global PROCESO_ACTIVO
        PROCESO_ACTIVO = True
        
        btn_start.disabled = True
        progress_bar.visible = True
        progress_bar.value = 0
        warning_banner.visible = True
        status_text.value = "Extrayendo informacion..."
        
        page.update()

        def log_ui(msg):
            # Guardar mensaje y actualizar lista visual
            LOGS_MEMORIA.append(msg)
            log_list.controls.append(ft.Text(msg, size=12, selectable=True))
            
            # Movimiento de barra segun hitos del registro
            if "Iniciando" in msg:
                progress_bar.value = min(progress_bar.value + 0.05, 0.9)
            elif "Guardad" in msg:
                progress_bar.value = min(progress_bar.value + 0.02, 0.98)
            
            try:
                # Actualizacion total para garantizar visibilidad en cada linea
                page.update()
            except:
                pass

        try:
            # Ejecucion directa del modulo integrado
            startScraping.ejecutar_todo_el_scraping(log_ui)
            
            progress_bar.value = 1.0
            status_text.value = "Proceso de extraccion finalizado."
        except Exception as e:
            log_ui(f"Error critico detectado: {str(e)}")
            status_text.value = "Fallo en la sincronizacion."
        finally:
            PROCESO_ACTIVO = False
            btn_start.disabled = False
            warning_banner.visible = False
            try:
                page.update()
            except:
                pass

    def on_click_start(e):
        LOGS_MEMORIA.clear()
        log_list.controls.clear()
        
        # Se pasa la referencia de la pagina al hilo para manejar actualizaciones
        hilo = threading.Thread(target=run_scrapers, args=(e.page,), daemon=True)
        hilo.start()

    btn_start.on_click = on_click_start

    return ft.Container(
        padding=20,
        expand=True,
        content=ft.Column([
            ft.Row([ft.Text("Sincronizacion de Datos", size=25, weight="bold", color=COLOR_PRIMARIO)]),
            ft.Divider(),
            warning_banner,
            ft.Row([btn_start, btn_save, progress_bar]),
            status_text,
            ft.Container(height=10),
            ft.Text("Registro de actividad (Seleccionable para copiar):", weight="bold"),
            ft.Container(
                content=log_list,
                expand=True,
                bgcolor=ft.Colors.GREY_50,
                border_radius=10,
                padding=10,
                border=ft.border.all(1, ft.Colors.GREY_300)
            )
        ], expand=True)
    )