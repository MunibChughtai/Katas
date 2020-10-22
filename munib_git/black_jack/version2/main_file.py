from bj_game import Bj_game

def main():
    black_jack=Bj_game()
    black_jack.prepare_for_game()
    result = black_jack.start_game()
    print(result)

if __name__ == '__main__':
    main()