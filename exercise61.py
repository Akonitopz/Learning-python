# Given a string s1, write a program to return the sum and average of the digits 
# that appear in the string, ignoring all other characters.

def sum_av(str1, total = 0 , div = 0):
    for i in range(len(str1)):
        if str1[i].isdigit() == True:
            div += 1
            total += float(str1[i])

        
    average = total / div
    return f"Total is: {total} and Average is: {average}"


string = "PYnative29@#8496"
print(sum_av(string))