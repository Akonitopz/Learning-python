#Print multiplication table from 1 to 10

for x in range(1,11):
    for y in range(1,11):
        product = y * x
        print(product, end = " ")
    print("\t\t")
        