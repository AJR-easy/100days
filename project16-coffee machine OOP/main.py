from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

def operate_machine():

    to_continue = True

    while to_continue == True:
        choice = input(f"What would you like {my_menu.get_items()} a 'report' or do you want to turn 'off' the machine?")
        if choice == 'off':
            to_continue = False
        elif choice == 'report':
            my_coffee_maker.report()
            my_machine.report()
        else:
            my_drink = my_menu.find_drink(choice)
            if(my_coffee_maker.is_resource_sufficient(my_drink) and my_machine.make_payment(my_drink.cost)):
                my_coffee_maker.make_coffee(my_drink)
            else:
                to_continue = False


operate_machine()