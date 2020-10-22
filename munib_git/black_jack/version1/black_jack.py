import random


# stack of cards
# the constructor used here also contains card nos, so that tests can be done in controlled environment.



class Player:
    def __init__(self):
        self._cards=[] # cards present with the player at any given moment. It hold instances of card object
        self._sum_cards=0 # sum of values of cards held by player
        self._no_of_cards=0 # number of cards held by player
        self._blackjack_found=0 # flag to see if blackjack has been found

    #picking up card from the deck either by player or dealer
    def hitting(self, my_game_deck, dealer_flag=0, ignore_output=0):
        self._cards.append(my_game_deck.pop_deck())

        if ignore_output ==0:
            if dealer_flag ==0:
                print(f'You draw [{self._cards[-1]._number}, {self._cards[-1]._sign}]')
            else:
                print(f'Dealer draws [{self._cards[-1]._number}, {self._cards[-1]._sign}]')
        self._no_of_cards += 1
        self.set_sum_card(dealer_flag)


    def get_number_of_cards(self):
        return self._no_of_cards

    def set_sum_card(self, dealer_flag):
       res = sum([card._value for card in self._cards])

       if res == 21:
           self._blackjack_found = 1
           self._sum_cards = res
           return

       elif res > 21:
           for card in self._cards:
               if card._number=='A' and card._value==11:
                   card._value=1
                   res -= 10
                   break
           else:
               if dealer_flag==0:
                   raise ValueError ('Dealer Wins') #*72
               elif dealer_flag==1:
                   raise ValueError ('You beat the dealer!') #* 82

       self._sum_cards = res
       return 0

    def get_sum_of_cards(self):
        return self._sum_cards

    def display(self, dealer=0):
        if dealer==0:
            print(f'You are currently at: {self.get_sum_of_cards()}')
        else:
            print(f'Dealer is currently at: {self.get_sum_of_cards()}')

        print('with the hand', end= '   ')
        for card in self._cards:
            print(f'[{card._number}, {card._sign}]', end= ',')


class Dealer(Player):
    def start_play(self, my_game_deck, player):
        while self.get_sum_of_cards() <17:
            print('\n')
            self.display(1)
            print('\n')
            self.hitting(my_game_deck, 1)

        if self._blackjack_found == 1 and player._blackjack_found == 1:
            return 'Game Tie'
        elif self._blackjack_found == 1:
            return 'Dealer Wins'         #*
        elif player._blackjack_found == 1:
            return 'You beat the dealer!' #* 96
        elif self._blackjack_found == 0 and player._blackjack_found == 0:
            if self.get_sum_of_cards() > player.get_sum_of_cards():
                return 'Dealer Wins'
            elif player.get_sum_of_cards() > self.get_sum_of_cards():
                return 'You beat the dealer!' #* 106
            elif player.get_sum_of_cards() == self.get_sum_of_cards():
                return 'Game Tie'

    def get_dealer_input(self, my_game_deck, player):
        print(self.start_play(my_game_deck, player))

def get_two_cards_each(player, dealer, my_game_deck):
    player.hitting(my_game_deck,0,1)
    player.hitting(my_game_deck,0,1)
    dealer.hitting(my_game_deck,1,1)
    dealer.hitting(my_game_deck,1,1)

def get_user_input(player, my_game_deck):
    user_input='1'

    while user_input =='1':
        if player._no_of_cards > 0:
            print()
            player.display()
            print()
        user_input = input(f'\nHit or Stay? (Hit = 1, Stay =0): ')
        if user_input == '1':
            player.hitting(my_game_deck)


def main():
    my_game_deck = Card_deck()
    my_game_deck.fill_deck()
    my_game_deck.shuffle()
    player = Player()
    dealer = Dealer()
    get_two_cards_each(player, dealer, my_game_deck)
    try:
        get_user_input(player, my_game_deck)
        dealer.get_dealer_input(my_game_deck, player)
    except ValueError as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

if __name__ == '__main__':
    main()