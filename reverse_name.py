def word_reverse(name):
    new_word = []
    for i in range(len(name), 0 , -1):
        new_word += name[i - 1]

    word = ''.join(new_word)
    print(word)


word_reverse(name = input("Please enter a word you would like to reverse: "))