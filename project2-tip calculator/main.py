#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Hope you enjoyed the dinner. We will now calculate the tip.")

bill = float(input("what is the total bill? $"))

num_people = int(input("How many people were there for dinner?"))

tip = int(input("What percent tip would you like to give?"))

tip_percent = tip / 100

tip_multiplier = 1 + tip_percent

your_share = (bill / num_people) * tip_multiplier

# print(f"You need to pay ${round(your_share,2)}.")

final_amt_formatted = "{:.2f}".format(your_share)

print(f"You need to pay ${final_amt_formatted}.")
