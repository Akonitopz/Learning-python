#Write a program to create a function that takes two arguments, name and age, and print their value.

def func1(*args):
    for i in args:
        print(i)
    

func1(20, 40, 60)
func1(80, 100)