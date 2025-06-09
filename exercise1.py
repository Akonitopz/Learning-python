# Given two integer numbers, write a Python code to return their product only if the product 
# is equal to or lower than 1000. Otherwise, return their sum.
num1 = float(input("Please input first number: "))
num2 = float(input("Please input first number: "))
prod = num1 * num2
sum = num1 + num2
if prod <= 1000:
    print("The product is:", prod)

else:
    print("The sum is: ", sum)