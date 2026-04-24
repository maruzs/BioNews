# src/ui/main_window.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QStackedWidget, QProgressBar, QLabel, QDialog, QDialogButtonBox, QApplication, QFrame
)
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QIcon
from .dashboard import DashboardView
from .legal import LegalView
from .styles import COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_FONDO
import sys
import os

# --- Worker para scraping en segundo plano ---
class ScrapingWorker(QThread):
    progreso = Signal(str, int)
    finalizado = Signal(bool, str)

    def run(self):
        try:
            from scrapers.mma import MMAScraper
            from scrapers.sbap import SBAPScraper
            from scrapers.diario_oficial import DiarioOficialScraper
            from scrapers.sea import SEAScraper
            from scrapers.sernageomin import SernageominScraper
            from scrapers.tribunal2 import TribunalScraper
            from scrapers.sea_legal import SEALegalScraper
            from scrapers.snifa import SnifaScraper
            from scrapers.sma import SMAScraper
            from scrapers.corteSuprema import CorteSupremaScraper
            from scrapers.tribunal3 import TercerTribunalScraper
            from scrapers.primerTribunal import PrimerTribunalScraper
            from scrapers.segundoTribunal import SegundoTribunalScraper
            from scrapers.tercerTribunal import TercerTribunalScraperLegal
            from scrapers.reqSEIA import SnifaIngresoScraper
            from scrapers.fiscalizaciones import SnifaFiscalizacionScraper
            from database.manager import DatabaseManager

            db = DatabaseManager()
            total_pasos = 17
            paso = 0

            def avanzar(mensaje):
                nonlocal paso
                paso += 1
                self.progreso.emit(mensaje, int(paso / total_pasos * 100))

            # Legales
            for scraper, nombre in [
                (PrimerTribunalScraper(), "1TA"),
                (SegundoTribunalScraper(), "2TA"),
                (TercerTribunalScraperLegal(), "3TA"),
                (SEALegalScraper(), "SEA Pertinencias"),
                (SnifaScraper(), "SNIFA Sancionatorios"),
                (SnifaIngresoScraper(), "SNIFA Ingreso"),
                (SnifaFiscalizacionScraper(), "SNIFA Fiscalizaciones"),
            ]:
                datos = scraper.get_legal_data()
                if datos:
                    db.save_legal(datos)
                avanzar(f"✔ Legal: {nombre}")

            # Noticias
            for scraper, nombre in [
                (TercerTribunalScraper(), "Tercer Tribunal"),
                (CorteSupremaScraper(), "Corte Suprema"),
                (SMAScraper(), "SMA"),
                (MMAScraper(), "MMA"),
                (SBAPScraper(), "SBAP"),
                (DiarioOficialScraper(), "Diario Oficial"),
                (SEAScraper(), "SEA"),
                (SernageominScraper(), "Sernageomin"),
                (TribunalScraper(), "Tribunal Ambiental"),
            ]:
                noticias = scraper.get_latest_news()
                if noticias:
                    db.save_news(noticias)
                avanzar(f"✔ Noticias: {nombre}")

            self.finalizado.emit(True, "Sincronización completada con éxito.")
        except Exception as e:
            self.finalizado.emit(False, f"Error: {str(e)}")

# --- Diálogo de progreso ---
class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sincronizando...")
        self.setFixedSize(450, 180)
        self.setModal(True)

        layout = QVBoxLayout(self)
        self.label = QLabel("Iniciando scraping...")
        layout.addWidget(self.label)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.btn_box = QDialogButtonBox(QDialogButtonBox.Cancel)
        self.btn_box.rejected.connect(self.reject)
        self.btn_box.setEnabled(False)
        layout.addWidget(self.btn_box)

    def actualizar(self, mensaje, porcentaje):
        self.label.setText(mensaje)
        self.progress.setValue(porcentaje)

    def terminar(self, exito, mensaje):
        self.label.setText(mensaje)
        self.progress.setValue(100 if exito else 0)
        self.btn_box.setEnabled(True)
        self.btn_box.setStandardButtons(QDialogButtonBox.Close)

