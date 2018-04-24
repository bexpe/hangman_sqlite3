import model.player.player_class
import controller.sqlraw
import random


class Game:

    def __init__(self):
        self.game_id = 1

    def run(self):
        words = ['sun', 'holidays', 'summertime', 'fun', 'wind']
        score = 0
        lives = 5
        print("Welcome in hangman game!")
        user_name = input("Type your name\n")
        new_player = model.player.player_class.Player([score, user_name, lives])
        secret = random.choice(words)
        print(secret)
        correct_guesses = set()
        incorrect_guesses = set()

        while True:
            print("\nLives: " + str(new_player.lives))
            guess = input("Type a letter u want to guess:\n")
            if guess.isdigit():
                print("You cant type a number")
                continue

            if guess in correct_guesses & incorrect_guesses:
                print('You already guessed that letter')

            elif guess in secret:
                # correct guess!
                correct_guesses.add(guess)
                display_word = ''.join(char if char in correct_guesses else '_' for char in secret)
                new_player.score += 10
                print(display_word)
                if display_word == secret:
                    print("Winner!!!")
                    controller.sqlraw.connect_to_db(new_player)
                    play_again = input("Do you want to play again? y/n\n")
                    if play_again.lower() == "y":
                        break
                    elif play_again.lower() == "n":
                        quit()
                    else:
                        print("Wrong answer\n")
                        quit()
            else:
                # incorrect guess!
                incorrect_guesses.add(guess)
                print('Oops, incorrect guess!\n')
                if new_player.lives > 1:
                    new_player.lives -= 1
                else:
                    print("\nThe correct answer was: " + secret)
                    print("\nGame over")
                    play_again = input("Do you want to play again? y/n\n")
                    if play_again.lower() == "y":
                        break
                    elif play_again.lower() == "n":
                        quit()
                    else:
                        print("Wrong answer\n")
                        quit()
            print("Correct guesses: ", end=" ")
            for i in correct_guesses:
                print(i, end=" ")
            print(" ")
            print("Incorrect guesses: ", end=" ")
            for i in incorrect_guesses:
                print(i, end=" ")
