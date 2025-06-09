from tkinter import *
window = Tk()
window.title("Test GUI")

arr = []
n = 0

def entry():
    global n
    data = mainEntry.get()
    n += 1 
    delButton = Button(window, text="Delete", font=("arial", 20))
    delButton.grid(row=2, column=2, padx=10, pady=5)
    arr.append(f"Task {n}: {data}  {delButton}")
    mainEntry.delete(0, END)
    label1.config(text='\n'.join(arr))
    
label = Label(window, text="To-Do-List", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

mainEntry = Entry(window, font=("arial", 20))
mainEntry.grid(row=1, column=1, padx=10, pady=5)

addButton = Button(window, text="Add", font=("arial", 20), command=entry)
addButton.grid(row=1, column=2, padx=10, pady=5)

label1 = Label(window, text=" ", font=("Arial", 20))
label1.grid(row=2, column=0, padx=10, pady=5)

window.mainloop()