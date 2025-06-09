from tkinter import *
arr = []

window = Tk()
window.geometry("500x500")
window.title("My first GUI app!")
window.config(background = "#5cfcff")

def Add():
   data = inputBox.get()
   arr.append(data)
   print(arr)

inputBox = Entry(window, 
              font=("Arial", 30))
inputBox.pack(side = "left")

button = Button(window, text = "Add", command = Add)
button.pack(side= "right")


window.mainloop()

