import os; os.system('cls')

print('Expressões Regulares - RegEx findall')
print()

#"Expressões regulares são uma espécie de minilinguagem de programação dotada de certos recursos úteis para se trabalhar com 'strings'."

#"findall" é utilizado para encontrar todas as ocorrências de uma determinada "string" (ou trecho de "string") dentro de outra "string".
#O resultado será retornado em forma de coleção.

import re #Importando RegEx's.

texto = 'Curso de Python do canal (no YouTube) CFB Cursos.'

resultado = re.findall('Python', texto) #Entre parênteses: primeiro, o que se procura ("Python"); depois, onde se procura (var "texto").

print(resultado)

resultado_2 = re.findall('so', texto)

print(f'\n{resultado_2}')

#Requisitando ao usuário o que se pesquisar:

poll = str(input('\nDigite o que você quer pesquisar: '))

resultado_3 = re.findall(poll, texto)

amount = resultado_3.count(poll) #Esse mesmo procedimento poderia ser feito com o método "len": "amount = len(resultado_3)".

print(f'\nResultado da pesquisa: "{resultado_3}". \n\nQuantidade de itens achados: {amount}.\n')

cont = 1

for t in resultado_3:
    print(f'{cont}ª Objeto encontrado: "{t}".\n')
    cont += 1
