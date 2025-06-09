#Display Fibonacci series up to 10 terms.
class Fibonacci:
    def __init__(self, num1, num2, sum):
        self.num1 = num1
        self.num2 = num2
        self.sum = sum

    def fibo(self, reps):
        if reps > 0:
            for i in range(self.num1 , reps):
                self.sum = self.num1 + self.num2
                print(self.sum)
                self.num1 , self.num2 = self.sum , self.num1


main = Fibonacci(int(input("Please enter first number: ")) , int(input("Please enter second number: ")) , 0)
main.fibo(int(input("Please enter repititions: ")))

                
            