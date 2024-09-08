#2023/10/04 00:00|Крестики-нолики

import os

game_field = [['        |', '   ', '   ', '   ', '|  '], 
              ['        |', ' * ', ' * ', ' * ', '|  '], 
              ['        |', ' * ', ' * ', ' * ', '|  '], 
              ['        |', ' * ', ' * ', ' * ', '|  ']]

def draw_game_menu():
    os.system('cls')
    print('\n>>> The game of tic tac toE <<<')
    print('\n Player 1 - X     Player 1 - O')

def draw_matrix_game_field():
    print('         _____________')
    for i in game_field:
        print(*i)
    print('        |_____________|\n')

def check_winer():
    if game_field[1][1] == ' X ' and game_field[1][2] == ' X ' and game_field[1][3] == ' X ':
        return ' X '
    if game_field[1][1] == ' O ' and game_field[1][2] == ' O ' and game_field[1][3] == ' O ':
        return ' O '

draw_game_menu()
draw_matrix_game_field()

for turn in range(1, 10):
    print(f'Ход :{turn}')
    if turn % 2 == 0:
        turn_char = ' O '
        print('Ход Player 2\n')
    else:
        turn_char = ' X '
        print('Ход Player 1\n')

    row = int(input('Введите номер строки (1, 2, 3) '))
    col = int(input('Введите номер столбца (1, 2, 3) '))
    
    if game_field[row][col] == ' * ':
        game_field[row][col] = turn_char
    else:
        print('Ячейка занята, вы пропускаете ход!')
        continue    

    draw_game_menu()
    draw_matrix_game_field()

    if check_winer() == ' X ':
        print('Player 1 WINS!')
        break
    if check_winer() == ' O ':
        print('Player 2 WINS!')
        break
    if check_winer() == ' * ':
        print('DROW')
        break