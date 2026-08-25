def record_sale(customer_name, product_name, quantity, price):
    total_amount = quantity * price

    print("Sale recorded successfully.")
    print("Customer:", customer_name)
    print("Product:", product_name)
    print("Quantity:", quantity)
    print("Total Amount:", total_amount)


record_sale("ABC Company", "Laptop", 2, 50000)
