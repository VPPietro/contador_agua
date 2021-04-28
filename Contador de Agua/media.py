

class Media:

    def __init__(self, dicionario_copos, list_quantidade):
        self.__dicionario = dicionario_copos
        self.__quantidade = list_quantidade

    def media(self):
        return sum(self.__quantidade) / len(self.__dicionario)
