
import os

from art import logo


absolutely_unused_variable = os.system("clear")

print(logo)

can_continue = True

biddict = {}

while can_continue:
    bidder_name = input("What is your name?")
    bidder_price = int(input("What is your bid?"))
    biddict[bidder_name] = bidder_price
    if(input("Do we have anyone else who wants to bid?").lower() !="yes"):
        can_continue = False
    elif:
        absolutely_unused_variable = os.system("clear")

maximum_bid = 0

highest_bidder = ""

for key in biddict:
    if biddict[key] > maximum_bid:
        maximum_bid = biddict[key]
        highest_bidder = key

print(f"The highest bidder is {highest_bidder} with a bid of ${maximum_bid}.")
