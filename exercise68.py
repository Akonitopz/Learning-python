#Find words with both alphabets and numbers
#wrong answer

str1 = "Emma25 is Data scientist50 and AI Expert"

accumulator = []
def stringAndNum(str1):
    for char in str1:
      if char.isdigit():
        accumulator.append(char)

      elif char.isalpha():
        accumulator.append(char)

      else:
        continue
      new_word = ''.join(accumulator)
    return new_word


print(stringAndNum(str1))