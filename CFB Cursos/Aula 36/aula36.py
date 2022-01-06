import os; os.system('cls')

print('JSON Em Python (Parte 1)')
print()

import json

carros_json = '{"marca": "honda", "modelo": "HRV", "cor": "prata"}' #Isso é um "JSON".

#As aspas devem ser postas exatamente assim para se evitar erros.

carros = json.loads(carros_json) #Carregando o "JSON" como uma "string".
print(carros)

#JSON's podem ser manipulados exatamente como dicionários:

print(f'\n{carros["marca"]}\n')

for x in carros: #"Printando" as chaves.
    print(x)

print()

for x in carros.values(): #"Printando" os valores.
    print(x)

print()

for x in carros.items(): #Imprimindo ambos (chaves e itens).
    print(x)

print()

for k, v in carros.items():
    print(f'Chave: "{k}", Valor: "{v}"')

#O grande diferencial cujo o qual a aula se propõe a exemplificar é a conversão de um JSON para uma "string" do Python;
#Assim como sua posterior manipulação feita do memso modo aplicado ao Dicionário.

#Transformando um dicionário em um JSON:

cars = {"marca": "honda", "modelo": "HRV", "cor": "prata"}
carros_json = json.dumps(cars) #Realizando a conversão.
print(f'\n{cars}')
