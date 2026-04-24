# src/main.py
import sys
import os
import subprocess

def instalar_chromium_auto():
    """Instala Chromium automáticamente si no existe"""
    try:
        from playwright.sync_api import sync_playwright
        
        # Intentar lanzar Chromium
        with sync_playwright() as p:
            browser = p.chromium.launch()
            browser.close()
        return True
        
    except Exception as e:
        if "Executable doesn't exist" in str(e) or "not found" in str(e).lower():
            # Intentar instalar automáticamente
            try:
                print("Instalando Chromium automáticamente...")
                subprocess.run(
                    [sys.executable, "-m", "playwright", "install", "chromium"],
                    check=True,
                    capture_output=True
                )
                # Verificar la instalación
                from playwright.sync_api import sync_playwright
                with sync_playwright() as p:
                    browser = p.chromium.launch()
                    browser.close()
                return True
            except Exception as install_error:
                print(f"Error instalando Chromium: {install_error}")
                return False
        return False

from PySide6.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Verificar/instalar Playwright
    playwright_ok = instalar_chromium_auto()
    
    window = MainWindow()
    
    if not playwright_ok:
        QMessageBox.warning(
            window,
            "Error de configuración",
            "No se pudo instalar Chromium automáticamente.\n\n"
            "Por favor ejecuta manualmente en una terminal:\n"
            "playwright install chromium\n\n"
            "El scraping estará deshabilitado hasta entonces."
        )
        window.btn_sync.setEnabled(False)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()