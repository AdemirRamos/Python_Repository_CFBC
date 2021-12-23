print('Funções (Parte 3 - Retorno de Valores')
print()

import os; os.system('cls')

values = [1, 5, 3, 2]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r #Aqui pode ser retornado o que você quiser. Uma "string", um variável, um número, et cetera.

print(f'O resultado devolvido pela função foi: "{somar(values)}".')
#Como foi retornada à chamada da função o resultado da função, agora, ao "printar" a função, temos esse resultado.
