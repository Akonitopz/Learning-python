#Print a downward half-pyramid pattern of stars
rows = 5

for x in range(rows, 0, -1):
    for y in range(x):
        print("*", end = " ")
    print(" ")