#Write a Python code to check if the given number is palindrome. 
# A palindrome number is a number that is the same after reverse. 
# For example, 545 is the palindrome

num = input("Please enter a 3 digit number: ")
print("Original number: ", num)
for x in num:
    if num[0] == num[-1]:
        print("Yes. given number is palindrome number.")
        break
    else:
        print("No. the given number is not a palindrome number.")
        break