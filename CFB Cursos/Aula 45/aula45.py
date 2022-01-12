import os; os.system('cls'); import re

print('Operações Em Arquivos - Parte 2')
print()

nome = 'aula45_teste.txt'
file = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome, 'rt')

nome_2 = 'aula45_teste.txt'
file_2 = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome_2, 'rt')

nome_3 = 'aula45_teste.txt'
file_3 = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome_3, 'rt')

nome_4 = 'aula45_teste.txt'
file_4 = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome_4, 'rt')

nome_5 = 'aula45_teste.txt'
file_5 = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome_5, 'rt')

#Modos de abertura de um documento:

#r: "read" (leitura) - o novo arquivo será aberto apenas para leitura;
#a: "append" (anexar) - o novo arquivo será adicionado ao final do arquivo;
#w: "write" (escrita) - o novo arquivo permitirá a escrita no arquivo;
#x: "create" (criação) - o novo arquivo permitirá a criação de conteúdo para si.
#t: "text" (texto) - o novo arquivo 
#b: "binary" (binário) - o novo arquivo

#O conteúdo do documento será lido por conta do método "read()" e armazenado em "file".

print(file.read())

#Lendo apenas um determinado número de caracteres:

print(f'\nLeitura da caracteres: "{file_2.read(10)}".')

#Entre parênteses vai o número de caracteres que se deseja que sejam lidos.

#Lendo linhas inteiras:

print(f'\nLeitura da linha: "{file_4.readline()}".')

#A cada novo "readline()", uma nova linha será lida.

#Também é possível usar estruturas de "loop" para se realizar a leitura de linhas:

cont = 1
for linha in file_4:
    print(f'Conteúdo da {cont}ª linha: {linha}')
    cont += 1

#Trabalhando com "strings":

resultado = re.sub('\s', '-', file_5.readline())
print(f'\nManipulando a "string": {resultado}')

#Reescrevendo trechos da "string":

file_5 = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45/' + nome_5, 'wt')
file_5.write(resultado)

#Todo o conteúdo do arquivo será substituído ao se escrever o conteúdo de "resultado".

file.close()
file_2.close()
file_3.close()
file_4.close()
file_5.close()
