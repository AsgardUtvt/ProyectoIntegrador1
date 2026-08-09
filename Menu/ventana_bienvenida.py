
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

    def cargar_datos_graficas(self):
        consultorio = AIUCSG.obetner_id_consultorio()
        inicio = self.fecha_inicio.date().toString("yyyy-MM-dd")
        fin = self.fecha_fin.date().toString("yyyy-MM-dd")

        lista_datos =[consultorio, f"{inicio} 00:00:00", f"{fin} 23:00:00"]

        citas = GMS.datos_grafica_citas(self.db, lista_datos)
        medicamentos = GMS.datos_grafica_medicamentos(self.db, lista_datos)

        # Gráfica 1
        self.ax1.clear()

        x1 = [d["EJEX"] for d in citas]
        y1 = [d["EJEY"] for d in citas]

        self.ax1.plot(x1, y1, marker="o", linestyle="-", color="#1A5276", linewidth=2, label="Citas")
        self.ax1.fill_between(x1, y1, 0, color="#B3D1FF", alpha=0.25)
        self.ax1.set_title("Citas por día")
        self.ax1.grid(True)
        self.ax1.legend()
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
        self.fig1.autofmt_xdate()
        self.fig1.tight_layout()
        self.canvas1.draw_idle()

        # Gráfica 2
        self.ax2.clear()

        x2 = [m["EJEX"] for m in medicamentos]
        y2 = [m["EJEY"] for m in medicamentos]


        self.ax2.plot(x2, y2, marker="o", linestyle="-", color="#2980B9", linewidth=2, label="Medicamento")
        self.ax2.fill_between(x2, y2, 0, color="#B3D1FF", alpha=0.25)
        self.ax2.set_title("Medicamentos preescritos")
        self.ax2.grid(True, axis="y")
        self.ax2.tick_params(axis="x", labelrotation=45)
        self.ax2.legend()
        self.fig2.tight_layout()
        self.canvas2.draw_idle()
