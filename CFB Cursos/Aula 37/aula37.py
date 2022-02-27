import os; os.system('cls')

print('JSON Em Python (Parte 2)')
print()

import json

carros_dictionary = {'marca': 'honda', 'modelo': 'HRV', 'cor': 'prata'}
#Dictionary -> Object JSON.

carros_list = ['honda', 'volkswagen', 'ford', 'fiat', 'chevrolet']
#List -> Array JSON.

carros_tupla = ('honda', 'volkswagen', 'ford', 'fiat', 'chevrolet')
#Tupla -> Array JSON.

cars_json = json.dumps(carros_dictionary)
print(f'{cars_json}.\n')

cars_json_2 = json.dumps(carros_list)
print(f'{cars_json_2}.\n')

cars_json_3 = json.dumps(carros_tupla)
print(f'{cars_json_3}.\n')

#Usando parâmetros de formatação:

cars_json_4 = json.dumps(carros_dictionary, indent = 4) #Indicando a indentação (espaço antes da "string", como se fosse um parágrafo).
print(f'{cars_json_4}.\n')

#Substituindo elementos ao imprimir o JSON:

cars_json_5 = json.dumps(carros_dictionary, indent = 4, separators = (':', '=')) #Similar ao método "replace" do Python.
print(f'{cars_json_5}.\n')

cars_json_6 = json.dumps(carros_dictionary, indent = 4, sort_keys = True) #Ordenando a ordem das chaves com "sort" (ordem alfabética).
print(f'{cars_json_6}.\n')
