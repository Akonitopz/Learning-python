#Write a Python code to remove characters from a 
# string from 0 to n and return a new string.
# n must be less than the length of the string.
name = input("Please input a word: ")
n = int(input("Enter the number of letters to be removed: "))
if n < len(name):
    print("Original word:", name)
    print("Modified word:", name[n:])

else:
    print("You exceeded the number of index! The program will now close.")