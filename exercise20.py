#Accept a list of 5 float numbers as an input from the user
num = []
for x in range(0,5,1):
    items = float(input(f"Please enter a number at index {x+1}: "))
    num.append(items)


print(f"Here's your list: {num}")

