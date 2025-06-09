#Given two lists of numbers, write a Python code to create a new list such that the latest list should 
# contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = [list1]
ans = []
for n in list3:
    for check1 in list1:
        factor = check1 % 10
        if factor != 0:
            ans.append(check1)
    for check2 in list2:
        factor = check2 % 10
        if factor == 0:
            ans.append(check2)
        

print(ans)