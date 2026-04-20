from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class ScrapingEngine:
    def get_soup(self, url, wait_for_selector=None):
        with sync_playwright() as p:
            # Agregamos un User-Agent real para evitar bloqueos
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            
            try:
                # Aumentamos el timeout de navegacion a 60s
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                
                if wait_for_selector:
                    # Aumentamos el timeout del selector a 30s
                    page.wait_for_selector(wait_for_selector, timeout=30000)
                
                content = page.content()
                browser.close()
                return BeautifulSoup(content, "html.parser")
            except Exception as e:
                print(f"Error al acceder a {url}: {e}")
                browser.close()
                return None