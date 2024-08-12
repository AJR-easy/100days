
from art import logo

def division(first_num,second_num):
    result = first_num / second_num
    print(f"{first_num} / {second_num} = {result}.")
    return result


def multiplication(first_num,second_num):
    result = first_num * second_num
    print(f"{first_num} * {second_num} = {result}.")
    return result


def addition(first_num,second_num):
    result = first_num + second_num
    print(f"{first_num} + {second_num} = {result}.")
    return result


def subtraction(first_num,second_num):
    result = first_num - second_num
    print(f"{first_num} - {second_num} = {result}.")
    return result


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():

    print(logo)
    
    first_num = float(input("What is the first number?"))

    operator = input("Pick an operation: + - * /")

    second_num = float(input("What is the next number?"))

    should_continue = "y"


    while(should_continue == "y"):
        function = operations[operator]
        first_num = function(first_num,second_num)
        should_continue = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation:")
        if should_continue == "y":
            operator = input("Pick an operation: + - * /")
            second_num = float(input("What is the next number?"))
        else:
            calculator()


calculator()
# while(should_continue == "y"):
#     if operator == "+":
#         first_num = addition(first_num, second_num)
#     elif operator == "-"
#         first_num = subtraction(first_num, second_num)
#     elif operator == "*"
#         first_num = multiplication(first_num,second_num)
#     elif operator == "/"
#         first_num = division(first_num,second_num)
#     should_continue = input("Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation:")
