def Insertion(nums): #Divide into two arrays tapos insert from array 2 to array 1.
    for i in range(1, len(nums)):
        value = i 
        while nums[value - 1] > nums[value] and value > 0:
            nums[value - 1] , nums[value] = nums[value] , nums[value - 1]
            value -= 1 #decrement or reduce para muabot sa 1


    return nums


print(Insertion([3,7,6,1,5,2,4]))
#after ma swap, mag add napud og new