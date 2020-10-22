from deck import Deck
from card_set import Card_set

class Player:
    def __init__(self, name):
        self._name=name
        #self._blackjack=0
        self._card_set=Card_set()

    def hit(self, game_deck, player):
        self._card_set.add_to_set(game_deck, player)
