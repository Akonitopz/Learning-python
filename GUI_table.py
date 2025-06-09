from tkinter import *

class Table:
  def __init__(self, window):

    for i in range(rows):
      for j in range(columns):

        self.table = Entry(window, 
                           width=20, 
                           fg='blue',
                           font=("Arial", 20))
        self.table.grid(row=i, column=j)
        self.table.insert(END, list1[i][j])

list1 = [(1,'Toyota', 30),
         (2,'Honda', 25),
         (3,'Kawasaki', 45),
         (4,'BMW', 67),
         (5,'Hyundai', 85)]

rows = len(list1)
columns = len(list1[0])

window = Tk()
t= Table(window)
window.mainloop()