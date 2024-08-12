

from art import logo

from art import vs

from game_data import data

import random

print(logo)

def select_record():
    index = random.randint(1,len(data))
    return data[index]

def print_record(rec,label):
    if label == "A":
        print(f"Compare A: {rec['name']}, a {rec['description']}, from {rec['country']}")
    else:
        print(f"Against B: {rec['name']}, a {rec['description']}, from {rec['country']}")


def higher_lower_game():
    to_continue = True

    recordA = select_record()
    recordB = select_record()

    score = 0

    while(to_continue):
        print_record(recordA, "A")
        print(vs)
        print_record(recordB, "B")
        user_choice = input("Who has more followers: Type 'A' or 'B'.")
        if (user_choice == 'A' and recordA['follower_count'] > recordB['follower_count']) or (user_choice == 'B' and recordB['follower_count'] > recordA['follower_count']):
            score += 1
            print(f"You're right! Current score: {score}.")
            recordA = recordB
            recordB = select_record()
        else:
            print(f"Sorry that's wrong. Final score: {score}.")
            to_continue = False

higher_lower_game()

