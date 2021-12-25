import os; os.system('cls')

print('POO Classes (Parte 3 - Herança')
print()

#O conceito de "Herança" involve "classes-filho" herdando "classes-pai".
#Todas as características da "classe-pai" serão herdadas pela "classe-filho".

class NPC: #Class base / pai / Super

    def __init__(self, nome, time, força, munição):
        self.nome = nome
        self.time = time
        self.força = força
        self.munição = munição
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome: {self.nome}; Time: {self.time}; Força: {self.força}; Munição: {self.munição};', end=' ')
        print(f'Vivo: {"Sim" if self.vivo else "Não"}; Energia: {self.energia}.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Como a classe NPC ("classe-pai") possui um construtor, será preciso criar um aqui, em "Soldado" ("classe-filho") para passar parâmetros.
#P. S.: O novo construtor irá subscrever o antigo (herdado).

class Soldado(NPC): #Fazendo com que "Soldado" herde "NPC".
    def __init__(self, nome, time):
        self.força = 200
        self.munição = 200
        super().__init__(nome, time, self.força, self.munição) #Super captura parâmetros e / ou métodos da "classe-pai".

class Guarda(NPC):
    def __init__(self, nome, time):
        self.força = 100
        self.munição = 20
        super().__init__(nome, time, self.força, self.munição)    

class Elite(NPC):
    def __init__(self, nome, time):
        self.força = 400
        self.munição = 500
        super().__init__(nome, time, self.força, self.munição)
        
    def inf(self):
        super().info()

s1 = Guarda('Olho Vivo', 'Whiskey Velho Olho Vermelho')
s2 = Soldado('Bala Na Agulha', 'Whiskey Velho Olho Vermelho')
s3 = Elite('Ninjolas', 'Whiskey Velho Olho Vermelho')
s4 = Guarda('Super Atento', 'Whiskey Velho Olho Rosa')
s5 = Soldado('Tiro Certo', 'Whiskey Velho Olho Rosa')
s6 = Elite('Zeca Urubu', 'Whiskey Velho Olho Rosa')

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()
