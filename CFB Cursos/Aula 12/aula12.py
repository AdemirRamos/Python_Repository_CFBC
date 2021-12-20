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

print()
for x in 'CFB Cursos':
    print(x)

#Resultado: através do conceito de Fatiamento, cada uma das letras da "string" será impressa na tela.

print()
for x in ['HRV', 'Golf', 'Argo', 'Focus']:
    print(x)

#Também é possível percorrer a Lista a adicionando diretamente no "for".

#É possível usar "break" também com o "for".

print()
carros_2 = ['HRV', 'Golf', 'Argo', 'Focus', 'Fit', 'Fusion', 'Polo']

for x in carros_2:
    if x == 'Fusion':
        break
