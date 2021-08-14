# Generate a random number between 1 and 5 and allow the user to guess.
# Keep prompting the user for their guesses until they guess correctly.
# Then, display the number of guesses.
# If the user doesn't enter a numeric value, there's no need to notify
# the user of their error. Just keep counting each entry as a guess. 

import random

number = random.randint(1, 5)
guess = 0
count = 0

while guess != number:
    guess = (input('Guess a number between 1 and 5: '))

    if guess.isnumeric():
        guess = int(guess)

    count += 1
else:
    print(f'You guessed it in {count} tries!')
