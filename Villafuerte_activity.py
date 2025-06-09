num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
for fibonacci in range(5):
    fibonacci = num1 + num2
    print(fibonacci)
    num1, num2 = num2, fibonacci
