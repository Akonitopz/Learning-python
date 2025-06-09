#Removal all characters from a string except integers.
new_string = ''
nums = []
def stringFind(str1):
  for char in str1:
    if char.isdigit():
      nums.append(char)
    new_string = ''.join(nums)

  return new_string

str1 = 'I am 25 years and 10 months old'
print(f"Old string: {str1}")
print(f"New String: {stringFind(str1)}")