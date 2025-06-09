#Convert Decimal number to octal using print() output formatting
num = int(input("Please input the number that you want to convert from decimal to octal: "))
octal = []
while num > 0:
    remainder = num % 8
    octal.append(remainder)
    num = num // 8

octal.reverse()
print("Decimal to Octal: ", '' .join(map(str, octal)))

#alternative solution
num = int(input("Please enter you want to convert: "))
print("Converted:", '%o' % num)


    