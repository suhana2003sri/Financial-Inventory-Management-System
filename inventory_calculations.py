def check_inventory(product_name, quantity, minimum_stock):
    if quantity <= minimum_stock:
        print(f"LOW STOCK: {product_name} - {quantity} units remaining.")
    else:
        print(f"Stock is sufficient: {product_name} - {quantity} units.")


check_inventory("Laptop", 5, 10)
