#Given two strings, s1 and s2. Write a program to create a new string s3 
# made of the first char of s1, then the last char of s2, Next, the second 
# char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

def string_combi(s1 , s2):
    s3 = len(s1) if len(s1) > len(s2) else len(s2)
    s2 = s2[::-1]
    new_word = ""
    for i in range(s3):
        if i < len(s1):
            new_word += s1[i]

        if i < len(s2):
            new_word += s2[i]
    
    print(new_word)


string_combi("abc" , "XYZ")



