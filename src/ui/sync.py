import flet as ft
import threading
import subprocess
import sys
import os
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
    
    progress_bar = ft.ProgressBar(width=400, visible=PROCESO_ACTIVO, color=COLOR_PRIMARIO)
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
        log_list.controls.append(ft.Text(m, size=12))

    def run_scrapers():
        global PROCESO_ACTIVO
        PROCESO_ACTIVO = True
        
        btn_start.disabled = True
        progress_bar.visible = True
        progress_bar.value = None
        warning_banner.visible = True
        
        btn_start.update()
        progress_bar.update()
        warning_banner.update()

        def log(msg):
            LOGS_MEMORIA.append(msg)
            log_list.controls.append(ft.Text(msg, size=12))
            log_list.update()

        try:
            log("--- INICIANDO MOTOR DE EXTRACCION ---")
            log("Conectando con startScraping.py...") # Añadido de vuelta
            
            # EL FIX: Añadimos "-u" para forzar la salida en tiempo real (unbuffered)
            process = subprocess.Popen(
                [sys.executable, "-u", "startScraping.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                cwd=os.getcwd() 
            )

            for line in iter(process.stdout.readline, ''):
                if line:
                    log(line.strip())
            
            process.wait()
            
            if process.returncode == 0:
                log("--- PROCESO FINALIZADO CON EXITO ---")
                status_text.value = "Extraccion completada."
            else:
                log(f"--- PROCESO FINALIZADO CON ERRORES (Code {process.returncode}) ---")
                status_text.value = "Error en la extraccion."

        except Exception as e:
            log(f"Error critico: {e}")
        finally:
            PROCESO_ACTIVO = False
            progress_bar.visible = False
            btn_start.disabled = False
            warning_banner.visible = False
            
            btn_start.update()
            progress_bar.update()
            warning_banner.update()
            status_text.update()

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
            ft.Row([btn_start, progress_bar]),
            status_text,
            ft.Container(height=10),
            ft.Text("Registro de actividad del motor:", weight="bold"),
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