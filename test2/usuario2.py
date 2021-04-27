
class Usuario:

    contador_id = 0
    list_dict_users = []
    Novo = True
    nome_ident = {}

    def __init__(self, nome):
        if nome in Usuario.nome_ident:
            print('existe')
            dict_user = Usuario.list_dict_users[Usuario.nome_ident[nome]]
            self.__ident = dict_user[list(dict_user)[0]]
            self.__nome = dict_user[list(dict_user)[1]]
            self.__quant_agua = dict_user[list(dict_user)[2]]
            self.__quant_vezes = dict_user[list(dict_user)[3]]
        else:
            self.__ident = Usuario.contador_id
            self.__nome = nome
            self.__quant_agua = 0     # Quantidade de água que o usuário bebeu
            self.__quant_vezes = 0    # Quantas vezes o usuário registrou que bebeu água
            Usuario.contador_id += 1
            self.nome_id()            # Adiciona a lista de dict o user e id '{'Pietro': 0}
            self.lista_dicionarios()  # Adiciona/Atualiza a lista de dict de atributos e valores de cada user

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
        Usuario.nome_ident[self.__nome] = self.__ident

    def lista_dicionarios(self):
        if Usuario.Novo:                                                     # teste se é nova inclusao na lista
            Usuario.list_dict_users.append(self.__dict__)                    # adiciona dict na lista
            return Usuario.list_dict_users[Usuario.nome_ident[self.__nome]]  # retorna a lista na posicao do dict (dict)
        else:
            del Usuario.list_dict_users[Usuario.nome_ident[self.__nome]]                    # deleta posição original
            Usuario.list_dict_users.insert(Usuario.nome_ident[self.__nome], self.__dict__)  # adiciona dict na lista
            return Usuario.list_dict_users[Usuario.nome_ident[self.__nome]]                 # adiciona na posição origi.


"""class ExeUsuario(AddUsuario):

    list_user = []

    def __init__(self, nome_user):
        if nome_user in ExeUsuario.list_user:
            dict_user = AddUsuario.list_dict_users[AddUsuario.nome_ident[nome_user]]
            self.__ident = dict_user[list(dict_user)[0]]
            self.__nome = dict_user[list(dict_user)[1]]
            self.__quant_agua = dict_user[list(dict_user)[2]]
            self.__quant_vezes = dict_user[list(dict_user)[3]]

        else:
            super().__init__(nome_user)
            print(self.__dict__)
            ExeUsuario.list_user.append(nome_user)
            AddUsuario.Novo = True

EU FUCKING PODERIA FUCKING TER FEITO FUCKING TUDO NA FUCKING MESMA FUCKING CLASSE :')
só colocar o if-else dentro do __init__ da AddUsuario
"""

"""wrong"""


