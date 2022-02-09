import os; os.system('cls')

print('Tkinter - Listbox')
print()

from tkinter import *

def imprimir_esporte():
    print(f'Esporte selecionado: {list_box_esportes.get(ACTIVE)}.')

def inserir_esporte():
    list_box_esportes.insert(END, novo_esporte.get())

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

lista_de_esportes = ['Futebol', 'Basquete', 'Vôlei']

list_box_esportes = Listbox(janela)

for esportes in lista_de_esportes:
    list_box_esportes.insert(END, esportes)

list_box_esportes.pack()

botão_esporte = Button(janela, text='Imprimir Esporte', command=imprimir_esporte)
botão_esporte.pack()

#Adicionando novos elementos ao "Listbox":

novo_esporte = Entry(janela)
novo_esporte.pack()

adicionar_esporte = Button(janela, text='Adicionar Esporte', command=inserir_esporte)
adicionar_esporte.pack()

janela.mainloop()
