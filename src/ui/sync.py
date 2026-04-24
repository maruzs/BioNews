import flet as ft
import threading
from ui.styles import COLOR_PRIMARIO, COLOR_FONDO, COLOR_TEXTO, COLOR_TEXTO_MEDIO, COLOR_ACENTO, COLOR_DIVIDER

# ── Definicion de scrapers con nombre legible ─────────────────────────────────
SCRAPERS_NOTICIAS = [
    ("MMA",              "scrapers.mma",           "MMAScraper",             "get_latest_news", "noticias"),
    ("SMA",              "scrapers.sma",            "SMAScraper",             "get_latest_news", "noticias"),
    ("SEA Noticias",     "scrapers.sea",            "SEAScraper",             "get_latest_news", "noticias"),
    ("SBAP",             "scrapers.sbap",           "SBAPScraper",            "get_latest_news", "noticias"),
    ("Sernageomin",      "scrapers.sernageomin",    "SernageominScraper",     "get_latest_news", "noticias"),
    ("Diario Oficial",   "scrapers.diario_oficial", "DiarioOficialScraper",   "get_latest_news", "noticias"),
    ("Tribunal Ambiental","scrapers.tribunal2",     "TribunalScraper",        "get_latest_news", "noticias"),
    ("Tercer Tribunal",  "scrapers.tribunal3",      "TercerTribunalScraper",  "get_latest_news", "noticias"),
    ("Corte Suprema",    "scrapers.corteSuprema",   "CorteSupremaScraper",    "get_latest_news", "noticias"),
]

SCRAPERS_LEGALES = [
    ("1TA Legal",        "scrapers.primerTribunal", "PrimerTribunalScraper",     "get_legal_data", "legal"),
    ("2TA Legal",        "scrapers.segundoTribunal","SegundoTribunalScraper",    "get_legal_data", "legal"),
    ("3TA Legal",        "scrapers.tercerTribunal", "TercerTribunalScraperLegal","get_legal_data", "legal"),
    ("SEA Pertinencias", "scrapers.sea_legal",      "SEALegalScraper",           "get_legal_data", "legal"),
    ("SNIFA Sancionatorios","scrapers.snifa",        "SnifaScraper",              "get_legal_data", "legal"),
    ("SNIFA Req. Ingreso","scrapers.reqSEIA",        "SnifaIngresoScraper",       "get_legal_data", "legal"),
    ("SNIFA Fiscalizaciones","scrapers.fiscalizaciones","SnifaFiscalizacionScraper","get_legal_data","legal"),
]

ALL_SCRAPERS = SCRAPERS_LEGALES + SCRAPERS_NOTICIAS


def _icon_estado(estado: str) -> ft.Icon:
    if estado == "ok":
        return ft.Icon(ft.icons.CHECK_CIRCLE, color="#2E7D32", size=18)
    elif estado == "error":
        return ft.Icon(ft.icons.ERROR_OUTLINE, color="#C62828", size=18)
    elif estado == "running":
        return ft.ProgressRing(width=16, height=16, stroke_width=2, color=COLOR_PRIMARIO)
    else:
        return ft.Icon(ft.icons.RADIO_BUTTON_UNCHECKED, color="#BDBDBD", size=18)


