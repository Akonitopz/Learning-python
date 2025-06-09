#Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

def uplowcheck(string):
    upper = []
    lower = []
    for i in string:
        if i.islower() == True:
            lower.append(i)
        else:
            upper.append(i)

    ans = ''.join(lower + upper)

    return ans

print(uplowcheck("PyNativeS"))
            