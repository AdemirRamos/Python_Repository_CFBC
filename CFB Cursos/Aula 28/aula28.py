import os; os.system('cls')

print('Exercício Prático (Parte 2)')
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
        print(f'\nO nome do veículo é: {self.nome}; \n\nA potência do veículo é: {self.potência};')
        print(f'\nA velocidade máxima do veículo é: {self.velocidade_máxima};')
        print(f'\nO carro está ligado/desligado: {"ligado" if self.ligado else "desligado"}.\n')

def menu():
    os.system('cls') or None #Checar "or None".
    print('1 - Novo carro')
    print('\n2 - Informações do carro')
    print('\n3 - Excluir carro')
    print('\n4 - Ligar o veículo')
    print('\n5 - Desligar o veículo')
    print('\n6 - Listar os carros')
    print('\n7 - Sair do programa')
    print(f'\nQuantidade de carros: {len(carros)}.')

    opção = int(input('\nDigite uma opção: '))
    return opção #Retorna para o menu a opção selecionada pelo usuário.

def novo_carro():
    os.system('cls') or None
    n = str(input('Nome do carro: '))
    p = int(input('\nPotência do carro: '))
    car = Carro(n, p)
    carros.append(car)
    print('\nCarro adicionado à lista com sucesso.\n')
    os.system('pause') #Checar.

def informações():
    os.system('cls') or None
    n = int(input('\nInforme o número do carro para mais informações: '))
    
    try:
        carros[n].instanciar() #Outra maneira de se escrever essa mesma linha de código: "carros[int(n)].info()"

    except:
        print('\nO número digitado não corresponde a nenhum carro da lista.\n')
    os.system('pause')

def excluir_carro():
    os.system('cls') or None
    n = int(input('\ninforme o número do carro que será excluído: '))

    try:    
        del carros[n]
        print('\nCarro excluído da lista com sucesso.\n')

    except:
        print('\nO número digitado não corresponde a nenhum carro da lista.\n')
    os.system('pause')

def ligar():
    os.system('cls') or None
    n = int(input('\ninforme o número do carro que será ligado: '))

    try:    
        carros[n].ligar()
        print('\nCarro ligado.\n')

    except:
        print('\nO número digitado não corresponde a nenhum carro da lista.\n')
    os.system('pause')

def desligar():
    os.system('cls') or None
    n = int(input('\ninforme o número do carro que será desligado: '))

    try:    
        carros[n].desligar()
        print('\nCarro desligado.\n')

    except:
        print('\nO número digitado não corresponde a nenhum carro da lista.\n')
    os.system('pause')

def listar():
    os.system('cls') or None

    p = 0
    for c in carros:
        print(f'{p}ª Carro: {c.nome}\n')
        p += 1
    os.system('pause')

retorno = menu()
while retorno < 7:
    
    if retorno == 1:
        novo_carro()

    elif retorno == 2:
        informações()

    elif retorno == 3:
        excluir_carro()

    elif retorno == 4:
        ligar()

    elif retorno == 5:
        desligar()

    elif retorno == 6:
        listar()

    retorno = menu()

os.system('cls') or None
print('\nPrograma finalizado.')
