import os; os.system('cls')

print('Tkinter - Grid')
print()

from tkinter import *

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

label_canal = Label(janela, text='CFB Cursos')
label_nome = Label(janela, text='Digite o seu nome: ')
label_idade = Label(janela, text='Digite a sua idade: ')

entry_nome = Entry(janela)
entry_idade = Entry(janela)

botão = Button(janela, text='YouTube')

#Trabalhando como o "Tkinter Grid":

label_canal.grid(column=0, row=0, columnspan=2, pady=10) #"pady": "padding" no eixo Y.

#Posicionando o elemento (selecionado) na coluna 0 e linha 0.
#"columnspan" mescla colunas.

label_nome.grid(column=0, row=1, sticky='w')
entry_nome.grid(column=0, row=2, padx=10) #"padx": "padding" do eixo X.

#"sticky" define o posicionamento do item que o recebe.
#Valores de "sticky": n == "north"; s == "south"; e == "east" ("right"); w == "west" ("left").

label_idade.grid(column=0, row=3, sticky='w') #Para deixar este "Entry" ao lado do anterior: (column = 1, row = 1).
entry_idade.grid(column=0, row=4, padx=10) #Para deixar este "Entry" ao lado do anterior: (column = 1, row = 2).

janela.mainloop()
