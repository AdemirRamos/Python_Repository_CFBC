print('POO Classes (Parte 1)')
print()

import os; os.system('cls')

#O que é uma Classe? De forma resumida:
#É a especificação de um Objeto; um conjunto de regras para um Objeto.
#O Objeto, por sua vez, é uma instância da Classe.
#Se pode entender a Classe como a planta de uma casa;
#O Objeto (classe instanciada), por sua vez, pode ser entendido como a casa em si.

#Como criar Classes em Python:

class Carro:
    velocidade_máxima = 0
    ligado = False
    cor = ''

#Se usa a palavra "class" para criar uma Classe; em seguida, se dá o nome da Classe; então se adiciona comandos à classe.

#Instanciando o novo Objeto:

car_1 = Carro()
car_2 = Carro()
car_3 = Carro()
