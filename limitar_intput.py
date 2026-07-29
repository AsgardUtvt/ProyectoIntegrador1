from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
class Limitar_Intput:
    """ Clase para limitar los caractres. """
    _tipo_limitdor_dict = {
        # Consultorio
        "regular": QRegularExpression("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]{10, 100}$"),
        "codigo_postal": QRegularExpression("^[0-9]{5}$"),
        "numero_telefonico": QRegularExpression("^[0-9]{10,13}$"),
        "calle": QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{4,100}$"),
        "consultorio": QRegularExpression("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]{6,50}$"),
        "numero_calle": QRegularExpression("^[snSN0-9]{3}$"),
        "calle_numero": QRegularExpression("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ]{6,50}$"),
        "fecha":QRegularExpression("^[0-9]{10,13}$"),
        # Usuario
        "datos_generales": QRegularExpression("^[a-zA-ZñÑáéíóúÁÉÍÓÚñÑ ]{6,50}$"),
        "cedula": QRegularExpression("^[0-9]{13}$")
    }
    @classmethod
    def limitar_caracteres(cls, tipo_limitador: str):
        tipo_limitador.lower()
        cls.validador = QRegularExpressionValidator(cls._tipo_limitdor_dict.get(tipo_limitador, QRegularExpression("^[a-zA-Z0-9áéíóúÁÍÓÚñÑ ]{10, 100}")))
        return cls.validador
