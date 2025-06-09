from tkinter import *
window = Tk()
window.title("Encrypt-Decrypt")

text_Widget = None
btn3 = None

def initializeFile():
  filepath = "Secret.txt"
  try:
    with open(filepath, "r") as file:
      content = file.read()
      if "NOTE" not in content:
        with open(filepath, "a") as file:
          file.write("NOTE: This widget automatically closes when a new text is entered to maintain security.\n")
  except FileNotFoundError:
    with open(filepath, "w"):
      file.write("NOTE: this widget automatically closes when new text is entered to maintain security.\n")

def placeHolder(inputBox, placeholder_text):
  inputBox.insert(0, placeholder_text)
  inputBox.config(fg="grey")

  def focusIn(event):
    if inputBox.get() == placeholder_text:
      inputBox.delete(0, END)
      inputBox.config(fg="black")

  def focusOut(event):
    if inputBox.get() == "":
      inputBox.insert(0, placeholder_text)
      inputBox.config(fg="grey")

  inputBox.bind("<FocusIn>", focusIn)
  inputBox.bind("<FocusOut>", focusOut)

def encrypt():
  global btn3, text_Widget
  result = ""
  word = inputBox.get().strip()
  if word == "" or word == "Enter text here: ":
    label2.config(text="You have not entered any words. Please try again", font=("Arial", 13))
    destroyWidgets()
    return
  else:
      for char in word:
        if char in ['x','y','z','X','Y','Z']:
          result += chr(ord(char) - 23)

        else:
          result += chr(ord(char) + 3)

      label2.config(text=f"Encrypted: {result}")

  with open("Secret.txt", "a") as file:
    file.write(f"\nOriginal string: {word}\nEncrypted string: {result}")
  addButton()
  if text_Widget:
    text_Widget.destroy()
    text_Widget = None

def decrypt():
  global btn3, text_Widget
  result = ""
  word = inputBox.get().strip()
  if word == "" or word == "Enter text here: ":
    label2.config(text="You have not entered any words. Please try again", font=("Arial", 13))
    destroyWidgets()
    return
  
  else:
      for char in word:
        if char in ['a','b', 'c', 'A', 'B', 'C']:
          result += chr(ord(char) + 23)

        else:
          result += chr(ord(char) - 3)

  label2.config(text=f"Decrypted: {result}")
  with open("secret.txt", "a") as file:
    file.write(f"\nOriginal string: {word}\ndecrypted strring: {result}")
  addButton()
  if text_Widget:
    text_Widget.destroy()
    text_Widget = None

def addButton():
  global btn3
  btn3 = Button(window, 
              text="Show Secret", 
              command=showSecret,
              font=("Arial", 20))
  btn3.grid(row=3, column=0,columnspan=3, padx=10, pady=5)

def showSecret():
  global text_Widget
  filepath = "Secret.txt"
  try:
    text_Widget = Text(window,
                      height=15,
                      width=75,
                      font=("Arial", 10))
    text_Widget.grid(row=4, column=0,columnspan=3, padx=10, pady=5)
    with open(filepath, "r") as file:
      content = file.read()
      text_Widget.delete("1.0", END)
      text_Widget.insert(END, content)

  except FileNotFoundError:
    text_Widget.delete("1.0" , END)
    text_Widget.insert(END, "Error! File not found.")

def destroyWidgets():
  global btn3, text_Widget
  if btn3:
    btn3.destroy()
    btn3 = None

  if text_Widget:
    text_Widget.destroy()
    text_Widget = None

label1 = Label(window, 
               text="Encrypt/Decrypt", 
               font=("Arial", 20))
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

inputBox = Entry(window, 
                 font=("Arial", 20))
inputBox.grid(row=1, column=0, padx=10, pady=5)
placeHolder(inputBox, "Enter text here: ")

bnt1 = Button(window, 
              text="Encrypt", 
              command=encrypt,
              font=("Arial", 20),
              bg="#1D1C9B",
              fg="#F7F7F7",
              activebackground="#1D1C9B",
              activeforeground="#F7F7F7")
bnt1.grid(row=1, column=1, padx=10, pady=5)

bnt2 = Button(window, 
              text="Decrypt", 
              command=decrypt,
              font=("Arial", 20),
              bg="#B41714",
              fg="#F7F7F7",
              activebackground="#B41714",
              activeforeground="#F7F7F7")
bnt2.grid(row=1, column=2, padx=10, pady=5)

label2 = Label(window, 
               text="", 
               font=("Arial", 20))
label2.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

initializeFile()
window.mainloop()