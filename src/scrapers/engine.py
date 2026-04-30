import os
import sys
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class ScrapingEngine:
    def _get_browser_executable(self):
        # En Docker/Linux, Playwright maneja su propio Chromium
        # Solo buscamos un exe embebido cuando corremos en Windows empaquetado
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        
        # Intenta el path de Windows empaquetado
        exe_path = os.path.join(base_path, "pw-browser", "chromium-1208", "chrome-win", "chrome.exe")
        if os.path.exists(exe_path):
            return exe_path
        
        # En Docker/Linux, Playwright encuentra Chromium automáticamente
        return None

    def get_soup(self, url, wait_for_selector=None):
        exe_path = self._get_browser_executable()
        
        with sync_playwright() as p:
            try:
                launch_args = {
                    "headless": True,
                    # Necesario en Docker para correr como root
                    "args": ["--no-sandbox", "--disable-setuid-sandbox"],
                }
                if exe_path:
                    launch_args["executable_path"] = exe_path
                
                browser = p.chromium.launch(**launch_args)
                
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                    viewport={"width": 1920, "height": 1080}
                )
                page = context.new_page()
                page.goto(url, timeout=90000, wait_until="load")
                
                if wait_for_selector:
                    page.wait_for_selector(wait_for_selector, timeout=45000)
                
                content = page.content()
                browser.close()
                return BeautifulSoup(content, "html.parser")
            except Exception as e:
                try:
                    browser.close()
                except:
                    pass
                raise RuntimeError(f"Fallo de conexion en {url}: {str(e)}")