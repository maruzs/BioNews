import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def test_scraper():
    url_base = "https://seia.sea.gob.cl"
    url_buscar = f"{url_base}/busqueda/buscarProyectoResumen.php"
    url_api = f"{url_base}/busqueda/buscarProyectoResumenAction.php"
    
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": url_base,
        "Referer": url_buscar
    })
    
    # Obtener cookies iniciales
    session.get(url_buscar)
    
    # fecha de hoy en formato dd/mm/yyyy
    fecha_hoy = datetime.now().strftime('%d/%m/%Y')
    
    payload = {
        "nombre": "",
        "titular": "",
        "folio": "",
        "selectRegion": "",
        "selectComuna": "",
        "tipoPresentacion": "Ambos",
        "projectStatus": "",
        "PresentacionMin": fecha_hoy,
        "PresentacionMax": fecha_hoy,
        "CalificaMin": "",
        "CalificaMax": "",
        "sectores_economicos": "",
        "razoningreso": "",
        "id_tipoexpediente": "",
        "offset": 1,
        "limit": 10,
        "orderColumn": "FECHA_PRESENTACION",
        "orderDir": "desc"
    }
    
    response = session.post(url_api, data=payload)
    print(f"Status Code: {response.status_code}")
    print(response.text[:500])

if __name__ == '__main__':
    test_scraper()
