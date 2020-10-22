import pytest

from black_jack import Card
from black_jack import Card_deck
from black_jack import Player
from black_jack import Dealer
from black_jack import *

#@pytest.fixture()
#def classInitialized():
#    mycard = Card()
    #return ps
#    None

#def test_positive_annualSal(classInitialized):
#    classInitialized.setAnnualSal(200000)
#    assert classInitialized.getAnnualSal() == 200000

def test1_card_initialization():
    c1= Card('5', 'HEART')
    assert c1.card_value() == "['5', 'HEART']"

def test_deck_total_number_of_cards():
    my_game_deck = Card_deck()
    my_game_deck.fill_deck()
    my_game_deck.shuffle()
    assert my_game_deck.total_no_of_cards() == 52

def test_deck_shuffle():
    my_game_deck = Card_deck()
    my_game_deck.fill_deck()
    my_game_deck.shuffle()
    assert my_game_deck.pop_deck().card_value() != "['K', 'Diamond']"


def test_player_initialized_card_numbers():
    my_game_deck = Card_deck()
    my_game_deck.fill_deck()
    my_game_deck.shuffle()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    assert player.get_number_of_cards()==2

def test1_sum_of_cards():
    my_game_deck = Card_deck(['A', '4'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    assert player.get_sum_of_cards() == 15

def test2_sum_of_cards():
    my_game_deck = Card_deck(['A', '4', 'Q'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    assert player.get_sum_of_cards() == 15

def test3_sum_of_cards():
    my_game_deck = Card_deck(['A', '4', 'Q', '2', '3'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    assert player.get_sum_of_cards() == 20

def test1_lose_game_player_went_over():
        my_game_deck = Card_deck(['10', '3', '9'], ['Heart'])
        my_game_deck.fill_deck()
        player = Player()
        player.hitting(my_game_deck)
        player.hitting(my_game_deck)
        with pytest.raises(ValueError) as e:
            player.hitting(my_game_deck)
        assert str(e.value) == 'Dealer Wins'


def test2_lose_game_dealer_found_black_jack():
    my_game_deck = Card_deck(['9', '2', '10', '3','6', 'A'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'Dealer Wins'

def test3_lose_game_dealer_closer_to_21():
    my_game_deck = Card_deck(['9', '10', '6', '5', '4', '3'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'Dealer Wins'

def test1_win_game_dealer_went_over():
    my_game_deck = Card_deck(['10', '3', '9', 'A', '4', 'Q', '2', '3'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    with pytest.raises(ValueError) as e:
        dealer.start_play(my_game_deck, player)
    assert str(e.value) == 'You beat the dealer!'

def test2_win_game_black_jack_found():
    my_game_deck = Card_deck(['A', '8', '5', '4', '3', '2', '9', '10'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'You beat the dealer!'

def test3_win_game_player_closer_to_21():
    my_game_deck = Card_deck(['6', '5', '4', '3', '9', '10'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'You beat the dealer!'

def test1_tie_game_black_jack_found():
    my_game_deck = Card_deck(['A', '2', '8', '2', '9', '10'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'Game Tie'

def test2_tie_game_black_jack_not_found():
    my_game_deck = Card_deck(['2', '7', '9', '8', '10'], ['Heart'])
    my_game_deck.fill_deck()
    player = Player()
    player.hitting(my_game_deck)
    player.hitting(my_game_deck)
    dealer = Dealer()
    assert dealer.start_play(my_game_deck, player) == 'Game Tie'