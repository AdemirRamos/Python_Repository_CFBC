print('Função Input')
print()

print('Curso de Python')

import os
os.system('cls') #Essa função limpa o terminal toda vez que o programa for executado.

nome = str(input('\nDigite o seu nome: '))
print(f'\nO nome digitado foi: "{nome}".')

#Um "input()" vazio, ao ser rodado, esperará pelo usuário para digitar e confirmar qualquer coisa para, então, prosseguir com o programa.

print()
num_1 = int(input('Digite um valor: '))
num_2 = int(input('Digite outro valor: '))
soma = num_1 + num_2
print(f'A soma entre {num_1} + {num_2} é igual a: {soma}.')

#Ao não usar o tipo primitivo "int" antes de "input", as informações passadas pelo usuário serão entendidas como "strings".
#Sendo assim, ao concatená-las, o programa apenas concatenará uma "string" a outra - ao invés de fazer a soma de ambas.
#Tudo o que é retornado pelo "input", por padrão, é uma "string". Caso se queira mudar o tipo do elemento, use "casting" (como acima).

print()
num_3 = int(input('Digite um valor: '))
num_4 = int(input('Digite outro valor: '))
res = num_3 + num_4
print('Soma dos valores: ' + str(res) + '.')
#O "casting" para "str" é necessário pois uma "string" não pode ser concatenada a um "int".
#Apesar do "casting", a variável "res" continua armazenando um valor "int".
