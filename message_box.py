
from PyQt6.QtWidgets import QMessageBox

class Message_Box:

    def message_box(self, parent, tipo: str, titulo: str, mensaje: str):
        tipo_dic = {
            "info": QMessageBox.information,
            "warning": QMessageBox.warning,
            "error": QMessageBox.critical,
            "question": QMessageBox.question
        }
        metodo =  tipo_dic.get(tipo.lower(), QMessageBox.information)
        if tipo.lower() == "question":
            return metodo(parent, titulo, mensaje, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return metodo(parent, titulo, mensaje)
