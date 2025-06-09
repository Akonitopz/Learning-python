class BankAccount:
    
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Account name: {self.account_name}\nNew Balance: ${self.balance}"
        return "Amount must be greater than zero!"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        elif amount > 0:
            self.balance -= amount
            return f"Account name: {self.account_name}\nNew Balance: ${self.balance}"
        return "Amount must be greater than zero!"

    def check_balance(self):
        return f"Account name: {self.account_name}\nBalance: ${self.balance}"


class BankOperations:
    
    def __init__(self):
        self.account = None  # No account created yet

    def create_account(self):
    
        name = input("Enter your name to create an account: ")
        self.account = BankAccount(name)
        print(f"Account for {name} created successfully!\n")

    def main_menu(self):
        """Displays menu and processes user choices."""
        if self.account is None:
            print("No account found. Please create one first.")
            self.create_account()

        while True:
            print("\nPlease choose an operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Input here: ").strip()

            if choice == '1':
                amount = int(input("Enter amount to deposit: "))
                print(self.account.deposit(amount))

            elif choice == '2':
                amount = int(input("Enter amount to withdraw: "))
                print(self.account.withdraw(amount))

            elif choice == '3':
                print(self.account.check_balance())

            elif choice == '4':
                print("Thank you! Have a great day!")
                break

            else:
                print("Invalid choice! Please try again.")



bank_app = BankOperations()
bank_app.main_menu()
