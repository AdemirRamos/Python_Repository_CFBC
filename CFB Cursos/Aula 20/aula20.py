print('Funções (Parte 2 - Argumentos de Entrada)')
print()

import os; os.system('cls')

def somar(n1, n2): #A essas variáveis, é dado o nome "parâmetro de entrada".
    soma = n1 + n2
    print(f'A soma dos valores apresentados é igual a: {soma}.')

somar(7, 9)

def textos(*t): #A esse argumento (precedido por um asterisco), se dá o nome de "argumento arbitrário".
    print()
    for p in t:
        print(f'O texto digitado foi: "{p}".')

textos('Olá, mundo!', 'Meu nome é Ademir', 'Tudo bem com vocês?')
