import os; os.system('cls')

print('Try / Except - Tratamento de Erros')
print()

x = 10

try:
    print(x)

except (NameError):
    print('Erro. Variável não definida.')

except:
    print('Erro desconhecido.')

else: #Se cai aqui quando não houver um erro / exceção.
    print('Nenhum erro / exceção foi encontrado (a).')

