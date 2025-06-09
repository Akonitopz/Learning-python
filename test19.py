menu = {
    1: ("Rice", 15.00),
    2: ("Fried Chicken", 20.00),
    3: ("Juice", 10.00),
    4: ("Chopsuey",10.00),
    5: ("Adobo Pork", 25.00),
    6: ("Lumpia", 5.00),
    7: ("Pancit", 10.00),
    8: ("Mineral Water", 15.00),

}
def display_menu():
    print("\nMenu:")
    for item, (name, price) in menu.items():
        print(f"{item}. {name} - {price:.2f}")

def main():
    total_sale = 0.00

    while True:
        display_menu()
        food_item = int(input("Enter Food: "))
        quantity = int(input("Enter Quantity: "))

        if food_item in menu:
            total_sale += menu[food_item][1] * quantity
        else:
            print("Invalid Food Item. Try again.")
            continue

        add_more = input("Do you want to add more? (y/n): ")
        if add_more == "y":
            continue
        elif add_more == "n":
            print(f"\nTotal Sale: {total_sale:.2f}")

        while True:
                amount_tendered = float(input("Enter Amount of money Tendered: "))
                if amount_tendered < total_sale:
                    print("Insufficient Money Received!")
                else:
                    change = amount_tendered - total_sale
                    print(f"Total Change: {change:.2f}")
                    break
    
        exit_program = input("Do you want to exit the program? (y/n): ")
        if exit_program == "y":
            print("Exit Program!")
            return
        elif exit_program == 'n':
            total_sale = 0.00
            continue


main()