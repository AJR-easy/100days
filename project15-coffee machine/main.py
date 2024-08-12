
from helper import MENU

from helper import SUPPLY

from helper import CASH

from helper import coffee_emoji

def print_report():
    for item in SUPPLY:
        print(f"{item}: {SUPPLY[item]}")
    print(f"current cash: {CASH}")

def is_sufficient(money_paid, choice):
    try:
        bill = MENU[choice]["cost"]
    except:
        print("Your choice is not available in the menu.")
    if bill > money_paid:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        return True

def charge_customer(money_paid, choice):
    global CASH
    bill = MENU[choice]["cost"]
    change = money_paid - bill
    print(f"Here is ${change} in change.")
    print(f"Here is your {choice} {coffee_emoji}. Enjoy!")
    CASH += bill

def check_resources(choice):
    try:
        for item in SUPPLY:
            if SUPPLY[item] < MENU[choice]["ingredients"][item]:
                print(f"Insufficient {item}. Please refill.")
                return False
        return True
    except:
        print("Your choice is not available in the menu.")



def update_resources(choice):
    for item in SUPPLY:
        SUPPLY[item] -=  MENU[choice]["ingredients"][item]



def accept_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies?: "))
    money_paid = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    money_paid = round(money_paid,2)
    return money_paid


def operate_machine():

    to_continue = True

    while to_continue == True:
        choice = input("What would you like 'espresso' / 'latte' / 'cappuccino' a 'report' or do you want to turn 'off' the machine?")
        if choice == 'off':
            to_continue = False
        elif choice == 'report':
            print_report()
        else:
            if(check_resources(choice)):
                money_paid = accept_money()
                if(is_sufficient(money_paid,choice)):
                    update_resources(choice)
                    charge_customer(money_paid, choice)
                else:
                    to_continue = False
            else:
                to_continue = False

#print(MENU["espresso"]["ingredients"].items())

operate_machine()
