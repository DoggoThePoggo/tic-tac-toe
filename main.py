'''
I am a tic tac toe game!
'''

import math
import random

game_size = 3

def main_menu():
    print('\n❌⭕ Hello! You are now playing Tic-Tac-Toe ⭕❌')

    # Allow player to choose player names
    input_check = False
    while input_check == False:
        try:
            p1 = input('Player 1\'s name: ')
            p2 = input('Player 2\'s name: ')

        except:
            pass

        else:
            if p1 == p2:
                print('Both players cannot share the same name.')
            
            else:
                input_check = True

    # Allow player to choose symbol
    shape_list = ['O', 'X']

    input_check = False
    while input_check == False:

        try:
            p1_symbol = int(input(f'\nSelect the symbol for {p1}:\n1. {shape_list[0]}\n2. {shape_list[1]}\n'))

        except:
            print('\nThat\'s not a  valid input, come on...')

        else:
            if p1_symbol == 1:
                p2_symbol = shape_list[1]
                input_check = True
            
            elif p1_symbol == 2:
                p2_symbol = shape_list[0]
                input_check = True

            else:
                print('\nThat\'s not a  valid input, come on...')
            
            p1_symbol = shape_list[p1_symbol - 1]

    # Allow player to select who starts first
    starting_player = ''

    input_check = False
    while input_check == False:
        try:
            starting_player = input(f'\nSelect a player to start first:\n{p1}\n{p2}\n')

        except:
            pass

        else:
            if starting_player == p1 or starting_player == p2:
                input_check = True

            else:
                print('Please enter the player\'s name exactly as displayed.')
                input_check = False


    return p1, p1_symbol, p2, p2_symbol, starting_player

def print_board(game_data):


    print('\n  ', end='')
    for x in range(game_size):
        print(f'  {x+1} ', end='')
    print('')

    for y in range(game_size):
        print('  ' + '+---' * game_size + '+')
        print(f'{y+1} ', end='')
        for x in range(game_size):
            print('| ' + '\033[1;32;40m' + game_data[x+1,y+1] + '\033[0m' + ' ', end='')
        print('|')

    print('  ' + '+---' * game_size + '+')

def make_move(game_data, player_name, player_symbol):
    input_checker = False
    while input_checker == False:
        try:
            x, y = input(f'{player_name}, please make a move. (left ➡ Right, Top ➡ Bottom e.g. {random.randint(1,3)}, {random.randint(1,3)})\n').split(',')
            x, y = int(x), int(y)

        except:
            print('Invalid input.\n')

        else:
            if x > 3 or x < 1 or y > 3 or y < 1:
                print('Invalid move.\n')

            elif game_data[(x,y)] != ' ':
                print('Invalid move.\n')

            else:
                game_data[(x,y)] = player_symbol
                input_checker = True

    return game_data

def begin_game(p1, p1_symbol, p2, p2_symbol, starting_player):
    '''
    Start the game by intializing empty data set
    Proceed to prompt each player for their moves and update dictionary accordingly
    '''

    players = {
        p1: p1_symbol, 
        p2: p2_symbol
        }

    game_data = {}
    winner = ''

    for x in range(game_size):
        for y in range(game_size):
            game_data[(x+1,y+1)] = ' '

    current_player = starting_player
    previous_player = ''
    
    print_board(game_data)

    while winner == '':
        if current_player == p1:
            game_data = make_move(game_data, p1, p1_symbol)
            current_player = p2
            previous_player = p1

        elif current_player == p2:
            game_data = make_move(game_data, p2, p2_symbol)
            current_player = p1
            previous_player = p2

        if winner_checker(game_data):
            winner = previous_player

        print_board(game_data)

    print(f'🎉🎉 {winner} has won! 🎉🎉')


def winner_checker(game_data):
    #check columns
    if game_data[(1,1)] == game_data[(1,2)] and game_data[(1,2)] == game_data[(1,3)] and game_data[(1, 1)] != ' ':
        return True
    
    elif game_data[(2,1)] == game_data[(2,2)] and game_data[(2,2)] == game_data[(2,3)] and game_data[(2, 1)] != ' ':
        return True
    
    elif game_data[(3,1)] == game_data[(3,2)] and game_data[(3,2)] == game_data[(3,3)] and game_data[(3, 1)] != ' ':
        return True

    #check columns
    elif game_data[(1,1)] == game_data[(2,1)] and game_data[(2,1)] == game_data[(3,1)] and game_data[(1, 1)] != ' ':
        return True
    
    elif game_data[(1,2)] == game_data[(2,2)] and game_data[(2,2)] == game_data[(3,2)] and game_data[(1, 2)] != ' ':
        return True
    
    elif game_data[(1,3)] == game_data[(2,3)] and game_data[(2,3)] == game_data[(3,3)] and game_data[(1, 3)] != ' ':
        return True

    #check diagonals
    elif game_data[(1,1)] == game_data[(2,2)] and game_data[(2,2)] == game_data[(3,3)] and game_data[(1, 1)] != ' ':
        return True
    
    elif game_data[(1,3)] == game_data[(2,2)] and game_data[(2,2)] == game_data[(3,1)] and game_data[(1, 3)] != ' ':
        return True
    
    else:
        return False

def main():
    p1, p1_symbol, p2, p2_symbol, starting_player = main_menu()
    begin_game(p1, p1_symbol, p2, p2_symbol, starting_player)

main()