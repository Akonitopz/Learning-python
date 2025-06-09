#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
#Also, it must return both addition and subtraction in a single return call.

def calculation(num1, num2):
    return num1 + num2, num1 - num2 


ans = calculation(40,10)
print(ans)