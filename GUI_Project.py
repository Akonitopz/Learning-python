from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Encrypt - Decrypt")

button3 = None
text_widget = None

def initialize_file():
    filepath = "Secret.txt"
    try:
        with open(filepath, "r") as file:
            content = file.read()
        if "NOTE" not in content:
            with open(filepath, "a") as file: 
                file.write("NOTE: This widget automatically closes when new text is entered to maintain security.\n")
                
    except FileNotFoundError:
        with open(filepath, "w") as file:  
            file.write("NOTE: This widget automatically closes when new text is entered to maintain security.\n")

def add_placeholder(inputBox, placeholder_text):
    inputBox.insert(0, placeholder_text)
    inputBox.config(fg="grey")
    
    def on_focus_in(event):
        if inputBox.get() == placeholder_text:
            inputBox.delete(0, END)
            inputBox.config(fg="black")
    
    def on_focus_out(event):
        if inputBox.get() == "":
            inputBox.insert(0, placeholder_text)
            inputBox.config(fg="grey")
    
    inputBox.bind("<FocusIn>", on_focus_in)
    inputBox.bind("<FocusOut>", on_focus_out)


def addButton():
    global button3
    button3 = Button(window, 
                 text="Open Secret", 
                 font=("Arial", 20), 
                 command=open_Secret)
    button3.grid(row=3, column=0,columnspan=3, padx=5, pady=5)

def open_Secret():
  global text_widget
  messagebox.showwarning("Warning!", "You are opening an encrypted file. Proceed?")
  filepath = "Secret.txt"
  try:  
        scroll_bar = Scrollbar(window, relief="raised")
        scroll_bar.grid(row=4, column=3, sticky="ns")
        text_widget = Text(window, 
                           font=("Arial", 16), 
                           wrap="word", height=15, 
                           width=45,
                           yscrollcommand= scroll_bar.set)
        text_widget.grid(row=4, column=0,columnspan=3, padx=5, pady=5)
        scroll_bar.config(command=text_widget.yview)
        with open(filepath, "r") as file:
            content = file.read()
        text_widget.delete("1.0", END) 
        text_widget.insert(END, content) 

  except FileNotFoundError:
        text_widget.delete("1.0", END)
        text_widget.insert(END, "File not found. Please make sure the file exists.")

def remove_widgets():
    global button3, text_widget

    if button3:
      button3.destroy()
      button3 = None
    
    if text_widget:
      text_widget.destroy()
      text_widget = None 

def encrypt():
  global button3, text_widget
  str1 = inputBox.get().strip()
  result = ""
  if str1 == "" or str1 == "Enter your text here...":
        label1.config(text="You have not entered any words. Please try again.")
        remove_widgets()
        return
  for char in str1:
    if char in ['x','y','z', 'X', 'Y', 'Z']:
      convert = ord(char) - 23
      result += chr(convert)
      
    else:
      convert = ord(char) + 3
      result += chr(convert)

  with open("Secret.txt", "a") as file:
    file.write(f"\nOriginal String: {str1}\nEncrypted: {result}")

  label1.config(text= f"The Encrypted word is: {result}")
  if text_widget:
    text_widget.destroy()
    text_widget = None

  addButton()

def decrypt():
  global button3, text_widget
  str1 = inputBox.get().strip()
  result = ""
  if str1 == "" or str1 == "Enter your text here...":
        label1.config(text="You have not entered any words. Please try again.")
        remove_widgets()
        return
  for char in str1:
    if char in ['a','b','c', 'A', 'B', 'C']:
      convert = ord(char) + 23
      result += chr(convert)

    else:
      convert = ord(char) - 3
      result += chr(convert)

  with open("Secret.txt", "a") as file:
    file.write(f"\nOriginal String: {str1}\nDecrypted: {result}")

  label1.config(text= f"The Decrypted word is: {result}")
  if text_widget:
    text_widget.destroy()
    text_widget = None

  addButton()

label = Label(window, 
              text="Encryption - Decryption App", 
              font=("Arial", 20))
label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

inputBox = Entry(window, 
                 font=("Arial", 20))
inputBox.grid(row=1, column=0, padx=10, pady=5)
add_placeholder(inputBox, "Enter your text here...")

button1 = Button(window, 
                 text="Encrypt", 
                 font=("Arial", 20), 
                 command=encrypt,
                 bg="#154ADD",
                 fg="#FFFFFF",
                 activebackground="#154ADD",
                 activeforeground="#FFFFFF")
button1.grid(row=1, column=1, padx=5, pady=5)

button2 = Button(window, 
                 text="Decrypt", 
                 font=("Arial", 20), 
                 command=decrypt,
                 bg="#D4070B",
                 fg="#FFFFFF",
                 activebackground="#D4070B",
                 activeforeground="#FFFFFF")
button2.grid(row=1, column=2, padx=5, pady=5)

label1 = Label(window, text="", font=("Arial", 20))
label1.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

initialize_file()
window.mainloop()