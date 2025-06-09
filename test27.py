from tkinter import *
from tkinter import messagebox, filedialog
from datetime import datetime
import random

CHOCOLATE_DARK = "#2c1a0a"     
CHOCOLATE_MEDIUM = "#4a3a2a"   
CHOCOLATE_LIGHT = "#6b5a45"    
CREAM = "#f8f4e6"             
GOLD = "#c0a080"              

root = Tk()
root.title("Point of Sale System")
root.geometry("1000x900")
root.configure(bg=CHOCOLATE_MEDIUM)

data = [
    {"Item": "Ferrero Rocher (3pcs)", "Inventory count": 35, "Purchase Price": 52.50, "Selling Price": 65.00},  
    {"Item": "KitKat (2-finger)", "Inventory count": 42, "Purchase Price": 14.25, "Selling Price": 18.00},  
    {"Item": "Snickers (regular)", "Inventory count": 15, "Purchase Price": 23.50, "Selling Price": 29.00},  
    {"Item": "Toblerone (100g)", "Inventory count": 20, "Purchase Price": 132.00, "Selling Price": 160.00},  
    {"Item": "Cadbury Dairy Milk (80g)", "Inventory count": 10, "Purchase Price": 38.75, "Selling Price": 48.00},  
    {"Item": "Cloud 9 (30g)", "Inventory count": 50, "Purchase Price": 9.50, "Selling Price": 12.00},  
    {"Item": "Choco Mucho (30g)", "Inventory count": 45, "Purchase Price": 8.25, "Selling Price": 10.50},  
    {"Item": "Flat Tops (pack)", "Inventory count": 60, "Purchase Price": 5.75, "Selling Price": 7.50},  
    {"Item": "Curly Tops (pack)", "Inventory count": 38, "Purchase Price": 5.75, "Selling Price": 7.50},  
    {"Item": "Choc Nut (pack)", "Inventory count": 55, "Purchase Price": 4.50, "Selling Price": 6.00}, 

]

total_sale = 0.0
total_profit = 0.0
receipt_lines = []
history = []
totalCounter = 0

def format_currency(val):
    return f"₱{val:.2f}"

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def random_invoice():
    sale_Counter = 0
    return f"INV{random.randint(1000, 9999)}"

