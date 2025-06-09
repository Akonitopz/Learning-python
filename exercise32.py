#Write a Python program to print the reverse number pattern using a for loop.

rows = 5
for x in range(rows , 0 , -1):
    for y in range(x , 0 , -1):
        print(y , end= " ")
    print(" ")