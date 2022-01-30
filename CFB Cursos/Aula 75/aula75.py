import os; os.system('cls')

print('Tkinter - SpinBox')
print()

from tkinter import *

def imprimir_valor_botão01():
    print(f'Valor do Botão 01: {spinbox_valores.get()}.')

def imprimir_valor_botão02():
    print(f'Valor do Botão 02: {spinbox_valores_2.get()}.')

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

#Primeira maneira de se trabalhar com "SpinBox":

spinbox_valores = Spinbox(janela, from_=1, to=10)
spinbox_valores.pack()

#Segunda maneira de se trabalhar com "SpinBox":

spinbox_valores_2 = Spinbox(janela, values=(1, 2, 3, 4, 5)) 
spinbox_valores_2.pack()

#Caso "values" receba um valor, esse valor não mais mudará e será o valor (fixo) dentro da caixa de valores.

botão_valor = Button(janela, text='Imprimir Valor - Botão 1', command=imprimir_valor_botão01)
botão_valor.pack()

botão_valor_2 = Button(janela, text='Imprimir Valor - Botão 2', command=imprimir_valor_botão02)
botão_valor_2.pack()

janela.mainloop()
