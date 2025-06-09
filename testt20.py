from tkinter import *
from tkinter import messagebox
import json
import pandas as pd
from datetime import datetime


root  = Tk()
root.title("Point of Sale")
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
            pd.DataFrame(data).to_string("Report.txt", index=False)


initialize_file()
try:
    with open("data.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    messagebox.showerror("Error", "Data file not found.")
    root.destroy()

#------------------Dire Akong Functions---------------------
selected_product = None; quantity = ''; total = 0.0; profit = 0.0; remaining_stock = 0; current_date = datetime.now()
final_date = current_date.strftime("%Y-%m-%d  %H:%M:%S")

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
    global selected_product, quantity, total, profit, remaining_stock
    if selected_product is None or quantity == '':
        messagebox.showinfo("Invalid Operation!", "Please choose a product and quantity before submitting.")
        product_label.config(text="Select products:")
        return
    
    item = data[selected_product]
    
    if float(quantity) > item['Inventory count']:
        messagebox.showwarning("Warning!", "This product is out of stock. Please refill to continue")
        product_label.config(text="Select products:")
        quantity_label.config(text="Enter Quantity:")
        return

    total += float(item['Selling Price']) * float(quantity) 

    profit += (float(item['Selling Price']) - float(item['Purchase Price'])) * float(quantity) 

    remaining_stock = float(item['Inventory count']) - float(quantity) 

    item['Inventory count'] = remaining_stock
    content_Box.insert(END, f"{item['Item']}\t\t\t\t₱{item['Selling Price']}\t\t{quantity}\n")

    with open("data.json", "w") as f: 
        json.dump(data, f, indent=4)

    selected_product = None
    quantity = ''
    remaining_stock = 0.0
    product_label.config(text="Select products:")
    quantity_label.config(text="Enter Quantity:")

def totalCalculation():
    global profit, total, quantity
    content_Box.insert(END, f"\nTotal Sale: {total}\nProfit: {profit} as of <{final_date}>\n\n")
    total = 0.0
    profit = 0.0
    check_stock()

def showInventory():
    window = Toplevel()
    window.title("Inventory")
    window.geometry("700x700")

    top_title = Label(window, 
                  text="INVENTORY", 
                  font=("Arial 20"))
    top_title.grid(row=0, column=0, columnspan=2)

    inventoryBox = Text(window, wrap=WORD)
    inventoryBox.grid(row=1, column=0, columnspan=2)

    display = pd.read_json("data.json")
    pd.options.display.colheader_justify ='left'
    inventoryBox.insert("1.0", display.to_string(index=1))

def reset():
    global selected_product, quantity, total, profit
    selected_product = None
    quantity = ''
    total = 0.0
    profit = 0.0
    product_label.config(text="Select products:")
    quantity_label.config(text="Enter Quantity:")
    content_Box.delete("0.1", END)
    content_Box.insert("0.1", "Item\t\t\t\tSelling Price\t\tQuantity\n")

def check_stock():
    global selected_product, quantity
    for idx, item in enumerate(data):
        if item['Inventory count'] <= 5:
            messagebox.showwarning("Warning!", f"Stock for {item['Item']} has reached below threshold. Please refill stock.")
            item['Inventory count'] = 50
            messagebox.showinfo("information", "Restock Successful")
            with open("data.json", "w") as f: 
                json.dump(data, f, indent=4)


#---------------- Dire dapit akong widgets for styling -------------------
menubar = Menu(root)

menu_list = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Menu", menu= menu_list)
menu_list.add_command(label='View Inventory', command=showInventory)
menu_list.add_command(label='Save Report', command=None)
menu_list.add_separator()
menu_list.add_command(label='Exit', command=root.destroy)

top_title = Label(root, 
                  text="POINT OF SALE", 
                  font=("Arial 20"))
top_title.grid(row=0, column=0, columnspan=2)

scroll_bar = Scrollbar(root, 
                       relief="sunken")
scroll_bar.grid(row=1, column=2, sticky="ns")

content_Box = Text(root, 
                   height=10, 
                   width=90,
                   yscrollcommand=scroll_bar.set)
content_Box.grid(row=1, column=0, columnspan=2)
content_Box.insert("0.1", "Item\t\t\t\tSelling Price\t\tQuantity\n")
scroll_bar.config(command=content_Box.yview)

product_label = Label(root,
                      text="Select products:")
product_label.grid(row=2, column=0)

quantity_label = Label(root, 
                       text="Enter Quantity")
quantity_label.grid(row=2, column=1)

left_frame = LabelFrame(root, 
                        text="Product List", 
                        padx=10, 
                        pady=10)
left_frame.grid(row=3, column=0,padx=30)

for index, item in enumerate(data):
    Button(left_frame, 
           text = item['Item'],
           command= lambda n=index: selectProduct(n),
           width=25).grid(row=index//3, column=index%3)
    
right_frame = LabelFrame(root, text="Quantity", padx=10, pady=10)
right_frame.grid(row=3, column=1)

for i in range(1,10):
    Button(right_frame, 
           text = i,
           command= lambda n=str(i): enterQuantity(n),
           height=2,
           width=4).grid(row=(i-1)//3, column=(i-1)%3)

Button(right_frame, 
       text="0",
       command= lambda n='0': enterQuantity(n),
       height=2,
       width=4).grid(row=3, column=1)

Button(root, 
       text="Submit",
       command= submit,
       height=2,
       width=15).grid(row=4, column=0, columnspan=2)

Button(root, 
       text="TOTAL",
       command= totalCalculation,
       height=2,
       width=15).grid(row=5, column=0, columnspan=2)

Button(root, 
       text="RESET",
       command= reset,
       height=2,
       width=15).grid(row=6, column=0, columnspan=2,)

root.config(menu=menubar)
check_stock()
root.mainloop()