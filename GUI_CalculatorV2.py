from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("510x510")

expression = ''; equation = StringVar(); numvar = 9; oper = ['+','-','*','/']; text ="Click 2 numbers to calculate"

def add_placeholder(inputBox,text):
  inputBox.insert(0,text)
  inputBox.config(fg="grey")

  def focusIn(event):
    if inputBox.get() != text:
      inputBox.delete(0, END)
      inputBox.config(fg="black")

  def focusOut(event):
    if inputBox.get() == '':
      inputBox.insert(0,text)
      inputBox.config(fg="grey")
  
  inputBox.bind("<FocusIn>", focusIn)
  inputBox.bind("<FocusOut>", focusOut)

def input(num):
  global expression
  if inputBox.get() == text:
    expression = ''
    equation.set('')
    inputBox.config(fg="black")
  expression += str(num)
  equation.set(expression)

def equals():
  global expression
  try:
    result = str(eval(expression))
    equation.set(result)
    expression = result
  except:
    equation.set("Error!")
    expression = ''

def clear():
  global expression
  expression = ''
  equation.set("")

label = Label(window, 
              text="Calculator", 
              font=("Arial", 20))
label.grid(row=0,column=0, columnspan=4,padx=10, pady=10)

inputBox = Entry(window, 
              textvariable=equation, 
              font=("Arial", 20),
              justify="right",
              width=25)
inputBox.grid(row=1,column=0, columnspan=4,padx=10, pady=10)
add_placeholder(inputBox, text)

for num in range(1,11):
  btn = Button(window, 
              text=f"{numvar}",
              command=lambda n = numvar: input(n),
              font=("Arial", 20),
              height=2,
              width=5)
  row, column = divmod(num-1, 3)
  btn.grid(row=row+2, column=column,padx=5, pady=5)
  numvar -= 1

for idx, oper in enumerate(oper):
  btn = Button(window, 
              text=oper,
              command=lambda n = oper: input(n),
              font=("Arial", 20),
              height=2,
              width=5)
  btn.grid(row=idx+2, column=4,padx=5, pady=5)

clear = Button(window, 
              text="AC",
              command=clear,
              font=("Arial", 20),
              height=2,
              width=5)
clear.grid(row=5, column=1,padx=5, pady=5)

equals = Button(window, 
              text="=",
              command=equals,
              font=("Arial", 20),
              height=2,
              width=5)
equals.grid(row=5, column=2,padx=5, pady=5)

window.mainloop()

