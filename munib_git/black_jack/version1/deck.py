import random
from .card import Card

class Card_deck:
    def __init__(self,
                 card_no_list= ['2','3','4','5','6','7','8','9','10', 'A', 'J', 'Q', 'K'],
                 card_symbols_list=['Spade', 'Club', 'Heart', 'Diamond']
                 ):
        self._card_no_list = card_no_list #['2','3','4','5','6','7','8','9','10', 'A', 'J', 'Q', 'K']
        self._card_symbols_list = card_symbols_list #['Spade', 'Club', 'Heart', 'Diamond']
        self._card_deck =[]

    #populate deck with all combinatons
    def fill_deck(self):
        for card_no in self._card_no_list:
            for card_symbol in self._card_symbols_list:
                self._card_deck.append(Card(card_no, card_symbol))
    #shuffling of deck
    def shuffle(self):
        random.shuffle(self._card_deck)

    #take the upper mostcard
    def draw_card(self):
        return self._card_deck.pop()

    # used in testing, no other significance
    #def total_no_of_cards(self):
    #    return len(self._card_deck)