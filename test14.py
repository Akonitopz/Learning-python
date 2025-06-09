#factorial recursion

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Please enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")