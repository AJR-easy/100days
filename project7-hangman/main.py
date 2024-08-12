
# list to string: str = ''.join(lst)
# string to list: lst = str.split(", ",1)


import random


from hangman_words import word_list
#word_list = ["meerkat", "mongoose", "giraffe", "baboon", "gorilla", "lion"]



from hangman_art import logo, stages
print(logo)

chosen_word = random.choice(word_list)

lives = 6

print(chosen_word)

word_length = len(chosen_word)

displayed_word = []

for i in range(1,word_length+1):
    displayed_word.append("_")

print(displayed_word)

while ("_" in displayed_word) and (lives != 0):

    guessed_letter = input("Guess a letter in the word.").lower()

    flag = False

    for i in range(word_length):
        if(chosen_word[i] == guessed_letter):
            flag = True
            displayed_word[i] = guessed_letter

    print(displayed_word)

    if flag == False:
        lives -= 1
        print (stages[lives])
    elif "_" not in displayed_word:
        print("You win!")
        exit()

print("You lose!")

#if(chosen_word.find(guessed_letter)==-1):
#    print("Wrong guess.")
#else:
#    print("Right guess.")
