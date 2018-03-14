import game_class


def main():
    while True:
        new_game = game_class.Game()
        new_game.run()
    # nie dziala jeszcze:
    # w bazie nie zapisuje sie trwale wynik


if __name__ == '__main__':
    main()