def calculate_column_widths(box_width):
    char_width = 6  
    max_chars = box_width // char_width
    
    item_width = max(15, min(25, max_chars//2))
    price_width = 10
    qty_width = 6
    
    total_width = item_width + price_width + qty_width + 8  
    if total_width > max_chars:
        item_width = max(15, max_chars - (price_width + qty_width + 8))
    
    return item_width, price_width, qty_width

def process_sale(idx, quantity):
    global total_sale, total_profit
    try:
        quantity_int = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity input.")
        return

    item = data[idx]
    if quantity_int > item['Inventory count']:
        messagebox.showerror("Error", "Quantity exceeds available stock!")
        return

    item['Inventory count'] -= quantity_int
    sale = item['Selling Price'] * quantity_int
    profit = (item['Selling Price'] - item['Purchase Price']) * quantity_int
    total_sale += sale
    total_profit += profit
    
    receipt_lines.append({
        'Item': item['Item'],
        'Price': item['Selling Price'],
        'Quantity': quantity_int
    })
    
    history.append(f"{item['Item']} - Qty: {quantity_int} - Sale: {format_currency(sale)}")
    updateReceipt()
    
    if 'entry_widget' in item and 'stock_label' in item:
        item['entry_widget'].delete(0, END)
        item['stock_label'].config(text=f"Stock: {item['Inventory count']}")

def updateReceipt():
    content_Box.delete("1.0", END)
    content_Box.tag_configure("bold", font=("Courier", 10, "bold"))
    content_Box.tag_configure("normal", font=("Courier", 10))  
    
    item_width = 20  
    price_width = 80
    qty_width = 10
    
    header = f"{'Item':<{item_width}}{'Price':^{price_width}}{'Qty':^{qty_width}}"
    content_Box.insert(END, header + "\n", "bold")
    
    for item in receipt_lines:
        item_name = item['Item'][:item_width]
        price = format_currency(item['Price'])
        qty = str(item['Quantity'])
        
        line = f"{item_name:<{item_width}}{price:^{price_width}}{qty:^{qty_width}}"
        content_Box.insert(END, line + "\n", "normal")
        
def totalCalculation():
    content = content_Box.get("2.0", END) #Nag add kog blocker para dile blangko imong transactions

    if content.strip() == "":
        messagebox.showwarning("Warning!", "You have not made any transactions.")
        return
    
    else:
        receipt_window = Toplevel(root)
        receipt_window.title("Receipt")
        receipt_window.geometry("300x1000")
        receipt_window.configure(bg=CREAM)

        receipt_text = Text(receipt_window, height=50, width=29, bg=CREAM, fg=CHOCOLATE_DARK, 
                        font=("Courier", 10), padx=10, pady=10)
        receipt_text.pack()

        receipt_text.insert(END, "Receipt\n", "bold")
        receipt_text.insert(END, f"Date: {get_datetime()}\n\n")
        
        for item in receipt_lines:
            line = f"{item['Item']} x {item['Quantity']} @ {format_currency(item['Price'])} = {format_currency(item['Price'] * item['Quantity'])}\n\n"
            receipt_text.insert(END, line)
        
        receipt_text.insert(END, f"\nTOTAL: {format_currency(total_sale)}\n\n", "bold")
        receipt_text.insert(END, "Thank you for your purchase! Hope to serve you again soon.\n")
        
        ok_button = Button(receipt_window, text="OK", command=receipt_window.destroy, 
                        bg=GOLD, fg=CHOCOLATE_DARK, font=("Arial", 10))
        ok_button.pack(pady=10)
        
        receipt_text.tag_configure("bold", font=("Courier", 10, "bold"))
        receipt_text.config(state=DISABLED)  
    
def reset():
    global total_sale, total_profit, receipt_lines, history, totalCounter
    totalCounter = 0
    total_sale = 0.0
    total_profit = 0.0
    receipt_lines.clear()
    history.clear()
    updateReceipt()
    for item in data:
        if 'stock_label' in item:
            item['stock_label'].config(text=f"Stock: {item['Inventory count']}")
        if 'entry_widget' in item:
            item['entry_widget'].delete(0, END)

def saveToFile():
    content = content_Box.get("1.0", END)
    if not history:
        messagebox.showinfo("No Data", "No transactions to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Point of Sale Receipt\n")
            file.write(f"Date/Time: {get_datetime()}\n")
            file.write(f"Invoice No: {random_invoice()}\n\n")
            
            box_width = 60  
            item_width, price_width, qty_width = calculate_column_widths(box_width * 6)  
            
            separator = "+" + "-"*(item_width+2) + "+" + "-"*(price_width+2) + "+" + "-"*(qty_width+2) + "+"
            header = f"| {'Item':^{item_width}} | {'Price':^{price_width}} | {'Qty':^{qty_width}} |"
            
            file.write(separator + "\n")
            file.write(header + "\n")
            file.write(separator + "\n")
            file.write(content)
            file.write(separator + "\n\n")
            
            total_line = f"| {'Total Sale:':<{item_width}} | {format_currency(total_sale):^{price_width}} | {'':^{qty_width}} |"
            profit_line = f"| {'Profit:':<{item_width}} | {format_currency(total_profit):^{price_width}} | {'':^{qty_width}} |"
            
            file.write(separator + "\n")
            file.write(total_line + "\n")
            file.write(profit_line + "\n")
            file.write(separator + "\n")
            
        messagebox.showinfo("Success", "Receipt saved successfully!")

def showHistory():
    history_window = Toplevel(root)
    history_window.title("Purchase History")
    history_window.geometry("600x400")
    history_window.configure(bg=CREAM)

    Label(history_window, text="Purchase History", font=("Arial", 16, "bold"), bg=CREAM, fg=CHOCOLATE_DARK).pack(pady=10)

    history_text = Text(history_window, height=20, width=70, bg=CREAM, fg=CHOCOLATE_DARK, font=("Courier", 10))
    history_text.pack(padx=10, pady=10)

    if history:
        for entry in history:
            history_text.insert(END, entry + "\n")
    else:
        history_text.insert(END, "No transactions yet.\n")

    history_text.config(state=DISABLED)

    Button(history_window, text="Close", command=history_window.destroy, bg=CHOCOLATE_DARK, fg="white").pack(pady=10)
    
def showRemainingItems():
    inventory_window = Toplevel(root)
    inventory_window.title("Remaining Items")
    inventory_window.geometry("600x400")
    inventory_window.configure(bg=CREAM)

    Label(inventory_window, text="Remaining Items", font=("Arial", 16, "bold"), bg=CREAM, fg=CHOCOLATE_DARK).pack(pady=10)

    inventory_text = Text(inventory_window, height=20, width=70, bg=CREAM, fg=CHOCOLATE_DARK, font=("Courier", 10))
    inventory_text.pack(padx=10, pady=10)

    header = f"{'Item':<30}{'Remaining Stock':<15}"
    inventory_text.insert(END, header + "\n")
    inventory_text.insert(END, "-" * 50 + "\n")
    for item in data:
        line = f"{item['Item']:<30}{item['Inventory count']:<15}"
        inventory_text.insert(END, line + "\n")

    inventory_text.config(state=DISABLED)

    Button(inventory_window, text="Close", command=inventory_window.destroy, bg=CHOCOLATE_DARK, fg="white").pack(pady=10)
    
def restockItems():
    if hasattr(root, 'restock_window') and root.restock_window.winfo_exists():
        root.restock_window.lift()  
        return
    
    root.restock_window = Toplevel(root)
    root.restock_window.title("Restock Items")
    root.restock_window.geometry("600x400")
    root.restock_window.configure(bg=CREAM)

    Label(root.restock_window, text="Restock Items", font=("Arial", 16, "bold"), bg=CREAM, fg=CHOCOLATE_DARK).pack(pady=10)

    restock_frame = Frame(root.restock_window, bg=CREAM)
    restock_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

    canvas = Canvas(restock_frame, bg=CREAM)
    scrollbar = Scrollbar(restock_frame, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=CREAM)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    for index, item in enumerate(data):
        item_label = Label(scrollable_frame, text=item['Item'], bg=CREAM, fg=CHOCOLATE_DARK, font=("Arial", 10))
        item_label.grid(row=index, column=0, padx=5, pady=5, sticky="w")

        stock_label = Label(scrollable_frame, text=f"Current Stock: {item['Inventory count']}", bg=CREAM, fg=CHOCOLATE_DARK, font=("Arial", 10))
        stock_label.grid(row=index, column=1, padx=5, pady=5, sticky="w")

        restock_entry = Entry(scrollable_frame, font=("Arial", 10), width=10, bg=CREAM, fg=CHOCOLATE_DARK)
        restock_entry.grid(row=index, column=2, padx=5, pady=5)

        restock_button = Button(scrollable_frame, text="Restock", bg=GOLD, fg=CHOCOLATE_DARK, font=("Arial", 10),
                                command=lambda i=index, e=restock_entry: updateStock(i, e.get(), stock_label))
        restock_button.grid(row=index, column=3, padx=5, pady=5)

    Button(root.restock_window, text="Done", command=root.restock_window.destroy, bg=CHOCOLATE_DARK, fg="white", font=("Arial", 10)).pack(pady=10)
    
def updateStock(index, quantity, stock_label):
    global totalCounter
    try:
        quantity_int = int(quantity)
        if quantity_int < 0:
            raise ValueError("Quantity cannot be negative.")
    except ValueError:
        error_window = Toplevel(root.restock_window)
        error_window.title("Error")
        error_window.geometry("300x150")
        error_window.configure(bg=CREAM)
        Label(error_window, text="Invalid quantity input!", fg="red", bg=CREAM, font=("Arial", 12)).pack(pady=20)
        Button(error_window, text="OK", command=error_window.destroy, bg=CHOCOLATE_DARK, fg="white", font=("Arial", 10)).pack(pady=10)
        return

    data[index]['Inventory count'] += quantity_int

    stock_label.config(text=f"Current Stock: {data[index]['Inventory count']}")

    if 'stock_label' in data[index]:
        data[index]['stock_label'].config(text=f"Stock: {data[index]['Inventory count']}")

    success_window = Toplevel(root.restock_window)
    success_window.title("Restock Successful")
    success_window.geometry("300x200")
    success_window.configure(bg=CREAM)

    Label(success_window, text=f"Restocked {data[index]['Item']}", bg=CREAM, fg="green", font=("Arial", 12)).pack(pady=10)
    Label(success_window, text=f"Quantity Added: {quantity_int}", bg=CREAM, fg=CHOCOLATE_DARK, font=("Arial", 10)).pack(pady=5)
    Label(success_window, text=f"New Stock: {data[index]['Inventory count']}", bg=CREAM, fg=CHOCOLATE_DARK, font=("Arial", 10)).pack(pady=5)

    Button(success_window, text="OK", command=success_window.destroy, bg=CHOCOLATE_DARK, fg="white", font=("Arial", 10)).pack(pady=10)
    
def on_resize(event):
    updateReceipt()

Label(root, text="Point of Sale", font=("Arial", 20, "bold"), 
      bg="#4a2a0a", fg="white").pack(pady=10, fill=X) 

content_Box = Text(root, height=10, width=70, bg=CREAM, fg=CHOCOLATE_DARK, font=("Courier", 10))
content_Box.pack(padx=10, pady=10, fill=BOTH)
updateReceipt()

button_frame = Frame(root, bg=CHOCOLATE_MEDIUM)
button_frame.pack(pady=10)

center_frame = Frame(button_frame, bg=CHOCOLATE_MEDIUM)
center_frame.pack()

num_columns = 7  
for index, item in enumerate(data):
    frame = Frame(center_frame, bg=CHOCOLATE_LIGHT, relief=RIDGE, bd=2, width=120, height=120)
    frame.grid(row=index // num_columns, column=index % num_columns, padx=5, pady=5, sticky="nsew")
    frame.grid_propagate(False)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    item_label = Label(frame, text=item['Item'], bg=CHOCOLATE_LIGHT, fg=CREAM, 
                      font=("Arial", 8, "bold"), wraplength=100, justify="center")
    item_label.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    
    price_label = Label(frame, text=f"Price: {format_currency(item['Selling Price'])}", 
                       bg=CHOCOLATE_LIGHT, fg=CREAM, font=("Arial", 8))
    price_label.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    
    stock_label = Label(frame, text=f"Stock: {item['Inventory count']}", 
                       bg=CHOCOLATE_LIGHT, fg=CREAM, font=("Arial", 8))
    stock_label.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
    
    quantity_entry = Entry(frame, font=("Arial", 8), width=5, justify="center", bg=CREAM, fg=CHOCOLATE_DARK)
    quantity_entry.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
    
    add_button = Button(frame, text="Add to Cart", 
                       command=lambda n=index, q=quantity_entry: process_sale(n, q.get()),
                       bg=GOLD, fg=CHOCOLATE_DARK, font=("Arial", 8))
    add_button.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
    totalCounter += 1

    item['entry_widget'] = quantity_entry
    item['stock_label'] = stock_label

action_frame = Frame(root, bg=CHOCOLATE_MEDIUM)
action_frame.pack(pady=5)

btn1 = Button(action_frame, text="Total", command=totalCalculation, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold"))
btn1.pack(side=LEFT, padx=5)

Button(action_frame, text="Reset", command=reset, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

Button(action_frame, text="Save", command=saveToFile, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

Button(action_frame, text="History", command=showHistory, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

Button(action_frame, text="Inventory", command=showRemainingItems, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

Button(action_frame, text="Restock", command=restockItems, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

Button(action_frame, text="Exit", command=root.destroy, height=2, width=12, 
       bg="#4a2a0a", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

root.bind('<Configure>', on_resize)

root.mainloop()