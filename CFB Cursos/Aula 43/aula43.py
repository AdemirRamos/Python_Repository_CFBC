import os; os.system('cls')

print('Expressões Regulares - RegEx Sub')
print()

import re

#"Sub" substitui caracteres de uma "string".

texto = 'CFB Cursos, curso de Python no canal do YouTube.'

resultado = re.sub(',', '.', texto)
#1ª: Temos o elemento que será procurado; 2ª: O elemento que irá substituí-lo; 3ª: o lugar onde procuramos o elemento.

#Trocando espaços por pontos:

resultado_2 = re.sub('\s', '-', texto) #Ao invés de "\s", também poderia ser escrito: "' '".

#Somando um segunda substituição à primeira:

resultado_2 = re.sub(',', '.', resultado_2)
#É importante, ao se escolher onde será feita a substituição, escolher a variável já formatada (nesse caso, "resultado_2").

print(f'O resultado obtido foi: "{resultado}".')
print(f'\nResultado na 3ª posição: "{resultado[2]}".')
print(f'\nSegundo resultado: "{resultado_2}".')
