from usuario import Usuario

opcao = input('1 - Registra novo usuário\n'
              '2 - Entra com usuário existente\n>')

if opcao == 1:
    usuario = Usuario(input('Digite seu nome'))
    print(usuario)

if opcao == 2:
    # como chamar o usuario existente
    pass
