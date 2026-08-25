import pandas as pd

sales_data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Quantity": [10, 25, 15],
    "Sales_Amount": [500000, 12500, 22500]
}

df = pd.DataFrame(sales_data)

df.to_csv("sales_powerbi_data.csv", index=False)

print("Sales data prepared for Power BI.")
print(df)
