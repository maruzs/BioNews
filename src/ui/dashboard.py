# src/ui/dashboard.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QScrollArea,
    QLabel, QFrame, QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QFont
from PySide6.QtWebEngineWidgets import QWebEngineView
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_FONDO

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.fuentes_disponibles = [
            "SMA", "SEA", "Corte Suprema", "Tercer Tribunal", "MMA",
            "SBAP", "Diario Oficial", "Sernageomin", "Tribunal Ambiental"
        ]
        self.seleccionadas = set(self.fuentes_disponibles)
        self.setup_ui()
        self.cargar_noticias()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        titulo = QLabel("📰 Noticias Ambientales")
        titulo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        layout.addWidget(titulo)

        filtros_layout = QHBoxLayout()
        filtros_layout.setSpacing(15)
        for fuente in self.fuentes_disponibles:
            cb = QCheckBox(fuente)
            cb.setChecked(True)
            cb.toggled.connect(lambda checked, f=fuente: self.toggle_fuente(f, checked))
            filtros_layout.addWidget(cb)
        layout.addLayout(filtros_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        self.web_container = QWidget()
        self.web_layout = QVBoxLayout(self.web_container)
        self.web_layout.setSpacing(15)
        self.web_layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area.setWidget(self.web_container)
        layout.addWidget(self.scroll_area)

    def toggle_fuente(self, fuente, checked):
        if checked:
            self.seleccionadas.add(fuente)
        else:
            self.seleccionadas.discard(fuente)
        self.cargar_noticias()

    def crear_tarjeta_html(self, titulo, fecha, fuente, link, imagen_url):
        titulo_escapado = titulo.replace('"', '&quot;').replace("'", "&#39;")
        fuente_escapada = fuente.replace('"', '&quot;').replace("'", "&#39;")
        
        imagen_html = ""
        if imagen_url and str(imagen_url).startswith('http'):
            imagen_html = f'<img src="{imagen_url}" style="width:100%;height:180px;object-fit:cover;border-radius:8px;margin-bottom:10px;" loading="lazy">'
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; }}
                .card {{
                    background: white;
                    border: 1px solid #ddd;
                    border-radius: 12px;
                    padding: 15px;
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    box-sizing: border-box;
                }}
                .card:hover {{ border-color: #2E7D32; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
                .fuente {{ color: #2E7D32; font-weight: bold; font-size: 11px; margin-bottom: 8px; }}
                .titulo {{ font-weight: bold; font-size: 14px; margin-bottom: 10px; color: #212121; line-height: 1.4; }}
                .fecha {{ color: #999; font-size: 11px; margin-bottom: 15px; }}
                .boton {{
                    background-color: #2E7D32;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 6px;
                    text-decoration: none;
                    text-align: center;
                    font-weight: bold;
                    font-size: 12px;
                    display: block;
                    margin-top: auto;
                }}
                .boton:hover {{ background-color: #1B5E20; }}
            </style>
        </head>
        <body>
            <div class="card">
                {imagen_html}
                <div class="fuente">{fuente_escapada}</div>
                <div class="titulo">{titulo_escapado}</div>
                <div class="fecha">📅 {fecha}</div>
                <a href="{link}" class="boton" target="_blank">Abrir en navegador</a>
            </div>
        </body>
        </html>
        """
        return html

    def cargar_noticias(self):
        # Limpiar tarjetas anteriores
        while self.web_layout.count():
            item = self.web_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        noticias = self.db.get_latest_news(limit=200)
        filtradas = [n for n in noticias if n[4] in self.seleccionadas]

        # Agrupar en filas de 3
        for i in range(0, len(filtradas), 3):
            fila_widget = QWidget()
            fila_layout = QHBoxLayout(fila_widget)
            fila_layout.setSpacing(15)
            fila_layout.setContentsMargins(0, 0, 0, 0)
            
            for j in range(3):
                if i + j < len(filtradas):
                    item = filtradas[i + j]
                    link = item[0]
                    titulo = item[1]
                    fecha = item[2]
                    imagen_url = item[3]
                    fuente = item[4]
                    
                    tarjeta_html = self.crear_tarjeta_html(titulo, fecha, fuente, link, imagen_url)
                    
                    web_view = QWebEngineView()
                    web_view.setHtml(tarjeta_html)
                    web_view.setMinimumWidth(350)
                    web_view.setMaximumWidth(400)
                    web_view.setMinimumHeight(400)
                    web_view.setMaximumHeight(500)
                    web_view.setStyleSheet("background: transparent;")
                    
                    fila_layout.addWidget(web_view)
                else:
                    spacer = QWidget()
                    spacer.setMinimumWidth(350)
                    fila_layout.addWidget(spacer)
            
            self.web_layout.addWidget(fila_widget)