import random

def print_result(computer, opponent):
    return 'You {}!'.format('Lose' if (computer == opponent) else 'Win')

def start():
    player = None
    choices = [
        'rock',
        'paper',
        'scissor'
    ]
    computer = random.choice(choices)

    while player not in choices:
        player = input('Choices: Rock, Paper, or Scissor?: ').lower()

    print('Player: ', player)
    print('Computer: ', computer)

    if not (player == computer):
        if player == 'rock':
            print(print_result(computer, 'paper'))
        elif player == 'paper':
            print(print_result(computer, 'scissor'))
        else:
            print(print_result(computer, 'rock'))
    else:
        print('It\'s a Tie!')

while True:
    start()

    continue_playing = input('Continue [Y/N]?: ').upper()

    if continue_playing != 'Y':
        break

print('Rock, Paper, or Scissor Game Done!')