print('Funções (Parte 2 - Argumentos de Entrada)')
print()

import os; os.system('cls')

def somar(n1, n2): #A essas variáveis, é dado o nome "parâmetro de entrada".
    soma = n1 + n2
    print(f'A soma dos valores apresentados é igual a: {soma}.')

somar(7, 9)

def textos(*txt): #A esse argumento (precedido por um asterisco), se dá o nome de "argumento arbitrário".
    print()
    for t in txt:
        print(f'O texto digitado foi: "{t}".')

textos('Olá, mundo!', 'Meu nome é Ademir', 'Tudo bem com vocês?')

def somar_2(* num):
    print()
    r = 0
    for n in num:
        r += n
    print(f'O resultado da soma dos números apresentados é igual a: {r}.')

somar_2(5, 7, 9, 3)

def carros(c = 'Golf'): #Função com argumento parão definido.
    print()
    print(f'O modelo desse carro é: {c}.')

carros('Honda City')
carros()

import random

def lista():
    valores = list()
    for v in range(0, 6):
        valores.append(random.randint(0, 10))
    print()
    print(f'Lista de valores aleatórios: {valores}.')

lista()

values = [1, 5, 3, 2]
def somar_3(num):
    r = 0
    for n in num:
        r += n
    print()
    print(f'A soma dos valores da lista "values" é: {r}.')

somar_3(values)
