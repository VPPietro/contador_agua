from usuario2 import Usuario


class Contagem:

    def __init__(self, dict_user):
        self.__ident = dict_user[list(dict_user)[0]]
        self.__nome = dict_user[list(dict_user)[1]]
        self.__quant_agua = dict_user[list(dict_user)[2]]
        self.__quant_vezes = dict_user[list(dict_user)[3]]

    @property
    def quant_agua(self):
        return self.__quant_agua

    @quant_agua.setter
    def quant_agua(self, ml):
        self.__quant_agua += ml
        self.__quant_vezes += 1

"""wrong"""
