from tkinter import *
from tkinter import messagebox
import json
import pandas as pd
from datetime import datetime

#Issue: select product. keyerror
root  = Tk()
root.title("Point of Sale")
root.geometry("800x800")
#------------Data(Dummy rani. dile pani final)-----------------
selected_product = None; quantity = ''; total = 0; profit = 0; remaining_stock = 0; current_date = datetime.now(); final_date = current_date.strftime("%Y-%m-%d  %H:%M:%S")

try:
    with open("data.json", "r") as file:
        data = json.load(file)
        items = data['Item']

except FileNotFoundError:
    data = [
        {"Item": "Coke Mismo", "Inventory count": 35, "Purchase Price": 15, "Selling Price": 16.50},
        {"Item": "Milo", "Inventory count": 42, "Purchase Price": 10, "Selling Price": 11.00},
        {"Item": "555 Sardines", "Inventory count": 15, "Purchase Price": 10, "Selling Price": 13.00},
        {"Item": "Nescafe Classic", "Inventory count": 20, "Purchase Price": 5, "Selling Price": 7.00},
        {"Item": "Surf", "Inventory count": 10, "Purchase Price": 10, "Selling Price": 13.00},
        {"Item": "Pantene Shampoo", "Inventory count": 34, "Purchase Price": 7, "Selling Price": 10.00},
        {"Item": "Pantene 100ml Bottle", "Inventory count": 13, "Purchase Price": 150, "Selling Price": 165.00},
        {"Item": "Freska Tuna", "Inventory count": 25, "Purchase Price": 15, "Selling Price": 21.00},
        {"Item": "Pepsi Mismo", "Inventory count": 20, "Purchase Price": 15, "Selling Price": 25.00},
        {"Item": "BearBrand Powdered Milk", "Inventory count": 35, "Purchase Price": 9, "Selling Price": 12.00},

        {"Item": "Coke Mismo", "Inventory count": 35, "Purchase Price": 15, "Selling Price": 16.50},
        {"Item": "Milo", "Inventory count": 42, "Purchase Price": 10, "Selling Price": 11.00},
        {"Item": "555 Sardines", "Inventory count": 15, "Purchase Price": 10, "Selling Price": 13.00},
        {"Item": "Nescafe Classic", "Inventory count": 20, "Purchase Price": 5, "Selling Price": 7.00},
        {"Item": "Surf", "Inventory count": 10, "Purchase Price": 10, "Selling Price": 13.00},
        {"Item": "Pantene Shampoo", "Inventory count": 34, "Purchase Price": 7, "Selling Price": 10.00},
        {"Item": "Pantene 100ml Bottle", "Inventory count": 13, "Purchase Price": 150, "Selling Price": 165.00},
        {"Item": "Freska Tuna", "Inventory count": 25, "Purchase Price": 15, "Selling Price": 21.00},
        {"Item": "Pepsi Mismo", "Inventory count": 20, "Purchase Price": 15, "Selling Price": 25.00},
        {"Item": "BearBrand Powdered Milk", "Inventory count": 35, "Purchase Price": 9, "Selling Price": 12.00}
    ]
    dataFrame = pd.DataFrame(data)
    pd.options.display.colheader_justify ='left'
    dataFrame.to_json("data.json", indent=4)  

#------------------Dire Akong Functions---------------------

def selectProduct(ind):
    global selected_product, quantity
    quantity = ""
    selected_product = ind
    product_label.config(text=f"Selected Product: {data[ind]['Item']}")

def enterQuantity(quan):
    global quantity
    quantity += quan
    quantity_label.config(text=f"Quantity: {quantity}")

def submit():
    global selected_product, quantity, total, profit, remaining_stock, dataFrame
    if selected_product is None or quantity == '':
        messagebox.showinfo("Invalid Operation!", "Please choose a product and quantity before submitting.")
        product_label.config(text="Select products:")
        return
    
    item = data[selected_product] #ibutang and data nga dict sulod sa item
    total += float(item['Selling Price']) * float(quantity) #pag calculate sa total
    profit += (float(item['Selling Price']) - float(item['Purchase Price'])) * float(quantity) #pang calcu sa profit
    remaining_stock = float(item['Inventory count']) - float(quantity) #pang update sa inventory count
    item['Inventory count'] = remaining_stock
    content_Box.insert(END, f"{item['Item']}\t\t\t\t₱{item['Selling Price']}\t\t{quantity}\n")

    with open("data.json", "w") as f:  #pang update sa JSON
        json.dump(data, f, indent=4)

    dataFrame = pd.DataFrame(data)    #pang update sa Panda

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
    inventoryBox.insert("1.0", display.to_string(index=True))

def reset():
    global selected_product, quantity, total, profit
    selected_product = None
    quantity = ''
    total = 0.0
    profit = 0.0
    product_label.config(text="Select products:")
    quantity_label.config(text="Enter Quantity:")
    content_Box.delete("0.1", END)
    content_Box.insert("1.0", "Item\t\t\t\tSelling Price\t\tQuantity\n")

def check_stock():
    for idx, item in enumerate(data):
        if item['Inventory count'] <= 5:
            messagebox.showwarning("Warning!", f"Stock for {item['Item']} has reached below threshold. Please refill stock.")

#---------------- Dire dapit akong widgets for styling -------------------
top_title = Label(root, 
                  text="POINT OF SALE", 
                  font=("Arial 20"))
top_title.grid(row=0, column=0, columnspan=2)

content_Box = Text(root, height=10, width=90)
content_Box.grid(row=1, column=0, columnspan=2)
content_Box.insert("0.1", "Item\t\t\t\tSelling Price\t\tQuantity\n")

product_label = Label(root,text="Select products:")
product_label.grid(row=2, column=0)

quantity_label = Label(root, text="Enter Quantity")
quantity_label.grid(row=2, column=1)

left_frame = LabelFrame(root, text="Product List", padx=10, pady=10)
left_frame.grid(row=3, column=0,padx=30)

for index, item in items.items():
    int_idx = int(index)
    Button(left_frame, 
            text=item,
            command=lambda n = int_idx: selectProduct(n),
            width=25).grid(row=int_idx//3, column=int_idx%3)

    
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
       width=15).grid(row=4, column=0, columnspan=2, pady=10)

Button(root, 
       text="TOTAL",
       command= totalCalculation,
       height=2,
       width=10).grid(row=5, column=0, columnspan=2)

Button(root, 
       text="RESET",
       command= reset,
       height=2,
       width=10).grid(row=6, column=0, columnspan=2,)

Button(root, 
       text="Show Inventory",
       command= showInventory,
       height=2,
       width=15).grid(row=7, column=0, columnspan=2,)

root.mainloop()