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
    
    for m in LOGS_MEMORIA:
        log_list.controls.append(ft.Text(m, size=12, selectable=True))

    # AQUI ESTA LA MAGIA: Recibimos el objeto 'page' directo desde el boton
    def run_scrapers(page):
        global PROCESO_ACTIVO
        PROCESO_ACTIVO = True
        
        btn_start.disabled = True
        progress_bar.visible = True
        progress_bar.value = 0
        warning_banner.visible = True
        
        try:
            page.update()
        except:
            pass

        def log(msg):
            LOGS_MEMORIA.append(msg)
            log_list.controls.append(ft.Text(msg, size=12, selectable=True))
            # Forzamos la actualizacion de toda la pagina para no depender del boton "Guardar"
            try:
                page.update()
            except:
                pass

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

            # Segun tu archivo de logs, los eventos importantes ocurren unas 25 veces
            pasos_estimados = 25 
            paso_actual = 0

            for line in iter(process.stdout.readline, ''):
                if line:
                    msg = line.strip()
                    log(msg)
                    
                    # Detectamos el inicio de un scraper o cuando guarda datos
                    if "Iniciando scraping" in msg or "Guardad" in msg:
                        paso_actual += 1
                        # Evitamos que llegue a 100% antes de que termine realmente el proceso
                        nuevo_valor = min(paso_actual / pasos_estimados, 0.95) 
                        progress_bar.value = nuevo_valor
                        try:
                            page.update()
                        except:
                            pass
            
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
            
            try:
                page.update()
            except:
                pass

    def on_click_start(e):
        LOGS_MEMORIA.clear()
        log_list.controls.clear()
        
        # Capturamos la pagina al hacer click y se la enviamos al hilo
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