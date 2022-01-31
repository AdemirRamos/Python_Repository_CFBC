import os; os.system('cls')

print('Tkinter - Abas e "Notebook"')
print()

from tkinter import *; from tkinter import ttk

janela = Tk()

janela.title=('CFB Cursos')
janela.geometry('500x300')

#Por este se tratar do primeiro elemento, o seu pai será a "janela".

notebook = ttk.Notebook(janela)
notebook.place(x=0, y=0, width=500, height=300)

#Adicionandos os "frames" (que serão as abas de "notebook"):

aba_1 = Frame(notebook)
aba_2 = Frame(notebook)

#Adicionando os "frames" ao "notebook":

notebook.add(aba_1, text='Cursos')
notebook.add(aba_2, text='Canal')

#Adicionando conteúdo às abas:

label_1 = Label(aba_1, text='Curso de Python')
label_1.pack()

label_2 = Label(aba_1, text='Curso de ReactNative')
label_2.pack()

label_3 = Label(aba_2, text='youtube.com/cfbcursos')
label_3.pack()

janela.mainloop()
