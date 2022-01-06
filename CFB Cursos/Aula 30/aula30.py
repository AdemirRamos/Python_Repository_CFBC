import os; os.system('cls'); import random; from colorama import Fore, Back, Style

print('Jogo da Velha Em Python')
print()

play_again = 'Sim'; jogadas = 0; turn = 2; max_moves = 9; win = 'Não'

#2 == Jogador; 1 == Programa.

velha = [

    [' '], [' '], [' '],
    [' '], [' '], [' '],
    [' '], [' '], [' ']

    ]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print('    0   1   2\n')
    print(f'0:  {velha[0][0]} | {velha[1][0]} | {velha[2][0]}')
    print('   -----------')
    print(f'1:  {velha[0][1]} | {velha[1][1]} | {velha[2][1]}')
    print('   -----------')
    print(f'2:  {velha[0][2]} | {velha[1][2]} | {velha[2][2]}')
    print(f'\nJogadas feitas: {Fore.GREEN} {jogadas} {Fore.RESET}')

def jogadas_jogdador():
    global jogadas
    global turn
    global max_moves

    if jogadas == 2 and jogadas < max_moves:

        try:
            l = int(input('Linha: '))
            c = int(input('Coluna: '))
            while velha[l][c] != ' ':
                l = int(input('Linha: '))
                c = int(input('Coluna: '))
            velha[l][c] = 'X'
            turn = l
            jogadas += 1

        except:
            print('Jogada inválida - linha e/ou coluna inválida.')
            os.system('pause')

def jogadas_programa():
    global jogadas
    global turn
    global max_moves    
    if jogadas == 1 and jogadas < max_moves:
        l = random.randint(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != ' ':
            l = random.randint(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = 'O'
        jogadas += 1
        turn = 2

while True:
    tela()
    jogadas_jogdador()
    jogadas_programa()
    break
