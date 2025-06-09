class MaxNum:
    def __init__(self, lists):
        self.max = 0
        self.lists = lists
        
    def Process(self):    
        self.max = self.lists[0]
        for i in self.lists:
            if i > self.max:
                self.max = i

    def printer(self):
        return f"The maximum number in the list is: {self.max}"
    

main = MaxNum([4, 6, 8, 24, 12, 2])
main.Process()
print(main.printer())
