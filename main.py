from usuario import Usuario, UsuarioExistente
from contagem import Contagem

lista_users = []
usuario_posicao_index = {}
login = False
usuario = ''


def main():

    global lista_users, usuario_posicao_index, login, usuario

    if login:
        print(f'# Logado como {usuario.nome} #')
    opcao = input('1 - Login com novo usuário\n'
                  '2 - Login com usuário existente\n'
                  '3 - Registrar a quantidade de água que bebeu.\n'
                  '>')

    if opcao == '1':
        usuario = Usuario(input('Digite seu nome: ').title())
        if usuario.nome in usuario_posicao_index:
            print('Usuário já existe!\n')
            return main()
        else:
            lista_users.append(usuario.__dict__)
            usuario_posicao_index[usuario.nome] = usuario.ident
            login = True

    elif opcao == '2':
        usuario = input('Digite seu nome: '.title())
        if usuario in usuario_posicao_index:
            usuario = UsuarioExistente(lista_users[usuario_posicao_index[usuario]])
            login = True
        else:
            print('Usuário não encontrado!')
            return main()

    elif opcao == '3':
        if login:
            usuario = Contagem(usuario.__dict__)
            usuario.quant_agua = int(input('Digite a quantidade de água (ml) > '))
            print(usuario.quant_agua)
            print(usuario.quant_vezes)
    print(lista_users)
    return main()


if __name__ == '__main__':
    main()
