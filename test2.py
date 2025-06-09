rows = 5
# outer loop for each row
for i in range(1, rows + 1):
    # print spaces to center the stars
    print(' ' * (rows - i), end='')
    # print stars
    print('*' * (2 * i - 1))
