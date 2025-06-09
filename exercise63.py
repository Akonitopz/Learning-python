#Reverse a given string

def str_reverse(str1):
    new_str = []
    for i in range(len(str1) , 0 , -1):
        new_str += str1[i - 1]
        final_str = ''.join(new_str)

    return f"Original String: {str1}, Reversed String: {final_str}"



print(str_reverse("PYNative"))
