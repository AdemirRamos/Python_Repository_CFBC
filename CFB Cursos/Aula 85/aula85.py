import os; os.system('cls')

print('Biblioteca URLLIB (Parte 1)')
print()

import urllib.request

página = urllib.request.urlopen('http://www.cfbcursos.com.br/modelocursopython.html') #Selecionando a página a ser manipulada.
texto = página.read().decode('utf8') #Decodificadndo a página para que essa possa ser lida.

print(texto)
