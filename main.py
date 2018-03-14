import game_class


def main():
    new_game = game_class.Game()
    new_game.run()
    # nie dziala jeszcze:
    #  jak jest wrong answer to nie moze printowac zyc
    # jak wezmiesz play again to nie drukuje nowego wyrazu tylko caly czas ten user_name
    # jak wezmiesz nie chce play again to wychodzi tylko z jednej petli
    # walidacja do wszystkich inputow czy zamiast literki nie wchodzi tez int?
    # wchodzi int a powinno tylko pisac ze to nie literka i nie odejmowac zycia
    # nie printuj calego seta tylko jego zawartosci
    # gdy user nie zgadnie 5 razy to wyswietl jakie bylo poprawne slowo


if __name__ == '__main__':
    main()
