print('O Que São As Tuplas Em Python')
print()

import os
os.system('cls')

#Lista:

carros = ['HRV', 'Golf', 'Argo']
carros[2] = 'Lexus'

for c in carros:
    print(c)

#Tupla (o uso de parênteses é facultativo):
#Os elementos das Tuplas não podem ser alterados (nas Listas, sim).

print()
cars = ('BMW', 'Mustang', 'Camaro')
for c in cars:
    print(c)

#".count": conta o número de elementos na Tupla.

#Alterando elementos de uma Tupla (gambiarra [com "casting"]):

print()
cars_2 = ('Ferrari', 'Corsa', 'Supra')
veículos = list(cars_2)
veículos[1] = 'Palio'
cars_3 = tuple(veículos) #Transformando a Lista (alterada) em Tupla novamente.

for c in cars_3:
    print(c)
print(f'\nTipo da variável "cars_3": {type(cars_3)}.')
