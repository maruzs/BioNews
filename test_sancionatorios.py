from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://snifa.sma.gob.cl/Sancionatorio/Resultado")
        
        # Click "Mostrar Busqueda" just in case it's needed to render the button
        try:
            page.locator("text=Mostrar Búsqueda").click()
            time.sleep(1)
        except:
            pass
            
        page.evaluate("buscar()")
        
        # Esperar a que la tabla cargue alguna fila
        try:
            page.wait_for_selector("table#myTable tbody tr td", timeout=30000)
        except Exception as e:
            print("Timeout waiting for table:", e)
            
        # Cambiar a -1 (todos)
        page.evaluate("""
            () => {
                const select = document.querySelector('select[name="myTable_length"]');
                if (select) {
                    select.value = '-1';
                    select.dispatchEvent(new Event('change'));
                } else {
                    console.log('No myTable_length found');
                }
            }
        """)
        
        # Esperar a que termine de cargar todos
        time.sleep(10)
        
        soup = BeautifulSoup(page.content(), 'html.parser')
        print("Rows:", len(soup.select('table#myTable tbody tr')))
        browser.close()

if __name__ == "__main__":
    run()
