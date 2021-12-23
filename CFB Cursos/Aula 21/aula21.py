print('Funções (Parte 3 - Retorno de Valores')
print()

import os; os.system('cls')

values = [1, 5, 3, 2]
def somar_3(num):
    r = 0
    for n in num:
        r += n
    print()
    print(f'A soma dos valores da lista "values" é: {r}.')

somar_3(values)
