import os; os.system('cls')

print('Gravando Dados Do Formulário No Banco De Dados')
print()

import os

c = os.path.dirname(__file__)
nome_arquivo = c + '\\dados.txt'

def gravar_dados():
    arquivo = open(nome_arquivo, 'a')
    arquivo.write('Nome.....: %s' % variável_nome.get())
    arquivo.write('\nTelefone.: %s' % variável_phone.get())
    arquivo.write('\nE-mail...: %s' % variável_mail.get())
    arquivo.write('\nTexto....: %s' % variável_texto.get('1.0', END))
    arquivo.write('\n')
    arquivo.close()

from tkinter import *

interface = Tk()

interface.title('CFB Cursos')
interface.geometry('500x300')
interface.configure(background='#dde')

Label(interface, text='Nome: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=10, width=100, height=20)

variável_nome = Entry(interface)

variável_nome.place(x=10, y=30, width=200, height=20)

Label(interface, text='Telefone: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=60, width=100, height=20)

variável_phone = Entry(interface)

variável_phone.place(x=10, y=80, width=200, height=20)

Label(interface, text='Email: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=110, width=100, height=20)

variável_mail = Entry(interface)

variável_mail.place(x=10, y=130, width=200, height=20)

Label(interface, text='Considerações: ', background='#dde', foreground='#009', anchor=W).place(x=10, y=160, width=100, height=20)

variável_texto = Text(interface)

variável_texto.place(x=10, y=180, width=200, height=80)

Button(interface, text='Gravar Dados', command=gravar_dados).place(x=10, y=270, width=100, height=20)

interface.mainloop()
