"""
Morgan Christensen

Card class for creating and schuffling cards

12/04/20
"""
import ctypes

from PIL import ImageTk, Image
import random
import os

cards_location = './card_images/cards/'
hidden_card_location = './card_images/hidden.jpg'


def collect_cards():
    cards = os.listdir(cards_location)

    cards = [card.split('.')[0] for card in cards]

    return cards


class Card():
    def __init__(self, name, suit, value=11, is_displayed=True):
        self.name = name # face cards
        self.suit = suit # suit of card
        self._is_displayed = is_displayed # whether the card is face up or down
        self._value = value # value of the card

    # getteers and setters
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
            self._value = 11 # sees aces as a value of 11
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

    @staticmethod
    #method to shuffle deck
    def shuffle_deck(deck):
        cards = deck

        random.shuffle(cards)

        dealed_card = cards[0]
        return dealed_card

    @staticmethod
    def get_card_image(card):
        try:
            card_file_location = f"{cards_location}/{getattr(card,'name')}.png"
            card_image = Image.open(card_file_location)
            card_image_shaped = card_image.resize((159,225), Image.ANTIALIAS) # this will reshape the card because its actual size its huge!
            card_image = ImageTk.PhotoImage(card_image_shaped)

            return card_image

        except:
            ctypes.windll.user32.MessageBoxW(0,
                                             "Could not find cards. Missing card_images folder with all the card images",
                                             "Cards Images are missing!", 1)

    @staticmethod
    def hidden_card():
        try:
            card_image = Image.open(hidden_card_location)
            card_image_shaped = card_image.resize((159,225), Image.ANTIALIAS) # this will reshape the card because its actual size its huge!
            card_image = ImageTk.PhotoImage(card_image_shaped)

            return card_image

        except:
            ctypes.windll.user32.MessageBoxW(0,
                                             "Could not find cards. Missing card_images folder with all the card images",
                                             "Cards Images are missing!", 1)