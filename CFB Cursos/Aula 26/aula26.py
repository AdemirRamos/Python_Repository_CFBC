import os; os.system('cls')

print('Try / Except - Tratamento de Erros')
print()

x = 10

try:
    print(x)

except (NameError):
    print('\nErro. Variável não definida.')

except:
    print('\nErro desconhecido.')

else: #Se cai aqui quando não houver um erro / exceção.
    print('\nNenhum erro / exceção foi encontrado (a).')

finally: #Independente da ocorrência de erros ou não, esse bloco será executado.
    print('\nFim do tratamento de erros.')

num = -10

if num < 0:
    raise Exception ('\nValor inválido! O valor não pode ser menor do que zero (0).')
    #Esse comando gera uma exceção / erro.

if type(num) is int: #Se "num" for do tipo "int".
    print('\nValor digitado válido.')

else:
    raise Exception ('\nErro. Digite somente números.')

num_2 = 'Ademir'

if type(num_2) is not int: #Se "num" não for do tipo "int".
    print('\nErro. Digite somente números.')

else:
    print('\nValor digitado válido.')

