import flet as ft
import threading
import subprocess
import sys
import os
from datetime import datetime
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
    
    # Boton para guardar logs manualmente
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
            
            # Notificacion simple si la pagina esta disponible
            print(f"Registro guardado en {path}")
        except Exception as ex:
            print(f"Error al guardar registro: {ex}")

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
    
    # Cargar logs previos y hacerlos seleccionables
    for m in LOGS_MEMORIA:
        log_list.controls.append(ft.Text(m, size=12, selectable=True))

    def run_scrapers():
        global PROCESO_ACTIVO
        PROCESO_ACTIVO = True
        
        btn_start.disabled = True
        progress_bar.visible = True
        progress_bar.value = 0
        warning_banner.visible = True
        
        btn_start.update()
        progress_bar.update()
        warning_banner.update()

        def log(msg):
            LOGS_MEMORIA.append(msg)
            # selectable=True permite que el usuario copie el texto
            log_list.controls.append(ft.Text(msg, size=12, selectable=True))
            log_list.update()

        try:
            log("--- INICIANDO MOTOR DE EXTRACCION ---")
            env = os.environ.copy()
            env["PYTHONPATH"] = os.path.join(os.getcwd(), "src")

            process = subprocess.Popen(
                [sys.executable, "-u", "startScraping.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                cwd=os.getcwd(),
                env=env
            )

            # Ajusta este numero segun la cantidad de fuentes reales
            fuentes_totales = 8 
            for line in iter(process.stdout.readline, ''):
                if line:
                    msg = line.strip()
                    log(msg)
                    if "Listo" in msg or "Finalizado" in msg:
                        if progress_bar.value < 1.0:
                            progress_bar.value += (1.0 / fuentes_totales)
                            progress_bar.update()
            
            process.wait()
            
            if process.returncode == 0:
                progress_bar.value = 1.0
                log("--- PROCESO FINALIZADO CON EXITO ---")
                status_text.value = "Extraccion completada con exito."
            else:
                log(f"--- FALLO DE EJECUCION (Codigo: {process.returncode}) ---")
                status_text.value = "Error en el proceso."

        except Exception as e:
            log(f"Error critico: {str(e)}")
        finally:
            PROCESO_ACTIVO = False
            btn_start.disabled = False
            warning_banner.visible = False
            btn_start.update()
            warning_banner.update()
            status_text.update()
            progress_bar.update()

    def on_click_start(e):
        LOGS_MEMORIA.clear()
        log_list.controls.clear()
        log_list.update()
        hilo = threading.Thread(target=run_scrapers, daemon=True)
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