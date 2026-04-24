import os
import sys
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class ScrapingEngine:
    def _get_browser_executable(self):
        """Detecta la ruta del navegador empaquetado o usa el sistema."""
        if getattr(sys, 'frozen', False):
            # Si es un .exe, busca en la carpeta temporal de PyInstaller
            base_path = sys._MEIPASS
        else:
            # Si es script, busca en la raiz del proyecto
            base_path = os.path.abspath(".")

        # IMPORTANTE: Revisa que el nombre sea 'chromium-1148'. 
        # Si cambia el numero en tu carpeta, ajustalo aqui abajo.
        exe_path = os.path.join(
            base_path, 
            "pw-browser", 
            "chromium-1148", 
            "chrome-win", 
            "chrome.exe"
        )
        
        return exe_path if os.path.exists(exe_path) else None

    def get_soup(self, url, wait_for_selector=None):
        exe_path = self._get_browser_executable()
        
        with sync_playwright() as p:
            try:
                # Lanzamos con la ruta especifica si existe
                if exe_path:
                    browser = p.chromium.launch(headless=True, executable_path=exe_path)
                else:
                    # Fallback para desarrollo (usa el del sistema)
                    browser = p.chromium.launch(headless=True)
                
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                    viewport={"width": 1920, "height": 1080}
                )
                page = context.new_page()
                
                # wait_until="load" es mas rapido para la mayoria de los sitios
                page.goto(url, timeout=90000, wait_until="load")
                
                if wait_for_selector:
                    page.wait_for_selector(wait_for_selector, timeout=45000)
                
                content = page.content()
                browser.close()
                return BeautifulSoup(content, "html.parser")
            except Exception as e:
                print(f"Error en {url}: {e}")
                try:
                    browser.close()
                except:
                    pass
                return None