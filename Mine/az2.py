def main():
    print("""
            Hello to this wonderful game of rock paper scissor...
            1. Rock
            2. Paper
            3. Scissor
    """)
    check()


def check():
    winnersList = []
    i = []
    gameNumber = 0

    while True:
        p1 = int(input('Rock paper scissor player 1'))
        p2 = int(input('Rock paper scissor player 2'))

        if p1 <= 3 and p1 >= 1 and p2 <= 3 and p2 >= 1:
            if p1 == 1 and p2 != 2:
                print('player 1 wins')
                winnersList.insert(gameNumber, 'player 1')
            elif p1 == 2 and p2 != 3:
                print('player 1 wins')
                winnersList.insert(gameNumber, 'player 1')
            elif p1 == 3 and p2 != 1:
                print('player 1 wins')
                winnersList.insert(gameNumber, 'player 1')
            elif p1 == p2:
                print('draw')
                winnersList.insert(gameNumber, 'draw')
            else:
                print('player 2 wins')
                winnersList.insert(gameNumber, 'player 2')
        else:
            print('please select proper numbers...')

        anotherGame = input('would you like another game? yes or no')

        if anotherGame == 'yes':
            i.insert(gameNumber, gameNumber)
            gameNumber = gameNumber + 1
            continue
        else:
            i.insert(gameNumber, gameNumber)

            for a in i:
                print(f'won game {a}', end='|')

            print('\n')

            for b in winnersList:
                print(f'{b}', end='|')
            else:
                print('done')

            break


main()