def Bubble(nums):  # Iswap ra iyang katapad
    for i in range(len(nums)-1, 0, -1): #Run thourgh array
        for j in range(i): #Compare and swap
            if nums[j] > nums[j+1]: #conditional/compare
                nums[j] , nums[j + 1] = nums[j+1] , nums[j] #swap
                

    
    return nums
        

print(Bubble([7,4,2,1,6,5,9,8]))

#bubble sort = Swap ang katapad.
#Selection sort = mangita og largest or smallest number sa array.
#Insertion sort = Divide into two arrays tapos insert from array 2 to array 1.

