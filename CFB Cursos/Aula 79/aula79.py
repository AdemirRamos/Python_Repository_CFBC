import os
from turtle import width; os.system('cls')

print('Tkinter - TreeView')
print()

from tkinter import *; from tkinter import ttk

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('600x300')

lista_de_nomes = [['0', 'Brertilda', '98888-8888'], ['1', 'Crisloidy', '97777-7777'], ['2', 'Julsivan', '96666-6666']]

#Definindo os nomes das colunas:

tree_view = ttk.Treeview(janela, columns=('id', 'nome', 'telefone'), show='headings')

#Aqui se define o nome da coluna e a largura mínima.

tree_view.column('id', minwidth=0, width=50)
tree_view.column('nome', minwidth=0, width=250)
tree_view.column('telefone', minwidth=0, width=100)

#Definindo os textos dos cabeçahos:

tree_view.heading('id', text='ID')
tree_view.heading('nome', text='Nome')
tree_view.heading('telefone', text='Telefone')
tree_view.pack()

#Inserindo dados às colunas:

for (id, nome, telefone) in lista_de_nomes:
    tree_view.insert('', 'end', values=(id, nome, telefone))
    #"end" indica que o elemento será introduzido ao final do seu container.

janela.mainloop()
