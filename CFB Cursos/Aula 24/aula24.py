import os; os.system('cls')

print('POO Classes (Parte 2 - Construtor e Métodos)')
print()

#O que são construtores? Basicamente:
#São um método ou função que irá ser chamado (automaticamente) ao se instanciar um objeto da classe.

#Criando um construtor [construtores são um método especial, por isso, a sua forma será esta: "def __init__()"]:
#Se usa "self" como parâmetro do construtor quando se quer alterar as propriedades da própria classe daquele objeto.
#O "self" é o "this" do Python, ou seja, uma referência à própria classe do objeto.

class Carro:
    velocidade_máxima = 0
    ligado = False
    cor = ''
    def __init__(self, v_m, lig, colour):
        self.velocidade_máxima = v_m
        self.ligado = lig
        self.cor = colour

    def mostrar(self):
        print()
        print(f'Velocidade máxima do veículo: {self.velocidade_máxima}.')
        print(f'\nCor de veículo: {self.cor}.')
        estado = 'Sim' if self.ligado else 'Não'
        print(f'\nO veículo está ligado?: {estado}.')
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if (self.ligado):
            print('\nAndando...')
        else:
            print('\nO carro está desligado!')

#A partir do momento em que se tem um Construtor definido, é preciso passar parâmetros para a chamada da classe.

car_1 = Carro('200km/h', False, 'Vermelho')
car_2 = Carro('300km/h', True, 'Azul')
car_3 = Carro('150km/h', True, 'Verde')

car_1.mostrar()
car_2.mostrar()
car_3.mostrar()

car_1.ligar()
car_2.desligar()
car_3.desligar()

car_1.andar()
car_2.andar()
car_3.andar()
