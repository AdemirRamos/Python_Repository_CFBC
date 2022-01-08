import os; os.system('cls')

print('JSON Em Python (Parte 3)')
print()

import json

json_37 = '{"nome": "Bruno", "time": "aviadores","vivo": "True", "energia": "100", "mochila": ["pederneira, "corda", "linha", "arame"], "aeronaves:" [{"tipo": "transporte", "habilidade": "80"}, {"tipo": "ataque", "habilidade": "100"}, {"tipo": "reconhecimento", "habilidade": "50"}]}'

itens = json.loads(json_37)

#Impressão das chaves:
for c in itens:
    print(c)

#Impressão dos itens:
print()
for i in itens.items():
    print(i)

#Impressão dos valores:
print()
for v in itens.values():
    print(v)

#Nome do Jogador:
print()
print(itens['nome'])

#Itens da mochila:
print()
for itens_mochila in itens['mochila']:
    print(itens_mochila)

#Aeronaves:
print()
for a in itens['aeronaves']:
    print(a)

#Tipos:
print()
for t in itens['aeronaves']:
    print(t['tipo'])

#Habilidades:
print()
for h in itens['aeronaves']:
    print(h['habilidade'])

#Tipos e habilidades:
print()
for th in itens['aeronaves']:
    print(f'Tipo: {th["tipo"]}; Habilidade: {th["habilidade"]}.')
