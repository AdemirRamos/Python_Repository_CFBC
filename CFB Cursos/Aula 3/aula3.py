num = num2 = res = 0 #Essas são todas "variáveis globais" (elas podem ser acessadas a partir de qualquer ponto do programa).

#Exemplo de variável de escopo global ("canal" declarada fora da "def" mas sendo usado dentro dela):

canal = 'CFB Cursos'

def channel():
    print(canal)

channel()

#Exemplo de variável de escopo "limitado" ("canal_2" foi declarada dentro da "def", portanto, não pode ser usada fora de lá):
#Para acessar a variável "canal_2" de fora do escopo da "def channel_2", basta, antes da variável, adicionar a palavra "global";
#Dessa forma, a variável "canal_2" se torna uma variável de escopo global (mesmo sendo declarada dentro da "def").
#Porém há um datalhe ao qual devemos nos atentar: ao declarar uma variável global, não podemos iniciá-la na mesma linha.

def channel_2():
    #global canal_2 = 'Canal Fessor Bruno' -> Errado.
    global canal_2
    canal_2 = 'Canal Fessor Bruno'
    print(canal_2)

#print(canal_2)
channel_2()
