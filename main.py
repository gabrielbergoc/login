import json


def main():
    a = input('Bem vindo ao sistema.\nDigite 1 para fazer login'
              '\nDigite 2 para criar uma conta\nDigite 3 para sair\n')

    if a == '1':
        login()
    elif a == '2':
        criar_conta()
    elif a == '3':
        exit()
    else:
        print('Opção inválida')
        main()


def login():
    users = le_usuarios()

    user = input('Usuário: ')
    senha = input('Senha: ')
    print()

    if user not in users:
        print('Usuário não existe')
        print()
        main()
    else:
        if senha != users[user]:
            print('Senha incorreta!')
            print()
            main()
        else:
            print('Bem vindo, %s' % user)
            print()
            main()


def criar_conta():
    user = input('Usuário: ')
    senha = input('Senha: ')
    conf_senha = input('Confirme a senha: ')
    print()

    if senha != conf_senha:
        print('Senhas não coincidem')
        print()
        criar_conta()
    else:
        usuario = {user: senha}
        usuario_key = list(usuario.keys())
        users = le_usuarios()

        if usuario_key[0] in users:
            print('Usuário já existente')
            print()
            criar_conta()
        else:
            with open('login.json', 'w+') as file:
                users.update(usuario)
                json.dump(users, file)
            main()


def le_usuarios():
    with open('login.json', 'r') as file:
        users = file.read()
        if len(users) > 0:
            users = json.loads(users)
            return users
        else:
            return {}


if __name__ == '__main__':
    main()
