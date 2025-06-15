#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

def pop_insert_append(str1):
  pop = str1.pop(4)
  print("List After removing element at index 4: ", str1)
  str1.insert(2, pop)
  print("List after Adding element at index 2: ", str1)
  str1.append(pop)
  print("List after Adding element at last: ", str1)

pop_insert_append([34, 54, 67, 89, 11, 43, 94])