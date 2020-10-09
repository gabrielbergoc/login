import json
from cliente import Cliente
import random
from caixa_eletronico import CaixaEletronico

caixa = CaixaEletronico()
notas_valores = [200, 100, 50, 20, 10, 5, 2]

def main():
    a = input('Bem vindo ao Banco Itauã.\nDigite 1 para fazer login'
              '\nDigite 2 para cadastrar um cliente\nDigite 3 para sair\n')
    print()

    if a == '1':
        login()
    elif a == '2':
        cadastra_cliente()
    elif a == '3':
        exit()
    else:
        print('Opção inválida')
        print()
        main()


def login():
    clientes = le_clientes()
    cliente = input('Cliente: ')
    cliente_dados = ()

    for i in range(len(clientes)):
        if clientes[i][0] == cliente:
            cliente_dados = clientes[i]
            break

    if cliente_dados == ():
        a = input('Cliente não cadastrado.\nDigite 1 para cadastrar cliente ou 2 para voltar\n')
        print()
        if a == '1':
            cadastra_cliente()
        elif a == '2':
            main()
    else:
        conta = input('Conta: ')
        senha = input('Senha: ')

        while conta != cliente_dados[3] or senha != cliente_dados[1]:
            print('Conta ou senha inválida')
            print()
            conta = input('Conta: ')
            senha = input('Senha: ')

        print()
        print('Bem-vindo/a/e, %s!' % cliente_dados[0])
        print()
        opera_conta(cliente_dados)


def opera_conta(cliente_dados):
    a = input('Digite 1 para ver o saldo\n'
              'Digite 2 para fazer um saque\n'
              'Digite 3 para fazer um depósito\n'
              'Digite 4 para fazer logout\n')
    print()
    if a == '1':
        consulta_saldo(cliente_dados)
    elif a == '2':
        saque(cliente_dados)
    elif a == '3':
        deposito(cliente_dados)
    elif a == '4':
        main()
    else:
        print('Opção inválida')
        print()
        opera_conta(cliente_dados)

def consulta_saldo(cliente_dados):
        print('Seu saldo é de R$%s' % cliente_dados[4])
        a = input('Digite 1 para fazer um saque\n'
                 'Digite 2 para fazer um depósito\n'
                 'Digite 3 para fazer logout\n')
        print()
        if a == '1':
            saque(cliente_dados)
        elif a == '2':
            deposito(cliente_dados)
        elif a == '3':
            main()
        else:
            print('Opção inválida')
            print()
            opera_conta(cliente_dados)

def saque(cliente_dados):
    valor = int(input('Digite o valor que deseja sacar: '))
    print()

    while valor > cliente_dados[4]:
        print('Saldo insuficiente')
        print()
        valor = int(input('Digite o valor que deseja sacar: '))
        print()

    saque = caixa.sacar(valor)

    if saque == None:
        saque(cliente_dados)
    else:
        print('Saque realizado com:')
        for i in range(len(saque)):
            if saque[i] > 0:
                print('%s notas de %s' % (saque[i], notas_valores[i]))

        print()
        cliente_atualizado = (cliente_dados[0], cliente_dados[1],
                              cliente_dados[2], cliente_dados[3], cliente_dados[4] - valor)
        clientes = le_clientes()

        for i in range(len(clientes)):
            if clientes[i][0] == cliente_dados[0]:
                clientes[i] = cliente_atualizado
        salva_clientes(clientes)
        opera_conta(cliente_atualizado)


def deposito(cliente_dados):
    valor = int(input('Digite o valor que deseja depositar: '))
    print()

    cliente_atualizado = (cliente_dados[0], cliente_dados[1],
                          cliente_dados[2], cliente_dados[3], cliente_dados[4] + valor)
    clientes = le_clientes()

    for i in range(len(clientes)):
        if clientes[i][0] == cliente_dados[0]:
            clientes[i] = cliente_atualizado

    print('Valor depositado com sucesso!')
    print()
    salva_clientes(clientes)
    opera_conta(cliente_atualizado)


def le_clientes():
    with open('clientes.json', 'r') as file:
        clientes = file.read()
        if len(clientes) > 0:
            clientes = json.loads(clientes)

            for i in range(len(clientes)):
                clientes[i] = tuple(clientes[i])

            return clientes
        else:
            return []


def salva_clientes(clientes):
    with open('clientes.json', 'w') as file:
        json.dump(clientes, file)
    print('Clientes salvos em clientes.json')
    print()


def cadastra_cliente():
    clientes = le_clientes()
    nome = input('Digite o nome completo: ')
    senha = input('Digite a senha: ')
    senha_conf = input('Confirme a senha: ')
    while senha != senha_conf:
        print('Senhas não coincidem!')
        senha = input('Digite a senha: ')
        senha_conf = input('Confirme a senha: ')
    conta = str(random.randint(10000, 99999))
    while conta in clientes:
        conta = random.randint(0, 6)
    cpf = input('Digite o CPF: ')
    print('O número da sua conta é %s' % conta)
    print()
    saldo = 0
    novo_cliente = Cliente(nome, senha, cpf, conta, saldo)
    cliente = (novo_cliente.nome, novo_cliente.senha,
               novo_cliente.cpf, novo_cliente.conta,
               novo_cliente.saldo)
    clientes.append(cliente)
    clientes.sort()
    salva_clientes(clientes)

if __name__ == '__main__':
    main()