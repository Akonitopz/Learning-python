age = int(input("Please choose a number betwen 2 and 10: "))

age *= 2
age += 5
age *= 50

choice = input("Have you already had your birthday this year?: ")
if choice == 'y':
    age += 1775

elif choice == 'n':
    age += 1774

year = int(input("What year were you born?: "))

age -= year

age -= 800  #If the user chooses 8 in the first question.

print("You age is: ", age)