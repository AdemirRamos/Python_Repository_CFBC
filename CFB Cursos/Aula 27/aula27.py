import os; os.system('cls')

print('Exercício Prático (Parte 1)')
print()

carros = []

class Carro:
    nome = ''
    potência = 0
    velocidade_máxima = 0
    ligado = False
    def __init__(self, name, power):
        self.nome = name
        self.potência = power
        self.velocidade_máxima = int(power) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def instanciar(self):
        print(f'O nome do veículo é: {self.nome}; \nA potência do veículo é: {self.potência};')
        print(f'\nA velocidade máxima do veículo é: {self.velocidade_máxima};')
        print(f'\nO carro está ligado/desligado: {"Sim" if self.ligado else "Não"}.')

def menu():
    os.system('cls') or None #Checar "or None".
    print('1 - Novo carro')
    print('\n2 - Informações do carro')
    print('\n3 - Excluir carro')
    print('\n4 - Ligar o veículo')
    print('\n5 - Desligar o veículo')
    print('\n6 - Listar os carros')
    print('\n7 - Sair do programa')
    print(f'Quantidade de carros: {len(carros)}.')

    opção = int(input('Digite uma opção: '))
    return opção #Retorna para o menu a opção selecionada pelo usuário.

def novo_carro():
    os.system('cls') or None
    n = str(input('Nome do carro: '))
    p = int(input('Potência do carro: '))
    car = Carro(n, p)
    carros.append(car)
    print('Carro adicionado à lista com sucesso.')
    os.system('pause') #Checar.

def informações():
    os.system('cls') or None
    n = int(input('Informe o número do carro para mais informações: '))
    
    try:
        carros[n].info() #Outra maneira de se escrever essa mesma linha de código: "carros[int(n)].info()"

    except:
        print('O número digitado não corresponde a nenhum carro da lista.')
    os.system('pause')

def excluir_carro():
    os.system('cls') or None
    n = int(input('informe o número do carro que será excluído: '))

    try:    
        del carros[n]

    except:
        print('O número digitado não corresponde a nenhum carro da lista.')
    os.system('pause')

def ligar():
    os.system('cls') or None
    n = int(input('informe o número do carro que será ligado: '))

    try:    
        carros[n].ligar()
        print('Carro ligado.')

    except:
        print('O número digitado não corresponde a nenhum carro da lista.')
    os.system('pause')

def desligar():
    os.system('cls') or None
    n = int(input('informe o número do carro que será desligado: '))

    try:    
        carros[n].desligar()
        print('Carro desligado.')

    except:
        print('O número digitado não corresponde a nenhum carro da lista.')
    os.system('pause')

def listar():
    os.system('cls') or None

    p = 0
    for c in carros:
        print(f'{p}ª Carro: {c}\n')
        p += 1
    os.system('pause')
