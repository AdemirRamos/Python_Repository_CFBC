print('Tipo Boolean')
print()

#Basicamente, o tipo "Boolean" representa se um conteúdo é verdaderiro ("True") ou falso ("False").

a = True
b = False
c = 10 > 15

print(f'{a}, {b}, {c}.')

#Usando "casting" para converter uma "string" para "boolean":

aula = 'Python'
aula_2 =''

print(f'\nValor da variável "aula": {bool(aula)}.')
print(f'\nValor da variável "aula_2": {bool(aula_2)}.')

if aula: #Significa: se a aula tem como valor "True".
    print('Possui texto.')
else:
    print('Não possui texto.')
