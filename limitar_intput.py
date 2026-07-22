from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
class Limitar_Intput:

    _tipo_limitdor_dict = {
        "regular": QRegularExpression("^[a-zA-Z0-9áéíóúÁÉÍÓÚ ]{10, 12}$"),
        "codigo_postal": QRegularExpression("^[0-9]{5}$"),
        "numero_telefonico": QRegularExpression("^[0-9]{10,13}$")
    }
    @classmethod
    def limitar_caracteres(cls, tipo_limitador: str):
        validador = QRegularExpressionValidator(cls._tipo_limitdor_dict.get(tipo_limitador, "regular"))
        return validador
