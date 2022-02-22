print('Tipos de Dados Em Python')
print()

x = 1
x = 'CFB Cursos'
x = 15.6
x = False #Essa é a variável ("const") constante do Python.
n1 = 5; n2 = 2; x_1 = complex(n1, n2)
#Esse é um método do Python que faz com que a primeira parte do número seja a sua parte real e, a segunda parte, um "número imaginário".

n3 = 5; n4 = 2; x_2 = complex(1j)

print(x_1.real) #Parte real do número;
print(x_1.imag) #Parte imaginária do número.

print(x_2.real) #Parte real do número.
print(x_2.imag) #Parte imaginária do número.

#x_1 -> tipo: "complex";
#x_2 -> tipo: "complex".

#Criando "vetores" (listas):

x_3 = ['Carro', 'Avião', 'Navio', 1, 18.3, True]
#Também poderia ser escrito assim: "x_3 = list()".
#Lista aceitam itens de diferentes tipos.

#Substituindo uma item da Lista:

x_3[0] = 'Ônibus'

#Tuplas:
#No caso das Tuplas, o uso de parênteses é opcional.
#Ao contrário das Listas, as Tuplas não podem ser mudadas.

x_4 = ('Carro', 'Avião', 'Navio', 1, 18.3, True)

#Range: Nos permite criar Listas de maneira mais fácil:

x_5 = range(0, 100, 10)
#Foi criada uma lista de 0 até 100. O terceiro valor representa o salto da lista (pulando de 10 em 10).
#Caso o terceiro valor seja negativo, o "contagem" será reversa.

#Dicionários:

#x_6 = dict() -> Um Dicionário pode ser criado assim.

x_6 = {'nome': 'Ademir', 'idade': 25, 'sexo': 'Feminino'}

#Tipo "set":
#"set" não repete valores.

x_7 = set{1, 2, 3, 4, 5, 1, 2 ,3}

#"Frozen Set":
#É criada um "set" porém ele não pode ser modificado.

x_8 = frozenset({9, 8, 7})

print(f'Valor da variável: {x}.')
print(f'Tipo da variável: {type(x)}.') #Esse comando imprime o "tipo" do objeto selecionado (entre parênteses).
print(x_3); print(x_3[0]) #Ambos pertencem ao tipo "list".
print(x_5); print(type(x_5)) #Aparentemente, "range" já não é mais um Objeto do tipo "list".
print(x_6['nome']) #Tipo: Dicionário.
print(x_7); print(x_8)

#Assunto para aulas futuras: "cast" é uma conversão de tipo (forçada).
