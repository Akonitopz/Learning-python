import tkinter as tk

str = []
def button1():
  inputdata = inputBox.get()
  label1.config(text= f"You entered: {inputdata}")
  str.append(inputdata)
  print(str)

window = tk.Tk()

label = tk.Label(window, text= "To-Do-list!", 
                 font=("Arial", 70))
label.grid(row=0, column=0, columnspan=2, padx=5, pady= 10)

inputBox = tk.Entry(window, textvariable="Input task here:", 
                    font=("Arial", 30))
inputBox.grid(row=1, column=1, padx=5, pady= 10)


button = tk.Button(window, 
                   text="Add", 
                   font=("Arial" , 30),
                   padx= 30,
                   pady= 30,
                   command=button1)

button.grid(row=1, column=2, padx=5, pady= 10)

label1 = tk.Label(window, text="", 
                  font=("Arial", 30))
label1.grid(row=2, column=1, columnspan=2, padx=5, pady=10 )


window.mainloop()