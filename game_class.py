import player_class


class Game:
    def run_game(self):
        print("Welcome in hangman game!")
        user_name = input("Type your name\n")
        new_player = player_class.Player(user_name)
        print(new_player.name)


if __name__ == '__main__':
    Game().run_game()
