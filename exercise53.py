#Write a program to create a new string made of the middle three characters of an input string.

def Mid_letter(string):
    mid = int(len(string) / 2)
    ans = string[mid - 1: mid + 2]
    print(f"The middle string for {string} is: {ans}")



Mid_letter("JohnDipPeta")
Mid_letter("JaSonay")



