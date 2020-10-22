import pytest

from card import Card
from deck import Deck
from card_set import Card_set
from player import Player
from bj_game import Bj_game

# As this function is used to display the card value at every tep, so i think this is imp test
def test_card_initialization_and_display():
    c1 = Card('5', 'HEART')
    assert c1.display_card() == "['5', 'HEART']"

# checking random function is working, this may fail as first element may remain unchanged
def test_is_deck_shuffle_working():
    my_game_deck = Deck()
    my_game_deck.deck_setup()
    assert my_game_deck.pick_next_card().display_card() != "[2, 'Heart']"

def test1_check_black_jack():
    my_game_deck = Deck(['Jack','Ace'],['Heart'])
    my_game_deck._fill_deck()
    player = Player('Player')
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    assert player._card_set.get_score() == 'Black Jack!'

def test1_check_card_set_score():
    my_game_deck = Deck([2,3,'Jack','Ace'],['Heart'])
    my_game_deck._fill_deck()
    player = Player('Player')
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    assert player._card_set.get_score() == 16

def test2_check_card_set_score():
    my_game_deck = Deck([4,2,3,'Jack','Ace'],['Heart'])
    my_game_deck._fill_deck()
    player = Player('Player')
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    assert player._card_set.get_score() == 20


def test1_check_bust():
    my_game_deck = Deck([6,2,3,'Jack','Ace'],['Heart'])
    my_game_deck._fill_deck()
    player = Player('Player')
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    assert player._card_set.get_score() == 'Bust!'

def test1_check_bust():
    my_game_deck = Deck([6,2,3,'Jack','Ace'],['Heart'])
    my_game_deck._fill_deck()
    player = Player('Player')
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    player.hit(my_game_deck, player._name)
    assert player._card_set.get_score() == 'Bust!'

def test1_check_player_dealer_game_player_busts():
    my_game_deck = Deck([6, 2, 3, 'Jack', 9], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck

    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'Dealer wins!'


def test2_check_player_dealer_game_dealer_busts():
    my_game_deck = Deck([3,5,8, 6, 'Queen', 'Jack', 9], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'You beat the dealer!'

def test3_check_player_dealer_game_player_blackjack():
    my_game_deck = Deck([3,5,8, 7, 'Queen',2, 'Jack', 9], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'You beat the dealer!'

def test4_check_player_dealer_game_dealer_blackjack():
    my_game_deck = Deck([3,5,8, 9, 'Queen',2, 'Jack', 9], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'Dealer wins!'

def test5_check_player_dealer_game_both_blackjack():
    my_game_deck = Deck([3,5,8, 9, 'Queen',2, 'Jack', 9,2], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'Its a Tie!'

def test6_check_player_dealer_game_player_high_score():
    my_game_deck = Deck([3,5,8, 6, 'Queen',2, 'Jack', 9,'Ace'], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'You beat the dealer!'

def test7_check_player_dealer_game_dealer_high_score():
    my_game_deck = Deck([3,5,8, 6, 'Queen',2, 'Jack', 7], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'Dealer wins!'

def test8_check_player_dealer_game_tie_score():
    my_game_deck = Deck([3,5,8, 5, 'Queen',2, 'Jack', 7], ['Heart'])
    my_game_deck._fill_deck()
    bj_game = Bj_game()
    bj_game._deck = my_game_deck
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    bj_game._player.hit(bj_game._deck, bj_game._player._name)
    assert bj_game.start_game(1) == 'Its a Tie!'