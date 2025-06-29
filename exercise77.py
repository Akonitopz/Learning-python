#Write a code to find the intersection (common) of two sets and remove those elements from the first set.

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("first set: ", first_set)
print("second set: ", second_set)

intersection_set = first_set.intersection(second_set)
print("Intersection of 2 sets: ", intersection_set)

for i in intersection_set:
  first_set.remove(i)

print("Updated first set after recoming intersection: ", first_set)