print('Strings (Parte 1)')
print()

curso = ' Curso de Python '.strip().lower()
print(curso)
curso_2 = 'Curso de JS'.upper().replace('DE', 'of')

#"Uma 'string', nada mais é, do que um 'array' de caracteres; do que uma lista de caracteres."

#Fatiamento:

print(curso[0])
print(curso[0:5])
print('Tamanho da "string": ' + str(len(curso)))
print(curso_2)
a = curso_2.split(' ') #O método "split()" separa uma "string" em vetor com base no valor informado (entre aspas).
print(a)
print(a[0])
