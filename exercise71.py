#Replace each special symbol with # in the following string

import string

def charReplace(str1):
  print("The original string is: ", str1)
  for char in string.punctuation:
    str1 = str1.replace(char, '#')
  
  print(f"The final string is: {str1}")


charReplace("'/*Jon is @developer & musician!!'")