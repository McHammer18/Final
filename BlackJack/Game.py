"""
Morgan Christensen

Black Jack: this program is black jack emulator that uses a gui to interact with
the player and allow them to place bets

11/28/20
"""
import random
MAX = 21
CARDS = {1: 'HA', 2: 'H2', 3: 'H3', 4: 'H4', 5: 'H5', 6: 'H6', 7: 'H7', 8: 'H8', 9: 'H9', 10: 'H10', 11: 'HJ', 12: 'HQ',
         13: 'HK',
         14: 'CA', 15: 'C2', 16: 'C3', 17: 'C4', 18: 'C5', 19: 'C6', 20: 'C7', 21: 'C8', 22: 'C9', 23: 'C10', 24: 'CJ',
         25: 'CQ', 26: 'CK',
         27: 'DA', 28: 'D2', 29: 'D3', 30: 'D4', 31: 'D5', 32: 'D6', 33: 'D7', 34: 'D8', 35: 'D9', 36: 'D10', 37: 'DJ',
         38: 'DQ', 39: 'DK',
         40: 'SA', 41: 'S2', 42: 'S3', 43: 'S4', 44: 'S5', 45: 'S6', 46: 'S7', 47: 'S8', 48: 'S9', 49: 'S10', 50: 'SJ',
         51: 'SQ', 52: 'SK'}

class Game:
    def __init__(self, dealer_t, player_t):
        self.dealer_total = dealer_t
        self.player_total = player_t

    def game(self):
        pass