from bj_game import Bj_game

def main():
    black_jack=Bj_game()
    black_jack._deck.deck_setup()
    black_jack.start_game()

if __name__ == '__main__':
    main()