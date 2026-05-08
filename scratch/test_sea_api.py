import requests
import json

url_api = "https://seia.sea.gob.cl/busqueda/buscarProyectoResumenAction.php"
payload = {
    "nombre": "",
    "titular": "",
    "folio": "",
    "selectRegion": "",
    "selectComuna": "",
    "tipoPresentacion": "Ambos",
    "projectStatus": "",
    "PresentacionMin": "01/05/2026",
    "PresentacionMax": "08/05/2026",
    "limit": 5,
    "offset": 1,
    "orderColumn": "FECHA_PRESENTACION",
    "orderDir": "desc"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.post(url_api, data=payload, headers=headers)
print(json.dumps(response.json(), indent=2))