# --- Ventana principal ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioNews – Inteligencia Ambiental V1.0")
        self.resize(1200, 800)
        
        # Configurar ícono de la ventana
        self.setup_icon()
        
        self.setup_ui()

    def setup_icon(self):
        # Obtener ruta del ícono
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        icon_path = os.path.join(base_path, "assets", "planet-earth.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            self.icon_path = icon_path
        else:
            self.icon_path = None

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barra superior con botón de scraping
        top_bar_widget = QFrame()
        top_bar_widget.setStyleSheet(f"background-color: {COLOR_PRIMARIO.name()};")
        top_bar_layout = QHBoxLayout(top_bar_widget)
        top_bar_layout.setContentsMargins(15, 10, 15, 10)

        # Ícono y título
        if self.icon_path and os.path.exists(self.icon_path):
            icono_label = QLabel()
            icono_label.setPixmap(QIcon(self.icon_path).pixmap(32, 32))
            top_bar_layout.addWidget(icono_label)
        
        titulo = QLabel(" BioNews")
        titulo.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        top_bar_layout.addWidget(titulo)

        top_bar_layout.addStretch()

        self.btn_sync = QPushButton("🔄 Actualizar datos")
        self.btn_sync.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2E7D32;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E8F5E9;
            }
        """)
        self.btn_sync.clicked.connect(self.iniciar_scraping)
        top_bar_layout.addWidget(self.btn_sync)

        main_layout.addWidget(top_bar_widget)

        # Navegación lateral + contenido
        content_layout = QHBoxLayout()
        content_layout.setSpacing(0)

        # Sidebar
        sidebar_widget = QFrame()
        sidebar_widget.setStyleSheet("background-color: #282828; min-width: 160px; max-width: 160px;")
        sidebar = QVBoxLayout(sidebar_widget)
        sidebar.setContentsMargins(10, 20, 10, 20)
        sidebar.setSpacing(10)

        self.btn_noticias = QPushButton("📰 Noticias")
        self.btn_legal = QPushButton("⚖️ Legal")
        for btn in [self.btn_noticias, self.btn_legal]:
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px;
                    border: none;
                    border-radius: 6px;
                    font-size: 14px;
                }
                QPushButton:checked {
                    background-color: #C8E6C9;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #E8F5E9;
                }
            """)
        self.btn_noticias.setChecked(True)
        self.btn_noticias.clicked.connect(lambda: self.cambiar_vista(0))
        self.btn_legal.clicked.connect(lambda: self.cambiar_vista(1))

        sidebar.addWidget(self.btn_noticias)
        sidebar.addWidget(self.btn_legal)
        sidebar.addStretch()

        # Stacked widget para las vistas
        self.stack = QStackedWidget()
        self.vista_noticias = DashboardView()
        self.vista_legal = LegalView()
        self.stack.addWidget(self.vista_noticias)
        self.stack.addWidget(self.vista_legal)

        content_layout.addWidget(sidebar_widget)
        content_layout.addWidget(self.stack)

        main_layout.addLayout(content_layout)

    def cambiar_vista(self, index):
        self.stack.setCurrentIndex(index)
        self.btn_noticias.setChecked(index == 0)
        self.btn_legal.setChecked(index == 1)
        if index == 0:
            self.vista_noticias.cargar_noticias()
        else:
            self.vista_legal.cargar_datos()

    def iniciar_scraping(self):
        self.dialog = ProgressDialog(self)
        self.worker = ScrapingWorker()
        self.worker.progreso.connect(self.dialog.actualizar)
        self.worker.finalizado.connect(self.on_scraping_finalizado)
        self.worker.start()
        self.dialog.show()

    def on_scraping_finalizado(self, exito, mensaje):
        self.dialog.terminar(exito, mensaje)
        # Refrescar vistas
        self.vista_noticias.cargar_noticias()
        self.vista_legal.cargar_datos()