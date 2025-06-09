#Print all prime numbers within a range
import math

start = int(input("Please enter the start number: "))
end = int(input("Please enter the end number: "))
print("Prime numbers between", start, "and", end, "are:")

if start < 2:
    start = 2

for num in range(start, end + 1):
    if num == 2:
        print(num)
        continue
    if num % 2 == 0:
        continue

    prime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
