from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Age Calculator")
root.geometry("410x300")
#----------Functions---------
def reset():
  dayEntry.delete(0,END)
  monthEntry.delete(0,END)
  yearEntry.delete(0,END)
  curent_dayEntry.delete(0,END)
  curent_monthEntry.delete(0,END)
  curent_yearEntry.delete(0,END)
  resultDay.delete(0,END)
  resultMonth.delete(0,END)
  resultYear.delete(0,END)

def checkError():
  if (dayEntry.get() == "" or monthEntry.get() == "" or
      yearEntry.get() == "" or curent_dayEntry.get() == "" or
      curent_monthEntry.get() == "" or curent_yearEntry.get() == ""):
    messagebox.showwarning("Warning!", "Warning! Please input a value first before calculating.")

    reset()
    return -1
  
def calculateAge():
  value = checkError()

  if value == -1:
    return
  
  else:
    day = int(dayEntry.get())
    month = int(monthEntry.get())
    year = int(yearEntry.get())

    curDay = int(curent_dayEntry.get())
    curMonth = int(curent_monthEntry.get())
    curYear = int(curent_yearEntry.get())

    month_count =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (curYear % 4 == 0 and curYear % 100 != 0) or (curYear % 400 == 0):
      month_count[1] = 29

    if(day > curDay):
      curMonth -= 1
      curDay += month_count[curMonth-2]

    if(month > curMonth):
      curYear -= 1
      curMonth += 12

    finalDay = curDay - day
    finalMonth = curMonth - month
    finalYear = curYear - year

    resultDay.delete(0, END)
    resultMonth.delete(0, END)
    resultYear.delete(0, END)

    resultDay.insert(END, finalDay)
    resultMonth.insert(END, finalMonth)
    resultYear.insert(END, finalYear)

#---------Widgets---------
Label(root, text="Age Calculator").grid(row=0, column=0, columnspan=4)

#-----------Left Frame--------
leftframe = Frame(root)
leftframe.grid(row=1, column=0)
Label(leftframe, text="Birth Day").grid(row=0,column=0)
Label(leftframe, text="Birth Month").grid(row=1,column=0)
Label(leftframe, text="Birth Year").grid(row=2,column=0)

dayEntry = Entry(leftframe)
dayEntry.grid(row=0, column=1)
monthEntry = Entry(leftframe)
monthEntry.grid(row=1, column=1)
yearEntry = Entry(leftframe)
yearEntry.grid(row=2, column=1)

#-----------Right Frame--------
rightFrame = Frame(root)
rightFrame.grid(row=1, column=2)
Label(rightFrame, text="Current Day").grid(row=0,column=0)
Label(rightFrame, text="Current Month").grid(row=1,column=0)
Label(rightFrame, text="Current Year").grid(row=2,column=0)

curent_dayEntry = Entry(rightFrame)
curent_dayEntry.grid(row=0, column=1)
curent_monthEntry = Entry(rightFrame)
curent_monthEntry.grid(row=1, column=1)
curent_yearEntry = Entry(rightFrame)
curent_yearEntry.grid(row=2, column=1)

Button(root, text="Result", command=calculateAge).grid(row=2, column=0, columnspan=4, pady=20)
Label(root, text="Days").grid(row=3, column=0, columnspan=4)
resultDay = Entry(root)
resultDay.grid(row=4, column=0, columnspan=4)

Label(root, text="Months").grid(row=5, column=0, columnspan=4)
resultMonth = Entry(root)
resultMonth.grid(row=6, column=0, columnspan=4)

Label(root, text="Years").grid(row=7, column=0, columnspan=4)
resultYear = Entry(root)
resultYear.grid(row=8, column=0, columnspan=4)

Button(root, text="Clear All", command=reset).grid(row=9, column=0, columnspan=4)

root.mainloop()