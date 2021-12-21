print('Loop While')
print()

import os
os.system('cls')

#Regras do While:

#1ª: inicialização de variável de controle;
#2ª: condição / teste lógico;
#3ª: enquanto o teste lógico retornar "True", o programa continuará; quando o resultado for "False", o programa parará;
#4ª: incremento, decremento ou controle da variável de controle.

#Caso a variável de controle sempre retorne "True", será iniciado um "loop infinito" (o programa não parará sozinho).

i = 0
while i < 10: #Os contadores, em Python, sempre param no penúltimo número.
    print(i)
    i += 1 #Esse comando também poderia ser escrito assim: "i = i + 1".
print('Fim do programa.')

#"Break":

print()
a = 0
while a < 10:
    print(a)
    a += 1
    if (a >= 5):
        break
print('Fim do programa.')

print()
carros = ['HRV', 'Golf', 'Argo', 'Onix', 'Focus']
b = 0
tamanho = len(carros)
while b < tamanho:
    print(carros[b])
    b += 1
print('Fim do programa.')

print()
carros_2 = []
carro = str(input('Digite o nome do novo carro: ')).lower().strip()
while carro != 'parar':
    carros_2.append(carro)
    carro = str(input('Digite o nome do novo carro: ')).lower().strip()

print()   
for x in carros_2:
    print(f'Nome do carro: {x}.\n')
print('Fim do programa.')
