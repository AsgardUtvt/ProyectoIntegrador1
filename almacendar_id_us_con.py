class Almacenar_Id_Usuario_Consultorio_SG:
    _instansia = None
    ids = {"usu": 0, "con": 0}

    def __new__(cls) :
        if cls._instansia is None:
            cls._instansia = super(Almacenar_Id_Usuario_Consultorio_SG, cls).__new__(cls)
            cls._instansia.ids = {}
        return cls._instansia

    @classmethod
    def agregar_id(cls, tipo: str, ids: int):
        """ se alamcenan los id """
        cls.ids[tipo]=ids

    @classmethod
    def obtener_id(cls) -> tuple:
        """ Se obitenen los id
            se retorna en una tupla para inmutabilidad
        """
        id_lista = []
        for Id in cls.ids.values():
            id_lista.append(Id)
        return tuple(id_lista)
