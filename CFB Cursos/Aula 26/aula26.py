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

