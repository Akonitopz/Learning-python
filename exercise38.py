#Find the factorial of a given number

class Factorial:
    def __init__(self , num):
        self.num = num

    def Product(self):
        num1 = self.num
        if self.num < 0:
            print("Error! The value entered must not be below zero.")
            
        elif self.num == 0:
            return f"The factorrial of {num1} is: 1"
        
        else:
            for i in range(self.num, 1, -1):
                self.num *= i - 1

            else:
                return f"The factorial of {num1} is: {self.num}"
        

main = Factorial(int(input("Please enter the number for factorial: ")))
print(main.Product())
