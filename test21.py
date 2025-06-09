#List Comprehension

#list_name = [(expression) (loop statement) (if statement)]

arr = [arr for arr in range(1,11) if arr % 2 == 0]
print(arr)