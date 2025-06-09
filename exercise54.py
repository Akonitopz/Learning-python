#Given two strings, s1 and s2. Write a program to 
#create a new string s3 by appending s2 in the middle of s1.

def combi(str1 , str2):
    
    newstr = str1[:len(str1)//2:] + str2 + str1[len(str1)//2:]
    return newstr

print(combi("Ault" , "Kelly"))