from tkinter import *

root = Tk()
root.title("Python Enterprises")
root.geometry("300x200")

#---------functions---------
def add_placeholder(entry_widget, placeholder_text, is_password=False):
    entry_widget.insert(0, placeholder_text)
    entry_widget.config(fg="grey")

    def on_focus_in(event):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")
            if is_password:
                entry_widget.config(show="*")

    def on_focus_out(event):
        if entry_widget.get() == "":
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="grey")
            if is_password:
                entry_widget.config(show="")

    entry_widget.bind("<FocusIn>", on_focus_in)
    entry_widget.bind("<FocusOut>", on_focus_out)

#---------widgets-----------
Label(root, text="Python Enterprises", font=("Arial", 20)).pack()

usernameLabel = Label(root, text="Username", font=("Arial", 12, "bold"))
usernameLabel.pack()

usernameEntry = Entry(root)
usernameEntry.pack()
add_placeholder(usernameEntry, "Enter username here...")

passwordLabel = Label(root, text="Password", font=("Arial", 12, "bold"))
passwordLabel.pack()

passwordEntry = Entry(root)
passwordEntry.pack()
add_placeholder(passwordEntry, "Enter password here...", is_password=True)

loginButton = Button(root,
                     text="Login",
                     font=("Arial", 12, "bold"),
                     command=None,
                     width=8, height=2)
loginButton.pack(pady=10)

root.mainloop()