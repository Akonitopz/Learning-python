def stringcount(str1):
    temp_string = "USA"
    str1 = str1.lower()
    x = str1.count(temp_string.lower())

    return x


str1 = "Welcome to USA. usa is awesome, isn't it?"
print(stringcount(str1))
