from art import game_logo

import random

EASY_TURNS = 10
HARD_TURNS = 5

def set_turns():
    level = input("Choose a difficulty level: 'easy' or 'hard':")
    if level == "easy":
        allowed_guesses = EASY_TURNS
    elif level == "hard":
        allowed_guesses = HARD_TURNS
    else:
        print("Invalid input.")
        eixt()
    return allowed_guesses


def guessing_game(allowed_guesses):
    count = allowed_guesses
    for i in range(allowed_guesses):
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess."))
        if my_number > guess:
            count -= 1
            print(f"Too low. \nGuess Again. \n")
        elif my_number < guess:
            count -= 1
            print(f"Too high. \nGuess Again. \n")
        else:
            print("You guessed the right number. Congrats!")
            exit()
    print("You coundn't guess the right number. You lose.")

print(game_logo)

print ("Welcome to the guessing game.\n")

print("I am thinking of a number between 1 and 100. \n")

my_number = random.randint(1,100)

print(f"The number to be guessed is {my_number}.")


allowed_guesses = set_turns()

guessing_game(allowed_guesses)

