# Write a Python code to accept a string from the user and display characters 
# present at an even index number.
name = input("Please enter a string: ")
print("Original String:", name)
for x in name[0::2]:
    print(x)
print(" ") 
# alternate solution
word = input('Enter word ')
print("Original String:", word)


size = len(word)

print("Printing only even index chars")
for i in range(0, size, 2):
    print("index[", i, "]", word[i])
