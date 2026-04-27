import flet as ft
import threading
import os
from datetime import datetime
from .styles import COLOR_PRIMARIO
# Importamos directamente el modulo de scraping
import startScraping 

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
            
            # Print para consola de depuracion
            print(f"Registro guardado en {path}")
        except Exception as ex:
            print(f"Error al guardar errores: {ex}")

    btn_save = ft.ElevatedButton(
        "Guardar errores",
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
    
    # Cargar logs previos si existen en la sesion actual
    for m in LOGS_MEMORIA:
        log_list.controls.append(ft.Text(m, size=12, selectable=True))

    def run_scrapers(page):
        global PROCESO_ACTIVO
        PROCESO_ACTIVO = True
        
        btn_start.disabled = True
        progress_bar.visible = True
        progress_bar.value = 0
        warning_banner.visible = True
        
        # Actualizacion inicial de la UI
        try:
            page.update()
        except:
            pass

        def log(msg):
            # Agregar a memoria y a la lista visual
            LOGS_MEMORIA.append(msg)
            log_list.controls.append(ft.Text(msg, size=12, selectable=True))
            
            # Forzamos la actualizacion directa de los componentes
            try:
                log_list.update()
            except:
                pass

        def update_progress(val):
            progress_bar.value = val
            try:
                progress_bar.update()
            except:
                pass

        try:
            log("--- INICIANDO MOTOR DE EXTRACCION ---")
            
            # Llamada directa a la funcion dentro de startScraping.py
            # IMPORTANTE: Asegurate de que en startScraping.py la funcion se llame run_sync
            startScraping.run_sync(log, update_progress)
            
            progress_bar.value = 1.0
            status_text.value = "Extraccion completada con exito."
            try:
                progress_bar.update()
                status_text.update()
                btn_start.update()
            except:
                pass
        except Exception as e:
            log(f"Error critico: {str(e)}")
            status_text.value = "Fallo en la sincronizacion."
        finally:
            PROCESO_ACTIVO = False
            btn_start.disabled = False
            warning_banner.visible = False
            
            try:
                btn_start.update()
                warning_banner.update()
                status_text.update()
            except:
                pass

    def on_click_start(e):
        LOGS_MEMORIA.clear()
        log_list.controls.clear()
        
        # Capturamos la referencia de la pagina y arrancamos el hilo
        page_ref = e.page
        page_ref.update()
            
        hilo = threading.Thread(target=run_scrapers, args=(page_ref,), daemon=True)
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