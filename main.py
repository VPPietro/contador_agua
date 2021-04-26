from usuario import Usuario, UsuarioExistente

opcao = input('1 - Novo Usuario\n'
              '2 - Usuário existente\n>')
lista_users = []
usuario_posicao_index = {}


def main():
    opcao = input('1 - Novo Usuario\n'
                  '2 - Usuário existente\n>')
    if opcao == '1':

        usuario = Usuario(input('Digite seu nome: '))
        lista_users.append(usuario.__dict__)
        # usuario_posicao_index[list(Usuario.adiciona_id(usuario).keys())[0]] = Usuario.adiciona_id(usuario)
        usuario_posicao_index[usuario.nome] = usuario.ident
        print(lista_users, '\n', usuario_posicao_index)

    elif opcao == '2':
        usuario = input('Digite seu nome: ')
        if usuario in usuario_posicao_index:
            print('existe', usuario_posicao_index[usuario])

while True:
    main()