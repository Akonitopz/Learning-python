average = 0
sum = 0
for i in range(3):
    print(f"Student number: {i+1}")
    average = 0
    for i in range(3):
        sum = float(input(f"Please input grade no {i + 1}: "))
        average += sum
    else:
        average /= 3
        print(f"Your average is: {average}")