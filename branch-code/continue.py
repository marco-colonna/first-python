# Write a short program that prints one of several messages to the user based on their input.
# First, prompt the user about whether they want to continue.
#   no or n: print the phrase 'Exiting.'
#   yes or y: print the phrases 'Continuing ...' and 'Complete!'
#   anything else: print the phrase 'Please try again and respond with yes or no.'

print('Would you like to continue?')

response = input()

if response == 'no' or response == 'n':
    print('Exiting.')
elif response == 'yes' or response == 'y':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')
