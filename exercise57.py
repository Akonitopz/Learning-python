#Count all letters, digits, and special symbols from a given string

def counter(str1):
    digits = 0
    chars = 0
    symbols = 0
    for i in str1:
        x = i.isdigit()
        y = i.isalpha()
        if x == True:
            digits += 1

        elif y == True:
            chars += 1

        else:
            symbols += 1

    print(f"chars: {chars}")
    print(f"digits: {digits}")
    print(f"symbols: {symbols}")



counter(input("Please enter a string containing numbers, letters, and symbols: "))

