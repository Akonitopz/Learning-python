#Print elements from a given list present at odd index positions

class Odd_index:
    def __init__(self, num):
        self.num = num

    def odd_indexing(self):
           return self.num[1::2]



main = Odd_index([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(main.odd_indexing())
        