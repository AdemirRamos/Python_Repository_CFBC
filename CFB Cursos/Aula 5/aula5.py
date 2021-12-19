print('Tipos Numéricos, Random e Operações de Casting')
print()

import random

num_i = 10
num_f = 5.2
num_c = 1j

num = 15.5
x = int(num)
#Dessa maneira ["int()"], convertemos o valor da variável "x" (15.5) para um valor inteiro.
#A conversão pode ser feita (seguindo a estrutura acima) para "float", "string", "int", et cetera.

random_number = random.randrange(0, 60) #Esse comando gera um número (aleatório) entre 0 e 59.

print('Números aleatórios:', end=' ')
for c in range(1, 7):
    x_2 = random.randint(0, 61)
    print(x_2, end=' ')
print()

print()
números = list()
números.append(x_2)
números.append(x)
print(números, end=' ')
print(números[0])
print()

print(f'Valor da 1ª variável: {num_i}; valor da 2ª variável: {num_f}; valor da 3ª variável: {num_c}.')
print(f'Tipo da 1ª variável: {type(num_i)}; tipo da 2ª variável: {type(num_f)}; tipo da 3ª variável: {type(num_c)}.')

#Casting:
#"Casting" consiste em converter o tipo / classe de objetos.

print('Valor: ' + str(x_2) + ' - Tipo: ' + str(type(x_2)))
