import os; os.system('cls')

print('Iterators')
print()

#Basicamente, um "iterator" é um Objeto que pode ser "iterado" (percorrer valores de uma coleção).
#Basicamente, "iterator" possui dois método: "iter()" e "next()".

carros = ['HRV', 'Polo', 'Jetta', 'Cruze', 'Fusion']

#Criando um "iterator":

iterator_carros = iter(carros)

for c in carros:
    print(c)

#Percorrendo a lista com "iterator":

print()
print(f'Lista com "iterator": {next(iterator_carros)}')

#Se tentarmos imprimir um item que não está na lista, será gerada uma exceção.

try:
    for c in range(0, 7):
        print(f'\nfLista com "iterator" 2: {next(iterator_carros)}')

except:
    print('\nErro. O número passado não corresponde a um carro da lista.')

finally:
    print('\nFim do programa.')

#"Iterator" com "while":

print()
while iterator_carros:
    
    try:
        print(f'Lista com "iterator" (e "while"): {next(iterator_carros)}')

    except (StopIteration):
        print('Erro.') #Para evitar que essa mensagem apareça, você pode simplesmente removê-la.
        break
