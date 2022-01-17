from cgitb import text
import os; os.system('cls')

print('Tkinter Radio Button')
print()

from tkinter import *

def imprimir_esporte():
    ve = var_esporte.get()

    if ve == 'foot':
        print('Esporte: futebol.')
    
    elif ve == 'vol':
        print('Esporte: vôlei.')

    elif ve == 'bask':
        print('Esporte: basquete.')


#"StringVar()" são variáveis que se relacionam com os elementos da interface recebendo informações e as armazenando.

janela = Tk()

var_esporte = StringVar()

var_colour = StringVar()

janela.title('CFB Cursos')

janela.geometry('500x300')

bl_esportes = Label(janela, text='Esportes')

bl_esportes.pack()

rb_futebol = Radiobutton(janela, text='Futebol', value='foot', variable=var_esporte)
rb_futebol.pack()

rb_voley = Radiobutton(janela, text='Vôlei', value='vol', variable=var_esporte)
rb_voley.pack()

rb_basket = Radiobutton(janela, text='Basquete', value='bask', variable=var_esporte)
rb_basket.pack()

rb_cor_verde = Radiobutton(janela, text='Verde', value='#0f0', variable=var_colour)
rb_cor_verde.pack()

rb_cor_vermelha = Radiobutton(janela, text='Vermelho', value='#f00', variable=var_colour)
rb_cor_vermelha.pack()

botão_esporte = Button(janela, text='Esporte Selecionado', command=imprimir_esporte)
botão_esporte.pack()

#Sempre se deve definir o "value" de um "Radiobutton".
#"value" é o valor efetivo do botão; "text" é somente o texto visível para o usuário.

janela.mainloop()
