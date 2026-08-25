def record_purchase(supplier_name, product_name, quantity, price):
    total_amount = quantity * price

    print("Purchase recorded successfully.")
    print("Supplier:", supplier_name)
    print("Product:", product_name)
    print("Quantity:", quantity)
    print("Total Amount:", total_amount)


record_purchase("XYZ Suppliers", "Laptop", 10, 45000)
