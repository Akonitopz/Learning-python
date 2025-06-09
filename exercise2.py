# Write a Python code to iterate the first 10 numbers, and in each iteration, 
# print the sum of the current and previous number.
print("printing current and previous number and their sum in a range(10)")
prevnum = 0

for num in range(10):
    print("Current number:", num, "Previous numeber:", prevnum, "sum:",num + prevnum)
    prevnum = num