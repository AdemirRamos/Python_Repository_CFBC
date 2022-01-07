import os; os.system('cls')

print('Expressões Regulares - RegEx Search')
print()

import re

texto = 'Curso de Python do CFB Cursos, canal no YouTube.'

resultado = re.search('Python', texto) #1ª: (Entre parênteses) o que se procura; 2ª: onde se procura (nesse caso, na variável "texto").

#"search" irá retornar a posição do elemento procurado. É possível definir se será a posição inicial ou final.

print(f'Posição inicial do elemento procurado: {resultado.start()}.') #Indicando que seja retornada a posição inicial do elemento.
print(f'\nPosição final do elemento procurado: {resultado.end()}.') #Indicando que seja retornada a posição final do elemento.

#Definindo o tamanho (em caracteres) do elemento buscado:

posição_inicial = resultado.start()
posição_final = resultado.end()
tamanho = posição_final - posição_inicial #A posição final deve vir primeiro.

print(f'\nEste é o tamanho (em caracteres) do elemento buscado: {tamanho}.')
print(f'\nElemento buscado: "{resultado}".')

#Caso seja pesquisado algo que não existe no local da pesquisa, como resultado, será retornada uma exceção.

if resultado != None:
    print('\nElemento encontrado.')

else:
    print(f'\nElemento não encontrado.')

#Personalizando a busca: "\AC". Traduzindo: "a 'string' começa com a letra 'C'".
