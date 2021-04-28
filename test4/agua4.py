

class Agua:

    def __init__(self, quantidade_copo):
        self.__quant_copo = quantidade_copo

    @property
    def quant_copo(self):
        return self.__quant_copo
