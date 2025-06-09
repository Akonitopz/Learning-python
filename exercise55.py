# Given two strings, s1 and s2, write a program to return 
# a new string made of s1 and s2’s first, middle, and last characters.


def combi(str1 , str2):
    return str1[0] + str2[0] + str1[len(str1)//2] + str2[len(str2)//2] + str1[len(str1)//2: ] + str2[len(str2)//2 :]

print(combi("America" , "Japan"))