# src/ui/legal.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem,
    QHeaderView, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QFont
from database.manager import DatabaseManager
from .styles import COLOR_PRIMARIO

class LegalView(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setup_ui()
        self.cargar_datos()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        titulo = QLabel("⚖️ Legal y Transparencia")
        titulo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        layout.addWidget(titulo)

        self.tabs_main = QTabWidget()
        layout.addWidget(self.tabs_main)

        # Pestaña Tribunales
        self.tab_tribunales = QWidget()
        self.tabs_main.addTab(self.tab_tribunales, "Tribunales")
        self.setup_tabla(self.tab_tribunales, "tribunales")

        # Pestaña SNIFA con subpestañas
        self.tab_snifa = QTabWidget()
        self.tabs_main.addTab(self.tab_snifa, "SNIFA")

        self.sub_sancionatorios = QWidget()
        self.tab_snifa.addTab(self.sub_sancionatorios, "Sancionatorios")
        self.setup_tabla(self.sub_sancionatorios, "sancionatorios")

        self.sub_ingreso = QWidget()
        self.tab_snifa.addTab(self.sub_ingreso, "Requisitos Ingreso")
        self.setup_tabla(self.sub_ingreso, "ingreso")

        self.sub_fiscalizaciones = QWidget()
        self.tab_snifa.addTab(self.sub_fiscalizaciones, "Fiscalizaciones")
        self.setup_tabla(self.sub_fiscalizaciones, "fiscalizaciones")

        # Pestaña SEA
        self.tab_sea = QWidget()
        self.tabs_main.addTab(self.tab_sea, "SEA")
        self.setup_tabla(self.tab_sea, "sea")

    def setup_tabla(self, parent_widget, tipo):
        layout = QVBoxLayout(parent_widget)
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Nombre", "Estado/Tipo", "Fecha", "Fuente", "Link"])
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.verticalHeader().setVisible(False)
        table.setStyleSheet("QTableWidget { border: 1px solid #ccc; gridline-color: #eee; }")
        layout.addWidget(table)
        parent_widget.table = table  # guardamos referencia

    def cargar_datos(self):
        datos = self.db.get_all_legal(limit=500)
        self._llenar_tabla(self.tab_tribunales.table, datos, "tribunales")
        self._llenar_tabla(self.sub_sancionatorios.table, datos, "sancionatorios")
        self._llenar_tabla(self.sub_ingreso.table, datos, "ingreso")
        self._llenar_tabla(self.sub_fiscalizaciones.table, datos, "fiscalizaciones")
        self._llenar_tabla(self.tab_sea.table, datos, "sea")

    def _llenar_tabla(self, table, datos, tipo):
        table.setRowCount(0)
        fuentes_tribunales = ["1TA", "2TA", "3TA", "Corte Suprema"]
        for item in datos:
            link, nombre, fecha, estado, tipo_db, fuente, _ = item

            # Filtros por tipo de pestaña
            if tipo == "tribunales" and fuente not in fuentes_tribunales:
                continue
            if tipo == "sea" and fuente != "SEA Pertinencias":
                continue
            if tipo == "sancionatorios" and "Sancionatorio" not in tipo_db:
                continue
            if tipo == "ingreso" and "Ingreso" not in tipo_db:
                continue
            if tipo == "fiscalizaciones" and "Fiscalizacion" not in tipo_db:
                continue
            if tipo not in ["tribunales", "sea"] and fuente == "SEA Pertinencias":
                continue
            if tipo in ["sancionatorios", "ingreso", "fiscalizaciones"] and fuente != "SNIFA":
                continue

            row = table.rowCount()
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(nombre))
            table.setItem(row, 1, QTableWidgetItem(f"{estado} / {tipo_db}"))
            table.setItem(row, 2, QTableWidgetItem(fecha))
            table.setItem(row, 3, QTableWidgetItem(fuente))

            btn_link = QPushButton("Abrir")
            btn_link.setStyleSheet(f"background-color: {COLOR_PRIMARIO.name()}; color: white; border: none; padding: 4px 8px;")
            btn_link.clicked.connect(lambda checked, url=link: QDesktopServices.openUrl(QUrl(url)))
            table.setCellWidget(row, 4, btn_link)