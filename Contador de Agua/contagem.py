
class Ranking:

    def __init__(self, lista_dict):
        self.__list = lista_dict

    def dict_para_listas(self):
        nome = []
        quantidade = []
        for x in self.__list:
            nome.append(list(x)[0])
            quantidade.append(x[list(x)[0]])
        return nome, quantidade

    def listas_para_dict_correto(self):
        nome, quantidade = self.dict_para_listas()
        lista_nomes = []
        dicionario = {}
        quant_vezes = {}
        cont = 0
        for x in nome:
            if x in lista_nomes:
                dicionario[x] += quantidade[cont]
                quant_vezes[x] += 1
            else:
                dicionario[x] = quantidade[cont]
                quant_vezes[x] = 1
                lista_nomes.append(x)
            cont += 1
        return dicionario, quant_vezes, quantidade
