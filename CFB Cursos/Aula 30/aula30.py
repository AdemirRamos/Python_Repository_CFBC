import os; os.system('cls'); import random; from colorama import Fore, Back, Style

print('Jogo da Velha Em Python (Parte 1)')
print()

play_again = 'Sim'; jogadas = 0; turn = 2; max_moves = 9; win = 'Não'

velha = [

    [' '], [' '], [' '],
    [' '], [' '], [' '],
    [' '], [' '], [' ']

    ]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print('    0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('0:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('0:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('\nJogadas fetas' + Fore.GREEN + str(jogadas) + Fore.RESET)

while True:
    tela()