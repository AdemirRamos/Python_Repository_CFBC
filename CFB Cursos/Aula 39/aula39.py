import os; os.system('cls')

print('JSON Em Python (Parte 4)')
print()

import json

with open('C:/Users/Lucineide Ferreira/Desktop/Programming/Python/Python_Repository_CFBC/CFB Cursos\Aula 39/js.json') as js:
    itens = json.load(js)

#Se usa "load" com arquivos JSON externos.
#Após o "as" vem o nome da variável que vai conter o JSON. Se pode dar a essa variável o nome que se desejar.

#Impressão das chaves:
for c in itens:
    print(f'Chave: {c}')

#Impressão dos itens:
print()
for i in itens.items():
    print(f'Item: {i}')

#Impressão dos valores:
print()
for v in itens.values():
    print(f'Valor: {v}')

#Nome do Jogador:
print()
print(f'Nome do jogador: {itens["nome"]}')

#Itens da mochila:
print()
for itens_mochila in itens['mochila']:
    print(f'Item da mochila: {itens_mochila}')

#Aeronaves:
print()
for a in itens['aeronaves']:
    print(f'Item de "aeronaves": {a}')

#Tipos:
print()
for t in itens['aeronaves']:
    print(f'Tipo de "aeronaves": {t["tipo"]}')

#Habilidades:
print()
for h in itens['aeronaves']:
    print(f'Habilidade de "aeronaves": {h["habilidade"]}')

#Tipos e habilidades:
print()
for th in itens['aeronaves']:
    print(f'Tipo: {th["tipo"]}; Habilidade: {th["habilidade"]}.')
