#Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second


def addLists(l1, l2):
  print(f"List with odd index: {l1[1::2]}\nList with even index: {l2[0::2]}")
  return f"List 1 + List 2: {l1[1::2] + l2[0::2]}"

print(addLists([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]))