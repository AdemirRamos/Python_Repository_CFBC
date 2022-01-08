import os; os.system('cls')

print('Expressões Regulares - RegEx Split')
print()

import re

texto = 'CFB Cursos, curso de Python no canal do YouTube.'

resultado = re.split('\s', texto) #1ª elemento: o caractere que será o divisor; 2ª elemento: onde será feita a busca.

#Espaço por ser indicado por um espaço ou por "\s"

print(f'Texto separado: {resultado}.')
print(f'\nElemento na terceira posição: "{resultado[2]}".')

print()
cont = 1
for e in resultado:
    print(f'{cont}ª Elemento: "{e}".')
    cont += 1
