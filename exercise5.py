# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.
a = [10, 20, 30, 40, 10]
b = [75, 65, 35, 75, 30]
bool = True
print("Given list a:", a)
if a[0] == a[-1]:
    print(bool)
else:
    bool = False
    print(bool)

print("Given list b:", b)   

if b[0] == b[-1]:
    print(bool)
else:
    bool = False
    print(bool)