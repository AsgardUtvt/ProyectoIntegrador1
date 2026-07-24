import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QCalendarWidget, QPushButton, QLabel, QMessageBox, QInputDialog
)
from PyQt6.QtCore import QDate

class CitasWindow(QMainWindow):
    def __init__(self, menu_principal_callback=None):
        
        super().__init__()
        self.menu_principal_callback = menu_principal_callback
        
        self.db_config = {
            'host': 'localhost',
            'database': 'sihmed',
            'user': 'root',
            'password': '' ## contraseña si la requiere
        }
        
        self.init_ui()

    def conectar_db(self):
        """Establece y retorna una nueva conexión a la base de datos."""
        try:
            return mysql.connector.connect(**self.db_config)
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos:\n{err}")
            return None

    def init_ui(self):
        self.setWindowTitle("SIHMED - Menú de Citas")
        self.resize(750, 500)

        # Widget central y layout principal
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        # --- SECCIÓN IZQUIERDA: Calendario e Indicadores ---
        left_layout = QVBoxLayout()
        
        self.label_titulo = QLabel("Gestión de Citas Médicas - SIHMED")
        self.label_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        left_layout.addWidget(self.label_titulo)

        # Calendario
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.mostrar_citas_dia)
        left_layout.addWidget(self.calendar)

        # Etiqueta para mostrar las citas del día seleccionado
        self.label_info_citas = QLabel("Citas registradas para la fecha:")
        self.label_info_citas.setStyleSheet("font-weight: bold; margin-top: 10px;")
        left_layout.addWidget(self.label_info_citas)

        self.label_detalle_citas = QLabel("Selecciona un día en el calendario.")
        left_layout.addWidget(self.label_detalle_citas)

        main_layout.addLayout(left_layout, stretch=2)

        # --- SECCIÓN DERECHA: Botones de Acción ---
        right_layout = QVBoxLayout()
        right_layout.addStretch()

        # Botón Generar Cita
        self.btn_generar = QPushButton("Generar Cita")
        self.btn_generar.setStyleSheet("background-color: #2ecc71; color: white; padding: 8px; font-weight: bold;")
        self.btn_generar.clicked.connect(self.generar_cita)
        right_layout.addWidget(self.btn_generar)

        # Botón Modificar Cita
        self.btn_modificar = QPushButton("Modificar Cita")
        self.btn_modificar.setStyleSheet("background-color: #f39c12; color: white; padding: 8px; font-weight: bold;")
        self.btn_modificar.clicked.connect(self.modificar_cita)
        right_layout.addWidget(self.btn_modificar)

        # Botón Eliminar Cita
        self.btn_eliminar = QPushButton("Eliminar Cita")
        self.btn_eliminar.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-weight: bold;")
        self.btn_eliminar.clicked.connect(self.eliminar_cita)
        right_layout.addWidget(self.btn_eliminar)

        right_layout.addStretch()

        # Botón Volver al Menú Principal
        self.btn_volver = QPushButton("Volver al Menú")
        self.btn_volver.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px;")
        self.btn_volver.clicked.connect(self.volver_menu)
        right_layout.addWidget(self.btn_volver)

        main_layout.addLayout(right_layout, stretch=1)

        self.setCentralWidget(central_widget)
        
        # Cargar las citas del día actual al iniciar
        self.mostrar_citas_dia()

    # --- LÓGICA DE LAS ACCIONES CONECTADA A LA BD ---

    def obtener_citas_por_fecha(self, fecha_qdate):
        """Consulta la base de datos para obtener las citas de una fecha específica."""
        conexion = self.conectar_db()
        if not conexion:
            return []
        
        citas = []
        try:
            cursor = conexion.cursor(dictionary=True)
            fecha_str = fecha_qdate.toString("yyyy-MM-dd")
            
            query = """
                SELECT c.id_cita, c.cita_date, c.cita_nota, 
                       p.paciente_name, p.paciente_paterno, 
                       co.conultorio_name, tr.tratamiento_name, ec.estado_cita
                FROM Cita c
                JOIN Paciente p ON c.id_paciente = p.id_paciente
                JOIN Consultorio co ON c.id_consultorio = co.id_consultorio
                JOIN Estado_Cita ec ON c.id_estado_cita = ec.id_estado_cita
                JOIN Tratamiento tr ON c.id_tratamiento = tr.id_tratamiento
                WHERE DATE(c.cita_date) = %s
            """
            cursor.execute(query, (fecha_str,))
            citas = cursor.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error de Base de Datos", f"No se pudieron cargar las citas:\n{err}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        return citas

    def mostrar_citas_dia(self):
        """Muestra en la interfaz las citas del día seleccionado en el calendario."""
        fecha_seleccionada = self.calendar.selectedDate()
        citas_del_dia = self.obtener_citas_por_fecha(fecha_seleccionada)
        
        if citas_del_dia:
            texto_list = []
            for c in citas_del_dia:
                hora = c['cita_date'].strftime("%H:%M")
                paciente = f"{c['paciente_name']} {c['paciente_paterno']}"
                texto_list.append(f"[{hora}] Paciente: {paciente} | Tratam: {c['tratamiento_name']} ({c['estado_cita']})")
            texto = "\n".join(texto_list)
        else:
            texto = "No hay citas programadas para este día."
            
        self.label_detalle_citas.setText(texto)

    def generar_cita(self):
        """Lógica para insertar una nueva cita en la tabla `Cita`."""
        fecha_seleccionada = self.calendar.selectedDate()
        
        id_paciente, ok_p = QInputDialog.getInt(self, "Generar Cita", "Ingrese el ID del Paciente:")
        if not ok_p: return
        
        id_consultorio, ok_c = QInputDialog.getInt(self, "Generar Cita", "Ingrese el ID del Consultorio:")
        if not ok_c: return
        
        id_estado, ok_e = QInputDialog.getInt(self, "Generar Cita", "Ingrese el ID del Estado de Cita:")
        if not ok_e: return
        
        id_tratamiento, ok_t = QInputDialog.getInt(self, "Generar Cita", "Ingrese el ID del Tratamiento:")
        if not ok_t: return
        
        nota, ok_n = QInputDialog.getText(self, "Generar Cita", "Nota o motivo de la cita:")
        if not ok_n: nota = ""

        hora_str, ok_h = QInputDialog.getText(self, "Generar Cita", "Hora de la cita (HH:MM:SS):", text="10:00:00")
        if not ok_h: return

        fecha_hora_str = f"{fecha_seleccionada.toString('yyyy-MM-dd')} {hora_str}"

        conexion = self.conectar_db()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO Cita (cita_date, cita_nota, id_paciente, id_consultorio, id_estado_cita, id_tratamiento) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (fecha_hora_str, nota, id_paciente, id_consultorio, id_estado, id_tratamiento))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Cita generada y guardada en la base de datos.")
                self.mostrar_citas_dia()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Error", f"No se pudo registrar la cita:\n{err}")
            finally:
                conexion.close()

    def modificar_cita(self):
        """Lógica para modificar los datos de una cita existente."""
        fecha_seleccionada = self.calendar.selectedDate()
        citas_del_dia = self.obtener_citas_por_fecha(fecha_seleccionada)
        
        if not citas_del_dia:
            QMessageBox.warning(self, "Atención", "No hay citas en este día para modificar.")
            return

        opciones = [f"ID: {c['id_cita']} - {c['paciente_name']} ({c['cita_date'].strftime('%H:%M')})" for c in citas_del_dia]
        seleccion, ok = QInputDialog.getItem(self, "Modificar Cita", "Seleccione la cita a modificar:", opciones, 0, False)
        
        if ok and seleccion:
            id_cita = int(seleccion.split(" - ")[0].replace("ID: ", ""))
            
            nueva_nota, ok_nota = QInputDialog.getText(self, "Modificar Cita", "Actualizar nota de la cita:")
            if not ok_nota: return

            conexion = self.conectar_db()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    query = "UPDATE Cita SET cita_nota = %s WHERE id_cita = %s"
                    cursor.execute(query, (nueva_nota, id_cita))
                    conexion.commit()
                    QMessageBox.information(self, "Éxito", "Cita modificada correctamente.")
                    self.mostrar_citas_dia()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Error", f"No se pudo actualizar:\n{err}")
                finally:
                    conexion.close()

    def eliminar_cita(self):
        """Lógica para eliminar una cita de la base de datos."""
        fecha_seleccionada = self.calendar.selectedDate()
        citas_del_dia = self.obtener_citas_por_fecha(fecha_seleccionada)
        
        if not citas_del_dia:
            QMessageBox.warning(self, "Atención", "No hay citas en este día para eliminar.")
            return

        opciones = [f"ID: {c['id_cita']} - {c['paciente_name']} ({c['cita_date'].strftime('%H:%M')})" for c in citas_del_dia]
        seleccion, ok = QInputDialog.getItem(self, "Eliminar Cita", "Seleccione la cita a eliminar:", opciones, 0, False)
        
        if ok and seleccion:
            id_cita = int(seleccion.split(" - ")[0].replace("ID: ", ""))
            
            confirmacion = QMessageBox.question(
                self, "Confirmar Eliminación", 
                "¿Está seguro de eliminar esta cita de la base de datos?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if confirmacion == QMessageBox.StandardButton.Yes:
                conexion = self.conectar_db()
                if conexion:
                    try:
                        cursor = conexion.cursor()
                        query = "DELETE FROM Cita WHERE id_cita = %s"
                        cursor.execute(query, (id_cita,))
                        conexion.commit()
                        QMessageBox.information(self, "Éxito", "Cita eliminada de la base de datos.")
                        self.mostrar_citas_dia()
                    except mysql.connector.Error as err:
                        QMessageBox.critical(self, "Error", f"No se pudo eliminar:\n{err}")
                    finally:
                        conexion.close()

    def volver_menu(self):
        """Regresa al menú principal del sistema."""
        if self.menu_principal_callback:
            self.menu_principal_callback()
        else:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CitasWindow()
    ventana.show()
    sys.exit(app.exec())