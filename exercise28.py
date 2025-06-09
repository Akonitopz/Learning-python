#Calculate sum of all numbers from 1 to a given number

num = int(input("Please enter a number: "))
sum = 0
for i in range(1, num + 1, 1):
    sum = sum + i
    i = sum

print(f"Sum is: {i}")