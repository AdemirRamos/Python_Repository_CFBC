import os; os.system('cls')

print('Tkinter - ComboBox')
print()

from tkinter import *; from tkinter import ttk

def esporte_selecionado():
    var_esporte = combobox_esportes.get()
    print(f'Esporte selecionado: "{var_esporte}".')

#"ComboBox" se encontra dentro da sub-biblioteca (do Tkinter) chamada "tkk".

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

#O "ComboBox" é uma caixa de opções.

#Todo "ComboBox" demanda uma lista:

lista_de_esportes = ['Futebol', 'Basquete', 'Vôlei']

label_esportes = Label(janela, text='Esportes')
label_esportes.pack()

#Criando o "ComboBox":

combobox_esportes = ttk.Combobox(janela, values=lista_de_esportes)

#Definindo um esporte para já vir marcado assim que a lista for criada.

combobox_esportes.set('Futebol')
combobox_esportes.pack()

#Caso o "set()" não seja definido, a caixa de opções virá sem nenhum opção pré-marcada.

botão_esporte = Button(janela, text='Esporte Selecionado', command=esporte_selecionado)
botão_esporte.pack()

janela.mainloop()
