def calculate_cash_balance(opening_balance, cash_received, cash_paid):
    closing_balance = opening_balance + cash_received - cash_paid

    print("Opening Balance:", opening_balance)
    print("Cash Received:", cash_received)
    print("Cash Paid:", cash_paid)
    print("Closing Balance:", closing_balance)


calculate_cash_balance(20000, 15000, 8000)
