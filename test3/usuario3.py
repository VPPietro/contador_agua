
class Usuario:

    contador_id = 0

    def __init__(self, nome):
        self.__ident = Usuario.contador_id
        self.__nome = nome
        Usuario.contador_id += 1

    @property
    def get_ident(self):
        return self.__ident

    @property
    def get_nome(self):
        return self.__nome
