class BankAccount:
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Account name: {self.account_name}\nNew Balance: {self.balance}"
        else:
            return "Amount must be greater than zero!"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        elif amount > 0:
            self.balance -= amount
            return f"Account name: {self.account_name}\nNew Balance: {self.balance}"
        else:
            return "Amount must be greater than zero!"

    def check_balance(self):
        return f"Account name: {self.account_name}\nBalance: {self.balance}"


main = BankAccount("Kristopher")
print(main.check_balance())

bool_num = True
while bool_num:
    choice = input("Please choose an operation:\n1.Deposit\n2.Withdraw\nInput here: ")

    if choice == '1':
        amount = int(input("Please enter the amount you wish to deposit: "))
        print(main.deposit(amount))

    elif choice == '2':
        amount = int(input("Please enter the amount you wish to withdraw: "))
        print(main.withdraw(amount))

    else:
        print("INVALID CHOICE! The program will now close.")
        break

    
    choice1 = input("Would you like to continue? (Y/N): ").strip().lower()
    print("\n")

    if choice1 != 'y': 
        print("Thank you! Have a great day!")
        bool_num = False
