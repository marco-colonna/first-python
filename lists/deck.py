# Create a list for a standard deck of cards:
#   Add every combination of suit and rank to a list that represents a deck of cards.
#   Display the number of cards in the deck.
# Randomly choose five cards to add to a player's hand:
#   Simulate the dealing of five random cards (choosing, adding to hand, and removing from deck)
#   Display the number of cards in the deck.
#   Print out the cards in the player's hand.

import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

deal = []

print('Dealing ...')
while len(deal) < 5:
    card = random.choice(deck)
    deal.append(card)
    deck.remove(card)

print(f'There are {len(deck)} cards in the deck.')

print('Player has the following cards in their hand:')
print(deal)
