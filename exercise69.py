#Remove special symbols / punctuation from a string

import string

str1 = "/*Jon is @developer & musician"

new_string = str1.translate(str.maketrans('', '',string.punctuation))

print(new_string)
