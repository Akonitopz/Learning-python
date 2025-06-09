import tkinter as tk

def numButton():
  num = entry.get()
  print(num)

window = tk.Tk()
window.title("Calculator")
window.geometry("500x300")
label = tk.Label(window, text="Calculator ni Tophe", font=("Arial"))
label.pack(side="top")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="1", command=numButton)
button.pack(side="bottom")

window.mainloop()
