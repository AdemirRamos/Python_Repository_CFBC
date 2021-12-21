print('Matrizes')
print()

import os
os.system('cls')

#A Matriz, em Python, é uma coleção de "arrays". Matrizes trabalham com dois índices: um para linha e outro para coluna.

carros = ['HRV', 'Golf', 'Focus', 'Argo']
carros[2] = 'Fusion'
print(carros[2])
print()
for c in carros:
    print(f'Nome do carro: {c}')

print()
carros_2 = [['Modelo', 'HRV'], ['Modelo', 'Golf'], ['Modelo', 'Focus'], ['Modelo', 'Argo']]
carros_2[2][1] = 'Mustang'
carros_2.append(['Cor', 'Prata'])
print(carros_2[1][1])
print()
for m, c in carros_2:
    print(f'{m}: {c}')
