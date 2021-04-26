
class Usuario:

    contador_id = 0

    def __init__(self, nome):
        self.__id = Usuario.contador_id + 1  # id do usuário
        self.__nome = nome
        self.__quant_agua = 0  # Quantidade de água que o usuário bebeu
        self.__quant_vezes = 0  # Quantas vezes o usuário bebeu água
        Usuario.contador_id = self.__id

    @property
    def quant_agua(self):
        return self.__quant_agua

    @property
    def quant_vezes(self):
        return self.__quant_vezes

    @property
    def nome(self):
        return self.__nome
