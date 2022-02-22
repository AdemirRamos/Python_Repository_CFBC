print('Coleção Lista')
print()

carros = ['HRV', 'Honda', 'Golf', 'Fox']
carros[3] = 'Fusion'
carros.append('Fox') #Adiciona novos itens à Lista (em sua última posição).
carros.remove('HRV')
#Remove o elemento selecionado.
#Caso se tente remover um item que não está na lista, ocorrerá um erro.

carros.pop() #Por padrão, remove o último item da lista. A seguir, temos outra maneira de se deletar um item da Lista:
del carros[1] #"del" pode ser usado com outras Objetos do Python.
#carros.clear() #Esse método limpa a lista por completo.

#Copiando Listas:

carros_2 = list(carros)

#Unindo Listas:

carros_3 = list()
carros_3.append('Ferrari')
carros_3.append('Mustang')
carros_3.append('Supra')
#Resultado a partir da linha 44.

try:
    carros.remove('BMW')

except (ValueError):
    print('Carro não encontrado.\n')

print(f'{carros}\n') #A quebra de linha ("\n") pode ir em qualquer ponto da "string" (porém somente em "strings").
print(f'Carro na posição 0: {carros[0]}.')
print(f'Carro na posição -1: {carros[-1]}.')
#Faz a impressão do segundo elemento da direita para a esquerda.
#Não existe elemento "-0", por isso, para essa lista ("carros"), o elemento[-1] será "Fox".

print('Tamanho da Lista "carros":', end=' ')
print(str(len(carros))) #Usando "casting" para imprimir o tamanho da lista (sem precisar de variáveis).

print(f'\nCópia da Lista de carros: {carros_2}.')

carros_4 = carros_3 + carros
print(f'Listas concatenadas: {carros_4}.')
print(f'Tamanho da Lista "carros_4": {len(carros_4)}.')
