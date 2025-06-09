#Write a Python program to count the total number of digits in a number using a while loop.

num = 758692547411
num1 = num
counter = 0
while num1 > 0:
    counter += 1
    num1 = num1 // 10

print(f"The number of digits inside {num} is: {counter}")