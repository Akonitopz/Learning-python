init_list = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7']
new_list = init_list.copy()
new_list.pop(4)
print("Previous list: ")
for x in init_list:
    print(x)
print(" ")
print("Updated list: ")
for x in new_list:
    print(x)