class SyncPanel:
    """Panel modal de sincronizacion con barra de progreso y estado por scraper."""

    def __init__(self, page: ft.Page, db, on_complete=None):
        self.page = page
        self.db = db
        self.on_complete = on_complete
        self._running = False

        # Estado de cada scraper: "pending" | "running" | "ok" | "error"
        self._states = {s[0]: "pending" for s in ALL_SCRAPERS}
        self._counts = {s[0]: 0 for s in ALL_SCRAPERS}

        # Controles UI
        self._progress = ft.ProgressBar(
            value=0,
            color=COLOR_PRIMARIO,
            bgcolor="#E8F5E9",
            height=8,
            border_radius=4,
        )
        self._progress_text = ft.Text("0 / 0", size=12, color=COLOR_TEXTO_MEDIO)
        self._status_text = ft.Text("Listo para sincronizar", size=13, color=COLOR_TEXTO_MEDIO)

        # Filas de estado
        self._rows: dict[str, ft.Row] = {}
        rows_controls = []
        for name, *_ in ALL_SCRAPERS:
            icon_ref = ft.Container(content=_icon_estado("pending"), width=24)
            count_text = ft.Text("", size=11, color=COLOR_TEXTO_MEDIO)
            row = ft.Row(
                [
                    icon_ref,
                    ft.Text(name, size=12, color=COLOR_TEXTO, font_family="DM Sans", expand=True),
                    count_text,
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            self._rows[name] = (row, icon_ref, count_text)
            rows_controls.append(
                ft.Container(
                    content=row,
                    bgcolor=COLOR_FONDO,
                    border_radius=8,
                    padding=ft.padding.symmetric(horizontal=12, vertical=7),
                    margin=ft.margin.only(bottom=4),
                )
            )

        self._btn_start = ft.ElevatedButton(
            "Iniciar sincronización",
            icon=ft.icons.SYNC,
            style=ft.ButtonStyle(
                bgcolor=COLOR_PRIMARIO,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.padding.symmetric(horizontal=20, vertical=12),
            ),
            on_click=self._start,
        )
        self._btn_close = ft.TextButton(
            "Cerrar",
            style=ft.ButtonStyle(color=COLOR_TEXTO_MEDIO),
            on_click=self._close,
            disabled=False,
        )

        scroll_list = ft.ListView(
            controls=rows_controls,
            expand=True,
            spacing=0,
            height=320,
        )

        panel_content = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.SYNC, color=COLOR_PRIMARIO, size=20),
                            ft.Text("Sincronización de datos",
                                    font_family="Sora", size=16,
                                    weight=ft.FontWeight.W_700, color=COLOR_TEXTO),
                        ],
                        spacing=8,
                    ),
                    ft.Divider(color=COLOR_DIVIDER, height=12),
                    self._status_text,
                    ft.Row(
                        [self._progress, self._progress_text],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Container(height=4),
                    scroll_list,
                    ft.Container(height=8),
                    ft.Row(
                        [self._btn_start, self._btn_close],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=8,
                    ),
                ],
                spacing=6,
            ),
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            padding=ft.padding.all(20),
            shadow=ft.BoxShadow(
                blur_radius=20,
                color=ft.colors.with_opacity(0.15, ft.colors.BLACK),
                offset=ft.Offset(0, -4),
            ),
        )

        self._sheet = ft.BottomSheet(
            content=panel_content,
            open=False,
            enable_drag=False,
        )
        self.page.overlay.append(self._sheet)

    def open(self):
        """Abre el panel."""
        if not self._running:
            self._reset_states()
        self._sheet.open = True
        self._sheet.update()

    def _close(self, _=None):
        if not self._running:
            self._sheet.open = False
            self._sheet.update()

    def _reset_states(self):
        for name in self._states:
            self._states[name] = "pending"
            self._counts[name] = 0
            _, icon_ref, count_text = self._rows[name]
            icon_ref.content = _icon_estado("pending")
            count_text.value = ""
        self._progress.value = 0
        self._progress_text.value = f"0 / {len(ALL_SCRAPERS)}"
        self._status_text.value = "Listo para sincronizar"
        self._btn_start.disabled = False
        self._btn_close.disabled = False
        try:
            self._sheet.update()
        except Exception:
            pass

    def _set_state(self, name: str, estado: str, count: int = 0):
        self._states[name] = estado
        self._counts[name] = count
        _, icon_ref, count_text = self._rows[name]
        icon_ref.content = _icon_estado(estado)
        if estado == "ok" and count > 0:
            count_text.value = f"+{count} nuevos"
            count_text.color = "#2E7D32"
        elif estado == "error":
            count_text.value = "Error"
            count_text.color = "#C62828"
        elif estado == "running":
            count_text.value = "..."
            count_text.color = COLOR_TEXTO_MEDIO
        else:
            count_text.value = ""

        done = sum(1 for s in self._states.values() if s in ("ok", "error"))
        total = len(ALL_SCRAPERS)
        self._progress.value = done / total
        self._progress_text.value = f"{done} / {total}"

        try:
            self._sheet.update()
        except Exception:
            pass

    def _start(self, _):
        if self._running:
            return
        self._running = True
        self._btn_start.disabled = True
        self._btn_close.disabled = True
        self._reset_states()
        self._sheet.update()
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        import importlib
        db = self.db
        total = len(ALL_SCRAPERS)
        done = 0

        for name, module_path, class_name, method_name, data_type in ALL_SCRAPERS:
            try:
                self._status_text.value = f"Consultando {name}..."
                self._set_state(name, "running")

                mod = importlib.import_module(module_path)
                cls = getattr(mod, class_name)
                instance = cls()
                method = getattr(instance, method_name)
                result = method()

                count = 0
                if result:
                    if data_type == "noticias":
                        count = db.save_news(result)
                    else:
                        count = db.save_legal(result)

                self._set_state(name, "ok", count)
            except Exception as e:
                print(f"Error en scraper {name}: {e}")
                self._set_state(name, "error")

            done += 1

        self._status_text.value = "✓ Sincronización completada"
        self._btn_start.disabled = False
        self._btn_close.disabled = False
        self._running = False

        try:
            self._sheet.update()
        except Exception:
            pass

        if self.on_complete:
            try:
                self.on_complete()
            except Exception:
                pass