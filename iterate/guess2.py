# Rebuild the guessing game, but this time:
#   Display the current guess number:
#   If the guess is too low, tell the user "Your guess is too low, try again!"
#   If the guess is too high, tell the user "Your guess is too high, try again!"
#   If the user enters a nonnumeric value, tell the user "Numbers only, please!"

import random

number = random.randint(1, 10)
guess = 0
count = 0

print('Guess a number between 1 and 10')
while(guess != number):
    count += 1

    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric() == False:
        print('Numbers only, please!')
        continue

    guess = int(guess)

    if guess > number:
        print('Your guess is too high, try again!')
    elif guess < number:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')
