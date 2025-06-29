#Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(f"Original List: {sample_list}")

final_dict = dict()
for item in sample_list:
    if item in final_dict:
        final_dict[item] += 1
    else:
        final_dict[item] = 1
        
print(f"Occurence of each element: {final_dict}")

