class LoginFunction:
    '''Funciones de el login'''
    def validar_datos(self, value:str):
        '''Validar datos de entrada'''
        if not value.strip():
            return True
        else:
            return False

