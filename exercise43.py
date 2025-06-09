class Pyramid:
    def __init__(self, rows):
        self.rows = rows

    def numPyramid(self):
        for i in range(self.rows):
            if i < self.rows // 2:
                for j in range(i):
                    print('*', end=' ')

            else:
                for k in range(self.rows - i, 0, -1):
                    print('*', end=' ')

            print()

main = Pyramid(10)
main.numPyramid()