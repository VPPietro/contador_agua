from agua4 import Agua


class User(Agua):

    def __init__(self, nome, quantidade_copo):
        super().__init__(quantidade_copo)
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
