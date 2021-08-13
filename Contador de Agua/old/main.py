from usuario import User
from contagem import Ranking
from media import Media


lista_dict = []

while True:
    nome = input('Digite seu nome ou sair para finalizar: ').title()
    if nome == 'Sair':
        break
    info = User(nome, int(input('Digite a quantidade de água que você tomou (ml): ')))
    lista_dict.append({info.nome: info.quant_copo})
    print(lista_dict)


rank = Ranking(lista_dict)
usuario_quantidade, quant_vezes, lista_quantidade  = rank.listas_para_dict_correto()
media = Media(usuario_quantidade, lista_quantidade)

print(f'\n\nA quantidade de água que cada usuário bebeu foi:\n{usuario_quantidade}')
print(f'A quantidade de vezes que cada usuário bebeu água foi:\n{quant_vezes}')
print(f'A média de água de todos os usuários foi: {media.media()}ml')
