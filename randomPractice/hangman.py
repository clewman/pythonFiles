#hangman
import random

print('\nWelcome to the 80s band version of Hangman! \nGuess the band using letters or the underscore "_" to create spaces between words. ')

answerlist = [
    'THE_HUMAN_LEAGUE',
     'DEPECHE_MODE',
     'DURAN_DURAN',
     'THE_CURE',
     'THE_SMITHS',
     'NEW_ORDER',
     'INXS'
     ]

random.shuffle(answerlist)

answer = list(answerlist[0])

display = []
display.extend(answer)

for i in range (len(display)):
    display[i] = '*'
# print(' '.join(display))

count = 0
while count < len(answer):
    guess = input('Please guess a letter: ')
    guess = guess.upper()
    print(count)

    for i in  range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count = count + 1

    print(' '.join(display))

print('You guess the 80s band!')
