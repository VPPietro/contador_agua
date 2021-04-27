from usuario3 import Usuario


class Contagem(Usuario):

    list_dict_users = []
    nome_ident = {}
    novo = True

    def __init__(self, nome):
        if nome in Contagem.nome_ident:
            print('ja existe')
            dict_user = Contagem.list_dict_users[Contagem.nome_ident[nome]]
            self.__ident = dict_user[list(dict_user)[0]]
            self.__nome = dict_user[list(dict_user)[1]]
            self.__quant_agua = dict_user[list(dict_user)[2]]
            self.__quant_vezes = dict_user[list(dict_user)[3]]
        else:
            super().__init__(nome)
            self.__quant_agua = 0
            self.__quant_vezes = 0
            Contagem.nome_ident = {self.get_nome: self.get_ident}
            Contagem.lista_dicionarios(self)
            Contagem.novo = False

    @property
    def quant_agua(self):
        return self.__quant_agua

    @quant_agua.setter
    def quant_agua(self, ml):
        self.__quant_agua += ml
        self.__quant_vezes += 1
        self.lista_dicionarios()

    def lista_dicionarios(self):
        if Contagem.novo:                                                     # teste se é nova inclusao na lista
            Contagem.list_dict_users.append(self.__dict__)                    # adiciona dict na lista
            return Contagem.list_dict_users[Contagem.nome_ident[self.get_nome]] # retorna a lista na posicao do dict (dict)
        else:
            del Contagem.list_dict_users[Contagem.nome_ident[self.__nome]]                    # deleta posição original
            Contagem.list_dict_users.insert(Contagem.nome_ident[self.__nome], self.__dict__)  # adiciona dict na lista
            return Contagem.list_dict_users[Contagem.nome_ident[self.__nome]]                 # adiciona na posição origi.


usuario = Contagem('Pietro')
print(usuario.__dict__)
usuario.quant_agua = 750
print(usuario.__dict__)

"""usuario = Contagem('Giovanni')
print(usuario.__dict__)
usuario.quant_agua = 750
print(usuario.__dict__)"""

usuario = Contagem('Pietro')
print(usuario.__dict__)
usuario.quant_agua = 750
print(usuario.__dict__)

usuario = Contagem('Giovanni')
print(usuario.__dict__)
usuario.quant_agua = 750
print(usuario.__dict__)