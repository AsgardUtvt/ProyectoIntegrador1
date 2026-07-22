
from PyQt6.QtWidgets import QMessageBox

class Message_Box:

    def message_box(self, tipo: str, titulo: str, mensaje: str):
        tipo_dic = {
            "info": QMessageBox.information,
            "warning": QMessageBox.warning,
            "error": QMessageBox.critical,
            "question": QMessageBox.question
        }
        metodo =  tipo_dic.get(tipo, "info")
        if tipo.lower() == "question":
            return metodo(self, titulo, mensaje, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return metodo(tipo.lower(), titulo, mensaje)
