class Almacenar_Id_Usuario_Consultorio_SG:
    _instansia = None
    ids = {"usu": 0, "con": 0}

    def __new__(cls) :
        if cls._instansia is None:
            cls._instansia = super(Almacenar_Id_Usuario_Consultorio_SG, cls).__new__(cls)
            cls._instansia.ids = {}
        return cls._instansia

    @classmethod
    def agregar_id_usuario(cls, id_usuario: int):
        """ se alamcenan los id del usuario"""
        cls.ids["usu"]=id_usuario

    @classmethod
    def agregar_id_consultorio(cls, id_consultorio: int):

        cls.ids["con"]=id_consultorio

    @classmethod
    def obtener_id_usuario(cls) -> int:
        """
        Se obitenen los id
        se retorna en una tupla para inmutabilidad
        """
        return cls.ids.get("usu", 0)

    @classmethod
    def obetner_id_consultorio(cls) -> int:

        return cls.ids.get("con", 0)

