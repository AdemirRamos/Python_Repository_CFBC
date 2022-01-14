from cgitb import text
import os; os.system('cls')

print('Interface Gráfica No Python Com Tkinter')
print()

from tkinter import * #Legenda: "from 'tkinter', importe tudo".

app = Tk()

#Configurando a janlea:

app.title('CFB Cursos') #Aplica um título à janela.

app.geometry('500x300') #Define o tamanho da janela. O primeiro valor é a largura e o segundo a altura.

#Para funcionar (a dimensão da janela), os valores devem ser digitados sem espaços e com o "x" entre eles.

app.configure(background='#008') #Define a cor de fundo da janela.

#Inserindo elementos na janela:

texto_1 = Label(app, text='Curso de Python', background='#008', foreground='#fff')

#Primeiro definimos onde o conteúdo será alocado (quem será o seu "pai"), depois suas propriedades.
#"text=": serve para definir o título do elemento que foi criado.
#"background=": cor de fundo do elemento. Também funciona assim: "bg=".
#"foreground=": cor do texto. Também funciona assim: "fg="

#Para que o elemento apareça na janela, é preciso configurar o seu "place":

texto_1.place(x=10, y=10, width=100, height=20)

#Através de "place()" podemos indicar a posição nos eixos X e Y, além de largura e altura.

#Também é possível usar variáveis para realizar as configurações vistas acima:

text_contents = 'Módulo Tkinter'
vbg = '#ff0'
vfg = '#000'
texto_2 = Label(app, text=text_contents, bg=vbg, fg=vfg)
texto_2.pack(ipadx=20, ipady=20, padx=5, pady=5, side='top', fill=X, expand=True)

#"pack()", normalmente, é usada para elementos dentro de containers.

#Através de "side=", podemos definir onde o elemento será posicionado.
#Alguns valores de "side=": "top", "right", "left", "bottom".

#"fill=": determina o preenchimento do elemento;

#"expand=": determina se o elemento será expansível ou não. Os valores, aqui usados, devem ser "boolean".

#"expand" com "fill=X": o elemento terá a sua largura expandida.
#"expand" com "fill=Y": o elemento terá a sua altura expandida.

#"ipadx" é equivalente a "padding-right/left".
#"ipaxy" é equivalente a "padding-top/bottom".
#"padx" é equivalente a "margin-right/left".
#"pady" é equivalente a "margin-top/bottom".

app.mainloop() #"mainloop()" é responsável por executar a nossa interface gráfica.
