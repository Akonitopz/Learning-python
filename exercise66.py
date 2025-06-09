#Remove empty strings from a list of strings.

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_string = []
for i in str_list:
  if i in ['', None]:
    continue

  else:
    new_string.append(i)

print(new_string)


