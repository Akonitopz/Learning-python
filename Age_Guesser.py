class AgeGuesser():
    def __init__(self, age):
        self.age = age

    def calculation(self):   #Dire mahitabo ang calculation
     while True:
        coeff  = self.age
        coeff *= 100
        self.age *= 2
        self.age += 5
        self.age *= 50
        print("Have you already had your birthday this year?")
        choice = str(input("Input here: ")).strip().lower() #Mao ni mag check if sakto ang gi input
        if choice in ['y' , 'yes']:   
            self.age += 1775
        elif choice in ['n' , 'no']:
            self.age += 1774
        else:
            print("Invalid input! Please answer only yes or no")
            continue
        
        while True:
            try:
                year = int(input("What year were you born?: "))

            except ValueError:
                print("Invalid input! Please use numbers and follow this format: 2000")
                continue
            else:
                self.age -= year
                self.age -= coeff
                print(f"Your age is:{self.age}")
                break

        while True:   #bug!!!! Mo Loop kaisa bisan og mag NO. Need to investigate
            choice1 = str(input("\nContinue Playing? Y/N:")).strip().lower()
            if choice1 in ['y' , 'yes']:
                self.main = MainMenu()
                self.main.mainOperation()
                break
            elif choice1 in ['n' , 'no']:
                print("Thank you for playing! Have a great day.")
                return #pang exit sa code
        
            else:
                print("Invalid input! Please try again.")
                continue
        break

class MainMenu():
    def __init__(self):
        self.num = None

    def mainOperation(self):
      while True:
        try:
            num1 = int(input("Please choose a number between 2 and 10: "))
        except ValueError:
            print("Invalid Input! Please use numbers only.")
            continue
        else:
            if num1 < 2 or num1 > 10:
                print("Invalid input! Please only between 2 and 10.")
                continue
            else:
                self.num = AgeGuesser(num1)  #mao ni tig tawag sa AgeGuesser nga class.
                self.num.calculation()
                break


class Check_Input():  # OKay nani. Mao ni tig check sa input.
    def __init__(self):
        self.main = None

    def Intro(self):
        while True:
            print("Would you like to play a game? Y/N")
            choice = str(input("Input here: ")).strip().lower()
            if choice in ['y' , 'yes']:
                print("Awesome! Let's start.")
                self.main = MainMenu()  #mao ni tig tawag sa main menu nga class
                self.main.mainOperation()
                break
            elif choice in ['n' , 'no']:
                print("Thank you, Have a great day!")
                break
            else:
                print("Invalid input! Please choose between yes and no only.")
                continue

main1 = Check_Input()  # mao ni gi call nga main class
main1.Intro()
         