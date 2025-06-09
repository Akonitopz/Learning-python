# Get an int value of base raises to the power of exponent
def exponent(base, expo):
    num = expo
    prod = 1
    while num > 0:
        prod = prod * base
        num -= 1
    print(f"raised to the power of {expo} is: {prod}")



exponent(base = int(input("please enter your base: ")), expo = int(input("Enter your exponent: ")))
