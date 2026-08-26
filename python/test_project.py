def test_sales_calculation():
    quantity = 2
    price = 50000
    total = quantity * price

    assert total == 100000
    print("Sales calculation test passed.")


def test_inventory():
    quantity = 5
    minimum_stock = 10

    assert quantity <= minimum_stock
    print("Low-stock test passed.")


def test_gst():
    amount = 10000
    gst_rate = 18
    gst = amount * gst_rate / 100

    assert gst == 1800
    print("GST calculation test passed.")


test_sales_calculation()
test_inventory()
test_gst()

print("All tests completed successfully.")
