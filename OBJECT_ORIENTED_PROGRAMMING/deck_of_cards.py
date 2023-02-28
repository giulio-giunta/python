# Each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card's __repr__ method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
from random import shuffle


class Card:

    allowed_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    allowed_values = ['A', '2', '3', '4', '5',
                      '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, value, suit):
        if suit not in Card.allowed_suits:
            raise ValueError(f'You can\'t have {self.suit} as suit')
        self.suit = suit
        if value not in Card.allowed_values:
            raise ValueError(f'You can\'t have {self.value} as value')
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

# Each instance of Deck should have a cards attribute with all 52 possible instances of Card.
# Deck should have an instance method called count which returns a count of how many cards remain in the deck.
# Deck's __repr__ method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck should have an instance method called _deal which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should raise a ValueError with the message "All cards have been dealt".
# Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
# Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that single card.
# Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from the deck and return that list of cards.

class Deck:

    cards = [Card(value, suit) for suit in Card.allowed_suits for value in Card.allowed_values]

    def __init__(self):     
        self.cards = Deck.cards

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        else:
            if self.count() >= num:
                self.dealt_card = self.cards[(len(self.cards) - num):]
                for n in range(num):
                    self.cards.pop()
            else:
                self.cards.clear()
            return self.dealt_card

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self.cards

    def deal_card(self, num=1):
        self._deal(num)
        return self.dealt_card[0]

    def deal_hand(self, num):
        self._deal(num)
        return self.dealt_card

d = Deck()
print(d)
# d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(20)
card2 = d.deal_card()
print(card2)
print(d.cards)
print(d.count())
card2 = d.deal_card()
print(d)



