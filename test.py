rows = 10
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(' ', end=' ')

    for k in range(b*2-1):
        print('*', end=' ')

    print('\r')