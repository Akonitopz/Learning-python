class BankOperations:
    def __init__(self, account_name, balance = 0):
        self.account_name = account_name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        return f"\nName: {self.account_name}\nNew balance: {self.balance}"
        
    def Withdraw(self, amount):
        self.balance -= amount
        return f"\nName: {self.account_name}\nNew balance: {self.balance}"
        
    def check_balance(self):
        return f"\nName: {self.account_name}\nNew balance: {self.balance}"
    

class BankAccount:
    def __init__(self):
        self.account = None  #No account created yet

    def create_account(self):
        name = input("\nPlease enter your name to create an account: ")
        self.account = BankOperations(name)
        print("Account Successfully created!")
        print(f"\nName: {self.account.account_name}\nNew balance: {self.account.balance}")

    def main_menu(self):
        if self.account is None:
            print("No account found! please create an account first.")
            self.create_account()
        
        while True:
                print("\nPlease enter a choice:\n1.Deposit\n2.Withdraw\n3.Check Balance\n4. Exit Application.")
                choice = int(input("Input choice here: "))

                if choice == 1:
                    amount = int(input("Please input the amount you wish to deposite: "))
                    if amount <= 0:
                        print("Error! Please enter an amount greater than zero!")
                        continue
                    else:
                        print(self.account.Deposit(amount))

                elif choice == 2:
                    amount = int(input("Please input the amount you wish to withdraw: "))
                    if amount > self.account.balance:
                        print("Your account balance is not sufficient! Please deposite first.")
                        continue
                    else:
                        print(self.account.Withdraw(amount))

                elif choice == 3:
                    print(self.account.check_balance())
                
                elif choice == 4:
                    print("Thank you for banking with us!")
                    break

                else:
                    print("Invalid choice! Please try again.")
                    continue
                

bank_app = BankAccount()
bank_app.main_menu()

