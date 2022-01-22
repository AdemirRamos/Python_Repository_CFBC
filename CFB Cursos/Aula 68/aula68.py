import os; os.system('cls')

print('Tkinter - PhotoImage')
print()

from tkinter import *

pasta_janela = os.path.dirname(__file__)

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

imagem_logo = PhotoImage(file=pasta_janela + '\\Songs For The Deaf (All Red).png')

label_logo = Label(janela, image=imagem_logo)
label_logo.place(x=10, y=10)

janela.mainloop()

#Caso se deseje diminuir ou aumentar o tamanho da imagem, o ideal é fazer isso através de algum programa de edição de imagens.
#Através de um programa de edição de imagens será muito mais prático alterar o tamanho da imagem.
