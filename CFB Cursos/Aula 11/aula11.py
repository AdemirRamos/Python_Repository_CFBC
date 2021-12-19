print('Condicionais "If", "Elif" e "Else"')
print()

#A vantagem de se usar os condicinais é que, ao se ter um testo lógico com valor "True", os demais não serão realizados.

print('Opções: \n\n1ª: "Sol"; \n2ª: "Chuva"; \n3ª: "Nublado".')

clima = int(input('\nSelecione uma opção: '))
lugar = ''

if clima == 1:
    lugar = 'clube'
    print(f'\nO dia está ensolarado! Hoje é um bom dia para ir para o {lugar}.')

elif clima == 2:
    lugar = 'casa'
    print(f'\nO clima está chuvoso! Hoje é um bom dia para ficar em {lugar}.')

elif clima == 3:
    lugar = 'apartamento'
    print(f'\nO dia está nublado! Hoje é um bom dia para ficar no {lugar}.')

else:
    print('A opção digitada é inválida.')

clima = 'sol'
dinheiro = 500
lugar = ''

print()
if clima == 'sol' and (dinheiro >= 150 and dinheiro <= 500):
    lugar = 'clube'
    print('Eu vou ao {}.'.format(lugar))

else:
    lugar = 'cinema'
    print('Eu vou ao {}.'.format(lugar))

a = 1
b = 2
c = 3
d = 4

print()
if c > a or b:
    print('C é maior do que A e B.')
elif c < 7 or c < d:
    print('C é menor do que 7 ou menor do que D.')

#Tabela:

#And: Para que tenha como resultado "True", todas as condições devem ser verdadeiras.

#And: V  + V = V | V + F = F | F + V = F | F + F = F

#Or: Para que tenha como resultado "True", basta que uma condição seja verdadeira.

#Or: V  + V = V | V + F = V | F + V = V | F + F = F

#Glossário: V == Verdadeiro; F == Falso.
