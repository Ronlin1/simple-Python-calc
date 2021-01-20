# Simple Python CLI Calc

# Addition
def add(x, y):
    return x + y


# Subtraction
def subtract(x, y):
    return x - y


# Division
def divide(x, y):
    return x / y


# Multiplication
def multiply(x, y):
    return x * y


# Finding Power of a number
def power(x, y):
    return x ** y


# Floor Division
def floor_division(x, y):
    return x // y


# Printing an initial statement
print("<<<---- Select an operation! ---->>>")
print("\n1.Add", "\n2.Subtract", "\n3.Divide", "\n4.Multiply", "\n5.Power", "\n6.Floor Division")

# We Want to keep this in a loop that contionously asks for an input from the user;
while True:
    choice = input("Enter Choice (1,2,3,4,5 0r 6): ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the Second Number: "))
        if choice == '1':
            print("\n---> The Answer is: ", add(num1, num2))
        elif choice == '2':
            print("\n---> The Answer is: ", subtract(num1, num2))
        elif choice == '3':
            print("\n---> The Answer is: ", divide(num1, num2))
        elif choice == '4':
            print("\n---> The Answer is: ", multiply(num1, num2))
        elif choice == '5':
            print("\n---> The Answer is: ", power(num1, num2))
        elif choice == '6':
            print("\n---> The Answer is: ", floor_division(num1, num2))
        break
    else:
        print("Invalid Input! Try Again!")

#  HOPE YOU ENJOY IT!
