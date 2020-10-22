import pytest

from card import Card
from deck import Deck
from card_set import Card_set
from player import Player

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