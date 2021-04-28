

class User:

    def __init__(self, nome, quantidade_copo):
        self.__nome = nome
        self.__quant_copo = quantidade_copo

    @property
    def nome(self):
        return self.__nome

    @property
    def quant_copo(self):
        return self.__quant_copo
