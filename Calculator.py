# Calculator.py

# This is a calculator program that performs the basic operations of:
# addition, subtraction, multiplication, and division operations. The function can also
# determine if the first numbers is less than, greater than or equal to the second number.

def add(num1, num2):  # Returns num1 plus num2
    return num1 + num2


def sub(num1, num2):  # Returns num1 minus num2
    return num1 - num2


def mul(num1, num2):  # Returns num1 times num2
    return num1 * num2


def div(num1, num2):  # Returns num1 divided by num2
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Please try again. \t Can not divide by 0")


def run_operation(operation, num1, num2):
    # Determines the operation to be run
    if operation == 1:
        print("Adding", num1, "+", num2, "which equals:")
        print(add(num1, num2))
    elif operation == 2:
        print("Subtracting", num1, "-", num2, "which equals:")
        print(sub(num1, num2))
    elif operation == 3:
        print("Multiplying", num1, "*", num2, "which equals:")
        print(mul(num1, num2))
    elif operation == 4:
        print("Dividing", num1, "/", num2, "which equals:")
        print(div(num1, num2))
    elif operation == 5:
        if num1 < num2:
            print("Comparing", num1, "with", num2)
            print(num1, "is less than", num2)
    elif operation == 6:
        if num1 > num2:
            print("Comparing", num1, "with", num2)
            print(num1, "is greater than", num2)
    elif operation == 7:
        if num1 == num2:
            print("Comparing", num1, "with", num2)
            print(num1, "is equal to", num2)
    else:
        print("I don't understand. Please try again")


def main():
    # Allows user to run operations with two numbers
    valid_input = False
    while not valid_input:
        # Getting user input and turning into integer
        try:
            print("This is a calculator that performs basic operations,")
            print("and has the ability to compare number 1 to number 2. \n")

            print("Enter 2 numbers below:")
            num1 = int(input("What is number 1?: "))
            num2 = int(input("What is number 2?: "))

            print("\nYou entered", num1, "for the first number.")
            print("You entered", num2, "for second number.\n")

            operation = int(input("What do you want to do? \n 1. add, 2. subtract, 3. multiply, 4. divide,"
                                  " 5. Number 1 \n Less than Number 2?, 6. Number 1 Greater Than Number 2? \n or "
                                  "7. Number 1 Equals Number 2."
                                  "\n\n Enter number: "))
            valid_input = True
        except ValueError:  # Handles the ValueError Exception
            print("Invalid input. Please try again.")
            continue
        except:
            print("Unknown error. Please try again")
            continue
        run_operation(operation, num1, num2)


if __name__ == "__main__":
    main()