#hangman
#make a hangman display that fills in each time someone guesses
#display the word when they win
#tell how many characters are in the answer
#tell how many characters are left

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

used_letters = []

random.shuffle(answerlist)

answer = list(answerlist[0])

display = []
display.extend(answer)
used_letters.extend(display)
for i in range (len(display)):
    display[i] = '*'
# print(' '.join(display))

count = 0
incorrect = 5

while count < len(answer) and incorrect > 0:
    guess = input('Please guess a letter: ')
    guess = guess.upper()
    print(count)

    for i in  range(len(answer)):
        if answer[i] == guess and guess in used_letters:
            display[i] = guess
            count = count + 1
            used_letters.remove(guess)

    if guess not in display:
        incorrect = incorrect - 1
        print(' You have ', incorrect, ' chances left.')


    print('You have guessed: ', count, 'correct characters.')
    print('You have', incorrect, ' chances left.')
    print(' '.join(display))

if count == len(answer):
    print(f'You guessed the 80s band! -- {answer} --')

else:
    print('You lose')
