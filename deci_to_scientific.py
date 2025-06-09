def decimalToScientific(num):
    counter = 0
    while num > 10:
        num /= 10
        counter += 1
    return f"{num:.3f}e{counter}"


print(decimalToScientific(1345278654345345))