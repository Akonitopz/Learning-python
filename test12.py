name = input("Please input the name you want to reverse: ")
new_word = []

for i in range(len(name), 0 , -1):
    new_word += name[i - 1]
    word = ''.join(new_word)

print(word)