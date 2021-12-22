print('Funções (Parte 1)')
print()

import os; os.system('cls')

#Em programação, uma função é um bloco de códigos que ficará armazenado em um programa podendo ser executado a qualquer momento.

def função():
    print('Curso de Python - CFB Cursos.')
    print('\nyoutube.com/cfbcursos')

def somar():
    r = n1 + n2
    print(f'A some entre os valores digitados é igual a: {r}.')

def subtrair():
    s = n1 - n2
    print(f'A subtração entre os valores digitados é igual a: {s}.')

#É possível chamar funções dentro de outras funções:

def cálculos():
    somar()
    subtrair()

n1 = 10
n2 = 5

somar()
subtrair()
print()
cálculos()
