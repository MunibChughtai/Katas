import random
from card import Card

class Deck:
    def __init__(self,
                 card_no_list_input = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace'],
                 card_shape_list_input = ['Heart', 'Diamond', 'Spade', 'Club']
                 ):
        self._card_list=[]
        self._card_no_list = card_no_list_input # input parameters
        self._card_shape_list = card_shape_list_input # input parameters

    def pick_next_card(self):
        return self._card_list.pop()

    def deck_setup(self):
        self._fill_deck()
        self._randomize_deck_cards()

    def _fill_deck(self):
        for card in self._card_no_list:
            for card_shape in self._card_shape_list:
                self._card_list.append(Card(card, card_shape))

    def _randomize_deck_cards(self):
        random.shuffle(self._card_list)