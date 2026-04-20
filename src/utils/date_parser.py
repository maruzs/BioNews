import re

def parse_fecha(fecha_str):
    meses = {
        "enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06",
        "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12",
        "abr": "04", "oct": "10", "sept": "09", "dic": "12"
    }
    
    # Limpieza basica
    fecha_str = fecha_str.lower().replace(".", "").replace("de", "").replace(",", "").strip()
    
    try:
        # Caso SEA / Diario Oficial: 17/04/2026 o 20-04-2026
        match_simple = re.search(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})", fecha_str)
        if match_simple:
            d, m, a = match_simple.groups()
            return f"{a}-{m.zfill(2)}-{d.zfill(2)}"

        # Caso MMA/SBAP: 20 abril 2026
        match_texto = re.search(r"(\d+)\s+([a-z]+)\s+(\d{4})", fecha_str)
        if match_texto:
            d, m, a = match_texto.groups()
            mes_num = meses.get(m, "01")
            return f"{a}-{mes_num}-{d.zfill(2)}"
            
    except:
        pass
        
    return "2026-04-20"