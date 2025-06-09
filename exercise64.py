#Write a program to find the last position of a substring “Emie” in a given string.

def str_finder(str1 , index = 0):
    index = str1.rfind("Emie", 0 , len(str1))
    return f"The last occurence of Emie is at index {index}"



print(str_finder("Emie is a data scientist who knows Python. Emie works at google."))
