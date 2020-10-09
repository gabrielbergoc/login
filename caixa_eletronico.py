class CaixaEletronico():

    def __init__(self, notas_200=10, notas_100=20, notas_50=30, notas_20=50,
                      notas_10=100, notas_5=100, notas_2=150):
        self.notas_disponiveis = [notas_200, notas_100, notas_50,
                         notas_20, notas_10, notas_5, notas_2]
        self.notas_valores = [200, 100, 50, 20, 10, 5, 2]

    def sacar(self, valor):
        notas_disponiveis = self.notas_disponiveis[:]
        notas_saque = [0, 0, 0, 0, 0, 0, 0]
        i = 0
        while valor > 0 and i < 7:
            if valor >= self.notas_valores[i] and notas_disponiveis[i] > 0:
                while valor >= self.notas_valores[i] and notas_disponiveis[i] > 0:
                    valor -= self.notas_valores[i]
                    notas_saque[i] += 1
                    notas_disponiveis[i] -= 1
            i += 1

        if valor > 0 and notas_disponiveis[6] > 0:
            notas_saque[5] -= 1
            notas_saque[6] += 3
            notas_disponiveis[6] -= 3
            self.notas_disponiveis = notas_disponiveis[:]
            return notas_saque
        elif valor > 0 and notas_disponiveis[6] == 0:
            print('Valor indisponível')
            return None
        else:
            self.notas_disponiveis = notas_disponiveis[:]
            return notas_saque


    def depositar(self, valor):
        pass

    def extrato(self):
        pass