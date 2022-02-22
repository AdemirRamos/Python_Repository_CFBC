print('Strings (Parte 2)')
print()

curso = 'Curso de Python'.split(' ')
anwser_1 = curso[2]
anwser_2 = 'Javascript'

resposta = 'Python' in curso
resposta_2 = 'Javascript' not in curso

if resposta and resposta_2 == True:
    print(f'A palavra "{anwser_1}" foi encontrada na variável "resposta".')
    print(f'A palavra "{anwser_2}" foi encontrada na variável "resposta_2".')

print()
texto = 'Olá, mundo!'
palavra = 'olá'

res = palavra.upper() in texto.upper()
print(res)

cidade = 'Belo Horizonte'
dia = 15
mês = 'Dezembro'
ano = 2019
canal = 'CFB Cursos'
data = '{}, {} de {} de {}.\n{}'
print(data.format(cidade, dia, mês, ano, canal))

#Como imprimir aspas (maneira complicada):
#A maneira simples consiste em alternar as aspas. Se a "string" foi posta entre aspas duplas, use aspas simples dentro dela e vice-versa.

nome = 'Ademir'
idade = 25
sexo = 'Feminino'
info = 'O nome informado foi: \"{}\"; a idade informada foi: \"{}\"; o sexo informado foi: \"{}\".'
print(info.format(nome, idade, sexo))

s1 = '\bVamos falar '
s2 = 'de Python!\r'
print(s1 + s2)

#Checar as funcionalidades de "\r" e "\b".
