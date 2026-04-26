import os
import sys
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

class ScrapingEngine:
    def __init__(self):
        self.browser_path = self._get_browser_executable()

    def _get_browser_executable(self):
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.abspath(".")

        # Lista de rutas posibles para cubrir todas las versiones (1208, 1148, etc.)
        # y todos los tipos de ejecutable (Chrome o Headless Shell)
        check_paths = [
            # Intento con Chromium 1208 (Versiones mas nuevas)
            os.path.join("pw-browser", "chromium-1208", "chrome-win", "chrome.exe"),
            os.path.join("pw-browser", "chromium_headless_shell-1208", "chrome-win", "headless_shell.exe"),
            os.path.join("pw-browser", "chromium_headless_shell-1208", "chrome-headless-shell-win64", "chrome-headless-shell.exe"),
            
            # Intento con Chromium 1148 (Versiones anteriores)
            os.path.join("pw-browser", "chromium-1148", "chrome-win", "chrome.exe"),
        ]

        for rel_path in check_paths:
            full_path = os.path.join(base_path, rel_path)
            if os.path.exists(full_path):
                print(f"Navegador encontrado en: {full_path}", flush=True)
                return full_path

        print("Alerta: No se encontro el ejecutable de Chromium en pw-browser", flush=True)
        return None

    def get_soup(self, url, wait_for_selector=None):
        if not self.browser_path:
            return None

        with sync_playwright() as p:
            # Forzamos el uso del ejecutable de nuestra carpeta pw-browser
            browser = p.chromium.launch(
                executable_path=self.browser_path, 
                headless=True
            )
            context = browser.new_context()
            page = context.new_page()
            
            try:
                page.goto(url, wait_until="networkidle", timeout=60000)
                if wait_for_selector:
                    page.wait_for_selector(wait_for_selector, timeout=20000)
                
                content = page.content()
                return BeautifulSoup(content, "html.parser")
            except Exception as e:
                print(f"Error en ScrapingEngine: {str(e)}", flush=True)
                return None
            finally:
                browser.close()