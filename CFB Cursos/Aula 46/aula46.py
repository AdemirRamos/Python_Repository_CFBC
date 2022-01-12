import os; os.system('cls'); import re; import time

print('Deletando Arquivos - Parte 3')
print()

#UM AVISO IMPORTANTE: é preciso fazer tomar certos cuidados para que a criação de arquivos ocorra sem nenhum erro.
#Por exemplo: após o nome final do endereço, é preciso barra invertida; é preciso usar "open()" para se adicionar o endereço do arquivo.
#E, ao concatenar os diferentes endereços que forma o endereço do arquivo, é preciso fazer exatamente como abaixo. 

nome = 'aula46_teste.txt'
caminho = 'C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos/Aula 46/' 

#Verificando se um arquivo já existe:

if os.path.exists(caminho + nome):
    print('Arquivo já existente.')
    
else:
    print('Criando o arquivo...')
    file = open(caminho + nome, 'x')
    file.close()
    time.sleep(1)
    print('\nArquivo criado com sucesso.')

#Removendo um arquivo (e verificando se um arquivo já foi deletado):

if os.path.exists:
    print('\nExcluindo o arquivo...')
    os.remove(caminho + nome)
    time.sleep(1)
    print('\nArquivo excluído com sucesso.')

else:
    print('Arquivo já excluído.')

#Para remover um arquivo já criado, é importante que as linhas de código relativas à criação desse arquivo sejam anuladas.
#Caso contrário, ocorrerá um erro.
#Caso se deseje criar um arquivo novamente, então devemos remover o "os.remove()" para evitar erros.
