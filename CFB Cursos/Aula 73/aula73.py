import os
from turtle import width; os.system('cls')

print('Tkinter - LabelFrame')
print()

from tkinter import *

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

#Em "LabelFrame", o "text" já será o "label" de "LabelFrame".

label_frame_esportes = LabelFrame(janela, text='Esportes', borderwidth=1, relief='solid')
label_frame_esportes.place(x=10, y=10, width=300, height=100)

label_esporte_1 = Label(label_frame_esportes, text='Futebol')
label_esporte_1.pack()

label_esporte_2 = Label(label_frame_esportes, text='Basquete')
label_esporte_2.pack()

label_esporte_3 = Label(label_frame_esportes, text='Vôlei')
label_esporte_3.pack()

janela.mainloop()
