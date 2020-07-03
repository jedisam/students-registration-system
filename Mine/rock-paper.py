# /usr/bin/env python 3

def main():
    print('\n----Welcome to rock-paper-scissor---\n')
    print('Enter rock, paper, or scissor\n')
    print('Press 1 to end game..')
    winner_list = []
    while True:
        x = input('Player 1: ')
        try:
            if int(x) == 1:
                break
        except:
            y = input('Player 2: ')
            try:
                if int(y) == 1:
                    break
            except:
                if(x == 'rock' and y == 'scissor' or x == 'scissor' and y == 'paper' or x == 'paper' and y == 'rock'):
                    winner_list.append('Player1')
                    print('\n Player 1 won')
                    print('Press 1 to quit...\n')
                    # winner = 'Player 1'
                elif(y == 'rock' and x == 'scissor' or y == 'scissor' and x == 'paper' or y == 'paper' and x == 'rock'):
                    winner_list.append('Player2')
                    print('\n Player 2...\n')
                    print('Press 1 to quit...\n')
                    # winner = 'Player 2'
                else:
                    print('\nTied!... \n Try again \n')
                    winner_list.append('Tied')

    # print(f'\nThe Winner is {winner}')
    print('\n ----Result----\n')
    print(winner_list)
    player1 = 0
    player2 = 0
    for i in winner_list:
        print(i)
        if i == 'player1':
            # print('hey')
            player1 += 1
        elif i == 'player2':
            print('wey')
            # player2 += 1
    score = [player1, player2]
    print(score)


main()
