from tkinter import *
root = Tk()
root.title("Mark Sheet")
root.geometry("500x500")

#--------Left Frame----------
name = Label(root, text="Name")
name.grid(row=0, column=0)

nameBox = Entry(root)
nameBox.grid(row=0, column=1)

rollnum = Label(root, text="Roll No.")
rollnum.grid(row=1, column=0)

rollnumBox = Entry(root)
rollnumBox.grid(row=1, column=1)

#-----------Right Frame----------
regnum = Label(root, text="Reg. No")
regnum.grid(row=0, column=3)

regnumBox = Entry(root)
regnumBox.grid(row=0, column=4)

#-----------Widgets-----------
Label(root, text="Srl. No").grid(row=2, column=0)
Label(root, text="Subject").grid(row=2, column=1)
Label(root, text="Grade").grid(row=2, column=2)
Label(root, text="Sub Credit").grid(row=2, column=3)
Label(root, text="Credit Obtained").grid(row=2, column=4)


root.mainloop()