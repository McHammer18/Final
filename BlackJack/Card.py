"""
Morgan Christensen

Card class for creating and schuffling cards

12/04/20
"""

class Card():
    def __init__(self, name, suit, value=11, is_displayed = True):
        self.name = name #face cards
        self.suit = suit #suit of card
        self._is_displayed = is_displayed #whether the card is face up or down
        self._value = value #value of the card

    #getteers and setters
    @property
    def is_displayed(self):
        return self._is_displayed

    @is_displayed.setter
    def is_displayed(self, value):
        self._is_displayed = value

    @property
    def value(self):
        if str(self.name)[0] in ['J', 'Q', 'K']:
            self._value = 10 # sees if card has a face card name to set value to 10
        elif str(self.name)[0] == 'A':
            self._value = 11 #sees aces as a value of 11
        else:
            self._value = int(self.name.split('-')[0])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value[0] == 'H':
            self._suit = "Hearts" # sees if card has a face card name to set value to 10
        elif value[0] == 'C':
            self._suit = "Clubs"
        elif value[0] == 'D':
            self._suit = "Diamonds"
        else:
            self._suit = "Spades"