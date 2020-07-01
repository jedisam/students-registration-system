# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess.
#  If the user guesses wrong then the prompt appears again until the guess is correct,
#  on successful guess, user will get a "Well guessed!" message, and the program will exit.
# /usr/bin/env python3

import random


def main():
    while True:
        randNum = random.randint(1, 9)
        print(randNum)
        num = int(input('Choose a random number: '))
        if(randNum == num):
            print('Yeahhhhhh')
            break


if __name__ == '__main__':
    main()
