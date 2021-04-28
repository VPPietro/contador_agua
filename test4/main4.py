from usuario4 import User
from ranking4 import Ranking

"""lista_dict = []
while True:
    nome = input('Digite seu nome ou sair para finalizar: ').title()
    if nome == 'Sair':
        break
    info = User(nome, int(input('Digite a quantidade de copos que você tomou: ')))
    lista_dict.append({info.nome: info.quant_copo})
    print(lista_dict)"""


rank = Ranking([{'Pietro': 2}, {'Neto': 2}, {'Pietro': 1}, {'Giovanni': 2}, {'Pietro': 6}, {'Giovanni': 50}])
print(rank.listas_para_dict_correto())


