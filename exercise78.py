#Write a code to checks if one set is a subset or superset of another set. If found, delete all elements from that set.

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is a subset of second set: ", first_set.issubset(second_set))
print("Second set is a subset of first set: ", second_set.issubset(first_set), "\n")
print("First set is a superset of second set: ", first_set.issuperset(second_set))
print("Second set a superset of first set: ", second_set.issuperset(first_set), "\n")

if first_set.issubset(second_set):
  first_set.clear()

if second_set.issubset(first_set):
  second_set.clear()
  
print("First set: ", first_set)
print("Second set: ", second_set)

