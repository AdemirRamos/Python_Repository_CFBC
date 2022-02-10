import os
from turtle import width; os.system('cls')

print('Tkinter - Inserindo Dados do Formulário no TreeView')
print()

from tkinter import *; from tkinter import ttk; from tkinter import messagebox

def inserir():
    if variável_id.get() == '' or variável_nome.get() == '' or variável_telefone.get() == '':
        messagebox.showinfo(title='ERRO', message='Um ou mais campos estão vazios.')
        return #O "return" irá parar a execução desta função.
    
    tree_view.insert('', 'end', values=(variável_id.get(), variável_nome.get(), variável_telefone.get()))
    
    variável_id.delete(0, END); variável_nome.delete(0, END); variável_telefone.delete(0, END)
    variável_id.focus()

def deletar():
    print()

def obter():
    print()

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('600x300')

label_id = Label(janela, text='ID') #anchor=W
variável_id = Entry(janela)

label_nome = Label(janela, text='Nome') #anchor=W
variável_nome = Entry(janela)

label_telefone = Label(janela, text='Telefone') #anchor=W
variável_telefone = Entry(janela)

tree_view = ttk.Treeview(janela, columns=('id', 'nome', 'telefone'), show='headings')

tree_view.column('id', minwidth=0, width=50)
tree_view.column('nome', minwidth=0, width=250)
tree_view.column('telefone', minwidth=0, width=100)

tree_view.heading('id', text='ID')
tree_view.heading('nome', text='Nome')
tree_view.heading('telefone', text='Telefone')

botão_inserir = Button(janela, text='Inserir', command=inserir)
botão_deletar = Button(janela, text='Deletar', command=deletar)
botão_obter = Button(janela, text='Obter', command=obter)

label_id.grid(column=0, row=0, stick='w')
variável_id.grid(column=0, row=1)

label_nome.grid(column=1, row=0, stick='w')
variável_nome.grid(column=1, row=1)

label_telefone.grid(column=2, row=0, stick='w')
variável_telefone.grid(column=2, row=1, stick='w')

tree_view.grid(column=0, row=3, columnspan=3, pady=5)

botão_inserir.grid(column=0, row=4)
botão_deletar.grid(column=1, row=4)
botão_obter.grid(column=2, row=4)

#tree_view.insert('', 'end', values=(id, nome, telefone))

janela.mainloop()
