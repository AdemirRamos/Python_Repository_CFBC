print('Jogo Simples de Adivinhação (Em Python)')
print()

import os; import random
os.system('cls')

computador = random.randint(0, 10)
print('Olá, eu acabei de pensar em um número entre 0 e 10. Será que você consegue adivinhar em qual número eu pensei?')
print('\nVocê tem 5 tentativas para acertar!')

contador = 0
chances = 4

while contador < 5:
    
    try:
        guess = int(input('\nDigite o seu palpite aqui: '))

    except:
        print('\nErro. Por favor, digite um número inteiro.')
        continue

    if guess == computador:
        print(f'\nVocê acertou! Eu pensei exatamente no número {computador}.')
        break

    elif guess > computador:
        print('\nVocê errou! Eu pensei em um número menor...')
        print(f'\nVocê tem mais {chances} chance (s).')
        contador += 1
        chances -= 1

    elif guess < computador:
        print('\nVocê errou! Eu pensei em um número maior...')
        print(f'\nVocê tem mais {chances} chance (s).')
        contador += 1
        chances -= 1

    if contador == 5:
        print(f'\nSuas tentativas acabaram! Eu venci!\nEu pensei no número {computador}.')
        break

#Resolução do Bruno:

print()
import random

erros = 0
sorteado = random.randrange(0, 100)
jogador = int(input('Digite o seu número: '))

while (sorteado != jogador):
    os.system('cls')
    
    if (sorteado > jogador):
        print('Erro. O número escolhido é maior.')
    
    elif (sorteado < jogador):
        print('Erro. O número escolhido foi menor.')

    erros += 1

    jogador = int(input('Digite o seu número aqui: '))

print(f'Número escolhido: {jogador}, número sorteado: {sorteado}. Você precisou de {erros + 1} tentativas para acertar.')
