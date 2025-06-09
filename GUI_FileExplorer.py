from tkinter import *
from tkinter import filedialog
window = Tk()
window.title("File Explorer")
window.geometry("500x500")

def fileExplorer():
  filename = filedialog.askopenfilename(initialdir="/", 
                                        title="Select a file",
                                        filetypes=(("Text files",
                                                    "*.txt*"),
                                                    ("all files",
                                                    "*.*")))
  output.config(text="File is opened" + filename)

label = Label(window,
              text='File Explorer',
              font=("Arial", 20))
label.grid(row=0, column=0)

btn = Button(window, 
             text="Browes Files",
             font=("Arial", 20),
             command=fileExplorer)
btn.grid(row=1, column=0)

output = Label(window,
              text=None,
              font=("Arial", 20))
output.grid(row=2, column=0)

exit = Button(window,
              text="Exit",
              command=exit,
              font=("Arial", 20))
exit.grid(row=3, column=0)
window.mainloop()
