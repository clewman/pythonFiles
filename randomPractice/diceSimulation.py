#random dice rolling simulator

import random


def roll(sides = 6):
    num_rolled = random.randint(1, sides)
    return num_rolled


def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input('Type ENTER to roll, or type QUIT to exit.').lower()
        if roll_again != 'quit':
            num_rolled = roll(sides)
            print('You rolled a', num_rolled)
        else:
            rolling = False

    print('Thanks for playing.')

main()
