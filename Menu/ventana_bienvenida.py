import numpy as np
from datetime import datetime, timedelta

from datetime import timedelta, datetime

from PyQt6 import uic
from PyQt6.QtCore import QTimer, QDate
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from message_box import Message_Box
from BaseDatos.MySqlManager import MySqlManager
from Login.Functions.Encrypt import Encrypt

from Menu.general_menu_service import General_Menu_Service as GMS
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG


class Ventana_Bienvenida(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()

        self.mb = Message_Box()
        self.navegar = navegar
        self.db = db
        self.en = Encrypt()

        uic.loadUi("Documentacion/QtDesigner/menu_principal.ui", self)

        self.inicializar_graficas()

        self.fecha_inicio.setDate(QDate.currentDate().addMonths(-1))
        self.fecha_fin.setDate(QDate.currentDate())
        self.fecha_inicio.dateChanged.connect(self.cargar_datos_graficas)
        self.fecha_fin.dateChanged.connect(self.cargar_datos_graficas)

        QTimer.singleShot(100, self.cargar_datos_graficas)

    def inicializar_graficas(self):
        # Gráfica 1 (líneas)
        self.fig1 = Figure(figsize=(7, 3), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.canvas1 = FigureCanvas(self.fig1)

        layout1 = QVBoxLayout(self.layout_grafica_1)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.addWidget(self.canvas1)

        # Gráfica 2 (barras)
        self.fig2 = Figure(figsize=(7, 3), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)
        self.canvas2 = FigureCanvas(self.fig2)

        layout2 = QVBoxLayout(self.layout_grafica_2)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.addWidget(self.canvas2)

        # Gráfica 3 (proyección citas)
        self.fig3 = Figure(figsize=(7, 3), dpi=100)
        self.ax3 = self.fig3.add_subplot(111)
        self.canvas3 = FigureCanvas(self.fig3)

        layout3 = QVBoxLayout(self.layout_grafica_3)
        layout3.setContentsMargins(0, 0, 0, 0)
        layout3.addWidget(self.canvas3)

        # Gráfica 4 (proyección medicamentos)
        self.fig4 = Figure(figsize=(7, 3), dpi=100)
        self.ax4 = self.fig4.add_subplot(111)
        self.canvas4 = FigureCanvas(self.fig4)

        layout4 = QVBoxLayout(self.layout_grafica_4)
        layout4.setContentsMargins(0, 0, 0, 0)
        layout4.addWidget(self.canvas4)

    def cargar_datos_graficas(self):
        inicio = self.fecha_inicio.date().toPyDate()
        fin = self.fecha_fin.date().toPyDate()

        datos_consulta = [AIUCSG.obetner_id_consultorio(), f"{inicio} 23:00:00", f"{fin} 00:00:00"]

        x1, y1 = self.serie_completa(GMS.datos_grafica_citas(self.db, datos_consulta ), inicio, fin)
        x2, y2 = self.serie_completa(GMS.datos_grafica_medicamentos(self.db, datos_consulta), inicio, fin)

        # Gráfica 1: citas
        self.ax1.clear()
        self.ax1.plot(x1, y1, marker="o", linestyle="-", color="#2b5b84", linewidth=2, label="Citas")
        self.ax1.fill_between(x1, y1, 0, color="#2b5b84", alpha=0.25)
        self.ax1.set_ylim(bottom=0)
        self.ax1.spines["top"].set_visible(False)
        self.ax1.spines["right"].set_visible(False)
        self.ax1.grid(True, linestyle="--", alpha=0.5)
        self.ax1.set_axisbelow(True)
        self.ax1.set_title("Citas por día")
        self.ax1.legend()
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
        self.fig1.autofmt_xdate()
        self.fig1.tight_layout()
        self.canvas1.draw_idle()

        # Gráfica 2: medicamentos
        self.ax2.clear()
        self.ax2.plot(x2, y2, marker="o", linestyle="-", color="#e67e22", linewidth=2, label="Medicamentos")
        self.ax2.fill_between(x2, y2, 0, color="#e67e22", alpha=0.25)
        self.ax2.set_ylim(bottom=0)
        self.ax2.spines["top"].set_visible(False)
        self.ax2.spines["right"].set_visible(False)
        self.ax2.grid(True, linestyle="--", alpha=0.5)
        self.ax2.set_axisbelow(True)
        self.ax2.set_title("Medicamentos preescritos")
        self.ax2.legend()
        self.ax2.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
        self.fig2.autofmt_xdate()
        self.fig2.tight_layout()
        self.canvas2.draw_idle()

                # --- Gráfica 3: proyección de citas ---
        x1_fut, y1_fut = self.proyectar(x1, y1)

        self.ax3.clear()
        self.ax3.plot(x1, y1, linestyle="-", color="#2b5b84", alpha=0.4, linewidth=1.5, label="Histórico")
        if x1_fut:
            self.ax3.plot(x1_fut, y1_fut, marker="o", linestyle="--", color="#c0392b", linewidth=2, label="Proyección 7 días")
            self.ax3.fill_between(x1_fut, y1_fut, 0, color="#c0392b", alpha=0.15)

        self.ax3.set_title("PROYECCIÓN DE CITAS", fontsize=14, fontweight="bold", color="#c0392b")
        self.ax3.set_ylim(bottom=0)
        self.ax3.spines["top"].set_visible(False)
        self.ax3.spines["right"].set_visible(False)
        self.ax3.grid(True, linestyle="--", alpha=0.5)
        self.ax3.set_axisbelow(True)
        self.ax3.legend()
        self.ax3.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
        self.fig3.autofmt_xdate()
        self.fig3.tight_layout()
        self.canvas3.draw_idle()

        # --- Gráfica 4: proyección de medicamentos ---
        x2_fut, y2_fut = self.proyectar(x2, y2)

        self.ax4.clear()
        self.ax4.plot(x2, y2, linestyle="-", color="#e67e22", alpha=0.4, linewidth=1.5, label="Histórico")
        if x2_fut:
            self.ax4.plot(x2_fut, y2_fut, marker="o", linestyle="--", color="#8e44ad", linewidth=2, label="Proyección 7 días")
            self.ax4.fill_between(x2_fut, y2_fut, 0, color="#8e44ad", alpha=0.15)

        self.ax4.set_title("PROYECCIÓN DE MEDICAMENTOS", fontsize=14, fontweight="bold", color="#8e44ad")
        self.ax4.set_ylim(bottom=0)
        self.ax4.spines["top"].set_visible(False)
        self.ax4.spines["right"].set_visible(False)
        self.ax4.grid(True, linestyle="--", alpha=0.5)
        self.ax4.set_axisbelow(True)
        self.ax4.legend()
        self.ax4.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
        self.fig4.autofmt_xdate()
        self.fig4.tight_layout()
        self.canvas4.draw_idle()


    def serie_completa(self, datos, inicio, fin):
        conteo = {}
        for d in datos:
            f = d["EJEX"]                      # fecha
            if isinstance(f, datetime):
                f = f.date()
            conteo[f] = d["EJEY"]              # conteo

        fechas, valores = [], []
        dia = inicio
        while dia <= fin:
            fechas.append(dia)
            valores.append(conteo.get(dia, 0))
            dia += timedelta(days=1)
        return fechas, valores

    def proyectar(self, x, y, dias=7):
        if len(x) < 2:
            return [], []

        xs = np.array([(d - x[0]).days for d in x])
        ys = np.array(y, dtype=float)

        poly = np.poly1d(np.polyfit(xs, ys, 1))

        xs_fut = np.arange(xs.max() + 1, xs.max() + dias + 1)
        ys_fut = np.maximum(poly(xs_fut), 0)

        fechas_fut = [x[0] + timedelta(days=int(d)) for d in xs_fut]
        return fechas_fut, ys_fut.tolist()
