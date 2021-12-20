print('Loop For')
print()

carros = ['HRV', 'Golf', 'Argo', 'Focus']
print(carros)

print()
for x in carros:
    print(f'Carro: {x}')
    if x == 'Golf' : #É possível colocar o teste lógico entre parênteses: "if (x == 'Golf'):".
        print(f'({carros[1]} VW)')


#A variável "x" se torna a chave dos elementos da Lista carros, ou seja, "x" representa cada elemento da Lista.
#Nesse caso, o "loop" só termina quando todos os elementos forem impressos.

