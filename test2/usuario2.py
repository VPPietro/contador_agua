
class AddUsuario:

    contador_id = 0
    list_dict_users = []
    Novo = True
    nome_ident = {}

    def __init__(self, nome):
        self.__ident = AddUsuario.contador_id
        self.__nome = nome
        self.__quant_agua = 0  # Quantidade de água que o usuário bebeu
        self.__quant_vezes = 0  # Quantas vezes o usuário bebeu água
        AddUsuario.contador_id += 1
        self.nome_id()
        self.lista_dicionarios()

    @property
    def ident(self):
        return self.__ident

    @property
    def nome(self):
        return self.__nome

    @property
    def quant_agua(self):
        return self.__quant_agua

    @quant_agua.setter
    def quant_agua(self, ml):
        self.__quant_agua += ml
        self.__quant_vezes += 1
        self.lista_dicionarios()

    @property
    def quant_vezes(self):
        return self.__quant_vezes

    def nome_id(self):
        AddUsuario.nome_ident[self.__nome] = self.__ident

    def lista_dicionarios(self):
        if AddUsuario.Novo:                                                             # teste se é nova inclusao na lista
            AddUsuario.list_dict_users.append(self.__dict__)                            # adiciona dict na lista
            return AddUsuario.list_dict_users[AddUsuario.nome_ident[self.__nome]]       # retorna a lista na posicao do dict (dict)
        else:
            del AddUsuario.list_dict_users[AddUsuario.nome_ident[self.__nome]]                  # deleta o dicionario desatualizado na lista
            AddUsuario.list_dict_users.insert(AddUsuario.nome_ident[self.__nome], self.__dict__)# adiciona dict na lista
            return AddUsuario.list_dict_users[AddUsuario.nome_ident[self.__nome]]               # retorna a lista na posicao do dict (dict)


class ExeUsuario(AddUsuario):

    list_user = []

    def __init__(self, nome_user):
        if nome_user in ExeUsuario.list_user:
            print('entrou no existente')
            dict = AddUsuario.list_dict_users[AddUsuario.nome_ident[nome_user]]
            self.__ident = dict[list(dict)[0]]
            self.__nome = dict[list(dict)[1]]
            self.__quant_agua = dict[list(dict)[2]]
            self.__quant_vezes = dict[list(dict)[3]]

        else:
            print('entrou no super')
            super().__init__(nome_user)
            ExeUsuario.list_user.append(nome_user)
            AddUsuario.Novo = True


"""
EU FUCKING PODERIA FUCKING TER FEITO FUCKING TUDO NA FUCKING MESMA FUCKING CLASSE :')

"""




usuario = ExeUsuario('Pietro')
usuario = ExeUsuario('Pietro')
print(usuario.__dict__)
usuario = ExeUsuario('Pietro')
print(usuario.__dict__)
usuario = ExeUsuario('Giovanni')
print(usuario.__dict__)
usuario = ExeUsuario('Giovanni')
print(usuario.__dict__)
usuario = ExeUsuario('Pietro')
print(usuario.__dict__)
usuario = ExeUsuario('cú')
usuario = ExeUsuario('boobs')
usuario = ExeUsuario('Pietro')
print(usuario.__dict__)
usuario = ExeUsuario('Giovanni')
print(usuario.__dict__)
usuario = ExeUsuario('boobs')
print(usuario.__dict__)
