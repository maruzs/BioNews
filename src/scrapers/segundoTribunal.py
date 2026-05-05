"""
Scraper del Segundo Tribunal Ambiental
Usa Playwright para interceptar JSON de la API del 2TA y guarda en la tabla Tribunales de data.db
"""
import sqlite3
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'data.db')


def obtener_ultima_fecha(conn):
    """
    Busca la fecha mas reciente ingresada en la base de datos para el Segundo Tribunal.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT Fecha FROM Tribunales WHERE Tribunal = 'Segundo Tribunal'")
        filas = cursor.fetchall()
        
        if not filas:
            return None
            
        fechas_validas = []
        for fila in filas:
            fecha_str = fila[0]
            if fecha_str:
                try:
                    # Intentamos ISO primero
                    if '-' in fecha_str and len(fecha_str.split('-')[0]) == 4:
                        dt = datetime.strptime(fecha_str, "%Y-%m-%d")
                    else:
                        dt = datetime.strptime(fecha_str, "%d-%m-%Y")
                    fechas_validas.append(dt)
                except ValueError:
                    continue
                    
        if fechas_validas:
            return max(fechas_validas)
        return None
        
    except sqlite3.OperationalError:
        return None


def extraer_nuevos_con_playwright(ano_actual, resultados_interceptados):
    print(f"Iniciando Chromium para buscar causas del ano {ano_actual}...")
    
    def manejar_respuesta(response):
        """Intercepta silenciosamente el JSON de respuesta del servidor."""
        if "searchPaginado" in response.url and response.status == 200:
            try:
                body = response.json()
                results = body.get('results', [])
                if results:
                    resultados_interceptados.extend(results)
            except Exception:
                pass

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        page.on("response", manejar_respuesta)
        
        print("Navegando a la pagina principal...")
        page.goto("https://2ta.lexsoft.cl/2ta/search?proc=4")
        page.wait_for_load_state("networkidle")
        
        # 1. Seleccionamos 'Buscar por: Rol' (indice 0)
        page.evaluate("document.getElementById('procedimiento').selectedIndex = 0; document.getElementById('procedimiento').dispatchEvent(new Event('change'));")
        
        # 2. Seleccionamos dinamicamente el ano actual
        script_ano = f"""
        let selEra = document.getElementById('era');
        for(let i=0; i<selEra.options.length; i++) {{
            if(selEra.options[i].text === '{ano_actual}') {{
                selEra.selectedIndex = i;
                selEra.dispatchEvent(new Event('change'));
                break;
            }}
        }}
        """
        page.evaluate(script_ano)
        
        # 3. Obtenemos la cantidad de tipos de causa
        opciones_tipo = page.locator("select#tipo option").count()
        
        for i in range(opciones_tipo):
            print(f"Consultando categoria de tramite #{i + 1} de {opciones_tipo}...")
            
            page.evaluate(f"document.getElementById('tipo').selectedIndex = {i}; document.getElementById('tipo').dispatchEvent(new Event('change'));")
            
            page.locator("button[type='submit']").last.click(force=True)
            page.wait_for_timeout(3000)
            
        browser.close()


def procesar_nuevos_registros(resultados_interceptados, conn, ultima_fecha_db):
    cursor = conn.cursor()
    
    nuevos_registros = 0
    ids_procesados = set()
    causas_procesadas = []
    
    for causa in resultados_interceptados:
        id_causa = causa.get('id')
        if not id_causa or id_causa in ids_procesados:
            continue
            
        ids_procesados.add(id_causa)
        
        fecha_ms = causa.get('fechaIngreso')
        if not fecha_ms:
            continue
            
        fecha_str = datetime.fromtimestamp(fecha_ms / 1000.0).strftime('%Y-%m-%d')
        try:
            dt = datetime.strptime(fecha_str, "%Y-%m-%d")
            causas_procesadas.append((dt, fecha_str, causa, id_causa))
        except ValueError:
            continue
            
    # Ordenar de mas reciente a mas antigua
    causas_procesadas.sort(key=lambda x: x[0], reverse=True)
    
    for dt, fecha_str, causa, id_causa in causas_procesadas:
        if ultima_fecha_db and dt < ultima_fecha_db:
            continue
            
        rol = causa.get('rol')
        if not rol:
            continue
            
        caratula = causa.get('descripcion', '')
        tribunal = 'Segundo Tribunal'
        
        procedimiento_obj = causa.get('procedimiento', {})
        tipo_procedimiento = procedimiento_obj.get('name', '') if procedimiento_obj else ''
        
        estado_procesal = ""
        cuadernos = causa.get('cuadernos', [])
        if cuadernos and len(cuadernos) > 0:
            estado_obj = cuadernos[0].get('estadoProcesal', {})
            estado_procesal = estado_obj.get('name', '') if estado_obj else ''
            
        accion = f"https://2ta.lexsoft.cl/2ta/search?proc=3&idCausa={id_causa}"
        
        cursor.execute('''
            INSERT OR REPLACE INTO Tribunales
            (Rol, Fecha, Caratula, Tribunal, Tipo_de_Procedimiento, Estado_Procesal, Accion, fecha_scraping)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (rol, fecha_str, caratula, tribunal, tipo_procedimiento, estado_procesal, accion, datetime.now()))
        
        nuevos_registros += 1
        
        if nuevos_registros >= 10:
            print("Se alcanzo el limite maximo de 10 nuevos registros.")
            break

    conn.commit()
    print(f"Actualizacion completada. Se guardaron o actualizaron {nuevos_registros} registros.")
    return nuevos_registros


class SegundoTribunalScraper:
    """Wrapper para integracion con el sistema BioNews."""
    
    def run(self):
        """Ejecuta el scraper y guarda directamente en la BD."""
        if not os.path.exists(DB_PATH):
            print("La base de datos no existe.")
            return 0
        
        ano_actual = str(datetime.now().year)
            
        try:
            conn = sqlite3.connect(DB_PATH)
            ultima_fecha = obtener_ultima_fecha(conn)
            
            if ultima_fecha:
                print(f"Ultima fecha en BD para el Segundo Tribunal: {ultima_fecha.strftime('%d-%m-%Y')}")
            else:
                print("No se encontraron fechas previas. Se procesaran los mas recientes.")
            
            resultados_interceptados = []
            extraer_nuevos_con_playwright(ano_actual, resultados_interceptados)
            
            nuevos = 0
            if resultados_interceptados:
                nuevos = procesar_nuevos_registros(resultados_interceptados, conn, ultima_fecha)
            else:
                print("No se interceptaron datos en la red.")
                
            conn.close()
            return nuevos
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return 0


if __name__ == "__main__":
    scraper = SegundoTribunalScraper()
    scraper.run()