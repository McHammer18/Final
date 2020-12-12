"""
Morgan Christensen

Dealer's actions

12/12/20
"""

class DealerAI():
    def __init__(self, dealer_score, player_score):
        self.dealer_score = dealer_score
        self.player_score = player_score

    @property
    def dealer_score(self):
        return self._dealer_score

    @dealer_score.setter
    def dealer_score(self,value):
        self._dealer_score = value

    @property
    def player_score(self):
        return self._player_score

    @player_score.setter
    def player_score(self, value):
        self._player_score = value

    def is_hit(self):
        if int(self.dealer_score) > int(self.player_score):
            return False
        else:
            return True