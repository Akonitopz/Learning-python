# Write a Python code to display numbers 
# from a list divisible by 5

list = [10, 20, 33, 46, 55]
dividend = []
for subl in list:
    if subl % 5 == 0:
        dividend.append(subl)

print(dividend)