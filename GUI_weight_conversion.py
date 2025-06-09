from tkinter import *

root = Tk()
root.title("Weight Converter")
#-------functions-----------

def conversion():
  kilo = inputBox.get()
  gram1 = float(kilo) * 1000
  pounds1 = float(kilo) * 2.2
  ounce1 = float(kilo) * 35.27396195

  gram.insert(END,f"{gram1}\n")
  pounds.insert(END, f"{pounds1}\n")
  ounce.insert(END, f"{ounce1:.2f}\n")

#--------------Widgets--------------------
Label(root, text="Enter the weight in Kilograms").grid(row=0, column=0)

inputBox = Entry(root)
inputBox.grid(row=0, column=1)

Button(root, text="convert", command=conversion).grid(row=0, column=2)

Label(root, text="Gram").grid(row=1, column=0)

Label(root, text="Pounds").grid(row=1, column=1)

Label(root, text="Ounce").grid(row=1, column=2)

gram = Text(root, width=20, height=5)
gram.grid(row=2, column=0)
gram.insert("1.0","Kilogram to grams:\n")

pounds = Text(root, width=20, height=5)
pounds.grid(row=2, column=1)
pounds.insert("1.0","Kilogram to pounds:\n")

ounce = Text(root, width=20, height=5)
ounce.grid(row=2, column=2)
ounce.insert("1.0", "Kilograms to ounce:\n")

root.mainloop()