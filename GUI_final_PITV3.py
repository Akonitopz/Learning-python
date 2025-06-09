from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import json
import pandas as pd
from datetime import datetime


root  = Tk()
root.title("Python Enterprises")
root.geometry("800x650")
#------------Data Creation and initializing ni dire-----------------
def initialize_file():
    filepath = "data.json"
    try:
        with open(filepath, "r") as file:
            json.load(file)  

    except (FileNotFoundError, json.JSONDecodeError):
            data = [
        {"Item": "Lucky Me Pancit Canton", "Inventory count": 50, "Purchase Price": 9.00, "Selling Price": 9.90},
        {"Item": "SkyFlakes Crackers", "Inventory count": 50, "Purchase Price": 12.00, "Selling Price": 13.20},
        {"Item": "Argentina Corned Beef", "Inventory count": 50, "Purchase Price": 25.00, "Selling Price": 27.50},
        {"Item": "Silver Swan Soy Sauce", "Inventory count": 50, "Purchase Price": 8.00, "Selling Price": 8.80},
        {"Item": "Datu Puti Vinegar", "Inventory count": 50, "Purchase Price": 9.00, "Selling Price": 9.90},
        {"Item": "Great Taste White Coffee", "Inventory count": 50, "Purchase Price": 5.00, "Selling Price": 5.50},
        {"Item": "C2 Green Tea", "Inventory count": 50, "Purchase Price": 12.00, "Selling Price": 13.20},
        {"Item": "Oishi Prawn Crackers", "Inventory count": 50, "Purchase Price": 6.00, "Selling Price": 6.60},
        {"Item": "Jack n' Jill Piattos", "Inventory count": 50, "Purchase Price": 8.00, "Selling Price": 8.80},
        {"Item": "Nestlé Chuckie", "Inventory count": 50, "Purchase Price": 12.00, "Selling Price": 13.20},
        {"Item": "Century Tuna Flakes in Oil", "Inventory count": 50, "Purchase Price": 20.00, "Selling Price": 22.00},
        {"Item": "Colgate Toothpaste 35g", "Inventory count": 50, "Purchase Price": 18.00, "Selling Price": 19.80},
        {"Item": "Safeguard Soap 90g", "Inventory count": 50, "Purchase Price": 15.00, "Selling Price": 16.50},
        {"Item": "Palmolive Shampoo Sachet", "Inventory count": 50, "Purchase Price": 6.00, "Selling Price": 6.60},
        {"Item": "Rebisco Crackers", "Inventory count": 50, "Purchase Price": 7.00, "Selling Price": 7.70},
        {"Item": "Nestea Iced Tea Powder", "Inventory count": 50, "Purchase Price": 12.00, "Selling Price": 13.20},
        {"Item": "M.Y. San Grahams", "Inventory count": 50, "Purchase Price": 32.00, "Selling Price": 35.20},
        {"Item": "Chippy BBQ Flavor", "Inventory count": 50, "Purchase Price": 8.00, "Selling Price": 8.80},
        {"Item": "Nissin Cup Noodles", "Inventory count": 50, "Purchase Price": 22.00, "Selling Price": 24.20},
        {"Item": "Selecta Ice Cream (1.3L)", "Inventory count": 50, "Purchase Price": 160.00, "Selling Price": 176.00}
                  ]
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)


