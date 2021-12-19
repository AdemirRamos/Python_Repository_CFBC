print('Como Usar o Comando "IF" em Python')
print()

a = True #Caso a expressão de "if" seja "True", o primeiro bloco de comandos é executado; caso seja "False", o segundo é executado.

if a:
    print('Verdadeiro.')
else:
    print('Falso.')

b = False
if b:
    print('Verdadeiro.')
else:
    print('Falso.')

c = 10
d = 5
e = 1

if c > d:
    print('Verdadeiro.')
else:
    print('Falso.')

if d == 5:
    resultado = c + d
else:
    resultado = d + e

print(resultado)
