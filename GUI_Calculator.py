from tkinter import *

expression = ""

def press(num):
  global expression
  expression += str(num)

  equation.set(expression)

def equalpress():
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""

  except:
    equation.set("Error!")
    expression = ""

def clearContents():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
  window = Tk()
  window.configure(background="light green")
  window.title("Calculator")
  window.geometry("270x150")
  equation = StringVar()
  expression_field = Entry(window, textvariable=equation)
  expression_field.grid(columnspan=4, ipadx=70)

  btn1 = Button(window, 
                text='1', 
                fg='black', 
                bg='red', 
                command=lambda: press(1), 
                height=1, 
                width=7)
  btn1.grid(row=2,column=0)

  btn2 = Button(window, 
                text='2', 
                fg='black', 
                bg='red', 
                command=lambda: press(2), 
                height=1, 
                width=7)
  btn2.grid(row=2,column=1)

  btn3 = Button(window, 
                text='3', 
                fg='black', 
                bg='red', 
                command=lambda: press(3), 
                height=1, 
                width=7)
  btn3.grid(row=2,column=2)

  btn4 = Button(window, 
                text='4', 
                fg='black', 
                bg='red', 
                command=lambda: press(4), 
                height=1, 
                width=7)
  btn4.grid(row=3,column=0)

  btn5 = Button(window, 
                text='5', 
                fg='black', 
                bg='red', 
                command=lambda: press(5), 
                height=1, 
                width=7)
  btn5.grid(row=3,column=1)

  btn6 = Button(window, 
                text='6', 
                fg='black', 
                bg='red', 
                command=lambda: press(6), 
                height=1, 
                width=7)
  btn6.grid(row=3,column=2)

  btn7 = Button(window, 
                text='7', 
                fg='black', 
                bg='red', 
                command=lambda: press(7), 
                height=1, 
                width=7)
  btn7.grid(row=4,column=0)

  btn8 = Button(window, 
                text='8', 
                fg='black', 
                bg='red', 
                command=lambda: press(8), 
                height=1, 
                width=7)
  btn8.grid(row=4,column=1)

  btn9 = Button(window, 
                text='9', 
                fg='black', 
                bg='red', 
                command=lambda: press(9), 
                height=1, 
                width=7)
  btn9.grid(row=4,column=2)

  btn10 = Button(window, 
                text='0', 
                fg='black', 
                bg='red', 
                command=lambda: press(0), 
                height=1, 
                width=7)
  btn10.grid(row=5,column=0)

  add = Button(window, 
                text='+', 
                fg='black', 
                bg='red', 
                command=lambda: press('+'), 
                height=1, 
                width=7)
  add.grid(row=2,column=3)

  minus = Button(window, 
                text='-', 
                fg='black', 
                bg='red', 
                command=lambda: press('-'), 
                height=1, 
                width=7)
  minus.grid(row=3,column=3)

  multiply = Button(window, 
                text='x', 
                fg='black', 
                bg='red', 
                command=lambda: press('*'), 
                height=1, 
                width=7)
  multiply.grid(row=4,column=3)

  divide = Button(window, 
                text='/', 
                fg='black', 
                bg='red', 
                command=lambda: press('/'), 
                height=1, 
                width=7)
  divide.grid(row=5,column=3)

  deci = Button(window, 
                text='.', 
                fg='black', 
                bg='red', 
                command=lambda: press('.'), 
                height=1, 
                width=7)
  deci.grid(row=5,column=2)

  add = Button(window, 
                text='=', 
                fg='black', 
                bg='red', 
                command=equalpress, 
                height=1, 
                width=7)
  add.grid(row=6,column=3)

  clear = Button(window, 
                text='AC', 
                fg='black', 
                bg='red', 
                command=clearContents, 
                height=1, 
                width=7)
  clear.grid(row=5,column=1)
  window.mainloop()