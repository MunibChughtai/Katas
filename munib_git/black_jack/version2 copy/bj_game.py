from deck import Deck
from player import Player

class Bj_game:
    def __init__(self):
        #self._deck = Deck([6,5,2,7, 'Queen', 'King',7], ['Heart'])
        self._deck = Deck()
        self._player = Player('Player')
        self._dealer = Player('Dealer')

    def start_game(self, test_mode=0):
        #self._deck.deck_setup()
        self._player._card_set.get_first_2_cards(self._deck)
        self._dealer._card_set.get_first_2_cards(self._deck)

        if(self._gotoconsole_player(test_mode) == 'Bust!'):
            print('Dealer wins!')
            return
        if (self._gotoconsole_dealer() == 'Bust!'):
            print('You beat the dealer!')
            return
        #if (self._dealer._card_set.get_score() == 'Bust!'):
        print(self._find_result())

    def _get_user_input(self):
        user_input = input(f'Hit or Stay? (Hit = 1, Stay =0): ')
        return user_input

    def _gotoconsole_player(self, test_mode):
        while True:
            self._player._card_set.display_set(self._player._name)
            if self._player._card_set.get_score()=='Black Jack!':
                return 1
            if self._player._card_set.get_score() == 'Bust!':
                return 'Bust!'

            user_input = 0 if test_mode else self._get_user_input()
            if int(user_input):
                self._player.hit(self._deck, self._player._name)
            else:
                return 0

    def _gotoconsole_dealer(self):
        self._dealer._card_set.display_set(self._dealer._name)
        #if self._dealer._card_set.get_score() == 'Bust!':
        #    return -1
        while self._dealer._card_set.get_score() not in ['Black Jack!', 'Bust!'] and self._dealer._card_set.get_score() < 17:
            self._dealer.hit(self._deck, self._dealer._name)
            self._dealer._card_set.display_set(self._dealer._name)

        if self._dealer._card_set.get_score() == 'Bust!':
            return 'Bust!'
        else:
            return

    def _find_result(self):
        if self._player._card_set.is_black_jack() and self._dealer._card_set.is_black_jack():
            return 'Its a Tie'
        elif self._player._card_set.is_black_jack():
            return 'You beat the dealer'
        elif self._dealer._card_set.is_black_jack():
            return 'Dealer wins'
        else:
            if self._player._card_set.get_score() > self._dealer._card_set.get_score():
                return 'You beat the dealer'
            elif self._dealer._card_set.get_score() > self._player._card_set.get_score():
                return 'Dealer wins'
            else:
                return 'Its a Tie'
