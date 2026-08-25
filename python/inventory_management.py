def check_stock(product_name, quantity):
    if quantity > 0:
        print(f"{product_name}: {quantity} units available.")
    else:
        print(f"{product_name}: Out of stock.")


check_stock("Laptop", 50)
