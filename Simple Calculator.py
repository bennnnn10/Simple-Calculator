#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

def calculator():
    try:
        #   Prompting the user to select an operation
        print("Please choose an operation")
        print("Addition(1), Subtraction(2), Multiplication(3), or Division(4)")
        #   Obtain user input for the operation
        math_operation = int(input("Choose one of the four math operations (1-4): "))
#   Collect two numbers from the user
#   Execute an operation based on user input
#   Print the result
    #   Handle runtime errors
    #   Handle division by zero error
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
#   Request if the user wants to make another computation.
#   If the user does not want to execute further calculation, the function should be closed.