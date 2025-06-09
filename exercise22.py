#Write a program to take three names as input from a user in the single input() function call.
names = input("Please enter three strings: ")
str_split = names.split()
n = 1
for x in str_split:
    print(f"Name{n}:", x)
    n += 1