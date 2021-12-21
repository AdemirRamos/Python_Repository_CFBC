print('Dictionary')
print()

import os
os.system('cls')

carros = {'Fabricante': 'Honda', 'Modelo': 'HRV', 'Ano de Fabricação': 2016, 'Cor': 'Prata'}

carros['Cor'] = 'Azul'
modelo = carros.get('Modelo') #O método "get()" captura o valor correspondente à chave indicada.
colour = carros['Cor']

#Criando novas chaves e valores:

carros['Câmbio'] = 'Manual'
carros['A'] = 'B'
carros['C'] = 'D'

#Removendo elementos do dicionário:

carros.pop('A')

#Outra maneira de se remover itens do dicionário:

del carros['C']

#Para limpar o dicionário:

#carros.clear()

#Essa é outra maneira de se criar Dicionários: "carros = dict()".
#Ordem dos elementos dos Dicionários: 1ª: chave; 2ª: valor.

print(f'Fabricante do veículo: {carros["Fabricante"]}.')
print(f'Modelo do veículo: {carros["Modelo"]}.')
print(f'Ano do veículo: {carros["Ano de Fabricação"]}.')
print(f'Cor do veículo: {carros["Cor"]}.')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'O modelo do carro é: {modelo}.')
print(f'A cor do carro é: {colour}.')
print('\n' + str(carros))

print()
for a in carros:
    print(f'Chave do dicionário: {a}.')
    print(f'Valor do cicionário: {carros[a]}.')

print()
c = 1
for k, v in carros.items():
    print(f'A {c}ª chave é: "{k}"; o valor é: "{v}".')
    c += 1

print()
c_2 = 1
for k in carros.keys():
    print(f'A {c_2}ª chave é: "{k}".')
    c_2 += 1
    print()

c_3 = 1
for v in carros.values():
    print(f'O valor da {c_3}ª chave é: "{v}".')
    c_3 += 1

print()
if 'Modelo' in carros:
    print('Sim, "Modelo" faz parte do dicionário (é uma chave).\n')

print(f'Tamanho do dicionário: {len(carros)}.')

#Dicionários dentro de dicionários:

cars = {
    'Car_1': {'Fabricante': 'Honda', 'Modelo': 'HRV'},
    'Car_2': {'Fabricante': 'Volkswagen', 'Modelo': 'Golf'},
    'Car_3': {'Fabricante': 'Ford', 'Modelo': 'Focus'}
    }

print()
print(f'Conteúdo do dicionário "cars": {cars}')
print(f"\nConteúdo do dicionário 'Car_1': {cars['Car_1']}.")
print(f"\n'Car_2' (Fabricante e Modelo): {cars['Car_2']['Fabricante']}, {cars['Car_2']['Modelo']}.")

car_1 = {'Fabricante': 'Honda', 'Modelo': 'HRV'}
car_2 = {'Fabricante': 'Volkswagen', 'Modelo': 'Golf'}
car_3 = {'Fabricante': 'Ford', 'Modelo': 'Focus'}
carros_2 = {'C1': car_1, 'C2': car_2, 'C3': car_3}

print(f'\nConteúdo do dicionário "carros_2": {carros_2}')
print(f"\nFabricante de 'C1': {carros_2['C1']['Fabricante']}; Modelo de 'C2': {carros_2['C2']['Modelo']}.")
print(f"\nFabricante e Modelo de 'C3': '{carros_2['C3']['Fabricante']}' | '{carros_2['C3']['Modelo']}'.")