initialize_file()
try:
    with open("data.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    messagebox.showerror("Error", "Data file not found.")
    root.destroy()

#------------------Dire Akong Functions---------------------
selected_product = None; quantity = ''; total = 0.0; profit = 0.0; remaining_stock = 0; current_date = datetime.now();final_date = current_date.strftime("%Y-%m-%d  %H:%M:%S"); sub_counter = 0; darkMode = False; product_btn = []; quantity_btn = []; save_to_file_counter = 0

def selectProduct(idx):
    global selected_product, quantity
    quantity = ""
    selected_product = idx
    product_label.config(text=f"Selected Product: {data[idx]['Item']}")

def enterQuantity(quan):
    global quantity
    quantity += quan
    quantity_label.config(text=f"Quantity: {quantity}")

def submit():
    global selected_product, quantity, total, profit, remaining_stock, sub_counter
    if selected_product is None or quantity == '':
        messagebox.showinfo("Invalid Operation!", "Please choose a product and quantity before submitting.")
        product_label.config(text="Select products:")
        return
    
    item = data[selected_product]
    
    if float(quantity) > item['Inventory count']:
        messagebox.showwarning("Warning!", "You are entering more quantity than the available stock in this product. Please check inventory before proceeding.")
        product_label.config(text="Select products:")
        quantity_label.config(text="Enter Quantity:")
        return

    total += float(item['Selling Price']) * float(quantity) 

    profit += (float(item['Selling Price']) - float(item['Purchase Price'])) * float(quantity) 

    remaining_stock = float(item['Inventory count']) - float(quantity) 

    item['Inventory count'] = remaining_stock
    content_Box.insert(END, f"{item['Item']:<40}₱{item['Selling Price']:<15}{quantity:<10}\n")

    with open("data.json", "w") as f: 
        json.dump(data, f, indent=4)

    remaining_stock = 0.0
    product_label.config(text="Select products:")
    quantity_label.config(text="Enter Quantity:")

    sub_counter += 1

def totalCalculation():
    global profit, total, quantity, selected_product, sub_counter, save_to_file_counter
    if sub_counter == 0:
        messagebox.showinfo("Invalid Operation!", "Please submit your product and quantity before calculating total sale.")
        reset()
        return
    
    content_Box.insert(END, f"\nTotal Sale: {total}\nProfit: ₱{profit} as of <{final_date}>\n\n")

    save_to_file_counter += 1
    selected_product = None
    quantity = ''
    total = 0.0
    profit = 0.0
    sub_counter = 0
    check_stock()

def showInventory():
    global darkMode
    window = Toplevel()
    window.title("Inventory")
    window.geometry("700x700")

    if darkMode == True:
        window.config(bg="black")
        top_title = Label(window, 
                    text="INVENTORY", 
                    font=("Arial", 20, "bold"),
                    bg="black",
                    fg="white")
        top_title.grid(row=0, column=0, columnspan=2)

        inventoryBox = Text(window, 
                            wrap=WORD,
                            bg="black",
                            fg="white")
        inventoryBox.grid(row=1, column=0, columnspan=2)    

    else:
        top_title = Label(window, 
                    text="INVENTORY", 
                    font=("Arial 20"))
        top_title.grid(row=0, column=0, columnspan=2)

        inventoryBox = Text(window, wrap=WORD)
        inventoryBox.grid(row=1, column=0, columnspan=2)

    display = pd.read_json("data.json")
    pd.options.display.colheader_justify ='left'
    inventoryBox.insert("1.0", display.to_string(index=True))

def reset():
    global selected_product, quantity, total, profit, sub_counter, save_to_file_counter
    selected_product = None
    quantity = ''
    total = 0.0
    profit = 0.0
    sub_counter = 0
    save_to_file_counter = 0
    product_label.config(text="Select products:")
    quantity_label.config(text="Enter Quantity:")
    content_Box.delete("0.1", END)
    content_Box.insert("0.1", f"{'Item':<40}{'Selling Price':<15}{'Quantity':<10}\n")

def check_stock():
    global selected_product, quantity
    for idx, item in enumerate(data):
        if item['Inventory count'] <= 5:
            messagebox.showwarning("Warning!", f"Stock for {item['Item']} has reached below threshold. Please refill stock.")
            item['Inventory count'] = 50
            messagebox.showinfo("information", "Restock Successful")
            with open("data.json", "w") as f: 
                json.dump(data, f, indent=4)

def save_to_file():
    global save_to_file_counter
    content = content_Box.get("1.0", END)
    if save_to_file_counter == 0:
            messagebox.showwarning("warning!", "You have no Sales input. Please generate sales first.")
            return
    else:
        if content.strip() == "":
            messagebox.showwarning("warning!", "Save Error! empty content. Please generate sales first.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("text files", "*.txt")],
                                                title="Save Sales Report")
        
        if filepath:
            try:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write("Sales Report\n")
                    file.write(f"Date and Time of Sale: {final_date}\n")
                    file.write("-" * 50 + "\n")
                    file.write(content)
                    file.write("-" * 50 + "\n")
                messagebox.showinfo("Save Successful!", f"You sales report on {final_date} has been saved successfully!")
            except Exception as e:
                messagebox.showerror("Error Saving File!", f"Failed to save file.\n{e}")

def manual_restock():
    for item in data:
        item['Inventory count'] = 50
    
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Sucess!", "Restock on all items has been successful!")

def dark_Mode():
    global darkMode, product_btn, quantity_btn
    darkMode = True
    root.config(bg="black")
    menu_list.config(bg="black", fg="white")
    menu_list1.config(bg="black", fg="white")
    menubar.config(bg="black", fg="white")
    top_title.config(bg="black", fg="white")
    content_Box.config(bg="black", fg="white")
    product_label.config(bg="black", fg="white")
    quantity_label.config(bg="black", fg="white")
    left_frame.config(bg="black", fg="white")
    right_frame.config(bg="black", fg="white")
    submitButton.config(bg="black", fg="yellow")
    totalButton.config(bg="black", fg="green")
    resetButton.config(bg="black", fg="red")

    for btn in product_btn:
        btn.config(bg="black", fg="white", activebackground="black", activeforeground="white")

    for btn1 in quantity_btn:
        btn1.config(bg="black", fg="white", activebackground="black", activeforeground="white")

    messagebox.showinfo("Success!", "Switched to Dark Mode.")


def light_Mode():
    global darkMode, product_btn, quantity_btn
    darkMode = False
    root.config(bg="white")
    menu_list.config(bg="white", fg="black")
    menu_list1.config(bg="white", fg="black")
    menubar.config(bg="white", fg="black")
    top_title.config(bg="white", fg="black")
    content_Box.config(bg="white", fg="black")
    product_label.config(bg="white", fg="black")
    quantity_label.config(bg="white", fg="black")
    left_frame.config(bg="white", fg="black")
    right_frame.config(bg="white", fg="black")
    submitButton.config(bg="yellow", fg="black")
    totalButton.config(bg="green", fg="black")
    resetButton.config(bg="red", fg="black")

    for btn in product_btn:
        btn.config(bg="white", fg="black", activebackground="white", activeforeground="black")

    for btn1 in quantity_btn:
        btn1.config(bg="white", fg="black", activebackground="white", activeforeground="black")

    messagebox.showinfo("Success!", "Switched to Light Mode.")

    
#---------------- Dire dapit akong widgets for styling -------------------
menubar = Menu(root)

menu_list = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu= menu_list)
menu_list.add_command(label='View Inventory', command=showInventory)
menu_list.add_command(label='Save Report', command=save_to_file)
menu_list.add_command(label='Manual Restock', command=manual_restock)
menu_list.add_separator()
menu_list.add_command(label='Exit', command=root.destroy)

