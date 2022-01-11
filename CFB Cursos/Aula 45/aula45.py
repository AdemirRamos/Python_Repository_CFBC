import os; os.system('cls')

print('Operações Em Arquivos - Parte 2')
print()

name = 'aula45_teste.txt'
file = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 45' + name, 'rt')

#Modos de abertura de um documento:

#r: "read" (leitura) - o novo arquivo será aberto apenas para leitura;
#a: "append" (anexar) - o novo arquivo será adicionado ao final do arquivo;
#w: "write" (escrita) - o novo arquivo permitirá a escrita no arquivo;
#x: "create" (criação) - o novo arquivo permitirá a criação de conteúdo para si.
#t: "text" (texto) - o novo arquivo 
#b: "binary" (binário) - o novo arquivo

#O conteúdo do documento será lido por conta do método "read()" e armazenado em "file".

print(file.read())

file.close()
