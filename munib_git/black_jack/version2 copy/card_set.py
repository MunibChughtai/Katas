from card import Card
from deck import Deck

class Card_set:
    def __init__(self):
        self._cards=[]
        self._digit_list = []
        self._face_card_list = []
        self._ace_card_list = []

    def segregate(self):
        # 2 - 10, J, Q, K, A
        self._digit_list = [digit_card.get_card_no() for digit_card in self._cards if str(digit_card.get_card_no()).isdigit()]
        self._face_card_list = [face_card.get_card_no() for face_card in self._cards if face_card.get_card_no() in ('Jack', 'Queen', 'King')]
        self._ace_card_list = [ace_card.get_card_no() for ace_card in self._cards if ace_card.get_card_no() == 'Ace']

    def get_first_2_cards(self, game_deck):
        self._cards.append(game_deck.pick_next_card())
        self._cards.append(game_deck.pick_next_card())

    def add_to_set(self, game_deck, player):
        self._cards.append(game_deck.pick_next_card())
        print(f'{player} draw {self._cards[len(self._cards)-1].display_card()}')

    def display_set(self, player_name):
        if player_name == 'Player': print(f'\nYou are currently at: {self.get_score()}')
        else: print(f'\nDealer is currently at: {self.get_score()}')
        print(f'with the hand [', end=' ')
        for key,card in enumerate(self._cards):
            if key==len(self._cards)-1:
                print(f'{card.display_card()}', end='')
            else:
                print(f'{card.display_card()}, ', end='')
        print(f']\n')
        #if self.get_score() == 'Bust!':
        #    raise ValueError('Busted')

    def is_black_jack(self):
        if self.get_score()=='Black Jack!':
            return True
        else:
            return False

    def get_score(self):
        res=0
        #self._digit_list = self._face_card_list = self._ace_card_list=[]
        self.segregate()
        while True:
            res = sum(self._digit_list) + (len(self._face_card_list)*10) + (len(self._ace_card_list)*11)
            if res > 21:
                if len(self._ace_card_list):
                    self.fix_ace_card_list()
                else:
                    return 'Bust!'
            elif res==21:
                return 'Black Jack!'
            else:
                return res

    def fix_ace_card_list(self):
        self._ace_card_list.pop()
        self._digit_list.append(1)