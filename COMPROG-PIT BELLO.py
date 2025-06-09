import tkinter as tk
from tkinter import ttk, font, messagebox, simpledialog
from datetime import datetime
import os

# --- Constants ---
DEFAULT_PRODUCTS_FILE = "products.txt"
DEFAULT_EXPORT_FILE = "exported_products.txt"
TAX_RATE = 0.08
LOW_STOCK_THRESHOLD = 5
PRODUCT_CATEGORIES = {
    "food": "#FF6B6B", "drinks": "#4ECDC4", "snacks": "#C44BD5", "non-food": "#F0AD4E"
}
DEFAULT_CATEGORY_COLOR = "#777777"

# --- Utility Functions ---
def show_error(title, message):
    messagebox.showerror(title, message)

def show_info(title, message):
    messagebox.showinfo(title, message, icon="info")

def validate_price(price_str):
    try:
        price = float(price_str)
        if price <= 0: raise ValueError("Price must be positive.")
        return price
    except ValueError: return None

def validate_stock(stock_str):
    try:
        stock = int(stock_str)
        if stock < 0: raise ValueError("Stock cannot be negative.")
        return stock
    except ValueError: return None

class Product:
    """Represents a product."""
    def __init__(self, id, name, price, category, stock):
        self.id, self.name, self.price, self.category, self.stock = id, name, price, category, stock

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "category": self.category, "stock": self.stock}

    @classmethod
    def from_string(cls, line):
        try:
            id_str, name, price_str, category, stock_str = line.strip().split("|")
            return cls(int(id_str), name, float(price_str), category, int(stock_str))
        except ValueError:
            print(f"Skipping invalid product line: {line.strip()}")
            return None

    def to_string(self):
        return f"{self.id}|{self.name}|{self.price}|{self.category}|{self.stock}"

