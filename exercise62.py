#Write a program to count occurrences of all characters within a string

def str_counter(str1):
    str1 = str1.lower()
    dict1 = {}
    for i in str1:
       if i in ['a' , 'p' , 'l' , 'e']:
           key = i.upper()
           dict1[key] = dict1.get(key,0) + 1


    return dict1
        
str1 = "Apple"
print(str_counter(str1))