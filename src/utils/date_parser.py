import re
from datetime import datetime

def parse_fecha(fecha_str):
    meses = {
        "enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06",
        "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12",
        "abr": "04", "oct": "10", "sept": "09", "dic": "12"
    }
    
    # Limpieza profunda para formatos como "15 de abril de 2026"
    fecha_str = fecha_str.lower().replace(".", "").replace(",", "").replace(" de ", " ").strip()
    
    try:
        # Formato Numerico: 20-04-2026
        match_num = re.search(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})", fecha_str)
        if match_num:
            d, m, a = match_num.groups()
            return f"{a}-{m.zfill(2)}-{d.zfill(2)}"

        # Formato Texto: 15 abril 2026
        match_txt = re.search(r"(\d+)\s+([a-z]+)\s+(\d{4})", fecha_str)
        if match_txt:
            d, m, a = match_txt.groups()
            mes_num = meses.get(m, "01")
            return f"{a}-{mes_num}-{d.zfill(2)}"
            
    except:
        pass
        
    return datetime.now().strftime("%Y-%m-%d")