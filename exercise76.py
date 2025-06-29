# Write a code to create a Python set such that it shows the element from both lists in a pair.

def listZipper(a , b):
  c = zip(a , b)
  return f"Zipped list: {tuple(c)}"

print(listZipper([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64]))