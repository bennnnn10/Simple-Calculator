#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

from termcolor import colored
import pyfiglet

#Header
def colored_ascii(text, color):
    ascii_art = pyfiglet.figlet_format(text, font="speed", justify="center")
    colored_ascii_art = colored(ascii_art, color)
    print(colored_ascii_art)

print("✹" * 78)
colored_ascii("Calculator", "cyan")
print(colored("Press <enter> to start!".center(75), "yellow"))
input("".center(39))

def calculator():
    try:
        #   Prompting the user to select an operation
        print("✹" * 78)
        print("\n")
        print(colored("Please choose an operation\n".center(75), "yellow"))
        print(colored("Addition(1), Subtraction(2), Multiplication(3), or Division(4)\n".center(75), "yellow"))

        #   Obtain user input for the operation
        print(colored("Choose one of the four math operations (1-4): ".center(75), "cyan"))
        math_operation = int(input("".center(37)))
        print("\n")

        #   Collect two numbers from the user
        first_number = float(input("\033[;1;3mEnter the first number: \033[0m"))
        second_number = float(input("\033[;1;3mEnter the second number: \033[0m"))

        #   Execute an operation based on user input
        result = None  # Initialize result with a default value
        if math_operation == 1:
            result = first_number + second_number
        elif math_operation == 2:
            result = first_number - second_number
        elif math_operation == 3:
            result = first_number * second_number
        elif math_operation == 4:
            result = first_number / second_number
        else:
            #   Deal with an invalid operation number
            print()
            print(colored("Invalid operation number.\n".center(75), "red"))
            calculator()

        #   Print the result
        print()
        print("\033[;1;92;3m➺   The result is", result, "\033[0m")

        #   Request if the user wants to make another computation.
        print("\n")
        try_again = input(colored("Would you like to make another calculation? (y/n): ", "yellow"))
        print("\n")

        if try_again.lower() == "y":
            calculator()
        else:
        #   If the user does not want to execute further calculation, the function should be closed.
            print("✹" * 78)
            print("\n")
            print(pyfiglet.figlet_format("Thank you!".center(11), justify="center"))
            exit()

    #   Handle runtime errors
    #   Handle division by zero error
    except ZeroDivisionError:
        print()
        print(colored("Error: Cannot divide by zero.\n".center(75), "red"))
        calculator()
    #   Handle invalid input error
    except ValueError:
        print()    
        print(colored("Error: Invalid input.\n".center(75), "red"))
        calculator()

calculator()