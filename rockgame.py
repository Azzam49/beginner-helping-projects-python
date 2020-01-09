import random
import sys
import time

# cases to avoid repeating myself.
case_0 = 'Its a draw'
case_1 = 'Player Wins'
case_2 = 'Computer Wins'

valid_inputs = ['rock', 'paper', 'scissors', 'lizard', 'spock', 'help', 'exit']
symbols = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# dic to check who wins
outcome_dict = {'rock': {'rock': case_0, 'paper': case_2, 'scissors': case_1, 'lizard': case_1, 'spock': case_2},
                'paper': {'rock': case_1, 'paper': case_0, 'scissors': case_2, 'lizard': case_2, 'spock': case_1},
                'scissors': {'rock': case_2, 'paper': case_1, 'scissors': case_0, 'lizard': case_1, 'spock': case_2},
                'lizard': {'rock': case_2, 'paper': case_1, 'scissors': case_2, 'lizard': case_0, 'spock': case_1},
                'spock': {'rock': case_1, 'paper': case_2, 'scissors': case_1, 'lizard': case_2, 'spock': case_0}}


print('''
******************** S T A R T     G A M E *********************
Hello player. Welcome to Rock Paper Scissors Lizards Spock.
Please select from either Rock, Paper, Scissors, Lizard or Spock.
If you do not know how to play this game, type Help.
If you wish to exit this game, type Exit.
Thanks
****************************************************************
''')

def handle_user_input():
    '''
    This function is responsible for assigning the sign
    (rock, paper etc) to the user or showing help text or
    exiting the game.

    OUTPUT:{
        1. closes the game
        2. prints help text and asks for input again
        3. assigns rock, paper etc to a variable and returns.
    }
    '''

    user_input = input('Please select a symbol or type exit or help.\n').lower()

    while user_input not in valid_inputs:
        print('Please enter a valid input.')
        user_input = input().lower()

    while user_input != 'exit()' and user_input in valid_inputs[:-1]:

        while user_input == 'help':
            print('''Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\n need help again? type help\n or type exit to exit\n or
             select any of the above symbols.''')
            user_input = input().lower()

            if user_input == 'exit':
                print('thanks for playing! :D')
                sys.exit()
            elif user_input in symbols:
                return user_input

        if user_input in symbols:
            return user_input

def play_game(player_choice):
    '''
    This function will compute the game played by taking in the following argument:

    INPUT: {
        player_choice = what the player has chosen as their symbol
    }

    OUTPUT: {
        returns the winner of the play
        player can choose to restart.
    }
    '''

    computer_choice = random.choice(symbols)

    print('...and the winner is ...\n')
    time.sleep(3)
    print(computer_choice)
    print('*****************************************')
    print(outcome_dict[player_choice][computer_choice])
    return outcome_dict[player_choice][computer_choice]

if __name__ == '__main__':
    restart = 'yes'

    while restart == 'yes':
        player_choice = handle_user_input()
        winner = play_game(player_choice)

        restart = input('type Yes to restart the game or type No to exit\n').lower()
    else:
        print('******************************************************')
        print('Thanks for playing')
