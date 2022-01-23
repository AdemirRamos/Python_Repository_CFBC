import os
from turtle import width; os.system('cls')

print('Tkinter - Checkbutton')
print()

from tkinter import *

def futebol_selecionado():
    print(f'Futebol: {var_futebol.get()}.')

def basquete_selecionado():
    print(f'Basquete: {var_basquete.get()}.')

def vôlei_selecionado():
    print(f'Vôlei: {var_vôlei.get()}.')

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

var_futebol = StringVar() #Outra opção: "var_futebol = IntVar()". - Dessa forma, as "checkboxes" não serão marcadas.
var_basquete = IntVar()
var_vôlei = StringVar()

frame_square_1 = Frame(janela, borderwidth=1, relief='solid')
frame_square_1.place(x=10, y=10, width=300, height=100)

#"onvalue=": quando o valor estiver selecionado; "offvalue=" quando o valor não estiver selecionado.

botão_futebol = Checkbutton(
        frame_square_1, text='Futebol',
        variable=var_futebol,
        onvalue='Sim', #1 == Selecionado - 1 no lugar de "Sim";
        offvalue='Não', #0 == Não selecionado - 0 no lugar de "Não".
        command=futebol_selecionado
    )

botão_futebol.pack(side=LEFT)

botão_basquete = Checkbutton(
        frame_square_1, text='Basquete',
        variable=var_basquete,
        onvalue=1,
        offvalue=0,
        command=basquete_selecionado
    )

botão_basquete.pack(side=LEFT)

botão_vôlei = Checkbutton(
        frame_square_1, text='Vôlei',
        variable=var_vôlei,
        onvalue='Sim',
        offvalue='Não',
        command=vôlei_selecionado
    )

botão_vôlei.pack(side=LEFT)

janela.mainloop()
