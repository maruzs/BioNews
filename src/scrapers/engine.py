from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class ScrapingEngine:
    def get_soup(self, url, wait_for_selector=None):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            # Agregamos mas headers y un viewport estandar
            context = browser.new_context(
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080}
            )
            page = context.new_page()
            
            try:
                # wait_until="networkidle" ayuda en paginas lentas como SINIA
                page.goto(url, timeout=90000, wait_until="load")
                
                if wait_for_selector:
                    # Aumentamos a 45 segundos para SINIA
                    page.wait_for_selector(wait_for_selector, timeout=45000)
                
                content = page.content()
                browser.close()
                return BeautifulSoup(content, "html.parser")
            except Exception as e:
                print(f"Error en {url}: {e}")
                browser.close()
                return None