#initial test for the code.

str1 = 'five hundred'
print(f"The string is: {str1}")
temp = str1.split()

for i in temp:
  if i in ['hundred']:
    num = 5
    num *= 100


print(f"The decimal equivalence: {num}")