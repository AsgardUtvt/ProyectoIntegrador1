from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox
from BaseDatos.MySqlManager import MySqlManager
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUC
from message_box import Message_Box as MB


class Ventana_Crear_Paciente(QDialog):

    def __init__(self, db: MySqlManager):
        super().__init__()
        self.db = db
        self.mb = MB()
        uic.loadUi("Documentacion/QtDesigner/pacientes_crear.ui", self)
        if hasattr(self, "btn_crear_paciente"):
            self.btn_crear_paciente.setText("Guardar Paciente")
            self.btn_crear_paciente.clicked.connect(self.guardar_paciente)

    def guardar_paciente(self):
        try:
            nombre = self.txt_nombre.text().strip()
            paterno = self.txt_paterno.text().strip()
            materno = self.txt_materno.text().strip()
            f_nacimiento = self.date_nacimiento.date().toString("yyyy-MM-dd")
            
            if hasattr(self, "txt_sexo"):
                sexo = self.txt_sexo.currentText()
            elif hasattr(self, "cmb_genero"):
                sexo = self.cmb_genero.currentText()
            else:
                sexo = "Masculino"
            
            if hasattr(self, "text_alergias"):
                if hasattr(self.text_alergias, "toPlainText"):
                    alergias = self.text_alergias.toPlainText().strip() or None
                else:
                    alergias = self.text_alergias.text().strip() or None
            else:
                alergias = None
                
            telefono = self.txt_telefono.text().strip()
            email = self.txt_email.text().strip() or None
            if hasattr(self, "text_direccion"):
                if hasattr(self.text_direccion, "toPlainText"):
                    direccion = self.text_direccion.toPlainText().strip() or None
                else:
                    direccion = self.text_direccion.text().strip() or None
            else:
                direccion = None

            if not nombre or not paterno or not materno or not telefono:
                self.mb.message_box(
                    self,
                    "warning",
                    "Campos obligatorios",
                    "Por favor completa Nombre, Apellidos y Teléfono."
                )
                return

            id_consultorio = AIUC.obetner_id_consultorio()
            
            if hasattr(AIUC, "obtener_id_usuario"):
                id_usuario = AIUC.obtener_id_usuario()
            else:
                id_usuario = 1

            if hasattr(self, "combo_tipo_sangre"):
                id_tipo_sangre = self.combo_tipo_sangre.currentIndex() + 1
            else:
                id_tipo_sangre = 1

            with self.db.obtener_cursor() as cursor:
                sql_insert = """
                    INSERT INTO Paciente (
                        paciente_name,
                        paciente_paterno,
                        paciente_materno,
                        paciente_telefono,
                        paciente_numero_emergencia1,
                        id_tipo_sangre,
                        id_consultorio,
                        id_usuario,
                        paciente_fecha_nacimiento,
                        paciente_sexo,
                        paciente_correo_electronico,
                        paciente_direccion
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                valores = (
                    nombre,
                    paterno,
                    materno,
                    telefono,
                    telefono,
                    id_tipo_sangre,
                    id_consultorio,
                    id_usuario,
                    f_nacimiento,
                    sexo,
                    email,
                    direccion,
                )
                cursor.execute(sql_insert, valores)
                self.db.conexion.commit()

            self.mb.message_box(
                self, "info", "Éxito", "Paciente registrado correctamente."
            )
            self.accept()

        except Exception as e:
            print(f"Error al registrar paciente: {e}")
            self.mb.message_box(
                self,
                "error",
                "Error al registrar",
                f"Ocurrió un error al registrar el paciente:\n{e}",
            )