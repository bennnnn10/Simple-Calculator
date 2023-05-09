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
        print("Please choose an operation")
        print("Addition(1), Subtraction(2), Multiplication(3), or Division(4)")

        #   Obtain user input for the operation
        math_operation = int(input("Choose one of the four math operations (1-4): "))

        #   Collect two numbers from the user
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        #   Execute an operation based on user input
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
            print("Invalid operation number.")
            calculator()

        #   Print the result
        print("The result is:", result)

        #   Request if the user wants to make another computation.
        try_again = input("Would you like to make another calculation? (y/n): ")

        if try_again.lower() == "y":
            calculator()
        else:
        #   If the user does not want to execute further calculation, the function should be closed.
            print("Thank you")

    #   Handle runtime errors
    #   Handle division by zero error
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        calculator()
    #   Handle invalid input error
    except ValueError:
        print("Error: Invalid input.")
        calculator()

calculator()