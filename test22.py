from tkinter import *

window = Tk()
window.title("Test GUI")

tasks = []
n = 0

def delete_task(task_index):
    tasks.pop(task_index)
    update_list()

def entry():
    global n
    data = mainEntry.get()
    if data:
        n += 1
        tasks.append(data)
        mainEntry.delete(0, END)
        update_list()

def update_list():
    for widget in frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_label = Label(frame, text=f"Task {index + 1}: {task}", font=("Arial", 20))
        task_label.grid(row=index, column=0, padx=10, pady=5)
        
        del_button = Button(frame, text="Delete", font=("Arial", 20), 
                            command=lambda i=index: delete_task(i))
        del_button.grid(row=index, column=1, padx=10, pady=5)

label = Label(window, text="To-Do List", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

mainEntry = Entry(window, font=("Arial", 20))
mainEntry.grid(row=1, column=0, padx=10, pady=5)

addButton = Button(window, text="Add", font=("Arial", 20), command=entry)
addButton.grid(row=1, column=1, padx=10, pady=5)

frame = Frame(window)
frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()