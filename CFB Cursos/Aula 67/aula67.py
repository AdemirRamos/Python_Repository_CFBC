import os; os.system('cls')

print('Tkinter - Label')
print()

from tkinter import *; from tkinter import messagebox

def mostrar_mensagem():
        messagebox.showinfo(title='CFB Cursos', message='CFB Cursos, Curso de Python / Tkinter')

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

número_caixa_texto = StringVar()

frame_novo_1 = Frame(janela, borderwidth=1, relief='raised')

frame_novo_1.place(x=10, y=10, width=300, height=100)

label_tipo = Label(janela, text='Tipo de Caixa [1, 2, 3]')

label_tipo.place(x=10, y=10)

text_box_número = Entry(frame_novo_1, textvariable=número_caixa_texto)

número_caixa_texto.set('1')

text_box_número.place(x=10, y=30)

botão_mensagem = Button(frame_novo_1, text='Mostrar Mensagem', command=mostrar_mensagem)

botão_mensagem.place(x=10, y=50)

botão_mensagem_2 = Button(frame_novo_1, text='Mostrar Mensagem', command=mostrar_mensagem)

botão_mensagem_2.place(x=10, y=50)

frame_novo_2 = Frame(janela, borderwidth=1, relief='sunken', background='#008')

frame_novo_2.place(x=10, y=120, width=300, height=100)

#Formatando a fonte:

label_canal = Label(frame_novo_2, text='CFB Cursos', background='#008', foreground='#fff', font=('Arial', 10))

#Posicionando o botão:

label_canal.pack(side=LEFT, fill=X, expand=TRUE) #Posicionamento à leteral; preenchimento completo do eixo X; expansão habilitada.

janela.mainloop()
