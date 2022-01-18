import os; os.system('cls')

print('Tkinter - Option Menu')
print()

from tkinter import *

def imprimir_esporte():
    ve = var_esporte.get()

    if ve == 'Futebol':
        print('Esporte: futebol.')
    
    elif ve == 'Vôlei':
        print('Esporte: vôlei.')

    elif ve == 'Basquete':
        print('Esporte: basquete.')

janela = Tk()

janela.title('CFB Cursos')

janela.geometry('500x300')

lista_de_esportes = ['Futebol', 'Vôlei', 'Basquete']

var_esporte = StringVar()

#Definindo o valor padrão:

var_esporte.set(lista_de_esportes[0])

bl_esportes = Label(janela, text='Esportes')
bl_esportes.pack()

option_sports = OptionMenu(janela, var_esporte, * lista_de_esportes) #O asterisco indica que todos os elementos da lista serão utilizados.
option_sports.pack()

botão_esporte = Button(janela, text='Esporte Selecionado', command=imprimir_esporte)
botão_esporte.pack()

janela.mainloop()
