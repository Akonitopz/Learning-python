from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("To-Do-list")
window.geometry("500x500")
taskLists = []; counter  = 1; row = 0

def Addtasks():
  global row

  def deletetasks():
    tasks.destroy()
    delete.destroy()

  task_entry = inputBox.get()
  tasks = Label(task_Frame,
                  font="lucida 15")
  tasks.grid(row=row, column=0)

  delete = Button(task_Frame,
                text="Delete task",
                command=deletetasks,
                bg="red",
                font="Arial 13",
                activebackground="red")
  delete.grid(row=row, column=2)
  tasks.config(text=task_entry)

  row += 1


title = Label(window, 
              text="To-DO-List",
              font=("Arrial", 20))
title.pack()

inputBox = Entry(window, width=20)
inputBox.pack()

btn = Button(window,
             text="submit",
             font=("Arial", 13),
             command=Addtasks,
             bg="blue",
             activebackground="blue")
btn.pack()

task_Frame = Frame(window)
task_Frame.pack()


window.mainloop()



