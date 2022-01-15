import os; os.system('cls')

print('Tkinter, Entry e Text')
print()

from tkinter import *

interface = Tk()

interface.title('CFB Cursos')
interface.geometry('500x300')
interface.configure(background='#dde')

Label(interface, text='Nome: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=10, width=100, height=20)

#Valores da "anchor": N: Norte; S: Sul; E: Leste; W: Oeste.
#Outros exemplos: NE: Nordeste; SE: Sudeste; SO: Sudoeste; NO: Noroeste. 

#Dentro da área delimitada para o conteúdo de "text=", a "anchor" define o posicionamento da mensagem "Nome:".

variável_nome = Entry(interface)

#Recomenda-se não usar o "place()" após o "Entry" pois, assim sendo, erros serão gerados.

variável_nome.place(x=10, y=30, width=200, height=20)

Label(interface, text='Telefone: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=60, width=100, height=20)

variável_phone = Entry(interface)

variável_phone.place(x=10, y=80, width=200, height=20)

Label(interface, text='Email: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=110, width=100, height=20)

variável_mail = Entry(interface)

variável_mail.place(x=10, y=130, width=200, height=20)

#Componente "Text()":

Label(interface, text='Considerações: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=160, width=100, height=20)

variável_texto = Text(interface)

variável_texto.place(x=10, y=180, width=200, height=80)

#O componente "Text()" é preferível quando se é preciso escrever várias lihas de texto. Já "Entry()" é preferível para linhas únicas.

interface.mainloop()
