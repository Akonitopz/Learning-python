def Addition(num1, num2):
    return f"\n{num1} + {num2} = {num1 + num2}"

def Subtraction(num1, num2):
    return f"\n{num1} - {num2} = {num1 - num2}"

def Multiplication(num1, num2):
    return f"\n{num1} x {num2} = {num1 * num2}"

def Division(num1, num2):
    if num2 == 0:
        return "\nDivision by zero is not allowed"
    return f"\n{num1} / {num2} = {num1 / num2}"

def main_menu(num1, num2):
    while True:
        print("\nPlease select an Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit Program")
        choice = int(input("Please input here: "))
        if choice == 1:
            print(Addition(num1, num2))
        elif choice == 2:
            print(Subtraction(num1, num2))
        elif choice == 3:
            print(Multiplication(num1, num2))
        elif choice == 4:
            print(Division(num1, num2))
        elif choice == 5:
            print("Thank you, Have a great day!")
            break
        else:
            print("Invalid input! Would you like try again?")
            choice1 = input("Input Here: ")
            if choice1 in ['Y', 'y']:
                continue
            else:
                print("Code will now exit. Thank you!")
            break

def Input_Check():
    while True:
        try:
            num1 = int(input("Please input first number: "))
            num2 = int(input("Please input second number: "))
        except ValueError:
            print("Error! Please use integers only and avoid characters.")
            continue
        else:
            main_menu(num1, num2)
            break

Input_Check()
