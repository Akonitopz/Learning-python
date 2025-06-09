from tkinter import *
import calendar

window = Tk()
window.title("calendar")

def show_cal():
    cal = Tk()
    cal.title("Calendar")
    cal.geometry("700x700")
    year = int(inputBox.get())
    data = calendar.calendar(year)

    content = Label(cal, 
                   text = data,
                   font="Consolas 10 bold")
    content.pack()

    cal.mainloop()

def add_placeholder(inputBox, text):
    inputBox.insert(0, text)
    inputBox.config(fg="grey")

    def focusIn(event):
      if inputBox.get() == text:
            inputBox.delete(0, END)
            inputBox.config(fg="black")

    def focusOut(event):
      if inputBox.get() == '':
            inputBox.insert(0, text)
            inputBox.config(fg="grey")

    inputBox.bind("<FocusIn>", focusIn)
    inputBox.bind("<FocusOut>", focusOut)

label1 = Label(window, 
               text="Calendar", 
               font=("Arial", 20))
label1.pack()

inputBox = Entry(window, 
               font=("Arial", 20))
inputBox.pack()
add_placeholder(inputBox, "Enter Year")

btn1 = Button(window, 
              text="Show Calendar",
              fg="blue",
              font=("Arial", 20),
              command=show_cal)
btn1.pack()

exit = Button(window,
              text="Exit",
              fg="red",
              font=("Arial", 20),
              command= exit)
exit.pack()

window.mainloop()



