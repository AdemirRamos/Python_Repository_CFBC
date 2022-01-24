import os
from turtle import width; os.system('cls')

print('Tkinter - Password')
print()

from tkinter import *

def exibir_senha():
    print(f'Senha digitada: "{var_senha.get()}".')

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

var_senha = StringVar()

#Transformando um "Entry" em um caixa de senha (através de "show"):

input_senha = Entry(janela, textvariable=var_senha, show='*')

#Após "show" (entre aspas), se escolhe o que será mostrado ao usuário ao se preencher um determinado campo.

input_senha.pack()

botão_exibir = Button(janela, text='Imprimir Senha', command=exibir_senha)

botão_exibir.pack()

janela.mainloop()
