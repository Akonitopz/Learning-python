#Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
final_list = {}
a = 0; b = 0 ; c = 0; d = 0; e = 0

for i in range(len(sample_list)):
  if sample_list[i-1] == 11:
    a += 1
    final_list["11"] = a
  elif sample_list[i-1] == 45:
    b += 1
    final_list["45"] = b
  elif sample_list[i-1] == 8:
    c += 1
    final_list["8"] = c
  elif sample_list[i-1] == 23:
    d += 1
    final_list["23"] = d
  elif sample_list[i-1] == 89:
    e += 1
    final_list["89"] = e


print("The number of occurences: " , final_list)

