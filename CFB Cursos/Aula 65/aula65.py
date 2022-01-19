import os; os.system('cls')

print('Tkinter - Messagebox')
print()

from tkinter import *; from tkinter import messagebox

def mostrar_mensagem(tipo_de_mensagem, mensagem):
    #Trabalhando com caixas de mensagens:

    if (tipo_de_mensagem == '1'):
        messagebox.showinfo(title='CFB Cursos', message=mensagem)

    elif (tipo_de_mensagem == '2'):
        messagebox.showwarning(title='CFB Cursos', message=mensagem)

    elif (tipo_de_mensagem == '3'):
        messagebox.showerror(title='CFB Cursos', message=mensagem)

#Trabalhando com caixas de mensagem interativas:

def resetar_text_box():
    resultado = messagebox.askretrycancel('Resetar', 'Confirmar Resetação da "Text Box"?')
    
    #Caso se clique em "yes" o retorno será "True"; em "no" o retorno será "False".

    if (resultado == True):
        text_box_número.delete(0, END) #Deletando o conteúdo da caixa de texto.
        text_box_número.insert(0, '') #Definindo, na posição 0, o texto "1".

#Tipos de caixa de mensagem interativa:

#1ª: "askyesno"; 2ª: "askquestion" | ambas apresentam os botões "sim" ("True") / "não" ("False").

#3ª: "askokcancel" - apresenta os botões "ok" ("True") e "cancelar" ("False");

#4ª: "askretrycancel" - apresenta os botões "repetir" ("True") e "cancelar" ("False");

#5ª: "askyesnocancel" - apresenta os botões "sim" ("True"), "não" ("False") e "cancelar" ("None").

#P. S.: Para ver cada uma dessas caixas de mensagem em prática, basta colar o seu nome após "messagebox." em resultado.

variável_mensagem = 'Curso de Python / Tkinter.'

janela = Tk()

janela.title('CFB Cursos')
janela.geometry('500x300')

número_caixa_texto = StringVar()

Label(janela, text='Tipo de Caixa [1, 2, 3]').pack()

text_box_número = Entry(janela, textvariable=número_caixa_texto)

#Definindo o valor de "número_caixa_texto":

número_caixa_texto.set('1')

text_box_número.pack()

botão_mensagem = Button(
    janela,
    text='Mostrar Mensagem',
    command = lambda: mostrar_mensagem(número_caixa_texto.get(), variável_mensagem)
)

botão_mensagem.pack()

botão_resetar = Button(janela, text='Resetar "Text Box"', command = resetar_text_box)

botão_resetar.pack()

janela.mainloop()
