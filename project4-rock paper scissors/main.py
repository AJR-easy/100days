
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

listofimages = [rock,paper,scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"You chose {listofimages[your_choice]}")

computer_choice = random.randint(0,2)

print(f"Computer chose {listofimages[computer_choice]}")

if (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1):
    print("You win!")
elif (computer_choice == 0 and your_choice == 2) or (computer_choice == 1 and your_choice == 0) or (computer_choice == 2 and your_choice == 1):
    print("Computer wins!")
else:
    print("It's a draw.")