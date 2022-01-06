from math import e
import os; os.system('cls'); import random; from colorama import Fore, Back, Style

print('Jogo da Velha Em Python')
print()

play_again = 'Sim'; jogadas = 0; turn = 2; max_moves = 9; win = 'Não'; vitória = 'não'

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

def victory():
    global velha
    vitória = 'não'
    símbolos = ['X', 'O']
    for s in símbolos:
        vitória = 'não'
        #Verificar vitória em linhas:

        line_index = column_index = 0

        while line_index < 3:
            soma = 0
            column_index = 0
            while column_index < 3:
                if (velha[line_index][column_index] == s):
                    soma += 1
                column_index += 1
            if soma == 3:
                vitória = s
                break
            line_index += 1
        if (vitória != 'não'):
            break

        #Verificar vitória em colunas:

        line_index = column_index = 0

        while column_index < 3:
            soma = 0
            line_index = 0
            while line_index < 3:
                if (velha[line_index][column_index] == s):
                    soma += 1
                line_index += 1
            if soma == 3:
                vitória = s
                break
            column_index += 1
        if (vitória != 'não'):
            break

        #Verificar vitória em diagonais (1ª diagonal):

        soma = 0
        diagonal_1 = 0
        while diagonal_1 < 3:
            if (velha[diagonal_1][diagonal_1] == s):
                    soma += 1
            diagonal_1 += 1
        if soma == 3:
            vitória = s
            break

        #Verificar vitória em diagonais (2ª diagonal):

        soma = 0
        diagonal_line = 0
        diagonal_column = 2
        while diagonal_column >= 0:
            if (velha[diagonal_line][diagonal_column] == s):
                    soma += 1
            diagonal_line += 1
            diagonal_column -= 1
        if soma == 3:
            vitória = s
            break

        return victory

def redefinir():
    global velha
    global jogadas
    global turn
    global max_moves
    global vitória

    velha = [

        [' '], [' '], [' '],
        [' '], [' '], [' '],
        [' '], [' '], [' ']

        ]    
while (play_again == 'sim'):
    while True:
        tela()
        jogadas_jogdador()
        jogadas_programa()
        tela()
        vitória = victory()

        if (vitória != 'não') or (jogadas >= max_moves):
            break

    print(f'{Fore.RED}Fim de jogo.{Fore.YELLOW}')
    
    if vitória == 'X' or vitória == 'O':
        print(f'Resultado: jogador {vitória} venceu.')

    else:
        print('Resultado: empate.')
    
    play_again = input(f'{Fore.BLUE}Jogar novamente? [s/n]: {Fore.RESET}')
    redefinir()
