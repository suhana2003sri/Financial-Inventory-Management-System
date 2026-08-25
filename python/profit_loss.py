def calculate_profit_loss(revenue, cost_of_goods, expenses):
    gross_profit = revenue - cost_of_goods
    net_profit = gross_profit - expenses

    print("Revenue:", revenue)
    print("Gross Profit:", gross_profit)
    print("Net Profit:", net_profit)


calculate_profit_loss(100000, 40000, 25000)
