def Selection(lists): #magpili ka og smallest or largest number sa array
    for i in range(len(lists)-1): #mag run trough sa array
        min_val = i #mangita og smallest
        for j in range(i + 1 , len(lists)):
            if lists[j] < lists[min_val]:
                min_val = j
                
        lists[i] , lists[min_val] = lists[min_val] , lists[i]

    print(lists)


Selection([7,4,2,1,6,5,9,8])