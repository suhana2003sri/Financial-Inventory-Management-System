def calculate_profit(revenue, expenses):
    profit = revenue - expenses
    return profit


revenue = 100000
expenses = 65000

profit = calculate_profit(revenue, expenses)

print("Total Revenue:", revenue)
print("Total Expenses:", expenses)
print("Net Profit:", profit)
