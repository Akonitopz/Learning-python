#Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it.

def function( a , b):
    def Add(a,b):
        return a + b

    add = Add(a,b)
    return add + 5

res = function(5, 10)
print(res)
