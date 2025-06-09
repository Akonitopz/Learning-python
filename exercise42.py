class SeriesofN:
    def __init__(self, start, n, sum):
        self.start = start
        self.n = n
        self.sum = sum

    def series(self):
        for i in range(0, self.n):
            print(self.start, end="")
            if i < self.n - 1:
                print("+", end="")
            self.sum += self.start
            self.start = self.start * 10 + 2

        return f"\nThe sum of the above series is: {self.sum}"
    


main = SeriesofN(int(input("Please enter a number: ")), int(input("Please enter the number of terms: ")), 0)
print(main.series())