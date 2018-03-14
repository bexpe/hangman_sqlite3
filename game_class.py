import player_class
import sqlraw
import random


class Game:

    def __init__(self):
        self.game_id = 1

    def run(self):
        while True:
            words = ['sun', 'holidays', 'summertime', 'fun', 'wind']
            print("Welcome in hangman game!")
            user_name = input("Type your name\n")
            new_player = player_class.Player(user_name)
            secret = random.choice(words)
            print(secret)
            correct_guesses = set()
            incorrect_guesses = set()

            while True:
                print("Lives: " + str(new_player.lives))
                guess = input("Type a letter u want to guess:\n")

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
                        sqlraw.connect_to_db(new_player)
                        play_again = input("Do you want to play again? y/n")
                        if play_again.lower() == "y":
                            continue
                        elif play_again.lower() == "n":
                            break
                        else:
                            print("Wrong answer")
                            continue
                else:
                    # incorrect guess!
                    incorrect_guesses.add(guess)
                    print('Oops, incorrect guess!')
                    if new_player.lives > 1:
                        new_player.lives -= 1
                    else:
                        print("Game over")
                        play_again = input("Do you want to play again? y/n")
                        if play_again.lower() == "y":
                            continue
                        elif play_again.lower() == "n":
                            break
                        else:
                            print("Wrong answer")
                            continue
                print("Correct guesses: " + str(correct_guesses))
                print("Incorrect guesses: " + str(incorrect_guesses))
