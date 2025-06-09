#Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

final_word = ''

result = []

temp = str1.split()

for item in temp:
  if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
    result.append(item)


for i in result:
  print(i)