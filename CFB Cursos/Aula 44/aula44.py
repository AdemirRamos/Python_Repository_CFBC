import os; os.system('cls')

print('Operações Em Arquivos - Parte 1')
print()

arquivo = 'aula44_teste.txt'
file = open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 44/' + arquivo, 'wt')

#Modos de abertura de um documento:

#r: "read" (leitura) - o novo arquivo será aberto apenas para leitura;
#a: "append" (anexar) - o novo arquivo será adicionado ao final do arquivo;
#w: "write" (escrita) - o novo arquivo permitirá a escrita no arquivo;
#x: "create" (criação) - o novo arquivo permitirá a criação de conteúdo para si.
#t: "text" (texto) - o novo arquivo 
#b: "binary" (binário) - o novo arquivo

#Caso o arquivo não exista, so se usar "read" ou "write", um novo arquivo será criado.
#Caso o arquivo já exista, ele será aberto para leitura.
#também se pode combinar as letras acima para gerar um novo arquivo. Exemplo "nome_do_arquivo, 'wt'".

#Escrevendo dentro do arquivo:

file.write('CFB Cursos.')
file.write('\n\nCurso de Python.')

#Caso o conteúdo não seja aberto no modo "append", um novo "write" sempre subscreverá o anterior.

#Adicionando "input's" ao arquivo:

texto = input('Digite algum texto: ')

#Também é possível usar "loop's" para adicionar elementos ao arquivo.

file.write(f'\n\n{texto}')

#Fechando o arquivo:

file.close()
