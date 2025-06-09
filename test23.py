from tkinter import *
from tkinter import filedialog 

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            content = file.read()
        text_widget.delete("1.0", END)  
        text_widget.insert(END, content) 

window = Tk()
window.title("Open File Example")


open_button = Button(window, text="Open File", font=("Arial", 20), command=open_file)
open_button.pack(pady=10)


text_widget = Text(window, font=("Arial", 16), wrap="word", height=15, width=60)
text_widget.pack(pady=10)

window.mainloop()