# Write a Python code to print the following number pattern using a loop.
rows = 5

for i in range(rows + 1):
    for j in range(i):
        print(j + 1, end= ' ')
    print(" ")