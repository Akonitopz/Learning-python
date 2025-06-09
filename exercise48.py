#Write a program to create a recursive function to calculate 
# the sum of numbers from 0 to 10.

def recur(num):
    if num:
        return num + recur(num - 1)
    else:
        return 0
    

print(recur(10))