class ProductCatalog:
    """Manages products."""
    def __init__(self, filename=DEFAULT_PRODUCTS_FILE):
        self.filename = filename
        self.products = {}
        self._load_products()
        if not self.products:
            self._initialize_default_products()
            self._save_products()

    def _initialize_default_products(self):
        default_data = [
            (1, "Instant Noodles", 12.00, "Food", 10), (2, "Canned Sardines", 25.00, "Food", 5),
            (3, "Softdrinks", 15.00, "Drinks", 3), (4, "Snack Chips", 10.00, "Snacks", 12),
            (5, "Biscuits", 8.00, "Snacks", 8), (6, "Coffee Stick", 7.00, "Drinks", 20),
            (7, "Laundry Soap", 20.00, "Non-Food", 5), (8, "Shampoo Sachet", 6.00, "Non-Food", 15)
        ]
        for pid, name, price, category, stock in default_data:
            self.products[pid] = Product(pid, name, price, category, stock)

    def get_all_products(self): return list(self.products.values())
    def get_product_by_id(self, product_id): return self.products.get(product_id)

    def add_product(self, name, price, category, stock):
        if not all([name, category]) or price is None: return "Missing product information."
        if any(prod.name.lower() == name.lower() for prod in self.products.values()): return "Product name already exists."
        new_id = (max(self.products.keys()) + 1) if self.products else 1
        self.products[new_id] = Product(new_id, name, price, category, stock)
        self._save_products()
        return None

    def update_product(self, product_id, name, price, category, stock):
        product = self.get_product_by_id(product_id)
        if not product: return "Product not found."
        if not all([name, category]) or price is None: return "Missing product information."
        if any(p.name.lower() == name.lower() and p.id != product_id for p in self.products.values()): return "Product name already exists for another ID."
        product.name, product.price, product.category, product.stock = name, price, category, stock
        self._save_products()
        return None

    def delete_product(self, product_id):
        if product_id not in self.products: return "Product not found."
        del self.products[product_id]
        self._save_products()
        return None

    def _load_products(self):
        if not os.path.exists(self.filename): return
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    product = Product.from_string(line)
                    if product: self.products[product.id] = product
        except Exception as e: print(f"Error loading products: {e}")

    def _save_products(self):
        try:
            with open(self.filename, "w") as f:
                for product in self.products.values(): f.write(product.to_string() + "\n")
        except Exception as e: print(f"Error saving products: {e}")

    def export_to_txt(self, export_filename=DEFAULT_EXPORT_FILE):
        try:
            with open(export_filename, "w") as f:
                for product in self.products.values(): f.write(product.to_string() + "\n")
            msg = f"Products exported to '{export_filename}' successfully."
            print(msg)
            return True, msg
        except Exception as e:
            error_msg = f"Error exporting products: {e}"
            print(error_msg)
            return False, error_msg

    def check_low_stock(self):
        low_stock_products = [p for p in self.products.values() if p.stock <= LOW_STOCK_THRESHOLD]
        if low_stock_products:
            message = "Warning: Low stock for the following products:\n" + \
                      "".join([f"- {p.name} (Stock: {p.stock})\n" for p in low_stock_products])
            messagebox.showwarning("Low Stock Alert", message)

    def decrease_stock(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product:
            if product.stock >= quantity:
                product.stock -= quantity
                self._save_products()
                self.check_low_stock()
                return True
            else:
                show_error("Stock Error", f"Not enough stock for {product.name}. Available: {product.stock}")
                return False
        else:
            print(f"Product with ID {product_id} not found for stock decrease.")
            return False

class OrderItem:
    """Represents an item in an order."""
    def __init__(self, product, quantity):
        self.product, self.quantity = product, quantity
    @property
    def id(self): return self.product.id
    @property
    def name(self): return self.product.name
    @property
    def price(self): return self.product.price
    @property
    def subtotal(self): return self.price * self.quantity

class Order:
    """Manages the current order."""
    def __init__(self, catalog):
        self.items, self.tax_rate, self.discount_percent, self.catalog = [], TAX_RATE, 0, catalog

    def add_item(self, product, quantity=1):
        if quantity <= 0: return "Quantity must be greater than zero."
        if product.stock < quantity: return f"Not enough stock of {product.name}. Only {product.stock} left."
        for item in self.items:
            if item.id == product.id:
                if product.stock < item.quantity + quantity: return f"Not enough stock of {product.name} to add {quantity} more. Only {product.stock - item.quantity} additional available."
                item.quantity += quantity
                return None
        self.items.append(OrderItem(product, quantity))
        return None

    def remove_item(self, item_index):
        if 0 <= item_index < len(self.items):
            del self.items[item_index]
            return None
        return "Invalid item index."

    def update_item_quantity(self, item_index, new_quantity):
        if not (0 <= item_index < len(self.items)): return "Invalid item index."
        if new_quantity <= 0: return self.remove_item(item_index)
        item = self.items[item_index]
        product_in_catalog = self.catalog.get_product_by_id(item.id)
        if not product_in_catalog: return "Product not found in catalog (should not happen)."
        if product_in_catalog.stock < new_quantity: return f"Not enough stock for {item.name}. Available: {product_in_catalog.stock}"
        item.quantity = new_quantity
        return None

    def get_subtotal(self): return sum(item.subtotal for item in self.items)
    def get_discount_amount(self): return self.get_subtotal() * (self.discount_percent / 100)
    def get_subtotal_after_discount(self): return self.get_subtotal() - self.get_discount_amount()
    def get_tax(self): return self.get_subtotal_after_discount() * self.tax_rate
    def get_total(self): return self.get_subtotal_after_discount() + self.get_tax()

    def apply_discount(self, discount_percent_str):
        try:
            discount = float(discount_percent_str)
            if not (0 <= discount <= 100): return "Invalid discount percent (must be 0-100)."
            self.discount_percent = discount
            return None
        except ValueError: return "Invalid discount format. Please enter a number."

    def clear(self): self.items, self.discount_percent = [], 0

class SimplePOSApp:
    """Main application class."""
    def __init__(self, root):
        self.root = root
        self.root.title("Simple POS System"); self.root.geometry("900x700")
        self.catalog = ProductCatalog(); self.order = Order(self.catalog)

        common_categories = PRODUCT_CATEGORIES
        self.light_mode_colors = {
            'bg': '#f0f0f0', 'panel': '#ffffff', 'accent': '#007bff', 'text': '#333333',
            'button_bg': '#007bff', 'button_fg': 'white', 'alt_button_bg': '#0056b3',
            'dialog_bg': '#ffffff', 'dialog_fg': '#333333',
            'report_button_bg': '#28a745', 'report_button_fg': 'white',
            'delete_button_bg': '#dc3545', 'delete_button_fg': 'white', **common_categories
        }
        self.dark_mode_colors = {
            'bg': '#2c3e50', 'panel': '#34495e', 'accent': '#3498db', 'text': '#ecf0f1',
            'button_bg': '#3498db', 'button_fg': 'white', 'alt_button_bg': '#2980b9',
            'dialog_bg': '#2d3e50', 'dialog_fg': '#ecf0f1',
            'report_button_bg': '#2ecc71', 'report_button_fg': 'white',
            'delete_button_bg': '#e74c3c', 'delete_button_fg': 'white', **common_categories
        }
        self.current_colors = self.light_mode_colors; self.dark_mode = False

        self._configure_styles(); self._create_layout()
        self.update_cart_display(); self.update_total_display()
        self.catalog.check_low_stock()

    def _get_color(self, key): return self.current_colors.get(key, '#000000')

    def _configure_styles(self):
        font.nametofont("TkDefaultFont").configure(family="Arial", size=10)
        self.fonts = {
            'title': font.Font(family="Arial", size=18, weight="bold"),
            'product_name': font.Font(family="Arial", size=11, weight="bold"),
            'product_details': font.Font(family="Arial", size=9),
            'button': font.Font(family="Arial", size=11, weight="bold"),
            'small_button': font.Font(family="Arial", size=9, weight="bold"),
            'dialog_title': font.Font(family="Arial", size=14, weight="bold"),
            'dialog_label': font.Font(family="Arial", size=11),
            'cart_item': font.Font(family="Arial", size=10),
            'total_label': font.Font(family="Arial", size=12, weight="bold"),
        }
        self.style = ttk.Style(); self.style.theme_use("clam")
        self.root.configure(bg=self._get_color('bg'))
        self.style.configure("TFrame", background=self._get_color('bg'))
        self.style.configure("TLabel", background=self._get_color('panel'), foreground=self._get_color('text'), font=self.fonts['dialog_label'])
        self.style.configure("Treeview", background=self._get_color('panel'), foreground=self._get_color('text'), fieldbackground=self._get_color('panel'))
        self.style.map("Treeview", background=[('selected', self._get_color('accent'))], foreground=[('selected', self._get_color('button_fg'))])
        self.style.configure("TButton", background=self._get_color('button_bg'), foreground=self._get_color('button_fg'), font=self.fonts['button'], relief="raised", borderwidth=1, padding=5)
        self.style.map("TButton", background=[("active", self._get_color('alt_button_bg'))])
        self.style.configure("Small.TButton", font=self.fonts['small_button'], padding=3)
        self.style.configure("Delete.TButton", background=self._get_color('delete_button_bg'), foreground=self._get_color('delete_button_fg'))
        self.style.map("Delete.TButton", background=[("active", self._get_color('alt_button_bg'))])
        self.style.configure("Report.TButton", background=self._get_color('report_button_bg'), foreground=self._get_color('report_button_fg'))
        self.style.map("Report.TButton", background=[("active", self._get_color('alt_button_bg'))])

    def _create_layout(self):
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10"); self.main_frame.pack(fill="both", expand=True)
        paned_window = ttk.PanedWindow(self.main_frame, orient=tk.HORIZONTAL); paned_window.pack(fill="both", expand=True)
        self._create_catalog_panel(paned_window); self._create_cart_panel(paned_window)
        paned_window.add(self.catalog_outer_frame, weight=2); paned_window.add(self.cart_outer_frame, weight=1)

        controls_frame = ttk.Frame(self.root, padding="10 5"); controls_frame.pack(side="bottom", fill="x")
        self.management_menu_var = tk.StringVar(value="Manage Products")
        m_ops = ["Manage Products", "Add Product", "Update Product", "Delete Product", "Export Products"]
        self.management_menu = ttk.OptionMenu(controls_frame, self.management_menu_var, m_ops[0], *m_ops, command=self._handle_management_action, style="TButton")
        self.management_menu.pack(side="left", padx=5)
        self.dark_mode_button = ttk.Button(controls_frame, text="Toggle Theme", command=self.toggle_dark_mode, style="TButton")
        self.dark_mode_button.pack(side="left", padx=5)
        self.generate_report_button = ttk.Button(controls_frame, text="Daily Report", command=self.generate_daily_report, style="Report.TButton")
        self.generate_report_button.pack(side="left", padx=5)
        self.refresh_catalog_button = ttk.Button(controls_frame, text="Refresh Catalog", command=self.update_product_grid, style="TButton")
        self.refresh_catalog_button.pack(side="right", padx=5)

    def _handle_management_action(self, selection):
        action_map = {"Add Product": self._add_product_dialog, "Update Product": self._update_product_dialog,
                      "Delete Product": self._delete_product_dialog, "Export Products": self._export_products_action}
        action = action_map.get(selection)
        if action: action()
        self.management_menu_var.set("Manage Products")

    def _export_products_action(self):
        success, message = self.catalog.export_to_txt()
        show_info("Export Successful", message) if success else show_error("Export Failed", message)

    def _create_catalog_panel(self, parent_paned_window):
        self.catalog_outer_frame = ttk.Frame(parent_paned_window, style="Panel.TFrame", relief="sunken", borderwidth=1)
        ttk.Label(self.catalog_outer_frame, text="Products Catalog", font=self.fonts['title'], anchor="center").pack(pady=10, fill="x")
        scroll_content_frame = ttk.Frame(self.catalog_outer_frame); scroll_content_frame.pack(fill="both", expand=True)
        self.catalog_canvas = tk.Canvas(scroll_content_frame, bg=self._get_color('panel'), highlightthickness=0)
        self.catalog_scrollbar = ttk.Scrollbar(scroll_content_frame, orient="vertical", command=self.catalog_canvas.yview)
        self.catalog_canvas.configure(yscrollcommand=self.catalog_scrollbar.set)
        self.catalog_canvas.pack(side="left", fill="both", expand=True); self.catalog_scrollbar.pack(side="right", fill="y")
        self.products_frame = ttk.Frame(self.catalog_canvas, style="TFrame")
        self.catalog_canvas.create_window((0, 0), window=self.products_frame, anchor="nw", tags="self.products_frame")
        self.products_frame.bind("<Configure>", lambda e: self.catalog_canvas.configure(scrollregion=self.catalog_canvas.bbox("all")))
        self.catalog_canvas.bind_all("<MouseWheel>", self._on_mousewheel_catalog)
        self.product_buttons = []; self.update_product_grid()

    def _on_mousewheel_catalog(self, event):
        widget_under_mouse = self.root.winfo_containing(event.x_root, event.y_root)
        if widget_under_mouse is self.catalog_canvas or self.catalog_canvas.winfo_children().__contains__(widget_under_mouse):
            if event.delta: self.catalog_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            elif event.num == 4: self.catalog_canvas.yview_scroll(-1, "units") # Linux scroll up
            elif event.num == 5: self.catalog_canvas.yview_scroll(1, "units")  # Linux scroll down

    def update_product_grid(self):
        for widget in self.products_frame.winfo_children(): widget.destroy()
        self.product_buttons.clear()
        products = sorted(self.catalog.get_all_products(), key=lambda p: p.name)
        if not products:
            ttk.Label(self.products_frame, text="No products available.", style="TLabel", font=self.fonts['dialog_label']).pack(padx=20, pady=20)
            return
        cols = 3
        for i, product in enumerate(products):
            row, col = divmod(i, cols)
            button_frame = self._create_product_button_frame(self.products_frame, product)
            button_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.products_frame.grid_columnconfigure(col, weight=1)
        self.root.after(100, lambda: self.catalog_canvas.configure(scrollregion=self.catalog_canvas.bbox("all")))

    def _create_product_button_frame(self, parent, product):
        bg_color = PRODUCT_CATEGORIES.get(product.category.lower(), DEFAULT_CATEGORY_COLOR)
        frame = tk.Frame(parent, bg=bg_color, relief="raised", borderwidth=2, padx=5, pady=5)
        frame.bind("<Button-1>", lambda e, p=product: self._add_to_cart(p))
        for text_info, font_style in [(product.name, 'product_name'), (f"Price: P{product.price:.2f}", 'product_details'), (f"Stock: {product.stock}", 'product_details')]:
            lbl = tk.Label(frame, text=text_info, font=self.fonts[font_style], bg=bg_color, fg="white")
            lbl.pack(fill="x"); lbl.bind("<Button-1>", lambda e, p=product: self._add_to_cart(p))
        return frame

    def _create_cart_panel(self, parent_paned_window):
        self.cart_outer_frame = ttk.Frame(parent_paned_window, style="Panel.TFrame", relief="sunken", borderwidth=1)
        ttk.Label(self.cart_outer_frame, text="Your Cart", font=self.fonts['title'], anchor="center").pack(pady=10, fill="x")
        cols = ("name", "qty", "price", "subtotal")
        self.cart_tree = ttk.Treeview(self.cart_outer_frame, columns=cols, show="headings", style="Treeview")
        for col_name in cols: self.cart_tree.heading(col_name, text=col_name.capitalize()); self.cart_tree.column(col_name, width=80, anchor="center")
        self.cart_tree.column("name", width=120, anchor="w"); self.cart_tree.pack(fill="both", expand=True, padx=5, pady=5)

        cart_actions_frame = ttk.Frame(self.cart_outer_frame); cart_actions_frame.pack(fill="x", pady=5)
        self.increase_qty_button = ttk.Button(cart_actions_frame, text="+ Qty", command=self._increase_selected_cart_item_qty, style="Small.TButton"); self.increase_qty_button.pack(side="left", padx=5)
        self.decrease_qty_button = ttk.Button(cart_actions_frame, text="- Qty", command=self._decrease_selected_cart_item_qty, style="Small.TButton"); self.decrease_qty_button.pack(side="left", padx=5)
        self.remove_item_button = ttk.Button(cart_actions_frame, text="Remove Item", command=self._remove_selected_cart_item, style="Delete.TButton"); self.remove_item_button.pack(side="right", padx=5)

        total_section_frame = ttk.Frame(self.cart_outer_frame, padding="5"); total_section_frame.pack(side="bottom", fill="x")
        discount_frame = ttk.Frame(total_section_frame); discount_frame.pack(fill="x", pady=2)
        ttk.Label(discount_frame, text="Discount (%):", font=self.fonts['dialog_label']).pack(side="left", padx=(0,5))
        self.discount_entry = ttk.Entry(discount_frame, width=5, font=self.fonts['dialog_label']); self.discount_entry.pack(side="left", padx=5)
        self.apply_discount_button = ttk.Button(discount_frame, text="Apply", command=self._apply_discount, style="Small.TButton"); self.apply_discount_button.pack(side="left")

        self.subtotal_label = ttk.Label(total_section_frame, text="Subtotal: P0.00", font=self.fonts['total_label'], anchor="e"); self.subtotal_label.pack(fill="x", pady=1)
        self.discount_applied_label = ttk.Label(total_section_frame, text="Discount: -P0.00", font=self.fonts['total_label'], anchor="e"); self.discount_applied_label.pack(fill="x", pady=1)
        self.tax_label = ttk.Label(total_section_frame, text=f"Tax ({self.order.tax_rate*100:.0f}%): P0.00", font=self.fonts['total_label'], anchor="e"); self.tax_label.pack(fill="x", pady=1)
        self.total_label = ttk.Label(total_section_frame, text="Total: P0.00", font=self.fonts['total_label'], anchor="e"); self.total_label.pack(fill="x", pady=3)
        self.checkout_button = ttk.Button(total_section_frame, text="Checkout", command=self._checkout, style="Report.TButton"); self.checkout_button.pack(fill="x", pady=5)

    def _add_to_cart(self, product):
        err_msg = self.order.add_item(product)
        if err_msg: show_error("Cart Error", err_msg); return
        self.update_cart_display(); self.update_total_display(); self.update_product_grid()

    def _get_selected_cart_item_index(self):
        selected_iid = self.cart_tree.focus()
        if not selected_iid: show_error("Cart Action", "Please select an item in the cart first."); return None
        try: return self.cart_tree.get_children().index(selected_iid)
        except ValueError: return None

    def _update_cart_item_qty_handler(self, increase=True):
        item_index = self._get_selected_cart_item_index()
        if item_index is not None:
            item = self.order.items[item_index]
            new_qty = item.quantity + 1 if increase else item.quantity - 1
            if new_qty > 0 :
                err_msg = self.order.update_item_quantity(item_index, new_qty)
                if err_msg: show_error("Quantity Error", err_msg)
            else: # quantity becomes 0 or less, remove item
                self.order.remove_item(item_index)
            self.update_cart_display(); self.update_total_display(); self.update_product_grid()

    def _increase_selected_cart_item_qty(self): self._update_cart_item_qty_handler(increase=True)
    def _decrease_selected_cart_item_qty(self): self._update_cart_item_qty_handler(increase=False)

    def _remove_selected_cart_item(self):
        item_index = self._get_selected_cart_item_index()
        if item_index is not None:
            self.order.remove_item(item_index)
            self.update_cart_display(); self.update_total_display(); self.update_product_grid()

    def update_cart_display(self):
        for item_row in self.cart_tree.get_children(): self.cart_tree.delete(item_row)
        for item in self.order.items:
            self.cart_tree.insert("", "end", values=(item.name, item.quantity, f"P{item.price:.2f}", f"P{item.subtotal:.2f}"))

    def update_total_display(self):
        subtotal, disc_amt, tax, total = self.order.get_subtotal(), self.order.get_discount_amount(), self.order.get_tax(), self.order.get_total()
        self.subtotal_label.config(text=f"Subtotal: P{subtotal:.2f}")
        self.discount_applied_label.config(text=f"Discount: -P{disc_amt:.2f}")
        self.tax_label.config(text=f"Tax ({self.order.tax_rate*100:.0f}%): P{tax:.2f}")
        self.total_label.config(text=f"Total: P{total:.2f}")

    def _apply_discount(self):
        err_msg = self.order.apply_discount(self.discount_entry.get())
        if err_msg: show_error("Discount Error", err_msg); self.discount_entry.delete(0, tk.END); return
        self.update_total_display(); show_info("Discount", "Discount applied successfully.")

    def _checkout(self):
        if not self.order.items: show_error("Checkout Error", "Your cart is empty."); return
        total = self.order.get_total()
        payment = simpledialog.askfloat("Payment", f"Total amount due: P{total:.2f}\nEnter amount received:", parent=self.root, minvalue=total)
        if payment is None: return
        if payment < total: show_error("Payment Error", f"Amount received (P{payment:.2f}) is less than total (P{total:.2f})."); return
        change = payment - total
        for item in self.order.items:
            if not self.catalog.decrease_stock(item.id, item.quantity):
                show_error("Stock Error", f"Could not decrease stock for {item.name}. Checkout aborted."); return
        self._log_transaction(self.order, payment, change)
        receipt = f"--- Receipt ---\n" + \
                  "".join([f"{item.name} x{item.quantity} @ P{item.price:.2f} = P{item.subtotal:.2f}\n" for item in self.order.items]) + \
                  f"--------------------\nSubtotal: P{self.order.get_subtotal():.2f}\n" + \
                  (f"Discount ({self.order.discount_percent}%): -P{self.order.get_discount_amount():.2f}\nSubtotal After Discount: P{self.order.get_subtotal_after_discount():.2f}\n" if self.order.discount_percent > 0 else "") + \
                  f"Tax ({self.order.tax_rate*100:.0f}%): P{self.order.get_tax():.2f}\n--------------------\n" + \
                  f"TOTAL: P{total:.2f}\nAmount Paid: P{payment:.2f}\nChange: P{change:.2f}\n--------------------\nThank you!\n"
        show_info("Checkout Successful", receipt)
        self.order.clear(); self.discount_entry.delete(0, tk.END)
        self.update_cart_display(); self.update_total_display(); self.update_product_grid()
        self.catalog.check_low_stock()

    def _log_transaction(self, order_details, payment_received, change):
        now = datetime.now(); date_str, time_str = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")
        filename = f"transactions_{date_str}.txt"
        try:
            with open(filename, "a") as f:
                f.write(f"--- Transaction: {date_str} {time_str} ---\n")
                for item in order_details.items: f.write(f"  Item: {item.name} (ID: {item.id}), Qty: {item.quantity}, Unit Price: {item.price:.2f}, Subtotal: {item.subtotal:.2f}\n")
                f.write(f"  Order Subtotal: {order_details.get_subtotal():.2f}\n")
                if order_details.discount_percent > 0: f.write(f"  Discount Applied: {order_details.discount_percent}%\n  Discount Amount: {order_details.get_discount_amount():.2f}\n  Subtotal After Discount: {order_details.get_subtotal_after_discount():.2f}\n")
                f.write(f"  Tax ({order_details.tax_rate*100:.0f}%): {order_details.get_tax():.2f}\n  Total Amount: {order_details.get_total():.2f}\n")
                f.write(f"  Payment Received: {payment_received:.2f}\n  Change Given: {change:.2f}\n--------------------------------------------------\n\n")
        except Exception as e: print(f"Error logging transaction: {e}"); show_error("Logging Error", f"Could not write to transaction log: {e}")

    def _product_dialog_helper(self, title, initial_values=None, is_update=False, product_id=None):
        dialog = ProductDialog(self.root, self, title=title, initial_values=initial_values)
        if dialog.result:
            name, price_str, category, stock_str = dialog.result
            price, stock = validate_price(price_str), validate_stock(stock_str)
            if price is None: show_error("Input Error", "Invalid price. Must be a positive number."); return
            if stock is None: show_error("Input Error", "Invalid stock. Must be a non-negative integer."); return
            if not name or not category: show_error("Input Error", "Name and Category cannot be empty."); return

            err_msg = self.catalog.update_product(product_id, name, price, category, stock) if is_update else self.catalog.add_product(name, price, category, stock)
            if err_msg: show_error(f"{'Update' if is_update else 'Add'} Product Error", err_msg)
            else:
                show_info("Success", f"Product {'updated' if is_update else 'added'} successfully.")
                self.update_product_grid()
                if is_update: self.update_cart_display() # If product in cart was updated

    def _add_product_dialog(self):
        self._product_dialog_helper(title="Add New Product")

    def _update_product_dialog(self):
        product_id_str = simpledialog.askstring("Update Product", "Enter Product ID to update:", parent=self.root)
        if not product_id_str: return
        try: product_id = int(product_id_str)
        except ValueError: show_error("Input Error", "Invalid Product ID format."); return
        product_to_update = self.catalog.get_product_by_id(product_id)
        if not product_to_update: show_error("Update Product Error", f"Product with ID {product_id} not found."); return
        self._product_dialog_helper(title=f"Update Product (ID: {product_id})", initial_values=product_to_update.to_dict(), is_update=True, product_id=product_id)

    def _delete_product_dialog(self):
        product_id_str = simpledialog.askstring("Delete Product", "Enter Product ID to delete:", parent=self.root)
        if not product_id_str: return
        try: product_id = int(product_id_str)
        except ValueError: show_error("Input Error", "Invalid Product ID format."); return
        if any(item.id == product_id for item in self.order.items):
            if not messagebox.askyesno("Confirm Delete", f"Product ID {product_id} is in the current cart. Removing it will also remove it from the cart. Continue?"): return
        err_msg = self.catalog.delete_product(product_id)
        if err_msg: show_error("Delete Product Error", err_msg)
        else:
            show_info("Success", "Product deleted successfully.")
            self.update_product_grid()
            self.order.items = [item for item in self.order.items if item.id != product_id] # Remove from cart
            self.update_cart_display(); self.update_total_display()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.current_colors = self.dark_mode_colors if self.dark_mode else self.light_mode_colors
        self._configure_styles()
        self.root.configure(bg=self._get_color('bg'))
        self.catalog_canvas.configure(bg=self._get_color('panel'))
        for label in [self.subtotal_label, self.tax_label, self.total_label, self.discount_applied_label]:
            label.configure(background=self._get_color('bg'), foreground=self._get_color('text')) # Assuming labels are on 'bg'
        self.update_product_grid(); self.update_cart_display(); self.update_total_display()
        print(f"Switched to {'Dark' if self.dark_mode else 'Light'} Mode")

    def generate_daily_report(self):
        now = datetime.now(); date_str = now.strftime("%Y-%m-%d")
        trans_file, report_file = f"transactions_{date_str}.txt", f"daily_sales_report_{date_str}.txt"
        sales_val, tax_coll, disc_given, prod_summary = 0, 0, 0, {}
        try:
            if not os.path.exists(trans_file): show_info("Report Generation", f"No transactions for {date_str}."); return
            with open(trans_file, "r") as f_trans:
                for line in f_trans:
                    line = line.strip()
                    if "Item:" in line:
                        parts = line.split(','); name_part = parts[0].split("Item:")[1].split("(ID:")[0].strip()
                        qty_part = int(parts[1].split("Qty:")[1].strip()); subtotal_part = float(parts[3].split("Subtotal:")[1].strip())
                        prod_summary.setdefault(name_part, {'qty': 0, 'value': 0.0})
                        prod_summary[name_part]['qty'] += qty_part; prod_summary[name_part]['value'] += subtotal_part
                    elif "Total Amount:" in line: sales_val += float(line.split("Total Amount:")[1].strip())
                    elif "Tax (" in line: tax_coll += float(line.split("):")[1].strip())
                    elif "Discount Amount:" in line: disc_given += float(line.split("Discount Amount:")[1].strip())

            report_content = f"Daily Sales Report - {date_str}\n========================================\n\n"
            report_content += "--- Product Sales Summary ---\n"
            if prod_summary: report_content += "".join([f"- {name}: Qty: {data['qty']}, Value: P{data['value']:.2f}\n" for name, data in sorted(prod_summary.items())])
            else: report_content += "No individual product sales logged.\n"
            report_content += f"\n--- Financial Summary ---\nTotal Gross Sales (after discounts, before tax): P{(sales_val - tax_coll):.2f}\n"
            report_content += f"Total Discounts Given: P{disc_given:.2f}\nTotal Tax Collected: P{tax_coll:.2f}\nTotal Net Sales (including tax): P{sales_val:.2f}\n"
            report_content += "\n========================================\nEnd of Report\n"
            with open(report_file, "w") as f_report: f_report.write(report_content)
            ReportDialog(self.root, "Daily Sales Report", report_content, self)
            show_info("Report Generated", f"Daily report saved to {report_file}\nand displayed.")
        except FileNotFoundError: show_error("Report Error", f"Transaction log '{trans_file}' not found.")
        except Exception as e: show_error("Report Error", f"Error generating report: {e}"); print(f"Report error: {e}")

class ProductDialog(simpledialog.Dialog):
    """Dialog for product details."""
    def __init__(self, parent, app, title="Product Details", initial_values=None):
        self.app, self.initial_values, self.result = app, initial_values or {}, None
        super().__init__(parent, title=title)

    def body(self, master):
        master.configure(bg=self.app._get_color('dialog_bg'))
        fields = ["Name", "Price", "Category", "Stock"]; self.entries = {}
        for i, field in enumerate(fields):
            tk.Label(master, text=f"{field}:", bg=self.app._get_color('dialog_bg'), fg=self.app._get_color('dialog_fg'), font=self.app.fonts['dialog_label']).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            entry = tk.Entry(master, width=30, bg=self.app._get_color('panel'), fg=self.app._get_color('text'), font=self.app.fonts['dialog_label'], insertbackground=self.app._get_color('text'))
            entry.grid(row=i, column=1, padx=5, pady=2); self.entries[field.lower()] = entry
            if field.lower() in self.initial_values: entry.insert(0, str(self.initial_values[field.lower()]))
        return self.entries.get('name')

    def buttonbox(self):
        box = ttk.Frame(self); box.pack(pady=5)
        ttk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE, style="TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(box, text="Cancel", width=10, command=self.cancel, style="TButton").pack(side=tk.LEFT, padx=5)
        self.bind("<Return>", lambda e: self.ok()); self.bind("<Escape>", lambda e: self.cancel())

    def apply(self): self.result = tuple(self.entries[f.lower()].get() for f in ["Name", "Price", "Category", "Stock"])

class ReportDialog(tk.Toplevel):
    """Dialog for displaying reports."""
    def __init__(self, parent, title, content, app_ref):
        super().__init__(parent); self.title(title); self.app = app_ref
        self.transient(parent); self.grab_set(); self.configure(bg=self.app._get_color('dialog_bg'))
        text_area = tk.Text(self, wrap="word", height=20, width=70, bg=self.app._get_color('panel'), fg=self.app._get_color('text'), font=("Courier New", 10), relief="sunken", borderwidth=1, padx=5, pady=5)
        text_area.insert("1.0", content); text_area.configure(state="disabled")
        text_area.pack(padx=10, pady=10, fill="both", expand=True)
        scrollbar = ttk.Scrollbar(text_area, command=text_area.yview); scrollbar.pack(side="right", fill="y")
        text_area['yscrollcommand'] = scrollbar.set
        ttk.Button(self, text="Close", command=self.destroy, style="TButton").pack(pady=10)
        self.update_idletasks()
        px, py, pw, ph = parent.winfo_rootx(), parent.winfo_rooty(), parent.winfo_width(), parent.winfo_height()
        dw, dh = self.winfo_width(), self.winfo_height()
        self.geometry(f"+{px + (pw - dw) // 2}+{py + (ph - dh) // 2}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePOSApp(root)
    root.mainloop()