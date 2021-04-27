from usuario2 import Usuario

nome_usuario = ''
usuario = ''

def main():

    global nome_usuario, usuario
    if nome_usuario != '':
        print(f'# Logado como {nome_usuario} #')

    opcao = input('1 - Login\n'
                  '2 - Registrar consumo de água\n'
                  '> ')
    if opcao == '1':
        usuario = Usuario(input('Digite seu nome: '))
        nome_usuario = usuario.nome
    elif opcao == '2':
        if nome_usuario == '':
            print('Você precisa fazer login antes de lançar consumo de água!')
            return main()
        else:
            usuario.quant_agua = int(input('Digite a quantidade de água em (ml) > '))
            print(usuario.__dict__)
            return main()
    main()



if __name__ == '__main__':
    main()
