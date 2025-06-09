#Print multiplication table of a given number
num = int(input("Please enter a number: "))
print(f"Multiplication table for number {num}:")
for i in range(1, 11):
    prod = i * num
    print(f"{num} x {i}: {prod}")