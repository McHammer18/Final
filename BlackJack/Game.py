"""
Morgan Christensen

Black Jack: this program is black jack emulator that uses a gui to interact with
the player and allow them to place bets

11/28/20
"""
import random
MAX = 21
CARDS = ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
         'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
         'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
         'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']
class Game:
    def __init__(self, dealer_t, player_t):
        self.dealer_total = dealer_t
        self.player_total = player_t

    def game(self):
        CARDS.sort(key=self.shuffle)

        print(self.player_total)

    def shuffle(self, n):
        i = random.randint(1, 53)
        return abs(n - i)
