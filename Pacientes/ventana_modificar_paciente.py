from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDialog
from BaseDatos.MySqlManager import MySqlManager


class Ventana_Modificar_Pacientes(QDialog):
    def __init__(self, db: MySqlManager, id_paciente: int):
        super().__init__()
        self.db = db
        self.id_paciente = id_paciente
        uic.loadUi("Documentacion/QtDesigner/pacientes_modificar.ui", self)
        self.cargar_datos_paciente()
        self.btn_modificar_paciente.clicked.connect(self.guardar_modificacion)

    def cargar_datos_paciente(self):
        try:
            with self.db.obtener_cursor() as cursor:
                sql = """
                    SELECT id_paciente, paciente_name, paciente_paterno, paciente_materno,
                        paciente_telefono, paciente_alergia, paciente_fecha_nacimiento,
                        paciente_sexo, paciente_correo_electronico, paciente_direccion
                    FROM Paciente
                    WHERE id_paciente = %s;
                """
                cursor.execute(sql, (self.id_paciente,))
                paciente = cursor.fetchone()
                print(f"Cargar de datos {paciente}")
                if paciente:
                    self.txt_nombre.setText(str(paciente['paciente_name'] or ''))
                    self.txt_paterno.setText(str(paciente['paciente_paterno'] or ''))
                    self.txt_apellido_materno.setText(str(paciente['paciente_materno'] or ''))
                    self.txt_telefono.setText(str(paciente['paciente_telefono'] or ''))
                    self.text_alergias.setPlainText(str(paciente['paciente_alergia'] or ''))
                    self.txt_email.setText(str(paciente['paciente_correo_electronico'] or ''))
                    self.text_direccion.setText(str(paciente['paciente_direccion'] or ''))

                    if paciente['paciente_sexo']:
                        index_sexo = self.cmb_genero.findText(paciente['paciente_sexo'])
                        if index_sexo >= 0:
                            self.cmb_genero.setCurrentIndex(index_sexo)

                    if paciente['paciente_fecha_nacimiento']:
                        fecha = paciente['paciente_fecha_nacimiento']
                        if hasattr(fecha, 'date'):
                            fecha = fecha.date()
                        self.date_nacimiento.setDate(QDate(fecha.year, fecha.month, fecha.day))
        except Exception as e:
            print(f"Error al cargar datos del paciente: {e}")

    def guardar_modificacion(self):
        try:
            nombre = self.txt_nombre.text().strip()
            paterno = self.txt_paterno.text().strip()
            materno = self.txt_apellido_materno.text().strip()
            f_nacimiento = self.date_nacimiento.date().toString("yyyy-MM-dd")
            sexo = self.cmb_genero.currentText()
            alergias = self.text_alergias.toPlainText().strip() or None
            telefono = self.txt_telefono.text().strip()
            email = self.txt_email.text().strip() or None
            direccion = self.text_direccion.text().strip() or None

            with self.db.obtener_cursor() as cursor:
                sql_update = """
                    UPDATE Paciente
                    SET paciente_name = %s,
                        paciente_paterno = %s,
                        paciente_materno = %s,
                        paciente_fecha_nacimiento = %s,
                        paciente_sexo = %s,
                        paciente_alergia = %s,
                        paciente_telefono = %s,
                        paciente_correo_electronico = %s,
                        paciente_direccion = %s
                    WHERE id_paciente = %s;
                """
                valores = (
                    nombre,
                    paterno,
                    materno,
                    f_nacimiento,
                    sexo,
                    alergias,
                    telefono,
                    email,
                    direccion,
                    self.id_paciente,
                )
                cursor.execute(sql_update, valores)
                self.db.commit_conexion()
            print(f"Paciente {self.id_paciente} actualizado con éxito en la BD.")
            self.accept()
        except Exception as e:
            print(f"Error al guardar modificación: {e}")
