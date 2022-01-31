import os; os.system('cls')

print('Tkinter - Abas e "Progressbar"')
print()

from tkinter import *; from tkinter import ttk

def valor_barra():
    variável_barra.set(50)

def valor_barra_2(máximo):
    cont = 0
    etapas = máximo / 100

    while cont < etapas:
        cont += 1
        i = 0
        while i < 100000000:
            i += 1
        variável_barra.set(cont)
        
        janela.update() #Atualizando a página para que o aumento da barra seja exibido gradualmente.


janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

variável_barra = DoubleVar()
variável_barra.set(0) #Definindo o valor a ser posto na barra de progresso.

progress_bar = ttk.Progressbar(janela, variable=variável_barra, maximum=100)

#É preciso criar uma variável para receber o valor que medirá o progresso da barra.
#"maximum" indica o valor máximo da barra de progresso.

#Alocando a "Progressbar" na interface:

progress_bar.place(x=0, y=0, width=500, height=40) #É possível controlar a largura e altura da barra através de "width" e "height".

#Criando um botão para alterar o valor da barra:

botão = Button(janela, text='Definir o valor da barra', command=lambda:valor_barra_2(10000))
botão.place(x=0, y=50, width=200, height=40)

janela.mainloop()
