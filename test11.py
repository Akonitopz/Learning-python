num = 123456
rev_num = 0
while num > 0:
    remainder = num % 10
    rev_num = (rev_num * 10) + remainder
    num = num // 10

print(rev_num)