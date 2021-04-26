
class Usuario:

    contador_id = 0

    def __init__(self, nome):
        self.__ident = Usuario.contador_id
        self.__nome = nome
        self.__quant_agua = 0  # Quantidade de água que o usuário bebeu
        self.__quant_vezes = 0  # Quantas vezes o usuário bebeu água
        Usuario.contador_id += 1

    @property
    def quant_agua(self):
        return self.__quant_agua

    @property
    def quant_vezes(self):
        return self.__quant_vezes

    @property
    def nome(self):
        return self.__nome

    @property
    def ident(self):
        return self.__ident

    """def adiciona_id(self):
        return self.__ident"""


class UsuarioExistente:

    def __init__(self, dict_user):
        self.__ident = dict_user[list(dict_user.keys())[0]]
        self.__nome = dict_user[list(dict_user.keys())[1]]
        self.__quant_agua = dict_user[list(dict_user.keys())[2]]
        self.__quant_vezes = dict_user[list(dict_user.keys())[3]]

    @property
    def quant_agua(self):
        return self.__quant_agua

    @quant_agua.setter
    def quant_agua(self, valor_adicionar):
        self.__quant_agua += valor_adicionar

    @property
    def quant_vezes(self):
        return self.__quant_vezes

    @quant_vezes.setter
    def quant_vezes(self):
        self.__quant_vezes += 1
