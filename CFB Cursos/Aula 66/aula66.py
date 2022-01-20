import os
from turtle import width; os.system('cls')

print('Tkinter - Frame')
print()

from tkinter import *; from tkinter import messagebox

def mostrar_mensagem():
        messagebox.showinfo(title='CFB Cursos', message='CFB Cursos, Curso de Python / Tkinter')

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

número_caixa_texto = StringVar()

#Definindo uma borda, a sua espessura e o seu tipo:

frame_novo_1 = Frame(janela, borderwidth=1, relief='raised')

#Valores de "relief": "flat" (valor padrão); "raised" (relevo 3D); "sunken" (profundidade 3D); "solid".

frame_novo_1.place(x=10, y=10, width=300, height=100)

#Para posicionar os elementos abaixo dentro do "frame", basta mudar vossos pai de "janela" para "frame_novo_1".

label_tipo = Label(janela, text='Tipo de Caixa [1, 2, 3]')

label_tipo.place(x=10, y=10)

text_box_número = Entry(frame_novo_1, textvariable=número_caixa_texto)

número_caixa_texto.set('1')

text_box_número.place(x=10, y=30)

botão_mensagem = Button(frame_novo_1, text='Mostrar Mensagem', command=mostrar_mensagem)

botão_mensagem.place(x=10, y=50)

frame_novo_2 = Frame(janela, borderwidth=1, relief='sunken', background='#008')

frame_novo_2.place(x=10, y=120, width=300, height=100)

botão_mensagem_2 = Button(frame_novo_2, text='Mostrar Mensagem', command=mostrar_mensagem)

botão_mensagem_2.place(x=10, y=50)

janela.mainloop()
