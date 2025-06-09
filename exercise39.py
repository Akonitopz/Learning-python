# Reverse a integer number

class Rev_num:
    def __init__(self, num, rev_num):
        self.num = num
        self.rev_num = rev_num
    
    def reverseInt(self):
        num1 = self.num
        while self.num > 0:
            remainder = self.num % 10
            self.rev_num = (self.rev_num * 10) + remainder
            self.num = self.num // 10
        
        return f"The reverse for {num1} is: {self.rev_num}"
    
main = Rev_num(int(input("Please input the integer you wish to reverse: ")), 0)
print(main.reverseInt())