menu_list1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="System", menu= menu_list1)
menu_list1.add_command(label="Dark Mode", command=dark_Mode)
menu_list1.add_command(label="Light Mode", command=light_Mode)

top_title = Label(root, 
                  text="POINT OF SALE", 
                  font=("Arial", 20, "bold"))
top_title.grid(row=0, column=0, columnspan=2, pady=5)

scroll_bar = Scrollbar(root, 
                       relief="sunken")
scroll_bar.grid(row=1, column=2, sticky="ns")

content_Box = Text(root, 
                   height=10, 
                   width=90,
                   yscrollcommand=scroll_bar.set)
content_Box.grid(row=1, column=0, columnspan=2)
content_Box.insert("0.1", f"{'Item':<40}{'Selling Price':<15}{'Quantity':<10}\n")
scroll_bar.config(command=content_Box.yview)

product_label = Label(root,
                      text="Select products:")
product_label.grid(row=2, column=0, pady=5)

quantity_label = Label(root, 
                       text="Enter Quantity")
quantity_label.grid(row=2, column=1, pady=5)

left_frame = LabelFrame(root, 
                        text="Product List", 
                        padx=10, 
                        pady=10)
left_frame.grid(row=3, column=0,padx=30, pady=5)

right_frame = LabelFrame(root, text="Quantity", padx=10, pady=10)
right_frame.grid(row=3, column=1, pady=5)

for index, item in enumerate(data):
    btn1 = Button(left_frame, 
        text = item['Item'],
        command= lambda n=index: selectProduct(n),
        width=25)
    btn1.grid(row=index//3, column=index%3)
    product_btn.append(btn1)

for i in range(1,10): 
    btn2 = Button(right_frame, 
        text = i,
        command= lambda n=str(i): enterQuantity(n),
        height=2,
        width=4)
    btn2.grid(row=(i-1)//3, column=(i-1)%3)
    quantity_btn.append(btn2)
    
btn3 = Button(right_frame, 
    text="0",
    command= lambda n='0': enterQuantity(n),
    height=2,
    width=4)
btn3.grid(row=3, column=1)
quantity_btn.append(btn3)

submitButton = Button(root, 
       text="SUBMIT",
       command= submit,
       bg="yellow",
       activebackground="yellow",
       height=2,
       width=15,
        font=("Arial", 9, "bold"))
submitButton.grid(row=4, column=0, columnspan=2)

totalButton = Button(root, 
       text="TOTAL",
       command= totalCalculation,
       bg="green",
       activebackground="green",
       height=2,
       width=15,
         font=("Arial", 9, "bold"))
totalButton.grid(row=5, column=0, columnspan=2)

resetButton = Button(root, 
       text="RESET",
       command= reset,
       height=2,
       width=15,
       bg="red",
       activebackground="red",
         font=("Arial", 9, "bold"))
resetButton.grid(row=6, column=0, columnspan=2,)

root.config(menu=menubar)
check_stock()
root.mainloop()