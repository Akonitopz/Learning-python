#Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, 
# the output shall be “6 3 5 7“, with a space separating the digits.

num = 7536
revnum = 0
while num > 0:
    digit = num % 10
    revnum = (revnum * 10) + digit
    num = num // 10

print(revnum)
