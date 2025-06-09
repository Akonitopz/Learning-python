# Calculate the cube of all numbers from 1 to a given number

class Cube_num:
    def __init__(self, num):
        self.num = num
    
    def numCube(self):
        for i in range(1, self.num + 1):
            print(f"Current number: {i} and the cube is: {i ** 3}")

        return
    
main = Cube_num(int(input("Please enter a number: ")))
main.numCube()
        
  




        


